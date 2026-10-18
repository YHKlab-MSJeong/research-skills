# Nature 기본 프로필

확인일: 2026-10-18. 기본 대상은 **Nature 본지 main figure**다. Nature 계열 전체, Extended Data, supplementary figure에 같은 규격을 적용하지 않는다. 실제 투고 규격을 확인하는 작업에서는 해당 저널·그림 유형의 최신 공식 안내를 다시 확인한다. 일반 제작 때 매번 검색할 필요는 없다.

## 공식 규격과 자체 기본값

아래 공식 규격은 [Preparing figures](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/)와 [Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/)를 기준으로 한다.

| 항목 | 공식 안내 | 템플릿 기본값 |
|---|---|---|
| 너비 | 상세 figure guide: 단일 열 89 mm, 이중 열 183 mm | 89 mm; `--width double`이면 183 mm |
| 높이 | 최대 170 mm | 단일 그래프 60 mm; 구성에 맞게 조정 |
| 일반 글자 | 5–7 pt, 읽을 수 있고 편집 가능 | 7 pt |
| 다중 패널 표시 | 8 pt bold, upright, lowercase a, b, c | 다중 패널 제작 시 별도 적용 |
| 글꼴 | sans-serif, Arial·Helvetica 선호 | Arial → Helvetica → Liberation Sans → DejaVu Sans |
| 데이터 선·축 | 모든 그림에 대한 고정 수치로 취급하지 않음 | 데이터 선 0.7 pt, 축·눈금 0.5 pt, marker 3 pt |
| 축·눈금 | 축선·눈금, 물리량과 괄호 안 단위 | 표시; 과학적 기준선은 필요할 때 추가 |
| 격자·장식 | 배경 격자·불필요한 장식·그림자 등 회피 | 흰 배경, 격자 없음 |
| 색상 | 접근성 있는 팔레트, RGB | 아래 범주형 팔레트; 순차형 `cividis`, 부호 차이에 `RdBu_r` |
| main figure 파일 | 편집 가능한 벡터 파일, PDF 등 선호 | PDF 제출 후보 + 450 dpi PNG 미리보기 |

일반 formatting guide에는 너비가 90/180 mm로도 안내된다. 이 스킬은 구체적인 artwork용 상세 figure guide의 **89/183 mm**를 채택한다. 저널에서 별도 지시가 오면 그 지시를 우선한다.

폰트가 없으면 실제 사용한 대체 글꼴과 이유를 보고한다. Liberation Sans와 DejaVu Sans는 실행 가능한 로컬 대안이며 Nature가 그 글꼴을 선호한다고 표현하지 않는다. 글꼴을 자동 다운로드·설치하지 않는다. 대체 글꼴 사용 시 Arial 사용 또는 완전한 제출 규격 준수를 보증하지 않는다.

## 색상

[Nature 가이드의 예시 팔레트](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/)는 다음과 같다. 순서는 템플릿의 자체 선택이다.

| 색 | Hex |
|---|---|
| Blue | `#0072B2` |
| Vermillion | `#D55E00` |
| Bluish green | `#009E73` |
| Reddish purple | `#CC79A7` |
| Orange | `#E69F00` |
| Sky blue | `#56B4E9` |
| Black | `#000000` |
| Yellow | `#F0E442` |

흰 배경에서 노랑의 가는 선·작은 점은 피하고 색상과 선 종류·기호를 함께 활용한다. 이 팔레트 선택만으로 모든 그림의 접근성 검증이 완료되지는 않는다. `RdBu_r`에 지각적 완전 균일성을 주장하지 않는다. signed heatmap은 물리적으로 의미 있는 0을 중심으로 `TwoSlopeNorm` 등을 사용하고 colorbar에 단위를 표시한다.

## 내보내기

- `pdf.fonttype=42`, `ps.fonttype=42`, `svg.fonttype='none'`으로 텍스트를 보존한다. SVG에 남은 텍스트는 열람 환경에도 해당 글꼴이 있어야 한다. 실제 PDF의 글꼴 embedding·Type 3 여부·텍스트 추출을 확인한다.
- 그림의 캔버스를 최종 mm 크기로 만든다. `bbox_inches='tight'`는 내보낸 페이지 크기를 바꿀 수 있으므로 템플릿은 사용하지 않는다. 레이아웃 안에서 레이블을 배치하고 잘림을 확인한다.
- 선·텍스트·화살표는 벡터로 유지한다. heatmap 등 raster가 필요한 부분은 그 부분만 rasterize할 수 있다. PNG를 PDF 안에 넣었다는 이유로 편집 가능한 벡터 그래프라 부르지 않는다.
- 공식 가이드는 사진에 최소 300 dpi, export 항목에는 이미지 최소 450 dpi를 안내한다. 여기서는 **최종 크기에서 raster 요소와 미리보기에 450 dpi**를 기본으로 선택한다. 원본 해상도가 부족하면 업샘플링으로 세부 정보가 복구되지 않음을 알린다.
- PNG는 내부 확인용이다. Nature main figure의 제출 파일로 그대로 안내하지 않는다. 모식도 SVG에는 외부 링크 이미지 대신 필요한 자원을 포함하고 텍스트와 도형을 보존한다.
- Extended Data는 별도의 파일 형식·해상도·크기 규정이 있으므로 이 main-figure export 설정을 자동으로 재사용하지 않는다.

## 템플릿 사용

[nature_template.py](../assets/nature_template.py)는 Python·NumPy·Matplotlib만 사용하는 독립 예제다. 데이터 파서나 과학적 분석 도구는 포함하지 않는다.

```bash
python nature_template.py --output-dir /tmp/my-figure-demo --width single
```

예제는 명시적으로 표시된 **합성 데이터**로 `synthetic_demo.pdf`와 `synthetic_demo.png`를 생성한다. 기존 대상 파일이나 symlink가 있으면 모두 쓰기 전에 거부한다. 실행할 때 지정한 출력 위치와 필요한 Matplotlib 캐시만 사용하며 외부 프로그램·계산·네트워크를 호출하지 않는다.

실제 작업에는 예제를 복사하고 `build_demo()`를 실제 데이터 로드·plotting 코드로 교체한다. `nature_rc()`와 `figure_size()`를 `matplotlib.rc_context` 안에서 사용하고 `save_figure()`에 별도 출력 stem을 전달한다. import만으로 그림을 생성하거나 전역 rcParams를 바꾸지 않는다. 좁은 서식 수정에는 이 템플릿을 통째로 적용하지 않는다.
