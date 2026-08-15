# P-CAB Intelligence Hub — 참고 템플릿 구조 노트

원본 파일: `reference/pcab-hub-template.html` (단일 HTML, ~98KB, 순수 HTML/CSS/JS, 프레임워크 없음)

이 문서는 Diabetes Hub(SGLT-2, SGLT-1,2 inhibitor)를 만들 때 동일 구조를 재사용하기 위한 요약입니다. 원본 HTML은 파일 크기가 크므로 전체를 다시 읽기보다 이 노트를 먼저 참고할 것.

## 전체 컨셉
당뇨약 대신 위식도역류질환/PPI/P-CAB 계열 약제(자스타프라잔 등)를 다루는 "medical intelligence hub". PubMed 등에서 수집한 최신 문헌을 주간 단위로 업데이트하고, 근거 수준·안전성 신호·경쟁 약물 간 비교를 한 화면에서 볼 수 있게 구성.

## 디자인 시스템
- 폰트: Noto Sans KR (Google Fonts)
- 컬러: 네이비(--navy-900~600) + 오렌지 포인트(--orange, --orange-dk, --orange-lt) + 크림 배경(--cream)
- 카드형 레이아웃, radius 13px, 은은한 shadow(--shadow)
- 레벨 뱃지(.lvl.hi/md/lo — 높음/중간/낮음 근거수준), 근거유형 태그(.tag RCT/Meta/NMA/SR/GL)
- 상단 헤더 + sticky 탭바(폴더 탭 스타일, .tab.on에 오렌지 그라디언트)

## 탭(패널) 구성 — data-p 속성으로 전환
1. **Overview (p0)** — 데이터 기준일/총 문헌수/자사약물 관련 문헌수 요약 pill, 핵심 메시지 카드 3열(ovlist/ovrow)
2. **Weekly Update (p1)** — 이번 주 신규 문헌 리스트(테이블), 각 행 클릭 시 초록 요약 펼침(.expand/.abs), 약물 태그·질환 카테고리 태그
3. **News Archive (p1b)** — 월별 아카이브 피커(.mrow/.mbtn), 월별 통계(mstat: 문헌수, 관련 약물 언급 등)
4. **Evidence Intelligence (p2)** — 자사약 vs 경쟁약 메시지 비교 2단 박스(.duo/.box, navy vs orange 헤더)
5. **Evidence Landscape (p3)** — 약물/적응증별 근거 지형 카드 그리드(.lgrid/.lcard), 문헌 수 막대그래프(.lbar 3분할), 약물칩(.dchip)
6. **Safety Signal (p5)** — PPI/P-CAB/자사약 3열 안전성 신호 비교(.safegrid/.sbox), 항목별 근거 인용

## 데이터 바인딩 방식
- `<script>window.APP = {...}</script>` 에 전체 데이터(JSON)를 인라인으로 삽입 (gen, win, total, pcab, weekly[], archive[], cards[], safety[] 등)
- 별도 JS(`const D=window.APP`)가 DOM을 순회하며 각 패널 렌더링 (rich(), bullets(), chipHtml(), refHtml() 등 헬퍼 함수)
- 완전 정적 파일 하나로 배포 가능 (백엔드 불필요, 데이터 갱신 시 APP 객체만 교체)
- 문헌 레코드 필드 예: `pd`(게재일), `t`(제목), `j`(저널/DOI), `a`(저자), `u`(URL), `id`(PMID/DOI), `ty`(문헌유형), `c`(질환카테고리), `s`(상세요약), `d`(관련약물 배열), `sum`(짧은 요약)

## Diabetes Hub 적용 시 변경 포인트
- 약물군: P-CAB(자스타프라잔 등) → SGLT-2 inhibitor / SGLT-1,2 inhibitor 계열로 교체
- 안전성 신호 3열: PPI/P-CAB/자사약 → 예: 타 계열 당뇨약/SGLT-2 계열/자사 SGLT-1,2 계열 식으로 재구성 검토 필요
- 질환 카테고리(c 필드): GERD, H.pylori 등 → 당뇨병, 심부전, 만성신질환(CKD), 체중감량 등으로 교체
- 데이터 소스: PubMed 검색 쿼리를 SGLT 계열 약물명으로 교체
- 문헌 근거 수준 판정 로직(높음/중간/낮음)은 그대로 재사용 가능
