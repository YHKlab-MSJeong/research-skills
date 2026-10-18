# 출처와 적용 범위

원문 확인일: **2026-10-18**. 아래는 짧은 요약이며 원문 복제본이 아니다. 설계 권고, 지각 실험, 학술지 요구사항을 구분한다. 실제 제출 규정은 해당 저널·그림 유형에서 다시 확인한다.

| 출처 | 자료 유형 | 이 스킬에서 사용하는 근거와 한계 |
|---|---|---|
| [MIT·Harvard Broad Institute: Figure Design](https://mitcommlab.mit.edu/broad/commkit/figure-design/) | 기관 교육 지침 | 독자·매체·메시지·증거에 맞는 그래프와 다중 패널, 불필요한 시각 정보 줄이기. 실험적 효과 크기를 제공하는 연구나 저널 제출 규정은 아님. |
| [Nature Methods: Points of View 모음](https://blogs.nature.com/methagora/2013/07/data-visualization-points-of-view.html) | 전문가 해설 시리즈; 2013 게시, 이후 갱신 | 배치·여백·색·타이포그래피·축·기호·모식도 등의 맥락별 설계. 링크된 개별 글의 전문을 모두 확인했다고 주장하지 않음. |
| [Rougier, Droettboom & Bourne (2014): Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833) | PLOS Computational Biology, 실용 Editorial; DOI: 10.1371/journal.pcbi.1003833 | 독자·메시지·매체, 기본값 검토, 색상·왜곡 방지·불필요한 장식 줄이기. 모든 스타일을 고정하는 규칙이나 통제 실험으로 취급하지 않음. |
| [Heer & Bostock (2010): Crowdsourcing Graphical Perception](https://hci.stanford.edu/publications/paper.php?id=142), [연구진 공개 PDF](https://idl.cs.washington.edu/files/2010-MTurk-CHI.pdf) | Stanford 연구진의 CHI 지각 실험; DOI: 10.1145/1753326.1753357 | 공간 인코딩·명도 대비 연구 재현 및 면적·차트 크기·격자 실험. 비교 과제별 정확도의 근거이며 모든 맥락에 동일한 순위를 강제하지 않음. |
| [Crameri, Shephard & Heron (2020): The misuse of colour in science communication](https://www.nature.com/articles/s41467-020-19160-7) | Nature Communications, Perspective; DOI: 10.1038/s41467-020-19160-7 | 지각적으로 불균일한 색상표가 가짜 경계·강조와 세부 손실을 만드는 문제. 데이터 의미에 맞는 순차·발산·순환 색상과 색각 접근성의 근거. |
| [Weissgerber et al. (2015): Beyond Bar and Line Graphs](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128) | PLOS Biology, 소표본 연속형 데이터의 표현 관행 검토; DOI: 10.1371/journal.pbio.1002128 | 요약 통계 뒤에 가려진 분포와 paired data의 문제, 개별 관측값 제시. 결정론적 계산에 표본 분포를 만들어 적용하지 않음. |
| [Nature: Preparing figures — our specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) | 공식 artwork 규격 | 축·단위, 5–7 pt 일반 글자, 8 pt 패널 표시, sans-serif·폰트 embedding, 벡터·RGB·raster 해상도. Nature main figure 프로필의 규격 근거. |
| [Nature: Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/) | 공식 artwork 규격 | 89/183 mm 너비, 최대 170 mm 높이, 패널 구성, 접근성 팔레트, main figure와 Extended Data 형식의 차이. |
| [Nature: Formatting guide](https://www.nature.com/nature/for-authors/formatting-guide), [Initial submission](https://www.nature.com/nature/for-authors/initial-submission) | 공식 원고·제출 안내 | 논리적으로 연결된 패널, 불필요한 복잡성 줄이기, 독립적으로 해석 가능한 캡션과 표본·오차 정의. 일반 안내의 90/180 mm와 상세 artwork 안내가 달라 기본 너비는 후자를 채택. |
| [Nature: Image Integrity](https://research-figure-guide.nature.com/figures/image-integrity/) | 공식 이미지 무결성 지침 | 원 데이터의 충실한 표현, 합성·삽입 경계 표시, 선택적 삭제·보정·생성형 이미지 편집 회피. 이 스킬은 Nature용 asset에 생성형 래스터 도구를 사용하지 않음. |

## 갱신과 인용

- 대상 저널의 규정과 이 파일의 요약이 다르면 최신 공식 지시를 우선하고 적용한 차이를 설명한다. 확인하지 못한 규정은 미확인으로 보고한다.
- 설계 원칙을 인용할 때는 해당 자료를 직접 연결한다. 연구논문의 캡션·본문에 이 자료들을 관성적으로 삽입하지 않는다.
- 선 0.7 pt, 축 0.5 pt, 기본 높이 60 mm, 기본 colormap, PNG 450 dpi는 스킬의 구현 선택이다. 이를 Nature의 일률적 필수 수치로 인용하지 않는다.
