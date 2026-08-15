"""전체 파이프라인을 순서대로 실행: (fetch_notion) -> transform -> build_hub -> render_hub

NOTION_TOKEN 환경변수가 설정되어 있으면 노션에서 최신 데이터를 먼저 가져온다.
설정되어 있지 않으면 data/diabetes_hub_data.json이 이미 존재한다고 가정하고
바로 transform 단계부터 진행한다(로컬에서 수동으로 데이터를 넣어 테스트할 때 유용).
"""
import runpy
import os

HERE = os.path.dirname(os.path.abspath(__file__))

steps = []
if os.environ.get('NOTION_TOKEN'):
    steps.append('fetch_notion.py')
steps += ['transform.py', 'build_hub.py', 'render_hub.py']

for step in steps:
    print(f'--- {step} ---')
    runpy.run_path(os.path.join(HERE, step), run_name='__main__')
