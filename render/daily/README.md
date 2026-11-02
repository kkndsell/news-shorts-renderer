# 일상 수사대 쇼츠 빌더 (023편~)

1. `episodes.py`에 편을 추가한다. 한 줄 = 내레이션 = 화면 자막(글자 그대로). 숫자는 출처 확인된 것만(`SOURCES`).
2. 문장별 음성: Actions `tts-lines`(cedar, 1.3배)를 `dir=daily-<번호>`, `lines_b64=[{id:"L01",text:...}]`로 실행 → `fetch` 브랜치 `tts/daily-<번호>/`.
3. `python render.py <tts 폴더> <출력 폴더> <번호...>` → `short.mp4`, `cover.jpg`, `subtitle.srt`, `post.json`.
   자막은 문장별 음성 길이로 맞추고, 2줄(한 줄 19자 안팎)을 넘으면 나눠서 순서대로 보여 준다.
4. gh-pages `daily/<번호>/`에 올리고 n8n `daily_detective_queue`에 `status=queued`로 추가.

예전 편(001~022) 자막: Actions `stt-shorts`로 받아쓰기 → 화면 자막과 대조해 고친 문장으로 `stt2srt.py`.
