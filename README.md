# Research Skills

연구논문·그림·발표와 한국어·영어 문체 편집을 위한 개인 스킬 모음입니다. 각 스킬의 참조 문서와 자산을 함께 보관합니다.

| 스킬 | 용도 |
|---|---|
| [scientific-paper-writing](skills/scientific-paper-writing/SKILL.md) | 연구논문 구상·개요·초안·논리 검토·문장 교정·번역 |
| [scientific-figure](skills/scientific-figure/SKILL.md) | 논문 그림 설계·제작·수정·검토, Nature 기본 프로필과 Matplotlib 템플릿 |
| [research-presentation](skills/research-presentation/SKILL.md) | 학회·세미나·랩미팅·학위심사 발표 구성·슬라이드 검토·발표 노트 |
| [humanizer](skills/humanizer/SKILL.md) | 과장·상투어·반복을 줄이는 한국어·영어 문체 편집 |

## 설치

스킬 설치를 지원하는 Codex 환경에서 다음과 같이 요청합니다.

```text
$skill-installer를 사용해 YHKlab-MSJeong/research-skills 저장소의 main 브랜치에서
다음 네 스킬을 설치해 줘:
- skills/scientific-paper-writing
- skills/scientific-figure
- skills/research-presentation
- skills/humanizer
```

이 저장소는 비공개이므로 설치 환경에 저장소 읽기 권한이 필요합니다. 기존 Git 인증이나 설치 도구가 지원하는 인증을 사용하고, 토큰은 프롬프트·원고·저장소에 넣지 않습니다. 인증되지 않았다면 해당 PC에서 먼저 GitHub 로그인을 완료합니다.

수동 설치 시에는 각 스킬 폴더 전체를 사용자 스킬 디렉터리로 복사합니다. 현재 공식 문서의 사용자 경로는 `~/.agents/skills/`이며 Windows에서는 사용자 홈 아래 `.agents\skills\`입니다. `$skill-installer`는 설치된 버전과 `CODEX_HOME` 설정에 따라 `~/.codex/skills/`를 기본 대상으로 사용할 수 있습니다. 설치 후 실제 Skills 목록에서 확인하고, 보이지 않으면 앱을 재시작합니다.

`SKILL.md`만 복사하지 말고 `references/`, `assets/`, `agents/`도 함께 보존합니다.

## 사용

설치된 환경은 요청과 스킬 설명이 맞으면 필요한 스킬을 선택할 수 있습니다. 직접 지정하는 예:

```text
$scientific-paper-writing 이 초록의 논리와 문장을 검토해 줘.
$scientific-figure 이 데이터로 논문용 그림을 만들어 줘.
$research-presentation 이 결과로 10분 학회 발표를 구성해 줘.
$humanizer 이 문단을 자연스럽게 다듬어 줘.
```

ChatGPT에서 지원되는 스킬 선택은 `@`를 사용합니다. 사용 가능한 기능과 설치 위치는 앱·실행 환경의 안내를 확인합니다.

## 실행 의존성

- 논문 작성·문체 편집·발표 구성 지침은 외부 계산 도구 없이 사용할 수 있습니다.
- `scientific-figure`의 Python 예제에는 NumPy와 Matplotlib이 필요합니다. 예제는 합성 데이터로만 그림을 생성하며 실제 연구 결과가 아닙니다.
- `.pptx` 생성·편집에는 별도 `slides` 스킬과 그 제작·렌더링 의존성이 필요합니다. 이 저장소에는 해당 스킬이나 실행 환경을 복제하지 않습니다.
- 발표 스킬에서 참조하는 `slides`의 원본은 `openai/skills`의 커밋 `e6afb0d74cc75d220df2faf3dd6c635c2dc6a108`, 경로 `skills/.curated/slides`입니다. 필요하면 `$skill-installer`에 이 저장소·커밋·경로를 명시해 별도로 설치합니다. 해당 스킬의 Apache-2.0 라이선스와 안내를 따릅니다.

스킬 설치는 Python·Node 패키지, 글꼴, LibreOffice 등의 설치를 대신하지 않습니다. 각 작업에 필요한 의존성만 별도 작업 환경에서 준비합니다.

## 업데이트와 검증 범위

저장소 push가 다른 PC에 설치된 복사본을 자동으로 갱신하지는 않습니다. 설치 도구는 같은 이름의 대상이 이미 있으면 중단할 수 있으므로, 업데이트할 때 기존 설치본의 로컬 변경 여부를 확인하고 새 버전과 비교합니다. 커밋을 지정하면 설치 버전을 고정할 수 있습니다.

스킬의 출처·접근 한계·합성 검증 기록은 각 `references/` 문서에 있습니다. 검증 기록에 나오는 로컬 산출물 경로는 작성 환경의 과거 기록이며 이 저장소에 포함되지 않습니다. 다른 PC의 실행 환경이나 Microsoft PowerPoint 호환성을 검증했다는 뜻이 아닙니다.

원본 연구 데이터·계산 출력·인증정보·검증용 실행 환경은 이 저장소에 포함하지 않습니다.

## 공식 안내

- [스킬 작성·설치·사용](https://learn.chatgpt.com/docs/build-skills)
- [Windows용 ChatGPT 앱](https://learn.chatgpt.com/docs/windows/windows-app)

글쓰기·그림·발표 원칙에 사용한 자료는 각 스킬의 출처 문서에서 확인합니다.
