import json, re, os
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
DATA_DIR = os.path.join(BASE, 'data')

rows = json.load(open(os.path.join(DATA_DIR, 'diabetes_hub_data.json'), encoding='utf-8'))

# ---- drug classification ----
DRUG_PATTERNS = {
    'Dapagliflozin': re.compile(r'다파글리플로진|dapagliflozin|forxiga|farxiga', re.I),
    'Empagliflozin': re.compile(r'엠파글리플로진|empagliflozin|jardiance', re.I),
}
OTHER_SGLT2_PATTERNS = {
    'Canagliflozin': re.compile(r'카나글리플로진|canagliflozin|invokana', re.I),
    'Ipragliflozin': re.compile(r'이프라글리플로진|ipragliflozin|suglat', re.I),
    'Ertugliflozin': re.compile(r'에르투글리플로진|ertugliflozin|steglatro', re.I),
    'Luseogliflozin': re.compile(r'루세오글리플로진|luseogliflozin|lusefi', re.I),
    'Tofogliflozin': re.compile(r'토포글리플로진|tofogliflozin|deberza|apleway', re.I),
    'Enavogliflozin': re.compile(r'에나보글리플로진|enavogliflozin', re.I),
    'Bexagliflozin': re.compile(r'벡사글리플로진|bexagliflozin|brenzavvy', re.I),
    'Remogliflozin': re.compile(r'레모글리플로진|remogliflozin', re.I),
    'Henagliflozin': re.compile(r'헤나글리플로진|henagliflozin', re.I),
}
DUAL_PATTERNS = {
    'Sotagliflozin': re.compile(r'소타글리플로진|sotagliflozin|inpefa|zynquista', re.I),
    'Licogliflozin': re.compile(r'리코글리플로진|licogliflozin', re.I),
}

def classify(row):
    text = (row['title'] or '') + ' ' + (row['abstract'] or '')
    hits = set()
    for name, pat in DRUG_PATTERNS.items():
        if pat.search(text):
            hits.add(name)
    for name, pat in OTHER_SGLT2_PATTERNS.items():
        if pat.search(text):
            hits.add('기타 SGLT-2 inhibitor')
    for name, pat in DUAL_PATTERNS.items():
        if pat.search(text):
            hits.add('SGLT-1,2 inhibitor')
    cats = row.get('category') or []
    if not hits:
        if 'SGLT-1/2' in cats:
            hits.add('SGLT-1,2 inhibitor')
        elif 'SGLT-2 inhibitor' in cats:
            hits.add('기타 SGLT-2 inhibitor')
    return sorted(hits)

DRUG_ORDER = ['Dapagliflozin', 'Empagliflozin', '기타 SGLT-2 inhibitor', 'SGLT-1,2 inhibitor']

for r in rows:
    r['drugs'] = classify(r)

# ---- stats ----
drug_counts = Counter()
for r in rows:
    for d in r['drugs']:
        drug_counts[d] += 1

cat_counts = Counter()
for r in rows:
    for c in (r['category'] or []):
        cat_counts[c] += 1

doc_type_counts = Counter(r['doc_type'] for r in rows)

print('TOTAL', len(rows))
print('DRUG COUNTS', dict(drug_counts))
print('CATEGORY COUNTS', dict(cat_counts))
print('DOC TYPE', dict(doc_type_counts))

no_drug = [r for r in rows if not r['drugs']]
print('no-drug-tagged rows:', len(no_drug))

json.dump(rows, open(os.path.join(DATA_DIR, 'diabetes_hub_classified.json'), 'w'), ensure_ascii=False)
