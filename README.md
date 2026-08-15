# Diabetes / SGLT-2·SGLT-1,2 Intelligence Hub

PubMed 등에서 수집한 SGLT-2 / SGLT-1,2 inhibitor 관련 최신 문헌을 주간 단위로 정리해
단일 정적 HTML 페이지("hub")로 배포하는 파이프라인입니다. `reference/` 폴더의 P-CAB 버전
구조를 그대로 재사용해 만들었습니다.

원본 문헌 데이터는 노션 데이터베이스("🍭 당뇨/대사질환 문헌 업데이트")에서 관리되며,
`pipeline/fetch_notion.py`가 Notion API로 이를 가져와 파이프라인에 넘깁니다.

## 폴더 구조

```
pipeline/     데이터 처리 스크립트
  fetch_notion.py   노션 DB에서 문헌 데이터를 가져와 data/diabetes_hub_data.json 생성
  transform.py      원본 수집 데이터에 약물/카테고리 태깅
  build_hub.py      태깅된 데이터 + 수기 작성 분석(analysis_content.py)을 합쳐 app_data.json 생성
  analysis_content.py  주간/반기 분석 코멘트, 안전성 신호, 가이드라인 등 수기 콘텐츠
  render_hub.py     app_data.json을 템플릿에 주입해 최종 docs/index.html 생성
  run_all.py        위 단계를 순서대로 실행하는 진입점 (NOTION_TOKEN이 있으면 fetch부터, 없으면 transform부터)

templates/    HTML 템플릿 (데이터 자리표시자 `/*__APP_DATA__*/` 포함)
reference/    원본 P-CAB 버전 템플릿 및 구조 노트 (신규 hub 제작 시 참고용)
data/         주차별 원본/가공 데이터 (diabetes_hub_data.json, *_classified.json, app_data.json)
docs/         빌드된 최종 정적 페이지 — GitHub Pages가 이 폴더를 서빙
```

## 노션 연동 설정 (최초 1회)

1. [notion.so/my-integrations](https://www.notion.so/my-integrations)에서 Internal Integration 생성 → Secret 토큰 복사
2. 노션에서 "🍭 당뇨/대사질환 문헌 업데이트" 데이터베이스 페이지 우측 상단 `···` → **Connections** → 방금 만든 Integration 추가 (이 단계가 없으면 API가 403을 반환합니다)
3. GitHub 저장소 Settings → Secrets and variables → Actions → New repository secret
   - Name: `NOTION_TOKEN`
   - Value: 위에서 복사한 시크릿 토큰

이후 워크플로가 매주 자동으로, 또는 로컬에서 `NOTION_TOKEN` 환경변수를 설정한 채
`python pipeline/run_all.py`를 실행하면 노션 최신 데이터로 전체 파이프라인이 돕니다.

## 로컬 실행

```bash
pip install -r requirements.txt

# 노션에서 최신 데이터를 가져와 전체 파이프라인 실행
export NOTION_TOKEN=secret_xxx
python pipeline/run_all.py

# 또는 data/diabetes_hub_data.json이 이미 있다면 (fetch 생략)
python pipeline/run_all.py
```

완료되면 `docs/index.html`이 갱신됩니다.

## 주간 업데이트 절차 (자동)

`.github/workflows/build-and-deploy.yml`이 매주 일요일 22:00 UTC(월요일 07:00 KST)에:
1. 노션에서 최신 문헌 데이터를 가져오고 (`fetch_notion.py`)
2. 약물/카테고리 태깅 → `app_data.json` 생성 → `docs/index.html` 렌더링
3. 변경사항을 자동 커밋하고 GitHub Pages에 배포

`pipeline/analysis_content.py`의 수기 분석 코멘트(주간/반기 요약, 안전성 신호 등)는
자동화 대상이 아니므로, 새로운 분석 코멘트가 필요하면 해당 파일을 직접 수정해 push하세요.

## GitHub Pages 설정

저장소 Settings → Pages → Source를 "GitHub Actions"로 지정하면
위 워크플로가 실행될 때마다 자동 배포됩니다.

## 참고

- `docs/index.html`은 데이터가 인라인으로 포함된 단일 파일이라 매주 diff가 큽니다.
  이력 추적이 중요하다면 `data/app_data.json`의 변경 이력을 기준으로 보는 것이 더 유용합니다.
- 노션 API 무료/일부 플랜은 초당 요청 수 제한이 있습니다. 문헌 수(현재 800건대)가
  크게 늘어나 페이지네이션 호출이 많아지면 `fetch_notion.py`에 재시도 로직을 추가하는 것을 고려하세요.
