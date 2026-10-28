"""projects.yml로 README.md의 프로젝트 영역(마커 사이)을 다시 만든다.

GH_TOKEN이 있으면 저장소별 최근 push 날짜를 GitHub API로 읽는다.
비공개 저장소 날짜를 읽으려면 모든 저장소의 메타데이터 읽기 권한이 있는 토큰이 필요하다.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OWNER = "MuYoul"
START, END = "<!-- projects:start -->", "<!-- projects:end -->"
STATUS = {"live": "🟢 운영 중", "dev": "🟡 개발 중", "ended": "⚪ 미운영"}


def pushed_at(repo, token):
    req = urllib.request.Request(f"https://api.github.com/repos/{OWNER}/{repo}")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.load(r)["pushed_at"][:10]
    except Exception as e:  # 권한 없음·삭제된 저장소는 날짜만 비운다
        print(f"warn: {repo}: {e}", file=sys.stderr)
        return None


def last_updated(p, token):
    dates = [d for d in (pushed_at(r, token) for r in p.get("repos", [])) if d]
    return max(dates) if dates else str(p.get("updated", "-"))


def render_details(p):
    out = ["<details>", f"<summary><b>{p['name']}</b> — {p['summary']}</summary>", ""]
    out += [f"- {f}" for f in p.get("features", [])]
    out.append(f"- 기술: {' · '.join(p.get('stack', []))}")
    if p.get("link"):
        out.append(f"- 링크: {p['link']}")
    imgs = p.get("images", [])
    if any("caption" in im for im in imgs):  # 설명 달린 여러 장은 2열 표
        out += ["", "<table><tr>"]
        for i, im in enumerate(imgs):
            if i and i % 2 == 0:
                out.append("</tr><tr>")
            out.append(f'<td width="50%"><img src="{im["src"]}" alt="{im["caption"]}"><br><sub>{im["caption"]}</sub></td>')
        out.append("</tr></table>")
    else:
        out += ["", *(f'<img src="{im["src"]}" alt="{p["name"]} 화면" width="{im.get("width", 240)}">' for im in imgs)]
    return out + ["", "</details>"]


def render_section(projects, cats, with_category):
    head = ("| 분야 " if with_category else "") + "| 프로젝트 | 한 줄 소개 | 상태 | 최근 갱신 |"
    sep = ("|---" if with_category else "") + "|---|---|---|---|"

    def table(ps):
        rows = [head, sep]
        for p in ps:
            name = f"[{p['name']}]({p['link']})" if p.get("link") else p["name"]
            cat = f"| {cats[p['category']]} " if with_category else ""
            rows.append(f"{cat}| **{name}** | {p['summary']} | {STATUS[p['status']]} | {p['_date']} |")
        return rows

    active = [p for p in projects if p["status"] != "ended"]
    ended = [p for p in projects if p["status"] == "ended"]
    out = table(active) + [""]
    for p in active:
        out += render_details(p)
    if ended:
        out += ["", "<details>", f"<summary>⚪ 미운영 {len(ended)}개 보기</summary>", ""] + table(ended) + [""]
        for p in ended:
            out += render_details(p)
        out += ["", "</details>"]
    return out


def render(data, token):
    cats = data["categories"]
    projects = data["projects"]
    for p in projects:
        p["_date"] = last_updated(p, token)
    order, status_order = list(cats), list(STATUS)
    # 상태(운영 → 개발 → 미운영) → 분야 → 최근 갱신 순
    projects.sort(key=lambda p: p["_date"], reverse=True)
    projects.sort(key=lambda p: (status_order.index(p["status"]), order.index(p["category"])))

    games = [p for p in projects if p["category"] == "game"]
    others = [p for p in projects if p["category"] != "game"]
    count = lambda s: sum(p["status"] == s for p in projects)
    out = [f"> 총 {len(projects)}개 · 🟢 운영 중 {count('live')} · 🟡 개발 중 {count('dev')} · ⚪ 미운영 {count('ended')}", ""]
    out += ["### 서비스 · AI · 인프라", ""] + render_section(others, cats, True)
    out += ["", "### 게임", ""] + render_section(games, cats, False)
    return "\n".join(out)


def main():
    data = yaml.safe_load((ROOT / "projects.yml").read_text(encoding="utf-8"))
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"README.md에 {START} / {END} 마커가 없습니다")
    body = render(data, os.environ.get("GH_TOKEN"))
    new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: f"{START}\n{body}\n{END}", text, flags=re.S)
    readme.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
