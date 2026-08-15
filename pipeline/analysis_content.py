# Hand-authored (LLM-synthesized from actual abstracts) trend / key-message / safety analysis.
# This must be re-authored by an LLM reading the newly added literature at each refresh cycle -
# it is NOT auto-derivable from counts alone. See project doc app/pipeline/README for the refresh process.
#
# NOTE ON **markup**: text wrapped in **...** renders as a highlighter-marker effect in the app
# (see richText() in template.html). Use it sparingly on the single most important clause/figure
# per sentence — not entire sentences — so the highlight still draws the eye.

ANALYSIS_GROUPS = ['SGLT-2 inhibitor(전체)', 'Dapagliflozin', 'Empagliflozin', 'SGLT-1,2 inhibitor']

WEEKLY_ANALYSIS = {
    'SGLT-2 inhibitor(전체)': {
        'n': 8,
        'trend': '이번 주(2026-08-08 등록분) SGLT-2 inhibitor 관련 신규 문헌은 **8건(고유 문헌 6편)**으로, 심부전 영역 후속분석 2건(EMPEROR-Reduced ICD 하위분석, 폐동맥고혈압 예비시험), 요로감염 안전성 메타분석 1건, 수술 전후 관리·신질환 바이오마커·실사용 연구가 각 1건씩 포함되었습니다. 심혈관·신장 보호 효과의 재확인과 안전성 프로파일 정교화가 동시에 진행되는 양상입니다.',
        'key': [
            {'text': '대규모 시험수준 메타분석(RCT 14편)에서 SGLT2억제제와 요로감염 위험 간 **유의한 연관성이 확인되지 않아**(RR 1.08-1.14, 경계선상), 생식기감염과 별개로 요로감염 관련 우려는 근거 수준에서 완화되었습니다.',
             'links': [{'t': 'Are SGLT2 inhibitors really associated with increased urinary tract infection risk? A trial-level meta-analysis', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42566081/'}]},
            {'text': '수술 전 SGLT2억제제를 지속 복용한 경우 심장합병증 발생률이 1.7%로, 중단 기간이 길어질수록(1일 5.7%→3일 이상 **11.5%**) 오히려 위험이 증가하여, 수술 전 중단을 권고하는 현행 가이드라인의 재검토 필요성이 제기되었습니다.',
             'links': [{'t': 'Perioperative discontinuation of SGLT2-inhibitors and cardiac complications after noncardiac surgery', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42270529/'}]},
            {'text': '일본 대규모 코호트(1,818명)에서 SGLT2억제제가 당뇨병성 신질환 환자의 BNP 감소와 **유의하게 연관**되어(OR 1.497) 심부전 바이오마커 개선 근거가 축적되고 있습니다.',
             'links': [{'t': 'B-type natriuretic peptide level reduction and its predictors following SGLT2 inhibitor treatment', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42297213/'}]},
        ],
        'safety': '이번 주 문헌에서는 새로운 위해 신호보다 안전성 우려를 완화하는 방향의 근거(**요로감염 위험 미증가**, 수술 전 중단 시 오히려 높은 심장합병증 위험)가 두드러졌습니다. 정상혈당 케톤산증은 수술 전후 코호트에서 1례만 보고되었습니다.',
    },
    'Dapagliflozin': {
        'n': 1,
        'trend': '이번 주 다파글리플로진 단독 특이적 신규 문헌은 없었으며, 5개 SGLT2억제제를 포괄한 요로감염 메타분석 1건에 함께 포함되었습니다.',
        'key': [
            {'text': '다파글리플로진을 포함한 SGLT2억제제 5종(엠파·다파·카나·에르투·벡사글리플로진) 계열 전반에서 **요로감염 위험 증가가 확인되지 않았습니다**.',
             'links': [{'t': 'Are SGLT2 inhibitors really associated with increased urinary tract infection risk? A trial-level meta-analysis', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42566081/'}]},
        ],
        'safety': '이번 주 특이적 안전성 신호는 보고되지 않았습니다.',
    },
    'Empagliflozin': {
        'n': 3,
        'trend': 'EMPEROR-Reduced 사후분석(ICD 병용 시 급사 위험), 폐동맥고혈압(PAH) 2a상 예비시험, 요로감염 메타분석 각 1건으로, 심부전 영역 근거 축적과 non-HF 적응증 확장 가능성 탐색이 동시에 진행되었습니다.',
        'key': [
            {'text': 'HFrEF 환자에서 ICD와 엠파글리플로진을 병용해도 **급사 위험 감소 효과가 유지**되었습니다(위약군 HR 0.31, 엠파글리플로진군 HR 0.59, 치료군-ICD 상호작용 비유의).',
             'links': [{'t': 'Implantable Cardioverter-Defibrillator Therapy in Contemporary Heart Failure Patients: An Analysis From the EMPEROR-Reduced Trial', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42390420/'}]},
            {'text': 'PAH 2a상 예비시험(8명)에서는 실험모델과 달리 NT-proBNP·기능등급·6분보행거리 등 임상 지표 개선이 확인되지 않았고, **우심실 박출률이 오히려 악화되는 경향**이 관찰되어 PAH로의 적응증 확장에는 신중한 해석이 필요합니다.',
             'links': [{'t': 'Empagliflozin Ameliorates Experimental Pulmonary Vascular Remodeling, but May Not Benefit Patients With Pulmonary Arterial Hypertension (EMPHOWER PoC)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42500881/'}]},
        ],
        'safety': 'PAH 예비시험에서 **우심실 기능 악화 경향**이 보고되어 주의가 필요하나, 8명 규모의 초기단계 연구로 추가 검증이 필요합니다.',
    },
    'SGLT-1,2 inhibitor': {
        'n': 0,
        'trend': '이번 주 SGLT-1,2 inhibitor(소타글리플로진 등) 관련 신규 문헌은 없었습니다.',
        'key': [],
        'safety': '해당 없음.',
    },
}

HALF_YEAR_ANALYSIS = {
    '2026-H2': {
        'label': '2026년 하반기',
        'SGLT-2 inhibitor(전체)': {
            'trend': '2026년 하반기(7~8월) 누적 문헌 기준 SGLT-2 inhibitor 관련 문헌은 **약 120건**으로, 심부전(HFrEF/HFpEF/HFmrEF) 영역이 가장 큰 비중을 차지했고 만성콩팥병, 급성심근경색 후 심근보호, 종양학적 이차효과(폐암·자궁내막암 위험 감소), 노인·허약(frailty) 환자에서의 내약성 등으로 근거가 확장되는 양상입니다.',
            'key': [
                {'text': '만성콩팥병 진행 억제 효과가 당뇨병 치료제 중 **가장 높은 정밀도로 확인**되었습니다(HR 0.66, 95% CI 0.60-0.74; class-level 네트워크 메타분석, RCT 9건 37,749명). 신보호 표준치료로서의 지위가 재확인되었습니다.',
                 'links': [{'t': 'Placebo-Referenced Class-Level Treatment Effects on CKD Progression in Diabetes', 'u': 'https://doi.org/10.1002/edm2.70285'}]},
                {'text': '고령(≥65세) 비투석 만성콩팥병 환자에서도 신장·심혈관 복합결과 위험이 각각 **32%, 26% 감소**하여(RCT 하위군 메타분석) 고령층 적응 확대 근거가 축적되고 있습니다.',
                 'links': [{'t': 'Renal and CV outcomes and safety of SGLT2 inhibitors in patients aged ≥65 years with non-dialysis CKD', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42420866/'}]},
                {'text': '관찰연구 기반으로 폐암(HR 0.84·0.73), 자궁내막암(HR 0.43), 치매(DPP-4i 대비 HR 0.72) 등 **혈당강하 이외의 이차적 이득 신호**가 다수 보고되었으나, 인과관계 확립을 위한 전향적 검증이 필요합니다.',
                 'links': [
                    {'t': 'Reduced Risk of Lung Cancer Associated with SGLT2 Inhibitors in COPD and T2DM', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42508725/'},
                    {'t': 'SGLT2 Inhibitors and Cancer Risk in T2DM: Active Comparator New-User Cohort', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42538609/'},
                    {'t': 'SGLT2 inhibitors with progestins and endometrial cancer risk', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42385610/'},
                    {'t': 'Comparative dementia risk: SGLT2i vs DPP-4i after traumatic brain injury', 'u': 'https://doi.org/10.1016/j.diabres.2026.113445'},
                 ]},
            ],
            'safety': '요로감염 자체의 위험 증가는 메타분석에서 반복적으로 부정되었으나(RR 0.99-1.14), **생식기 진균감염 위험 증가**는 다수 연구에서 일관되게 재확인되었습니다(RR 2.40, 노인 CKD 메타분석; HR 4.29, 대만 코호트). WHO 약물감시 데이터베이스 분석에서는 **포경/감돈포경 보고빈도비가 34.72**로 유의하게 높게 나타나 생식기 국소 이상반응에 대한 주의가 필요합니다. 정상혈당 케톤산증은 드물게 보고되며(수술 전후 코호트 1례 등) 급성신손상 증가 신호는 확인되지 않았습니다. 다만 노쇠한 고령 심부전 환자에서는 6개월 내 약제 불내성(중단·감량) 비율이 노쇠군에서 유의하게 높았습니다(39.2% vs 18.8%, 보정OR 2.31).',
        },
        'Dapagliflozin': {
            'trend': '급성심근경색 후 심부전 예방(RCT), 제1형 당뇨병 3제요법(TTT1 설계), 급성신손상 중환자 안전성(DEFENDER 사후분석), 지질대사(VLDL 동태연구) 등 다양한 임상시험·기전 연구가 발표되어 심혈관·대사 전반의 근거가 균형 있게 축적되고 있습니다.',
            'key': [
                {'text': '급성심근경색+제2형 당뇨병 환자 RCT(181명)에서 다파글리플로진이 18개월 심부전 발생을 위약 대비 **유의하게 감소**시켰고(29.5%→5.3%, HR 0.18), 좌심실박출률도 함께 개선되었습니다.',
                 'links': [{'t': 'Dapagliflozin in acute myocardial infarction with type 2 diabetes: RCT', 'u': 'https://doi.org/10.1016/j.cpcardiol.2026.103401'}]},
                {'text': '급성신손상 동반 중환자 대상 DEFENDER 사후분석에서 28일 사망률·신대체요법 필요성에 **유의한 차이가 없었고** 혈역학적 불안정 신호도 관찰되지 않아, 중환자군 대상 전용 임상시험의 타당성을 뒷받침합니다.',
                 'links': [{'t': 'Safety and Outcomes of Dapagliflozin in Critically Ill Patients with AKI (DEFENDER)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42537430/'}]},
                {'text': '경구 GLP-1RA 오르포글리프론과의 비열등성 3상(ACHIEVE-2)에서 오르포글리프론이 **HbA1c 감소 면에서 우월성**을 보여, 향후 경구 혈당강하제 시장 내 위치 변화 가능성을 시사합니다.',
                 'links': [{'t': 'Orforglipron compared with dapagliflozin (ACHIEVE-2)', 'u': 'https://doi.org/10.1016/S0140-6736(26)00800-7'}]},
            ],
            'safety': '급성신손상 중환자·급성심근경색 등 고위험군에서도 **뚜렷한 신규 안전성 신호는 관찰되지 않았습니다**. 다만 남인도 실사용 코호트에서 여성의 생식기 진균감염(10.3%)이 남성(2.1%) 대비 높게 보고되었습니다.',
        },
        'Empagliflozin': {
            'trend': '심부전(HFrEF/HFpEF/HFmrEF) 영역 근거가 가장 두드러지며, 급성심근경색 후 심근보호(PRESTIGE-AMI), 만성콩팥병+피네레논 병용 최적화, 부정맥·약물감시 신호 등 안전성 세부 프로파일 연구도 다수 발표되었습니다.',
            'key': [
                {'text': 'PRESTIGE-AMI RCT(200명)에서는 경색 크기·좌심실 재형성에 **유의한 차이가 없어** 심근보호 효과는 확인되지 않았으나, 기존 안전성 프로파일은 재확인되었습니다.',
                 'links': [{'t': 'SGLT2 Inhibitor on Infarct Size and LV Remodeling by CMR in AMI (PRESTIGE-AMI)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42508844/'}]},
                {'text': 'HFmrEF 환자에서 엠파글리플로진이 다파글리플로진 대비 입원(HR 0.54)·심부전 악화(HR 0.63)·요로감염(HR 0.70) 위험이 **낮게 관찰**되어(TriNetX 코호트, 각 1,386명 매칭) 계열 내 이질성 가능성이 제기되었습니다.',
                 'links': [{'t': 'Differential Outcomes With Empagliflozin and Dapagliflozin in HFmrEF', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42034323/'}]},
                {'text': '엠파글리플로진+GLP-1RA 병용이 DPP-4i 병용 대비 주요심혈관사건(HR 0.81), 심부전입원/사망(HR 0.61) 위험을 **낮춰**(EMPRISE 코호트) 병용요법 근거가 축적되고 있습니다.',
                 'links': [{'t': 'Cardiovascular outcomes of empagliflozin-GLP-1RA combination therapy (EMPRISE)', 'u': 'https://doi.org/10.1186/s12933-026-03287-w'}]},
            ],
            'safety': 'WHO 약물감시 데이터베이스 분석에서 SGLT2억제제 계열 중 엠파글리플로진의 **포경/감돈포경 보고 위험이 가장 높게** 나타났습니다. 그 외 심실부정맥 위험 증가 신호는 없었으며, 오히려 당뇨병군에서 위험 감소 경향이 관찰되었습니다.',
        },
        'SGLT-1,2 inhibitor': {
            'trend': '소타글리플로진 관련 임상시험·메타분석이 절대다수를 차지하며(제1형 당뇨병 심부전 SOPHIST, 신장이식 환자 대상 시험 등 3상급 연구 다수 진행 중), 국내 신약 JP-2266의 2상 결과도 처음 보고되어 계열 내 파이프라인이 확장되는 양상입니다. 제1형 당뇨병에서의 DKA 위험 관리(연속 케톤 모니터링 활용)가 핵심 연구 주제로 부상하고 있습니다.',
            'key': [
                {'text': 'SOLOIST-WHF 관련 후속분석에서 소타글리플로진을 심부전 악화 입원 환자의 퇴원 전후 조기에 투여할 경우 90일 심혈관사망/심부전 사건 위험이 **유의하게 감소**했고(HR 0.54), 삶의 질(KCCQ-12)도 개선되었습니다.',
                 'links': [{'t': 'Effect of Sotagliflozin on Early Mortality and HF-Related Events (SOLOIST-WHF post hoc)', 'u': 'https://doi.org/10.1016/j.jchf.2023.05.026'}]},
                {'text': '여러 네트워크 메타분석에서 소타글리플로진이 심부전 입원·심혈관사망 복합결과 감소 효과 면에서 엠파글리플로진(RR 0.88)·다파글리플로진(RR 0.86)보다 **우수한 경향**을 반복적으로 보였습니다.',
                 'links': [{'t': 'Effects of different SGLT2 inhibitors in HFrEF/HFpEF: network meta-analysis', 'u': 'https://doi.org/10.3389/fcvm.2024.1379765'}]},
                {'text': '제1형 당뇨병 대상 inTandem 통합분석에서 **중증 저혈당 위험을 위약 대비 낮추고**(200mg군 7%, 400mg군 4% vs 위약 17%) 심혈관·신장 이득도 함께 확인되어, 1형 당뇨병에서의 근거가 점차 축적되고 있습니다.',
                 'links': [{'t': 'Efficacy and Safety of Sotagliflozin in Patients with Type 1 Diabetes and CKD (inTandem pooled)', 'u': 'https://doi.org/10.1681/ASN.0000000540'}]},
            ],
            'safety': 'SGLT-1,2 inhibitor 계열의 핵심 안전성 이슈는 **당뇨병성 케톤산증(DKA)**입니다. 제1형 당뇨병 대상 다수 연구(inTandem 사후분석, KARMA, 연속 케톤모니터링 활용 연구 등)에서 베타하이드록시부티레이트 상승과 DKA 위험 간 연관성이 반복 확인되어, 연속 케톤 모니터링 기반 위험관리 전략이 활발히 연구되고 있습니다. 생식기감염·설사·체액감소 위험도 다파·엠파글리플로진 대비 다소 높게 보고되는 경향이나(CKD 메타분석: 생식기진균감염↑, 설사↑, eGFR 감소폭↑), 전체사망률·주요심혈관사건에는 유의한 차이가 없었습니다.',
        },
    },
}

# ---- dedicated Safety Signal section (itemized, with evidence citations) ----
SAFETY_SIGNAL_WEEKLY = {
    'SGLT-2 inhibitor(전체)': [
        {'label': '요로감염 위험 — 증가 없음(재확인)', 'text': '시험수준 메타분석(RCT 14편, 5개 SGLT2억제제)에서 전체/중증 요로감염 위험 모두 위약 대비 **유의한 차이 없음**(RR 1.08-1.14, 경계선상; 중증 RR 0.99).', 'evidence': 'Trial-level meta-analysis, T2DM·HF·CKD, RCT 14편'},
        {'label': '수술 전후 관리 — 중단이 오히려 위험 증가', 'text': '비심장수술 전 SGLT2억제제를 지속 복용한 경우 심장합병증 발생률 1.7%, 중단 기간이 길어질수록(1일 5.7%→3일 이상 **11.5%**) 위험 증가. 우려되던 정상혈당 케톤산증은 1례만 발생.', 'evidence': '전향적 관찰연구 2건 이차분석, n=451'},
    ],
    'Dapagliflozin': [
        {'label': '특이 신호 없음', 'text': '이번 주 다파글리플로진 단독 안전성 신호는 보고되지 않았으며, 계열 전체 요로감염 메타분석에 함께 포함됨.', 'evidence': '-'},
    ],
    'Empagliflozin': [
        {'label': '폐동맥고혈압(PAH) 적응증 확장 — 우심실 기능 악화 경향', 'text': '2a상 예비시험(8명)에서 NT-proBNP·기능등급·6분보행거리 개선 없이 **우심실 박출률이 오히려 악화**되는 경향. 초기단계 소규모 연구로 신중한 해석 필요.', 'evidence': 'EMPHOWER PoC, 2a상, n=8'},
    ],
    'SGLT-1,2 inhibitor': [],
}

SAFETY_SIGNAL_HALFYEAR = {
    '2026-H2': {
        'SGLT-2 inhibitor(전체)': [
            {'label': '생식기 진균감염 / 포경·감돈포경 — 지속적으로 확인되는 신호', 'text': '65세 이상 비투석 CKD 환자 메타분석에서 생식기 진균감염 위험 증가(**RR 2.40**), 대만 코호트에서는 노인 환자 생식기감염 위험비 4.29. WHO 약물감시 데이터베이스(약 1,134만 건) 분석에서 SGLT2억제제 계열의 **포경/감돈포경 보고빈도비가 34.72**로 다른 당뇨병약제 대비 유의하게 높음(엠파글리플로진이 최고).',
             'links': [
                {'t': 'Renal and cardiovascular outcomes and safety of SGLT2 inhibitors in patients aged ≥65 years with non-dialysis CKD', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42420866/'},
                {'t': 'Efficacy and safety of SGLT2 inhibitors in elderly patients with type 2 diabetes (Taiwan cohort)', 'u': 'https://doi.org/10.1080/07853890.2026.2696636'},
                {'t': 'Association between SGLT2 inhibitors and reporting of phimosis/paraphimosis: a comparative pharmacovigilance analysis', 'u': 'https://doi.org/10.1007/s00592-026-02742-0'},
             ]},
            {'label': '요로감염 — 위험 증가 없음(재확인)', 'text': '시험수준 메타분석(RCT 14편)에서 전체/중증 요로감염 위험 모두 위약과 **유의한 차이 없음**(RR 0.99-1.14). 생식기감염과는 구분되는 신호.',
             'links': [
                {'t': 'Are SGLT2 inhibitors really associated with increased urinary tract infection risk? A trial-level meta-analysis', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42566081/'},
             ]},
            {'label': '케톤산증 / 급성신손상 — 매우 드묾, 증가 신호 없음', 'text': '수술 전후 코호트에서 정상혈당 케톤산증 **1례만 발생**. 65세 이상 CKD 메타분석 및 급성심부전 조기투여 메타분석에서도 급성신손상 증가 신호 확인되지 않음.',
             'links': [
                {'t': 'Perioperative discontinuation of SGLT2-inhibitors and cardiac complications after noncardiac surgery', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42270529/'},
             ]},
            {'label': '고령·노쇠 환자 내약성', 'text': '75세 이상 노쇠 심부전 환자에서 6개월 내 약제 불내성(중단·감량) 비율이 노쇠군에서 **유의하게 높음**(39.2% vs 18.8%, 보정OR 2.31), 특히 eGFR 45 미만에서 더 두드러짐.',
             'links': [
                {'t': 'Frailty index and tolerability of SGLT2 inhibitors in elderly (≥75 years) patients with heart failure', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42432928/'},
             ]},
        ],
        'Dapagliflozin': [
            {'label': '생식기 진균감염 — 여성에서 높은 발생률', 'text': '남인도 실사용 코호트(다파·엠파글리플로진 추가요법)에서 여성 생식기 진균감염 **10.3%**로 남성(2.1%) 대비 높게 보고. 중대한 이상반응은 없었음.',
             'links': [
                {'t': 'Real-world efficacy and safety of SGLT2 inhibitor add-on triple therapy in south indian patients with type 2 diabetes', 'u': 'https://doi.org/10.1186/s13098-026-02240-x'},
             ]},
            {'label': '급성신손상 중환자 — 안전성 신호 없음', 'text': 'DEFENDER 임상시험 사후분석(급성신손상 동반 중환자 212명)에서 28일 사망률, 신대체요법 필요성 모두 대조군과 **유의한 차이 없었고** 혈역학적 불안정 신호도 관찰되지 않음.',
             'links': [
                {'t': 'Safety and Outcomes of Dapagliflozin Initiation in Critically Ill Patients with Acute Kidney Injury (DEFENDER post-hoc)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42537430/'},
             ]},
        ],
        'Empagliflozin': [
            {'label': '포경·감돈포경 — 계열 내 최고 위험 신호', 'text': 'WHO 약물감시 데이터베이스 분석에서 SGLT2억제제 계열 중 엠파글리플로진의 **포경/감돈포경 보고 위험이 가장 높게** 나타남.',
             'links': [
                {'t': 'Association between SGLT2 inhibitors and reporting of phimosis/paraphimosis: a comparative pharmacovigilance analysis', 'u': 'https://doi.org/10.1007/s00592-026-02742-0'},
             ]},
            {'label': '심실부정맥 — 위험 증가 신호 없음', 'text': '질환별 네트워크 메타분석(RCT 32건, 140,156명)에서 대부분 약제가 부정맥 위험을 **유의하게 증가시키지 않았고**, 엠파글리플로진은 당뇨병군에서 오히려 위험 감소 경향(탐색적).',
             'links': [
                {'t': 'Efficacy and Safety of SGLT2 Inhibitors and GLP-1 Receptor Agonists on Ventricular Arrhythmias and Cardiovascular Outcomes', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42426564/'},
             ]},
            {'label': '폐동맥고혈압 적응증 확장 — 우심실 기능 악화 경향', 'text': '2a상 예비시험(8명)에서 **우심실 박출률 악화 경향**, 초기단계 소규모 연구로 추가 검증 필요.',
             'links': [
                {'t': 'Empagliflozin Ameliorates Experimental Pulmonary Vascular Remodeling, but May Not Benefit Patients With Pulmonary Arterial Hypertension (EMPHOWER PoC)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42500881/'},
             ]},
        ],
        'SGLT-1,2 inhibitor': [
            {'label': '당뇨병성 케톤산증(DKA) — 핵심 안전성 이슈', 'text': '제1형 당뇨병 대상 다수 연구(inTandem 사후분석, KARMA, 연속 케톤모니터링 연구 등)에서 베타하이드록시부티레이트 상승이 **DKA 위험의 유의한 예측인자**로 반복 확인(기저 BHB 0.1mmol/L 증가마다 DKA 위험 18%↑). 연속 케톤 모니터링 기반 위험관리 전략이 활발히 연구되고 있음.',
             'links': [
                {'t': 'Beta-Hydroxybutyrate Levels and Risk of Diabetic Ketoacidosis in Adults with Type 1 Diabetes Treated with Sotagliflozin (inTandem post-hoc)', 'u': 'https://doi.org/10.1089/dia.2023.0605'},
                {'t': 'Ketone Monitoring Approaches for Diabetic Ketoacidosis Risk Mitigation in People With T1D on Adjunctive SGLT2 Inhibitors (KARMA)', 'u': 'https://clinicaltrials.gov/study/NCT07421518'},
             ]},
            {'label': '생식기감염·설사·체액감소 — 다파·엠파 대비 다소 높음', 'text': 'T2DM+CKD 메타분석(RCT 3건, 11,648명)에서 생식기 진균감염·설사·체액감소 위험이 위약 대비 **유의하게 높았으나**, 전체사망률·주요심혈관사건에는 유의한 차이 없음.',
             'links': [
                {'t': 'Safety and efficacy of sotagliflozin in patients with type II diabetes mellitus and chronic kidney disease: a meta-analysis', 'u': 'https://doi.org/10.1007/s40620-023-01818-2'},
             ]},
            {'label': '중증 저혈당 — 오히려 위험 감소', 'text': '제1형 당뇨병 inTandem 통합분석에서 소타글리플로진군의 **중증 저혈당 발생률이 위약군보다 낮음**(200mg 7%, 400mg 4% vs 위약 17%).',
             'links': [
                {'t': 'Efficacy and Safety of Sotagliflozin in Patients with Type 1 Diabetes and CKD (inTandem pooled)', 'u': 'https://doi.org/10.1681/ASN.0000000540'},
             ]},
            {'label': '신장이식 환자 — 초기 가역적 eGFR 감소', 'text': '신장이식 환자 40명 대상 시험에서 투여 1주 후 eGFR이 평균 6.9% 감소했으나 **휴약 후 2.4%로 회복**, 이상반응으로 인한 탈락은 있었으나 eGFR 감소로 인한 탈락은 없었음.',
             'links': [
                {'t': 'Safety and Tolerability of Sotagliflozin Among Kidney Transplant Recipients', 'u': 'https://doi.org/10.1097/TP.0000000000005503'},
             ]},
        ],
    },
}

# ---- Guideline section: major society recommendations on SGLT-2/SGLT-1,2 inhibitors ----
# Hand-curated from primary/secondary guideline sources; re-verify at each refresh cycle
# (guidelines update far less frequently than the literature DB, so this needs less frequent
# re-authoring than WEEKLY_ANALYSIS/HALF_YEAR_ANALYSIS above, but should still be checked
# whenever a new guideline publication appears in the DB doc_type == '진료지침' set).
GUIDELINES = [
    {
        'org': '2026 AHA/ACC/ADA/ASN 심혈관-신장-대사(CKM) 증후군 통합 진료지침',
        'body': '미국심장학회·미국심장협회·미국당뇨병학회·미국신장학회 공동 (PubMed 원문 전문 확인)',
        'year': '2026',
        'summary': 'CKM 증후군에 대한 최초의 다학회 통합 임상진료지침으로, 제2형 당뇨병을 동반한 CKM 2-3단계 환자에서 SGLT-2 inhibitor의 사용 시점·우선순위를 공식 권고등급(Class of Recommendation, COR)·근거수준(Level of Evidence, LOE)과 함께 명시했습니다.',
        'points': [
            {'text': 'CKM 2-3단계 + 제2형 당뇨병 + 심혈관위험 증가(10년 PREVENT-CVD ≥7.5%) 환자에서는 입증된 심혈관 이득이 있는 **SGLT-2 inhibitor 또는 GLP-1 계열 치료를 치료계획에 포함**하도록 권고되며(**Class 1, LOE A**), 만성콩팥병 또는 심부전전단계(pre-HF)를 동반한 경우 SGLT-2 inhibitor가 우선적으로 고려됩니다.',
             'links': [{'t': '2026 AHA/ACC/ADA/ASN Guideline for CKM Syndrome (JACC)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42265997/'}]},
            {'text': '만성콩팥병(제2형 당뇨병 동반, 또는 비동반이면서 요알부민/크레아티닌비 ≥200mg/g)이면서 **eGFR ≥20mL/min/1.73m²**인 환자에서 SGLT-2 inhibitor는 신기능 저하·심부전입원·심혈관사망 위험 감소를 위해 권고되고(**Class 2a, LOE B-R**), 알부민뇨가 낮은(30-199mg/g) 비당뇨 CKD 환자에서도 사용을 고려할 수 있습니다.',
             'links': [{'t': '2026 AHA/ACC/ADA/ASN Guideline for CKM Syndrome (Circulation)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42263157/'}]},
            {'text': '박출률감소 심부전(HFrEF)에서는 RASi·베타차단제·MRA와 함께 SGLT-2 inhibitor가 **4제 표준요법(quadruple GDMT)의 핵심 축**으로 명시되었고, 박출률경도감소·보존 심부전(HFmrEF/HFpEF)에서도 SGLT-2 inhibitor가 1차 치료로 제시되었습니다.',
             'links': [{'t': '2026 AHA/ACC/ADA/ASN Guideline for CKM Syndrome (JACC)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42265997/'}]},
        ],
        'source_label': 'Circulation 2026;154:e50-e158 / JACC 2026;87(22S):e1889-e2007',
        'url': 'https://pubmed.ncbi.nlm.nih.gov/42265997/',
    },
    {
        'org': 'ADA Standards of Care in Diabetes — 2026',
        'body': '미국당뇨병학회(ADA); 국제 비교리뷰로 재확인 (PubMed 원문 전문 확인)',
        'year': '2026',
        'summary': 'ADA는 **인물중심·위험도기반(person-centered, risk-based)** 접근을 취하며, 심장-신장 동반질환이 있는 환자에서는 혈당수치나 메트포르민 복용 여부와 무관하게 SGLT-2 inhibitor를 우선 고려하도록 권고합니다.',
        'points': [
            {'text': '심혈관·신장 동반질환이 확인된 환자에서는 **SGLT-2 inhibitor 또는 GLP-1 RA가 메트포르민 병용 여부와 무관하게 적절한 초기치료**가 될 수 있다고 명시해, 전통적인 "메트포르민 우선" 원칙에서 벗어난 개별화 전략을 취합니다.',
             'links': [{'t': 'Contemporary Type 2 Diabetes Guidelines: Position of the KDA Framework (ADA 비교 섹션 포함)', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42298756/'}]},
            {'text': '제2형 당뇨병+만성콩팥병 환자 중 **eGFR ≥20mL/min/1.73m² 및 요알부민/크레아티닌비 ≥200mg/g**인 경우 콩팥병 진행 억제를 위해 SGLT-2 inhibitor 사용이 권고되며(**Grade A**), 알부민뇨가 낮은 환자에서도 Grade B로 권고됩니다.',
             'links': [{'t': 'ADA Standards of Care 2026 — key aspects for internist practice', 'u': 'https://pubmed.ncbi.nlm.nih.gov/41692340/'}]},
            {'text': '박출률 보존 또는 감소 심부전 환자 모두에서 심부전 악화·심혈관사망 위험 감소를 위해 사용이 권고되며(**Grade A**), 매년 개정되는 Standards of Care 특유의 **신속한 근거 반영 주기**를 통해 SGLT-2 inhibitor의 심장-신장 보호 근거가 즉시 반영된다는 점이 다른 지침과 구별되는 특징입니다.',
             'links': [{'t': 'ADA Standards of Care 2026 — key aspects for internist practice', 'u': 'https://pubmed.ncbi.nlm.nih.gov/41692340/'}]},
        ],
        'source_label': 'Rev Clin Esp 2026;226(4):502491 / Endocrinol Metab (Seoul) 2026;41(3):351-357',
        'url': 'https://pubmed.ncbi.nlm.nih.gov/41692340/',
    },
    {
        'org': '대한당뇨병학회(KDA) 2025 개정 진료지침 — SGLT-2 inhibitor 포지션',
        'body': '국제 비교리뷰(Kim SK, et al.)로 재확인, Endocrinology and Metabolism (Seoul), 2026 (PubMed 원문 전문 확인)',
        'year': '2025-2026',
        'summary': '2025년 개정된 KDA 진료지침은 기존의 **혈당중심(glycemia-centered) 치료구조**를 유지하면서도 동반질환 기반 의사결정을 적극적으로 통합하는 방향으로 진화했습니다. ADA·NICE·JDS 지침과 KDA를 직접 비교한 국제 리뷰가 이 변화를 상세히 분석했습니다.',
        'points': [
            {'text': '2025년 개정판부터 **메트포르민 단독 1차요법 의무 규정이 폐지**되어, 임상적으로 필요한 경우 조기 병용요법이나 주사제 치료로 초기치료를 개별화할 수 있게 되었습니다.',
             'links': [{'t': 'Contemporary Type 2 Diabetes Guidelines: Converging Evidence, Diverging Strategies, and the Position of the KDA Framework', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42298756/'}]},
            {'text': '죽상경화성 심혈관질환·심부전·만성콩팥병을 동반한 환자에서는 SGLT-2 inhibitor 및 GLP-1 RA가 **적극적으로 권고**되어 국제 근거와의 정합성을 갖추었으며, 뇌졸중·일과성허혈발작 병력이 있는 환자를 별도 치료 고려군으로 명시한 점이 KDA 지침만의 특징입니다.',
             'links': [{'t': 'Contemporary Type 2 Diabetes Guidelines: Converging Evidence, Diverging Strategies, and the Position of the KDA Framework', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42298756/'}]},
            {'text': 'KDA 프레임워크는 혈당중심 구조에 동반질환 기반 접근을 결합한 **실용적 하이브리드 모델(pragmatic hybrid model)**로 평가되며, 경구 4제요법을 포함한 유연한 조기 병용요법을 허용해 국내 임상현장 적용성을 높인 것이 ADA·NICE·JDS 지침과의 핵심 차이로 제시되었습니다.',
             'links': [{'t': 'Contemporary Type 2 Diabetes Guidelines: Converging Evidence, Diverging Strategies, and the Position of the KDA Framework', 'u': 'https://pubmed.ncbi.nlm.nih.gov/42298756/'}]},
        ],
        'source_label': 'Endocrinol Metab (Seoul) 2026;41(3):351-357',
        'url': 'https://pubmed.ncbi.nlm.nih.gov/42298756/',
    },
    {
        'org': 'KDIGO 2024 만성콩팥병(CKD) 진료지침',
        'body': 'Kidney Disease: Improving Global Outcomes',
        'year': '2024',
        'summary': '만성콩팥병 환자에서 SGLT-2 inhibitor 사용 기준을 eGFR·알부민뇨 수준별로 등급화하여 제시한 국제 신장병 진료지침입니다.',
        'points': [
            {'text': '제2형 당뇨병을 동반한 CKD 환자 중 **eGFR ≥20mL/min/1.73m²**인 경우 SGLT-2 inhibitor 사용을 최고 근거수준으로 권고합니다(**Recommendation 1A**).',
             'links': [{'t': 'KDIGO 2024 CKD Guideline Executive Summary', 'u': 'https://kdigo.org/wp-content/uploads/2017/02/KDIGO-2024-CKD-Guideline-Executive-Summary.pdf'}]},
            {'text': 'eGFR ≥20이면서 요알부민/크레아티닌비 ≥200mg/g이거나, 알부민뇨 수준과 무관하게 **심부전을 동반**한 CKD 환자에서도 동일하게 강력히 권고합니다(**1A**).',
             'links': [{'t': 'KDIGO 2024 CKD Guideline Executive Summary', 'u': 'https://kdigo.org/wp-content/uploads/2017/02/KDIGO-2024-CKD-Guideline-Executive-Summary.pdf'}]},
            {'text': 'eGFR 20-45이면서 알부민뇨가 낮은(200mg/g 미만) 환자에서는 상대적으로 낮은 근거수준으로 사용을 제안하며(**2B**), 이미 투여 중인 경우 **eGFR이 20 미만으로 떨어져도 금기가 아닌 한 지속 투여**를 권고합니다.',
             'links': [{'t': 'KDIGO 2024 CKD Guideline Executive Summary', 'u': 'https://kdigo.org/wp-content/uploads/2017/02/KDIGO-2024-CKD-Guideline-Executive-Summary.pdf'}]},
        ],
        'source_label': 'KDIGO 2024 CKD Guideline Executive Summary',
        'url': 'https://kdigo.org/wp-content/uploads/2017/02/KDIGO-2024-CKD-Guideline-Executive-Summary.pdf',
    },
    {
        'org': '2023 ESC 당뇨병 동반 심혈관질환 관리 진료지침',
        'body': '유럽심장학회(ESC)',
        'year': '2023',
        'summary': '제2형 당뇨병 환자의 심혈관질환 위험도·심부전 박출률에 따라 권장 SGLT-2 inhibitor 약제를 구체적으로 제시한 유럽 진료지침입니다.',
        'points': [
            {'text': '죽상경화성 심혈관질환을 이미 진단받았거나 **다수의 위험인자를 동반한 제2형 당뇨병 환자**에서 심부전 입원 위험 감소를 위해 empagliflozin·canagliflozin·dapagliflozin·ertugliflozin·sotagliflozin 사용을 권고합니다.',
             'links': [{'t': '2023 ESC Guidelines for the management of cardiovascular disease in patients with diabetes', 'u': 'https://www.escardio.org/Congresses-Events/ESC-Congress/Congress-resources/Congress-news/2023-esc-clinical-practice-guidelines-for-the-management-of-cardiovascular-disease-in-patients-with-diabetes'}]},
            {'text': '박출률경도감소 및 박출률보존 심부전(LVEF >40%) 환자에는 empagliflozin 또는 dapagliflozin을, **박출률감소 심부전(LVEF ≤40%)** 환자에는 dapagliflozin·empagliflozin·sotagliflozin을 심부전입원·심혈관사망 감소 목적으로 권고합니다.',
             'links': [{'t': '2023 ESC Guidelines for the management of cardiovascular disease in patients with diabetes', 'u': 'https://www.escardio.org/Congresses-Events/ESC-Congress/Congress-resources/Congress-news/2023-esc-clinical-practice-guidelines-for-the-management-of-cardiovascular-disease-in-patients-with-diabetes'}]},
        ],
        'source_label': 'European Heart Journal, 2023',
        'url': 'https://www.escardio.org/Congresses-Events/ESC-Congress/Congress-resources/Congress-news/2023-esc-clinical-practice-guidelines-for-the-management-of-cardiovascular-disease-in-patients-with-diabetes',
    },
    {
        'org': '2022 AHA/ACC/HFSA 심부전 관리 진료지침',
        'body': '미국심장협회·미국심장학회·미국심부전학회 공동',
        'year': '2022',
        'summary': '박출률 구간(HFrEF/HFmrEF/HFpEF)별로 SGLT-2 inhibitor의 권고등급을 세분화하여 제시한 심부전 표준 진료지침입니다.',
        'points': [
            {'text': '박출률감소 심부전(HFrEF, LVEF ≤40%)에서는 **당뇨병 동반 여부와 무관하게** 심부전입원·심혈관사망 감소를 위해 SGLT-2 inhibitor 사용이 강력히 권고됩니다(**Class 1**, DAPA-HF·EMPEROR-Reduced 근거).',
             'links': [{'t': '2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure', 'u': 'https://www.ahajournals.org/doi/10.1161/CIR.0000000000001063'}]},
            {'text': '박출률경도감소 심부전(HFmrEF, LVEF 41-49%) 및 박출률보존 심부전(HFpEF, LVEF ≥50%)에서는 EMPEROR-Preserved 등의 근거를 바탕으로 **사용을 고려할 수 있다는 권고**입니다(**Class 2a**); HFmrEF·HFpEF 전용 대규모 RCT가 상대적으로 부족하다는 근거의 한계도 함께 명시되어 있습니다.',
             'links': [{'t': '2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure', 'u': 'https://www.ahajournals.org/doi/10.1161/CIR.0000000000001063'}]},
        ],
        'source_label': 'Circulation / JACC, 2022',
        'url': 'https://www.ahajournals.org/doi/10.1161/CIR.0000000000001063',
    },
    {
        'org': '대한당뇨병학회(KDA) SGLT-2 inhibitor 안전 사용 성명서',
        'body': '대한당뇨병학회',
        'year': '2025',
        'summary': '국내에서 SGLT-2 inhibitor가 체중감량·미용 목적으로 오남용되는 사례에 대한 우려를 담아 발표한 학회 성명서입니다. 치료적 포지션이 아닌 안전 사용에 초점을 둔 별도 문서입니다.',
        'points': [
            {'text': '**체중감량 또는 미용 목적의 무분별한 사용은 명백한 오남용**이며, 비대면 진료를 통한 무분별한 처방에 대해 경계가 필요하다고 명시했습니다.',
             'links': [{'t': "대한당뇨병학회 SGLT2억제제 안전 사용 성명서 관련 보도", 'u': 'https://dangnyoshinmun.co.kr/news/article.html?no=24224'}]},
            {'text': '탈수·근육감소 위험이 있는 **75세 이상 고령·노쇠 환자**에서는 특히 신중한 처방과 지속적인 감시가 필요하다고 권고했습니다.',
             'links': [{'t': "대한당뇨병학회 SGLT2억제제 안전 사용 성명서 관련 보도", 'u': 'https://dangnyoshinmun.co.kr/news/article.html?no=24224'}]},
            {'text': '생식기 감염 위험 증가에 대한 지속적인 감시, 인슐린 분비 저하 환자에서의 당뇨병케톤산증 위험에 대한 경각심을 함께 강조했습니다.',
             'links': [{'t': "대한당뇨병학회 SGLT2억제제 안전 사용 성명서 관련 보도", 'u': 'https://dangnyoshinmun.co.kr/news/article.html?no=24224'}]},
        ],
        'source_label': '당뇨병신문, 2025',
        'url': 'https://dangnyoshinmun.co.kr/news/article.html?no=24224',
    },
]

# ---- Overview: brochure-style key messages (academic tone, "~다" register) ----
OVERVIEW_BRIEF = {
    'weekIssue': {
        'label': '이번 주 핵심 이슈',
        'period': '2026-08-08 등록분',
        'headline': 'SGLT2억제제, **요로감염 위험과 무관** — 주술기 중단 지침 재검토 필요성 제기',
        'points': [
            '대규모 시험수준 메타분석(RCT 14편)에서 SGLT2억제제와 요로감염 위험 간 **유의한 연관성이 확인되지 않아**, 관련 안전성 우려가 근거 수준에서 완화되었다.',
            '비심장수술 전 SGLT2억제제를 지속 복용한 경우 심장합병증 발생률이 1.7%에 그친 반면, 중단 기간이 길어질수록(3일 이상 **11.5%**) 오히려 위험이 증가하여 현행 주술기 중단 권고의 재검토가 제기되었다.',
            '엠파글리플로진의 폐동맥고혈압 적응증 확장 가능성을 탐색한 2a상 예비시험에서는 **우심실 기능 악화 경향**이 관찰되어 신중한 해석이 요구된다.',
        ],
    },
    'sglt2': {
        'label': 'SGLT-2 inhibitor 핵심 메시지',
        'headline': '신장·심혈관 보호 효과의 근거 수준이 **가장 높은 약물군**으로 재확인',
        'points': [
            '만성콩팥병 진행 억제 효과에서 당뇨병 치료제 계열 중 **가장 높은 정밀도의 근거**를 보인다(HR 0.66, 95% CI 0.60–0.74; class-level 네트워크 메타분석, RCT 9건 37,749명).',
            '고령(65세 이상) 비투석 만성콩팥병 환자에서도 신장·심혈관 복합결과 위험이 각각 **32%, 26% 감소**하여, 고령층으로의 적용 근거가 확대되고 있다.',
            '요로감염 위험 증가는 반복적으로 부정되는 반면, **생식기 진균감염 및 포경·감돈포경**은 계열 전반에서 일관되게 관찰되는 안전성 신호로 확인된다.',
            '혈당강하 효과를 넘어 폐암·자궁내막암·치매 위험 감소 등 **이차적 이득 신호**가 관찰연구를 통해 보고되고 있으나, 인과관계 확립을 위한 전향적 검증이 필요하다.',
        ],
    },
    'dapaEmpa': {
        'label': 'Dapagliflozin 및 Empagliflozin 핵심 메시지',
        'dapa': {
            'name': 'Dapagliflozin',
            'points': [
                '급성심근경색을 동반한 제2형 당뇨병 환자에서 조기 투여 시 18개월 심부전 발생 위험을 **유의하게 낮췄다**(29.5%→5.3%, HR 0.18).',
                '급성신손상을 동반한 중환자에서도 사망률·신대체요법 필요성에 **유의한 차이가 없어**, 고위험군 대상 전용 임상시험의 타당성을 뒷받침한다.',
            ],
        },
        'empa': {
            'name': 'Empagliflozin',
            'points': [
                '경도박출률감소심부전(HFmrEF)에서 다파글리플로진 대비 입원(HR 0.54) 및 심부전 악화(HR 0.63) 위험이 **낮게 관찰**되어, 계열 내 이질성 가능성이 제기된다.',
                'GLP-1 수용체작용제와의 병용요법이 주요심혈관사건(HR 0.81) 및 심부전입원·사망(HR 0.61) 위험을 **추가로 낮추는 것**으로 나타났다.',
                'WHO 약물감시 데이터베이스 분석에서 SGLT2억제제 계열 중 **포경·감돈포경 보고 위험이 가장 높게** 나타나 주의가 필요하다.',
            ],
        },
    },
}
