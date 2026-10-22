# lemy0715

한 일을 사실 위주로 정리한 기록입니다. 대부분 1인으로 기획·개발·배포·운영했습니다.

- 포트폴리오: https://lemy0715.mycsbot.com/
- 이메일: lemy0715@gmail.com

## 서비스 · 앱

| 프로젝트 | 한 일 | 역할 | 스택 |
|---|---|---|---|
| **UMMA 배달 주문 서비스** | 사용자 앱, 배달기사 앱(Flutter), 관리자 웹, 백엔드 개발·배포. 실서비스라 화면은 비공개 | 전체 개발·배포 | Flutter, Dart, Python, Docker Compose, Cloudflare Tunnel |
| **[simsim AI 비서](https://simsim.mycsbot.com/)** | 구글 로그인 기반 AI 비서와 OAuth 원격 MCP 서버. AI 클라이언트가 로그인 후 도구로 사용 | 기획·개발·배포 (1인) | Python, FastAPI, React, OAuth, MCP |
| **슬기로운 AI 공방** | 멤버 실습·발표·출석·운영 현황 관리 플랫폼 (멤버 웹, 운영진 웹, API, 인프라) | 기획·개발 | Next.js, FastAPI, SQLAlchemy, Terraform, GitHub Actions |
| **ThreadScope** | Threads 글마다 조회·반응 지표를 계산해 보여 주는 크롬 확장(MV3). 서버 없이 브라우저 안에서 동작 | 기획·개발 (1인) | JavaScript, Chrome Extension MV3 |
| **[A4 Workshop](https://muyoul.github.io/a4workshop/)** | 한글 쓰기 연습용 A4 학습지 생성기 | 개발 (1인) | HTML, JavaScript |

## Gridmint — 암호화폐 자동매매 플랫폼

기획·개발·운영 1인. 실제 계정으로 운영 중입니다. 스크린샷의 금액·수량은 가렸습니다(`•••••`).

| 서비스 | 한 일 | 스택 |
|---|---|---|
| **Gridmint Bots** | 그리드봇·시그널봇·스캘퍼를 한 콘솔에서 생성·정지·관리. 거래소 잔고를 포지션 단위로 나눠 담당 봇을 추적 | Python, FastAPI, PostgreSQL, React/TypeScript |
| **Gridmint Ledger** | 여러 거래소의 자산·수익·거래 내역을 모아 KRW·USDT를 구분해 표시 | Next.js, React, Python, FastAPI |
| **Candle Collector · MCP** | Binance·Bitget·OKX 1분봉 수집, OHLC API와 MCP 서버 제공 (2026-09 운영 종료) | TypeScript, SQLite, MCP |

- 연동 거래소: Upbit · Coinone · Bitget · OKX (Bybit·Binance 준비 중)
- 배포·운영: GitHub Actions 커밋(SHA) 고정 릴리스·롤백, Cloudflare Tunnel, AWS Lightsail, Prometheus/Grafana

<table>
  <tr>
    <td width="50%"><img src="assets/gridmint/grid-bots.jpg" alt="그리드봇 목록"><br><sub>그리드봇 — 봇별 상태·예산·손익·미청산 한도</sub></td>
    <td width="50%"><img src="assets/gridmint/flow.jpg" alt="포지션·봇 흐름도"><br><sub>흐름도 — 거래소 잔고 → 포지션 → 담당 봇 소유권</sub></td>
  </tr>
  <tr>
    <td><img src="assets/gridmint/position-manager.jpg" alt="포지션 관리자"><br><sub>포지션 관리자 — 거래소별 보유 자산을 봇에 편입·보호</sub></td>
    <td><img src="assets/gridmint/scalper.jpg" alt="스캘퍼 콘솔"><br><sub>스캘퍼 — 선물 포지션 수동 진입·청산 콘솔</sub></td>
  </tr>
  <tr>
    <td><img src="assets/gridmint/ledger-assets.jpg" alt="Gridmint Ledger 자산"><br><sub>Gridmint Ledger — 거래소 통합 자산</sub></td>
    <td></td>
  </tr>
</table>

## 멀티플랫폼 게임 6종 — AI 활용 1인 개발

토스 앱인토스 출시를 목표로 시작해, 같은 코드로 모든 플랫폼에서 돌아가는 게임으로 넓혔습니다.
AI를 개발 전 과정에 활용해 기획·개발·그림·배포를 혼자 짧은 기간에 소화했습니다.

- 기간: 첫 커밋 2026-09-28 → 약 3주 만에 6종 플레이 가능 (2026-10-15 기준)
- 플랫폼: 토스 앱인토스, 웹(Cloudflare Pages), 원스토어 웹 게임, Capacitor 앱 빌드(AdMob 광고, 구글 플레이·앱스토어 결제 연동)
- 구조: 공통 셸 `appintoss-kit`에 메뉴·단계·저장·효과음과 플랫폼별 저장·광고·결제를 모아 두고, 게임마다 플랫폼 파일만 바꿔 빌드
- AI 활용: 코드 작성·검증, 단계 생성기, 틀린그림찾기 그림 생성 파이프라인

| 게임 | 내용 |
|---|---|
| [사천성](https://sacheonseong.mycsbot.com/) | 꺾인 선 3번 규칙 짝맞추기, 단계마다 판 확장·경로 시각화 |
| [보석 맞추기](https://jewel-match.mycsbot.com/) | 1,200단계 매치3, 목표 7종을 단계 생성기로 생성 |
| [틀린그림찾기](https://spot-diff.mycsbot.com/) | AI 이미지 생성 파이프라인으로 100단계 제작 |
| [폴짝 러너](https://hop-run.mycsbot.com/) | 원터치 러너 |
| [두더지 잡기](https://mole-catch.mycsbot.com/) | 60초 아케이드 |
| [카드 뒤집기](https://card-flip.mycsbot.com/) | 기억력 짝 맞추기 |

## 기술 스택

- **Frontend**: TypeScript, React, Next.js, Vite, Flutter/Dart
- **Backend**: Python, FastAPI, SQLAlchemy, PostgreSQL
- **Infra**: Docker Compose, Cloudflare (Pages·Tunnel), AWS Lightsail, Terraform, GitHub Actions, Prometheus/Grafana
- **AI**: MCP 서버, OAuth, AI 이미지 파이프라인, LLM 에이전트 워크플로

## GitHub 활동

연도별 기여 수(비공개 저장소 포함): 2023 521 · 2024 172 · 2025 1,110 · 2026 3,802 (10월 15일 기준)
