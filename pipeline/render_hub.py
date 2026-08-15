"""
templates/app_pipeline_template.html 안의 `/*__APP_DATA__*/` 자리표시자에
data/app_data.json 내용을 주입해 배포용 정적 HTML(docs/index.html)을 생성한다.

실행 순서: transform.py -> build_hub.py -> render_hub.py
(또는 저장소 루트에서 `python pipeline/run_all.py` 한 번에 실행)
"""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
DATA_DIR = os.path.join(BASE, 'data')
TEMPLATE_PATH = os.path.join(BASE, 'templates', 'app_pipeline_template.html')
OUTPUT_PATH = os.path.join(BASE, 'docs', 'index.html')

PLACEHOLDER = '/*__APP_DATA__*/'

with open(os.path.join(DATA_DIR, 'app_data.json'), encoding='utf-8') as f:
    app_data = json.load(f)

with open(TEMPLATE_PATH, encoding='utf-8') as f:
    template = f.read()

if PLACEHOLDER not in template:
    raise SystemExit(f'템플릿에서 {PLACEHOLDER} 자리표시자를 찾을 수 없습니다.')

html = template.replace(PLACEHOLDER, json.dumps(app_data, ensure_ascii=False))

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'생성 완료: {OUTPUT_PATH} ({len(html):,} bytes)')
