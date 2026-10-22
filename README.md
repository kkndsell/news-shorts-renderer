# news-shorts-renderer

'뉴스 뒤의 주식' 3초 퀴즈 숏폼을 만드는 렌더러. n8n이 `render-short` 워크플로를 `workflow_dispatch`로 실행하고,
결과 MP4는 Actions 아티팩트(30일)로 남기고 텔레그램 관리자 채팅으로 검수용 발송한다.

- `render/template.html` 화면 템플릿 (1080×1920)
- `render/build.py` 음성(OpenAI TTS, verse · 음높이 +6% · 속도 ×1.25) → 타임라인 → 프레임 → MP4
- 마지막 멘트는 반드시 "댓글로 달아봐"로 끝나야 하며, 아니면 빌드가 멈춘다.

필요한 저장소 Secrets: `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
