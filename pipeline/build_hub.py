import json, re, sys, os, datetime
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
DATA_DIR = os.path.join(BASE, 'data')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # so analysis_content imports
from analysis_content import ANALYSIS_GROUPS, WEEKLY_ANALYSIS, HALF_YEAR_ANALYSIS, SAFETY_SIGNAL_WEEKLY, SAFETY_SIGNAL_HALFYEAR, OVERVIEW_BRIEF, GUIDELINES

rows = json.load(open(os.path.join(DATA_DIR, 'diabetes_hub_classified.json'), encoding='utf-8'))

DRUG_ORDER = ['Dapagliflozin', 'Empagliflozin', '기타 SGLT-2 inhibitor', 'SGLT-1,2 inhibitor']
CAT_ORDER = ['Diabetes','SGLT-2 inhibitor','SGLT-1/2','CKM','MASLD','Obesity','Metabolic syndrome','diabetic comorbidity','hypoglycemic agents']

def short_sum(s, n=110):
    s = (s or '').strip()
    if len(s) <= n: return s
    cut = s[:n]
    return cut.rsplit(' ',1)[0] + '…'

def half_year_key(date_str):
    if not date_str: return None
    y, m = date_str[:4], int(date_str[5:7])
    return f"{y}-{'H1' if m<=6 else 'H2'}"

def rec(r):
    return {
        'pd': r['added_date'],
        'pub': r['pub_date'],
        't': r['title'],
        'j': r['journal'],
        'a': r['authors'],
        'u': r['url'],
        'id': r['pmid_doi'],
        'ty': r['doc_type'],
        'c': (r['category'] or [])[:3],
        'd': r['drugs'],
        's': r['abstract'],
        'sum': short_sum(r['abstract']),
    }

def group_membership(r):
    """which of the 4 analysis groups this record belongs to"""
    g = set()
    if any(d in r['drugs'] for d in ('Dapagliflozin','Empagliflozin','기타 SGLT-2 inhibitor')):
        g.add('SGLT-2 inhibitor(전체)')
    if 'Dapagliflozin' in r['drugs']: g.add('Dapagliflozin')
    if 'Empagliflozin' in r['drugs']: g.add('Empagliflozin')
    if 'SGLT-1,2 inhibitor' in r['drugs']: g.add('SGLT-1,2 inhibitor')
    return g

all_dates = sorted(set(r['added_date'] for r in rows if r['added_date']))
latest_date = all_dates[-1]
weekly_rows = [r for r in rows if r['added_date'] == latest_date]
weekly_rows.sort(key=lambda r: r['title'])

# ---- half-year archive ----
hy_keys = sorted(set(half_year_key(r['added_date']) for r in rows if r['added_date']), reverse=True)
half_years = []
for hy in hy_keys:
    items = [r for r in rows if half_year_key(r['added_date']) == hy]
    dt_counts = Counter(r['doc_type'] for r in items)
    drug_counts = Counter()
    for r in items:
        for dr in r['drugs']:
            drug_counts[dr] += 1
    items_sorted = sorted(items, key=lambda r: r['added_date'] or '', reverse=True)
    hy_meta = HALF_YEAR_ANALYSIS.get(hy, {})
    analysis = {}
    for g in ANALYSIS_GROUPS:
        a = hy_meta.get(g)
        if a:
            analysis[g] = a
    safety = {}
    for g in ANALYSIS_GROUPS:
        s = SAFETY_SIGNAL_HALFYEAR.get(hy, {}).get(g)
        if s is not None:
            safety[g] = s
    half_years.append({
        'key': hy,
        'label': hy_meta.get('label', hy),
        'n': len(items),
        'docType': dict(dt_counts),
        'drugCounts': dict(drug_counts),
        'analysis': analysis,
        'safety': safety,
        'items': [rec(r) for r in items_sorted],
    })

# ---- landscape cards ----
cards = []
for drug in DRUG_ORDER:
    items = [r for r in rows if drug in r['drugs']]
    dt_counts = Counter(r['doc_type'] for r in items)
    cat_counts = Counter()
    for r in items:
        for c in (r['category'] or []):
            cat_counts[c] += 1
    items_sorted = sorted(items, key=lambda r: r['added_date'] or '', reverse=True)
    cards.append({
        'drug': drug,
        'n': len(items),
        'docType': dict(dt_counts),
        'topCats': cat_counts.most_common(5),
        'recent': [rec(r) for r in items_sorted[:8]],
    })

cat_counts = Counter()
for r in rows:
    for c in (r['category'] or []):
        cat_counts[c] += 1

doc_type_counts = Counter(r['doc_type'] for r in rows)
drug_total_counts = Counter()
for r in rows:
    for d in r['drugs']:
        drug_total_counts[d] += 1

sglt_related = len([r for r in rows if r['drugs']])

# ---- cumulative safety (all periods to date, merged; later period overrides same-label item) ----
cumulative_safety = {g: {} for g in ANALYSIS_GROUPS}
for hy in sorted(SAFETY_SIGNAL_HALFYEAR.keys()):  # chronological ascending so later periods win on label collision
    for g in ANALYSIS_GROUPS:
        for item in SAFETY_SIGNAL_HALFYEAR[hy].get(g, []):
            cumulative_safety[g][item['label']] = item
cumulative_safety = {g: list(v.values()) for g, v in cumulative_safety.items()}

# ---- weekly analysis (grounded, hand-authored per refresh) ----
weekly_analysis = {}
weekly_safety = {}
for g in ANALYSIS_GROUPS:
    a = WEEKLY_ANALYSIS.get(g)
    if a:
        weekly_analysis[g] = a
    s = SAFETY_SIGNAL_WEEKLY.get(g)
    if s is not None:
        weekly_safety[g] = s

APP = {
    'gen': datetime.date.today().isoformat(),
    'latestBatch': latest_date,
    'total': len(rows),
    'sgltRelated': sglt_related,
    'docType': dict(doc_type_counts),
    'catCounts': {k: cat_counts.get(k,0) for k in CAT_ORDER},
    'drugCounts': {k: drug_total_counts.get(k,0) for k in DRUG_ORDER},
    'analysisGroups': ANALYSIS_GROUPS,
    'overview': OVERVIEW_BRIEF,
    'weekly': {
        'date': latest_date,
        'n': len(weekly_rows),
        'analysis': weekly_analysis,
        'safety': weekly_safety,
        'items': [rec(r) for r in weekly_rows],
    },
    'halfYears': half_years,
    'cards': cards,
    'safetyCumulative': cumulative_safety,
    'guidelines': GUIDELINES,
}

json.dump(APP, open(os.path.join(DATA_DIR, 'app_data.json'), 'w'), ensure_ascii=False)
print('weekly count', len(weekly_rows))
print('half-year buckets', [(h['key'], h['n']) for h in half_years])
print('cards', [(c['drug'], c['n']) for c in cards])
print('total size bytes', len(json.dumps(APP, ensure_ascii=False)))
