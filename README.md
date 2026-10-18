# Research Skills

연구논문 작성, 과학 그림, 연구 발표, 한국어·영어 문체 편집을 위한 **네 가지 Codex 스킬**입니다. 지침과 참고 자료, 제작 자산을 스킬별로 함께 제공합니다.

[스킬 소개](#스킬-소개) · [설치](#설치) · [사용 예시](#사용-예시) · [참고 자료](#스킬별-참고-자료) · [의존성과 업데이트](#의존성과-업데이트)

## 스킬 소개

| 스킬 | 주요 작업 | 포함 자료 |
| --- | --- | --- |
| [scientific-paper-writing](skills/scientific-paper-writing/SKILL.md) | 논문 구상·개요·초안, 논리 검토, 문장 교정·번역 | 글쓰기 가이드, 출처와 확인 범위 |
| [scientific-figure](skills/scientific-figure/SKILL.md) | 데이터 그래프·다중 패널·연구 모식도 설계, 제작·수정·검토 | 설계 가이드, Nature 기본 프로필, Matplotlib 템플릿 |
| [research-presentation](skills/research-presentation/SKILL.md) | 학회·세미나·랩미팅·학위심사 발표 구성, 슬라이드 검토·발표 노트 | 유형별 가이드, 제작·검토 절차, 검증 기록 |
| [humanizer](skills/humanizer/SKILL.md) | 한국어·영어 글의 상투어·반복·과장을 줄이는 문체 편집 | 언어별 편집 패턴, 전후 예시, 근거와 한계 |

수치·조건·인용·불확실성과 과학적 의미를 보존하는 것을 공통 원칙으로 합니다. 입력에 없는 연구 결과나 참고문헌을 만들어 채우지 않습니다.

## 설치

### Codex에서 설치

`skill-installer`를 사용할 수 있는 Codex에서 다음을 요청합니다.

```text
$skill-installer로 YHKlab-MSJeong/research-skills의 main 브랜치에서
다음 네 스킬을 모두 설치해 줘.
- skills/scientific-paper-writing
- skills/scientific-figure
- skills/research-presentation
- skills/humanizer
```

이 저장소는 공개되어 있어 저장소를 읽기 위한 GitHub 로그인은 필요하지 않습니다. 설치 환경에서는 GitHub 네트워크 접근이 가능해야 합니다.

### 수동 설치

```bash
git clone https://github.com/YHKlab-MSJeong/research-skills.git
```

`skills/` 아래에서 필요한 스킬 폴더 전체를 사용 중인 환경의 사용자 스킬 디렉터리로 복사합니다. 설치 도구·버전에 따라 `~/.agents/skills/` 또는 `~/.codex/skills/` 등을 사용하므로 실제 환경의 안내를 따릅니다. `$skill-installer`의 대상 경로는 `CODEX_HOME` 설정에도 영향을 받습니다.

`SKILL.md`와 함께 `references/`, `assets/`, `agents/`를 보존합니다. 설치 후 스킬 목록을 확인하고, 목록에 반영되지 않으면 앱을 재시작합니다.

## 사용 예시

```text
$scientific-paper-writing 이 초록의 주장과 근거 연결을 검토하고 문장을 다듬어 줘.

$scientific-figure 이 CSV로 논문용 2패널 그림을 만들어 줘.
단위와 원본 데이터는 유지하고 PDF와 PNG, 재생성 코드를 제공해 줘.

$research-presentation 이 결과로 10분 학회 발표를 구성해 줘.
슬라이드별 메시지, 근거 그림, 발표 노트를 정리해 줘.

$humanizer 이 문단을 부분 수정으로 자연스럽게 다듬어 줘.
전문용어와 수치, 인용은 유지해 줘.
```

논문 본문·캡션은 `scientific-paper-writing`, 그림 자체는 `scientific-figure`, 발표 전체 구성은 `research-presentation`, 자연스러운 문체 편집은 `humanizer`를 지정하면 됩니다. Figure 스킬은 신규 그림에 Nature 기본 프로필을 적용하며, 대상 저널이나 기존 스타일을 별도로 지정할 수 있습니다.

## 스킬별 참고 자료

아래는 저장소의 출처 문서에 기록된 자료와 활용 내용을 정리한 목록입니다. 출처 문서의 확인 기준일은 **2026-10-18**입니다. 실험 연구, 실무 조언, 공식 제출 규격과 스킬 작성자의 응용을 구분합니다. 자세한 접근 범위와 적용 한계는 각 스킬의 출처 문서를 따릅니다.

### scientific-paper-writing — 연구논문 글쓰기

| 참고 자료 | 자료 유형·확인 범위 | 반영한 내용 |
| --- | --- | --- |
| Joshua Schimel (2012), [*Writing Science: How to Write Papers That Get Cited and Proposals That Get Funded*](https://www.oupjapan.co.jp/en/products/detail/9759?language=en). Oxford University Press. | 출판사 소개·목차·서지정보 | 중심 메시지, 논문 전체와 절·문단·문장의 연결, 초안과 퇴고 |
| Michael Alley (2018), [*The Craft of Scientific Writing*, 4th ed.](https://doi.org/10.1007/978-1-4419-8288-9). Springer. | 출판사 소개·목차·서지정보 | 정확성·명료성, 모호함 해소, 정보 연결과 강조 |
| George D. Gopen & Judith A. Swan (1990), [*The Science of Scientific Writing*](https://courses.ems.psu.edu/styleforstudents/print/c10_p6.html). American Scientist 78(6):550–558. | 허가된 전문 재수록 | 독자 기대, 맥락과 새 정보의 배치, 문장의 중심과 강조 위치 |
| Brett Mensh & Konrad Kording (2017), [*Ten simple rules for structuring papers*](https://doi.org/10.1371/journal.pcbi.1005619). PLOS Computational Biology. | 공개 전문 및 [정정](https://doi.org/10.1371/journal.pcbi.1005830) | 중심 기여, 논증 순서, 절·문단 구조, 그림과 주장의 연결 |
| [MIT NSE Communication Lab — CommKit](https://mitcommlab.mit.edu/nse/use-the-commkit/) | 공개 교육 가이드 | 초록·서론·방법·결과·논의·그림의 역할과 정보 완결성 |
| Kristin Sainani — *Writing in the Sciences*. [Stanford 안내](https://rdcommunity.stanford.edu/resources) · [강의 페이지](https://www.coursera.org/learn/sciwrite) | 공식 소개·공개 강의계획 | 문장 수정, 초안·퇴고의 구분, 논문 작성 과정 |
| Nature Methods (2017), [*So you’re writing a paper*](https://doi.org/10.1038/nmeth.4532). 14:1115. | 공식 페이지의 검색 색인 본문·서지정보 | 독자·메시지·데이터, 직접적인 언어, 간결성, 피드백 |

CommKit에서 참조한 개별 가이드: [Abstracts](https://mitcommlab.mit.edu/nse/commkit/abstracts/), [Introduction](https://mitcommlab.mit.edu/nse/commkit/journal-article-introduction/), [Methods](https://mitcommlab.mit.edu/nse/commkit/journal-article-methods/), [Results](https://mitcommlab.mit.edu/nse/commkit/journal-article-results/), [Discussion](https://mitcommlab.mit.edu/nse/commkit/journal-article-discussion/), [Figure Design](https://mitcommlab.mit.edu/nse/commkit/figure-design/).

책 두 권은 본문 전체를 열람한 요약이 아니며, 강의 전체를 수강한 것으로 기술하지 않습니다. 영어 산문의 정보 배치 원칙도 한국어의 고정 어순으로 적용하지 않습니다.

상세 문서: [출처와 확인 범위](skills/scientific-paper-writing/references/sources.md) · [글쓰기 가이드](skills/scientific-paper-writing/references/writing-guide.md)

### scientific-figure — 과학 그림

| 참고 자료 | 자료 유형 | 반영한 내용 |
| --- | --- | --- |
| [MIT·Harvard Broad Institute — Figure Design](https://mitcommlab.mit.edu/broad/commkit/figure-design/) | 기관 교육 지침 | 독자·매체·메시지·증거에 맞는 그래프와 다중 패널 |
| [Nature Methods — Points of View](https://blogs.nature.com/methagora/2013/07/data-visualization-points-of-view.html) | 전문가 해설 시리즈 | 배치·여백·색·타이포그래피·축·기호·모식도 |
| Rougier, Droettboom & Bourne (2014), [*Ten Simple Rules for Better Figures*](https://doi.org/10.1371/journal.pcbi.1003833). PLOS Computational Biology. | 실용 Editorial | 독자·메시지·매체, 기본값 검토, 색상과 왜곡 방지 |
| Heer & Bostock (2010), [*Crowdsourcing Graphical Perception*](https://hci.stanford.edu/publications/paper.php?id=142). CHI. [PDF](https://idl.cs.washington.edu/files/2010-MTurk-CHI.pdf) · [DOI](https://doi.org/10.1145/1753326.1753357) | 지각 실험 | 공간 인코딩, 명도 대비, 면적·차트 크기·격자와 비교 정확도 |
| Crameri, Shephard & Heron (2020), [*The misuse of colour in science communication*](https://doi.org/10.1038/s41467-020-19160-7). Nature Communications. | Perspective | 지각적으로 균일한 색상표, 데이터 의미에 맞는 색상, 색각 접근성 |
| Weissgerber et al. (2015), [*Beyond Bar and Line Graphs*](https://doi.org/10.1371/journal.pbio.1002128). PLOS Biology. | 데이터 표현 관행 검토 | 요약 통계가 가리는 분포, 개별 관측값과 paired data 표현 |
| Nature — [Preparing figures: our specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) | 공식 artwork 규격 | 글꼴·패널 표시·축·단위·벡터·색상·해상도 |
| Nature — [Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/) | 공식 artwork 규격 | 패널 크기·구성·출력 형식·접근성 팔레트 |
| Nature — [Formatting guide](https://www.nature.com/nature/for-authors/formatting-guide) · [Initial submission](https://www.nature.com/nature/for-authors/initial-submission) | 공식 원고·제출 안내 | 패널의 논리적 연결, 캡션·표본·오차 정의 |
| Nature — [Image Integrity](https://research-figure-guide.nature.com/figures/image-integrity/) | 공식 이미지 무결성 지침 | 원 데이터의 충실한 표현, 합성 경계 표시, 선택적 보정 방지 |

Nature 프로필은 신규 그림의 기본값입니다. 저널·그림 유형에 따라 실제 제출 규정을 다시 확인합니다. 템플릿의 선 두께·기본 높이·colormap·미리보기 해상도 등 구현 선택을 Nature의 일률적인 의무 규정으로 취급하지 않습니다. Points of View의 모든 개별 글을 전문 검토한 것으로 기술하지 않습니다.

상세 문서: [출처와 적용 범위](skills/scientific-figure/references/sources.md) · [설계 가이드](skills/scientific-figure/references/design-guide.md) · [Nature 프로필](skills/scientific-figure/references/nature-profile.md) · [Matplotlib 템플릿](skills/scientific-figure/assets/nature_template.py)

### research-presentation — 연구 발표

| 참고 자료 | 자료 유형 | 반영한 내용 |
| --- | --- | --- |
| Kristen M. Naegle (2021), [*Ten simple rules for effective presentation slides*](https://doi.org/10.1371/journal.pcbi.1009554). PLOS Computational Biology. | Editorial·실무 지침 | 한 장의 중심 목적, 메시지형 제목, 필요한 내용과 그림, 출처·리허설 |
| Joanna K. Garner & Michael P. Alley (2013), [*How the Design of Presentation Slides Affects Audience Comprehension: A Case for the Assertion–Evidence Approach*](https://www.ijee.ie/articles/Vol29-6/23_ijee2791ns.pdf). International Journal of Engineering Education 29(6):1564–1579. | 실험 연구 | 주장과 시각적 근거를 연결하는 슬라이드 구성 |
| Michael Alley, [*Tutorial: Creating an Assertion-Evidence Presentation*](https://www.craftscicom.org/ae_tutorial.html) | 개발자의 실무 안내 | 문장형 제목, 시각적 근거, 발표 노트로 보조 설명 분리 |
| Philip E. Bourne (2007), [*Ten Simple Rules for Making Good Oral Presentations*](https://doi.org/10.1371/journal.pcbi.0030077). PLOS Computational Biology. | 실무 지침 | 청중의 배경·기대, 내용 선별, 구조와 연습 |
| Christopher J. Lortie (2017), [*Ten simple rules for short and swift presentations*](https://doi.org/10.1371/journal.pcbi.1005373). PLOS Computational Biology. | 짧은 발표용 실무 지침 | 제한 시간에서 메시지·그림을 선별하고 실제 시간을 확인하는 연습 |
| Stephen M. Kosslyn et al. (2012), [*PowerPoint® Presentation Flaws and Failures: A Psychological Analysis*](https://doi.org/10.3389/fpsyg.2012.00230). Frontiers in Psychology. | 심리학적 원칙을 적용한 연구 | 지각·기억·이해, 구별·조직·강조와 인지 부담 |
| Microsoft — [Tips for creating and delivering an effective presentation](https://support.microsoft.com/en-us/powerpoint/tips-for-creating-and-delivering-an-effective-presentation) | 공식 실무 안내 | 글꼴·크기·대비, 간결한 텍스트 |
| Microsoft — [Make your PowerPoint presentations accessible](https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities) · [Design slides for people with dyslexia](https://support.microsoft.com/en-us/powerpoint/accessibility/video-design-slides-for-people-with-dyslexia) | 공식 접근성 안내 | 여백·대비, 색 이외의 정보 전달, 대체 텍스트와 읽기 순서 |

Assertion–Evidence 실험은 특정 청중·주제에서 여러 설계 원칙을 묶어 비교한 결과입니다. 모든 발표에서의 우월성이나 제목 하나의 독립 효과로 일반화하지 않습니다. ‘한 장당 1분’, ‘6단어×7줄’, ‘18pt’ 등은 상황별 출발점이며 보편적인 합격 기준이 아닙니다.

상세 문서: [출처와 근거](skills/research-presentation/references/sources.md) · [유형별 작성 가이드](skills/research-presentation/references/presentation-guide.md) · [제작·검토 절차](skills/research-presentation/references/production-review.md) · [기존 검증 기록](skills/research-presentation/references/validation.md)

### humanizer — 한국어·영어 문체 편집

| 참고 자료 | 자료 유형 | 반영한 내용과 한계 |
| --- | --- | --- |
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | 위키백과 편집자의 관찰 | 과장, 모호한 권위, 반복 대조, 정형적 전망, 과도한 서식 등. 정책이나 AI 판별 규칙이 아닙니다. |
| [*Do LLMs write like humans? Variation in grammatical and rhetorical styles*](https://doi.org/10.1073/pnas.2422455122). PNAS (2025). [arXiv](https://arxiv.org/abs/2410.16107) | 영어 문체 비교 연구 | 문법적 선호와 장르별 문체 차이. 조사한 모델·시점·언어의 범위를 넘어 일반화하지 않습니다. |
| [*Delving into LLM-assisted writing in biomedical publications through excess vocabulary*](https://doi.org/10.1126/sciadv.adt3813). Science Advances (2025). [arXiv](https://arxiv.org/abs/2406.07016) | 영어 의생명 논문 초록의 어휘 변화 연구 | 집합적 어휘 변화에 대한 관찰. 개별 글의 AI 사용 여부를 판별하는 근거가 아닙니다. |

한국어 표현·전후 예문·편집 방법은 스킬 작성자의 적용 제안입니다. 영어 연구에서 검증된 한국어 판별 지표로 제시하지 않습니다. 특정 단어를 일괄 삭제하거나 AI 탐지기 점수·통과를 보장하지 않습니다.

상세 문서: [패턴과 근거](skills/humanizer/references/patterns.md)

## 저장소 구조

```text
research-skills/
├── README.md
└── skills/
    ├── scientific-paper-writing/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    ├── scientific-figure/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   ├── assets/nature_template.py
    │   └── references/
    ├── research-presentation/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    └── humanizer/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/patterns.md
```

## 의존성과 업데이트

| 작업 | 필요한 환경 |
| --- | --- |
| 논문·문체 편집, 발표 구성·검토 | 스킬을 읽고 적용할 수 있는 Codex 환경 |
| Figure 템플릿 실행 | Python, NumPy, Matplotlib |
| 실제 `.pptx` 생성·편집 | 발표 스킬이 참조하는 별도 `slides` 스킬과 제작·렌더링 의존성 |

Figure 템플릿은 합성 데이터 예제입니다. 스킬 설치는 Python·Node 패키지, 글꼴이나 렌더링 도구의 설치를 대신하지 않습니다.

발표 스킬에서 참조한 제작 도구는 [OpenAI skills의 `slides`](https://github.com/openai/skills/tree/e6afb0d74cc75d220df2faf3dd6c635c2dc6a108/skills/.curated/slides)이며, 고정 커밋은 `e6afb0d74cc75d220df2faf3dd6c635c2dc6a108`입니다. 이 저장소에는 해당 도구를 포함하지 않습니다. 별도로 설치할 때는 원본의 Apache-2.0 `LICENSE.txt`와 안내를 따릅니다. 이 라이선스 표기는 외부 `slides` 도구에 대한 것입니다.

저장소의 변경 사항이 이미 설치된 스킬에 자동 반영되지는 않습니다. 업데이트할 때는 기존 설치본의 로컬 수정 여부를 확인하고 새 버전과 비교합니다. 설치 도구는 같은 이름의 대상 폴더가 있으면 중단할 수 있습니다. 재현 가능한 설치가 필요하면 브랜치 대신 커밋을 지정합니다.

기존 검증 기록의 로컬 산출물 경로는 작성 환경의 과거 기록입니다. 원본 연구 데이터·계산 출력·인증정보·검증 실행 환경은 배포하지 않으며, 기록만으로 다른 PC의 실행이나 Microsoft PowerPoint 호환성을 보증하지 않습니다.

## 출처 표기와 기여

참고 자료의 저작권과 이용 조건은 각 원문에 따릅니다. 이 README와 `references/`는 활용한 원칙과 확인 범위를 설명하며, 책·강의·논문 전체의 복제본을 제공하지 않습니다. 이 자료들은 스킬의 작성·편집 원칙에 대한 근거이며, 사용자 연구 결과의 과학적 인용으로 자동 추가하지 않습니다.

오류·개선 제안은 [Issues](https://github.com/YHKlab-MSJeong/research-skills/issues) 또는 Pull Request로 남겨 주세요. 참고 자료나 지침을 수정할 때는 원문 링크, 반영할 내용, 적용 범위와 한계를 함께 적어 주세요.
