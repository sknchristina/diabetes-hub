"""
노션 DB("🍭 당뇨/대사질환 문헌 업데이트")에서 문헌 레코드를 가져와
transform.py가 기대하는 형식의 data/diabetes_hub_data.json 으로 저장한다.

필요 환경변수:
  NOTION_TOKEN   Notion Internal Integration의 시크릿 토큰
                 (해당 데이터베이스에 이 Integration이 "연결"되어 있어야 함:
                  노션 페이지 우측 상단 ··· → Connections → Integration 추가)

사용법:
  export NOTION_TOKEN=secret_xxx
  python pipeline/fetch_notion.py
"""
import json
import os
import sys
import urllib.request
import urllib.error

# 데이터베이스 URL: https://app.notion.com/p/eec6ccd35f7b477b9d3822510da7a4bc
# fetch 결과에서 확인한 Data Source ID:
DATA_SOURCE_ID = "671f806d-e96b-422e-bc68-07dd47cd6bdd"

NOTION_VERSION = "2025-09-03"  # data source 기반 신규 API
API_BASE = "https://api.notion.com/v1"

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
DATA_DIR = os.path.join(BASE, "data")

DOC_TYPE_MAP = {
    "임상논문": "임상논문",
    "임상시험": "임상시험",
    "진료지침": "진료지침",
}


def _request(url, token, payload=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Notion API 오류 {e.code}: {body}")


def _plain_text(rich_text_list):
    return "".join(t.get("plain_text", "") for t in (rich_text_list or []))


def _prop(props, name, kind):
    p = props.get(name)
    if not p:
        return None
    if kind == "title":
        return _plain_text(p.get("title"))
    if kind == "rich_text":
        return _plain_text(p.get("rich_text"))
    if kind == "url":
        return p.get("url")
    if kind == "select":
        sel = p.get("select")
        return sel.get("name") if sel else None
    if kind == "multi_select":
        return [o.get("name") for o in (p.get("multi_select") or [])]
    if kind == "date":
        d = p.get("date")
        return d.get("start") if d else None
    return None


def fetch_all_rows(token):
    rows = []
    cursor = None
    while True:
        payload = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        result = _request(f"{API_BASE}/data_sources/{DATA_SOURCE_ID}/query", token, payload)
        for page in result.get("results", []):
            props = page.get("properties", {})
            row = {
                "title": _prop(props, "논문 제목", "title") or "",
                "abstract": _prop(props, "초록 요약", "rich_text") or "",
                "category": _prop(props, "카테고리", "multi_select") or [],
                "doc_type": DOC_TYPE_MAP.get(_prop(props, "자료유형", "select"), _prop(props, "자료유형", "select")),
                "added_date": _prop(props, "노션 등록일", "date"),
                "pub_date": _prop(props, "출판연월", "rich_text") or "",
                "journal": _prop(props, "저널명 및 서지사항", "rich_text") or "",
                "authors": _prop(props, "저자명", "rich_text") or "",
                "url": _prop(props, "논문 링크", "url") or "",
                "pmid_doi": _prop(props, "PMID_DOI", "rich_text") or "",
            }
            rows.append(row)
        if not result.get("has_more"):
            break
        cursor = result.get("next_cursor")
    return rows


def main():
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        sys.exit("NOTION_TOKEN 환경변수가 설정되어 있지 않습니다.")

    rows = fetch_all_rows(token)
    os.makedirs(DATA_DIR, exist_ok=True)
    out_path = os.path.join(DATA_DIR, "diabetes_hub_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=None)

    print(f"{len(rows)}건 저장 완료: {out_path}")


if __name__ == "__main__":
    main()
