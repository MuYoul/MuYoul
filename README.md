# lemy0715

> **AI를 대하는 방식**
>
> AI는 유능한 동료이자 비서입니다. 하지만 만능은 아닙니다.
> 결과의 쓸모와 효율은 무엇을 원하는지, 즉 목적과 요구사항을 얼마나 분명히 전하느냐에 달려 있습니다.
> 그래서 AI의 강점과 한계, 일을 맡기고 피드백하는 방식을 익혀 한 명의 코워커처럼 함께 일하려 합니다.
> 목표를 정하고 결과를 판단하는 것은 제 몫이고, 그렇게 아낀 시간으로 더 많은 것을 만듭니다.

한 일을 사실 위주로 정리한 기록입니다. 대부분 1인으로 기획·개발·배포·운영했습니다.

- 포트폴리오: https://lemy0715.mycsbot.com/
- 이메일: lemy0715@gmail.com

## 프로젝트

<!-- projects:start -->
> 총 22개 · 🟢 운영 중 16 · 🟡 개발 중 3 · ⚪ 미운영 3

### 서비스 · AI · 인프라

| 분야 | 프로젝트 | 한 줄 소개 | 상태 | 최근 갱신 |
|---|---|---|---|---|
| AI · MCP | **Simsim AI 비서** | 영수증 추출·기관 양식 문서 작성을 돕는 AI 비서와 원격 MCP 서버 | 🟢 운영 중 | 2026-07 |
| Gridmint 트레이딩 | **Gridmint Bots** | 그리드봇·시그널봇·스캘퍼를 한 콘솔에서 생성·정지·관리 | 🟢 운영 중 | 2026-10-17 |
| Gridmint 트레이딩 | **Gridmint Ledger** | 여러 거래소의 자산·수익·거래 내역을 모아 KRW·USDT 구분 표시 | 🟢 운영 중 | 2026-09-23 |
| 서비스 · 도구 | **UMMA 배달 주문 서비스** | 사용자 앱·배달기사 앱·관리자 웹·백엔드 외주 개발 (실서비스라 화면 비공개) | 🟢 운영 중 | 2026-10-28 |
| 서비스 · 도구 | **Ablog (autoblog)** | Google Docs 원고를 WordPress·네이버 카페·네이버 블로그에 자동 게시 | 🟢 운영 중 | 2026-10-18 |
| 서비스 · 도구 | **[A4 Workshop](https://muyoul.github.io/a4workshop/)** | 한글 쓰기 연습용 A4 학습지 생성기 | 🟢 운영 중 | 2026-08-15 |
| 인프라 · 운영 | **lemy0715-observability** | 모든 서비스의 지표를 모으는 중앙 Prometheus·Grafana 플랫폼 | 🟢 운영 중 | 2026-10-17 |

<details>
<summary><b>Simsim AI 비서</b> — 영수증 추출·기관 양식 문서 작성을 돕는 AI 비서와 원격 MCP 서버</summary>

- Google 로그인 + OAuth 원격 MCP 서버
- OpenAPI에서 MCP 도구를 자동 생성해 API 전체를 AI에 제공
- 메모·이미지·Drive·RAG API, Slack 등 대화 환경에서 사용
- 기술: Python · FastAPI · React · OAuth · MCP


</details>
<details>
<summary><b>Gridmint Bots</b> — 그리드봇·시그널봇·스캘퍼를 한 콘솔에서 생성·정지·관리</summary>

- 거래소 잔고를 포지션 단위로 나눠 담당 봇을 추적
- 커밋(SHA) 고정 릴리스·롤백, Prometheus/Grafana 관측
- 연동 거래소 Upbit · Coinone · Bitget · OKX
- 기술: Python · FastAPI · PostgreSQL · React · TypeScript

<table><tr>
<td width="50%"><img src="assets/gridmint/grid-bots.jpg" alt="그리드봇 — 봇별 상태·예산·손익·미청산 한도"><br><sub>그리드봇 — 봇별 상태·예산·손익·미청산 한도</sub></td>
<td width="50%"><img src="assets/gridmint/flow.jpg" alt="흐름도 — 거래소 잔고 → 포지션 → 담당 봇 소유권"><br><sub>흐름도 — 거래소 잔고 → 포지션 → 담당 봇 소유권</sub></td>
</tr><tr>
<td width="50%"><img src="assets/gridmint/position-manager.jpg" alt="포지션 관리자 — 거래소별 보유 자산을 봇에 편입·보호"><br><sub>포지션 관리자 — 거래소별 보유 자산을 봇에 편입·보호</sub></td>
<td width="50%"><img src="assets/gridmint/scalper.jpg" alt="스캘퍼 — 선물 포지션 수동 진입·청산 콘솔"><br><sub>스캘퍼 — 선물 포지션 수동 진입·청산 콘솔</sub></td>
</tr></table>

</details>
<details>
<summary><b>Gridmint Ledger</b> — 여러 거래소의 자산·수익·거래 내역을 모아 KRW·USDT 구분 표시</summary>

- 거래소 통합 자산·손익 조회
- 백엔드 API를 MCP로 제공해 AI로 필요한 뷰를 만들도록 설계
- 기술: Next.js · React · Python · FastAPI · MCP

<table><tr>
<td width="50%"><img src="assets/gridmint/ledger-assets.jpg" alt="거래소 통합 자산"><br><sub>거래소 통합 자산</sub></td>
</tr></table>

</details>
<details>
<summary><b>UMMA 배달 주문 서비스</b> — 사용자 앱·배달기사 앱·관리자 웹·백엔드 외주 개발 (실서비스라 화면 비공개)</summary>

- Flutter 사용자·배달기사 앱, 관제용 관리자 웹
- 결제·지도 연동, Docker Compose + Cloudflare Tunnel 배포
- 기술: Flutter · Dart · Python · Docker Compose · Cloudflare Tunnel


</details>
<details>
<summary><b>Ablog (autoblog)</b> — Google Docs 원고를 WordPress·네이버 카페·네이버 블로그에 자동 게시</summary>

- Docs 인라인 이미지를 순서대로 올려 본문에 그대로 배치
- Instagram·Threads용 파생 글 생성·편집
- 기술: Python · Google Docs API · WordPress REST API


</details>
<details>
<summary><b>A4 Workshop</b> — 한글 쓰기 연습용 A4 학습지 생성기</summary>

- 기술: HTML · JavaScript
- 링크: https://muyoul.github.io/a4workshop/

<img src="assets/screens/a4workshop.jpg" alt="A4 Workshop 화면" width="600">

</details>
<details>
<summary><b>lemy0715-observability</b> — 모든 서비스의 지표를 모으는 중앙 Prometheus·Grafana 플랫폼</summary>

- 각 서비스는 Alloy 수집기로 remote-write, 플랫폼은 이 저장소가 관리
- 기술: Prometheus · Grafana · Docker Compose


</details>

<details>
<summary>⚪ 미운영 3개 보기</summary>

| 분야 | 프로젝트 | 한 줄 소개 | 상태 | 최근 갱신 |
|---|---|---|---|---|
| AI · MCP | **AiMER** | 샘플 데이터로 병명 후보를 추천해 병리 보고서를 만드는 실험 | ⚪ 미운영 | 2026-07-23 |
| Gridmint 트레이딩 | **Candle Collector** | Binance·Bitget·OKX 1분봉 수집과 OHLC API·MCP 서버 (2026-09 종료) | ⚪ 미운영 | 2026-09-19 |
| 서비스 · 도구 | **슬기로운 AI 공방** | 멤버 실습·발표·출석·운영 현황을 한곳에서 관리하는 플랫폼 (운영 중지) | ⚪ 미운영 | 2026-10-28 |

<details>
<summary><b>AiMER</b> — 샘플 데이터로 병명 후보를 추천해 병리 보고서를 만드는 실험</summary>

- 샘플 입력·보고서 생성 API를 MCP로 제공
- 협업 의사의 채팅에 연결해 사이트 없이 보고서 생성
- 테스트 검토 후 품질·비용 문제로 종료 (실제 의료 업무 미사용)
- 기술: TypeScript · Express · Prisma · Next.js · MCP


</details>
<details>
<summary><b>Candle Collector</b> — Binance·Bitget·OKX 1분봉 수집과 OHLC API·MCP 서버 (2026-09 종료)</summary>

- 기술: TypeScript · SQLite · MCP


</details>
<details>
<summary><b>슬기로운 AI 공방</b> — 멤버 실습·발표·출석·운영 현황을 한곳에서 관리하는 플랫폼 (운영 중지)</summary>

- 멤버 웹·운영진 웹(Next.js 정적) + FastAPI 백엔드
- Terraform으로 CloudFront·S3·인증서, GitHub Actions 배포
- 기술: Next.js · FastAPI · SQLAlchemy · Terraform · GitHub Actions


</details>

</details>

### 게임

| 프로젝트 | 한 줄 소개 | 상태 | 최근 갱신 |
|---|---|---|---|
| **[틀린그림찾기](https://spot-diff.mycsbot.com/)** | AI 이미지 생성 파이프라인으로 그림 100단계 제작 | 🟢 운영 중 | 2026-10-28 |
| **appintoss-kit · 게임 제작 매뉴얼** | 모든 게임이 쓰는 공통 셸과, 게임 7종을 만들며 겪은 절차·이슈 매뉴얼 | 🟢 운영 중 | 2026-10-27 |
| **[사천성](https://sacheonseong.mycsbot.com/)** | 꺾인 선 3번 규칙 짝맞추기, 단계마다 판 확장·경로 시각화 | 🟢 운영 중 | 2026-10-27 |
| **[보석 맞추기](https://jewel-match.mycsbot.com/)** | 1,200단계 매치3, 목표 7종을 단계 생성기로 생성 | 🟢 운영 중 | 2026-10-27 |
| **[브릭 스톰](https://brick-storm.mycsbot.com/)** | 한 손가락 조준·발사 벽돌깨기, 스토어판 86개 언어 | 🟢 운영 중 | 2026-10-27 |
| **[폴짝 러너](https://hop-run.mycsbot.com/)** | 원터치 러너 | 🟢 운영 중 | 2026-10-27 |
| **[왼쪽 오른쪽](https://left-right.mycsbot.com/)** | 봄나물은 밥상, 봄꽃은 꽃병으로 나누는 1분 좌우 나누기 | 🟢 운영 중 | 2026-10-06 |
| **[두더지 잡기](https://mole-catch.mycsbot.com/)** | 60초 아케이드 | 🟢 운영 중 | 2026-10-06 |
| **[카드 뒤집기](https://card-flip.mycsbot.com/)** | 기억력 짝 맞추기 | 🟢 운영 중 | 2026-10-06 |
| **[워터 레스큐](https://water-rescue.mycsbot.com/)** | 관을 돌리고 옮겨 물길을 잇는 현장 출동 퍼즐 | 🟡 개발 중 | 2026-10-27 |
| **[Farm Rush](https://farm-rush.mycsbot.com/)** | 터치로 즐기는 오리지널 농장 경영 게임, 1,000 스테이지 | 🟡 개발 중 | 2026-10-21 |
| **Abyss Relay** | 전력을 배분하며 3분을 버티는 절차 생성 잠수함 생존 게임 | 🟡 개발 중 | 2026-09-25 |

<details>
<summary><b>틀린그림찾기</b> — AI 이미지 생성 파이프라인으로 그림 100단계 제작</summary>

- 기술: TypeScript · Python
- 링크: https://spot-diff.mycsbot.com/

<img src="assets/screens/spot-diff.jpg" alt="틀린그림찾기 화면" width="240">

</details>
<details>
<summary><b>appintoss-kit · 게임 제작 매뉴얼</b> — 모든 게임이 쓰는 공통 셸과, 게임 7종을 만들며 겪은 절차·이슈 매뉴얼</summary>

- 메뉴·단계·저장·효과음 + 플랫폼별 저장·광고·결제를 셸에 모음
- 게임마다 플랫폼 파일만 바꿔 토스 앱인토스·웹·Android/iOS로 빌드
- 출시 절차, 이슈 카탈로그, 광고·결제·GA4 가이드
- 기술: TypeScript · Capacitor · Cloudflare Pages · AdMob


</details>
<details>
<summary><b>사천성</b> — 꺾인 선 3번 규칙 짝맞추기, 단계마다 판 확장·경로 시각화</summary>

- 기술: TypeScript
- 링크: https://sacheonseong.mycsbot.com/

<img src="assets/screens/sacheonseong.jpg" alt="사천성 화면" width="240">

</details>
<details>
<summary><b>보석 맞추기</b> — 1,200단계 매치3, 목표 7종을 단계 생성기로 생성</summary>

- 기술: TypeScript
- 링크: https://jewel-match.mycsbot.com/

<img src="assets/screens/jewel-match.jpg" alt="보석 맞추기 화면" width="240">

</details>
<details>
<summary><b>브릭 스톰</b> — 한 손가락 조준·발사 벽돌깨기, 스토어판 86개 언어</summary>

- 기술: TypeScript · Capacitor
- 링크: https://brick-storm.mycsbot.com/

<img src="assets/screens/brick-storm.jpg" alt="브릭 스톰 화면" width="240">

</details>
<details>
<summary><b>폴짝 러너</b> — 원터치 러너</summary>

- 기술: TypeScript
- 링크: https://hop-run.mycsbot.com/

<img src="assets/screens/hop-run.jpg" alt="폴짝 러너 화면" width="240">

</details>
<details>
<summary><b>왼쪽 오른쪽</b> — 봄나물은 밥상, 봄꽃은 꽃병으로 나누는 1분 좌우 나누기</summary>

- 기술: TypeScript
- 링크: https://left-right.mycsbot.com/

<img src="assets/screens/left-right.jpg" alt="왼쪽 오른쪽 화면" width="240">

</details>
<details>
<summary><b>두더지 잡기</b> — 60초 아케이드</summary>

- 기술: TypeScript
- 링크: https://mole-catch.mycsbot.com/

<img src="assets/screens/mole-catch.jpg" alt="두더지 잡기 화면" width="240">

</details>
<details>
<summary><b>카드 뒤집기</b> — 기억력 짝 맞추기</summary>

- 기술: TypeScript
- 링크: https://card-flip.mycsbot.com/

<img src="assets/screens/card-flip.jpg" alt="카드 뒤집기 화면" width="240">

</details>
<details>
<summary><b>워터 레스큐</b> — 관을 돌리고 옮겨 물길을 잇는 현장 출동 퍼즐</summary>

- 기술: TypeScript
- 링크: https://water-rescue.mycsbot.com/

<img src="assets/screens/water-rescue.jpg" alt="워터 레스큐 화면" width="240">

</details>
<details>
<summary><b>Farm Rush</b> — 터치로 즐기는 오리지널 농장 경영 게임, 1,000 스테이지</summary>

- 기술: JavaScript
- 링크: https://farm-rush.mycsbot.com/

<img src="assets/screens/farm-rush.jpg" alt="Farm Rush 화면" width="240">

</details>
<details>
<summary><b>Abyss Relay</b> — 전력을 배분하며 3분을 버티는 절차 생성 잠수함 생존 게임</summary>

- 기술: TypeScript


</details>
<!-- projects:end -->

## 기술 스택

- **Frontend**: TypeScript, React, Next.js, Vite, Flutter/Dart
- **Backend**: Python, FastAPI, SQLAlchemy, PostgreSQL
- **Infra**: Docker Compose, Cloudflare (Pages·Tunnel), AWS Lightsail, Terraform, GitHub Actions, Prometheus/Grafana
- **AI**: MCP 서버, OAuth, AI 이미지 파이프라인, LLM 에이전트 워크플로

## GitHub 활동

연도별 기여 수(비공개 저장소 포함): 2023 521 · 2024 172 · 2025 1,110 · 2026 3,802 (10월 15일 기준)
