"""Check documentation arithmetic; this is not a game engine or economic test."""
import calendar
import csv
import json
from datetime import date
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'docs/assets/data'
getcontext().prec = 40
f = json.loads((DATA / 'monthly-rule-fixtures.json').read_text())
with (DATA / 'uk-opening-evidence.csv').open(newline='') as stream:
    rows = list(csv.DictReader(stream))
assert len({row['id'] for row in rows}) == len(rows)
for row in rows:
    assert all(row.values()), row['id']
    Decimal(row['value'])
    assert row['source_id'] in {'T01', 'T02', 'T03'}
values = {row['id']: Decimal(row['value']) for row in rows}

# Independent calendar enumeration, including leap-day coverage and final window.
months = [f'{year}-{month:02}' for year in range(2010, 2020) for month in range(1, 13)]
c = f['calendar']
assert (months[0], months[-1], len(months)) == (c['start'], c['last'], c['total_turns'])
assert c['years'] * c['turns_per_year'] == len(months)
assert c['assessment'] == '2020-01'
assert months[c['final_window_start_index']] == '2017-01'
assert len(months[c['final_window_start_index']:]) == c['final_window_months'] == 36
assert calendar.monthrange(2012, 2)[1] == calendar.monthrange(2016, 2)[1] == 29
assert calendar.monthrange(2010, 2)[1] == 28

p = f['equal_payment']
assert len(p['monthly_pence']) == 12
assert sum(p['monthly_pence']) == p['annual_pence']
assert max(p['monthly_pence']) - min(p['monthly_pence']) == 1
n = f['nominal_interest']
assert n['principal_pence'] * Decimal(n['annual_nominal_rate']) == n['annual_paid_pence']
assert n['monthly_interest_pence'] * 12 == n['annual_paid_pence']
assert n['closing_principal_pence'] == n['principal_pence']
e = f['effective_interest']
assert abs((1 + Decimal(e['monthly_rate'])) ** 12 - Decimal(e['annual_factor'])) < Decimal('1e-14')
assert Decimal(e['annual_factor']) == 1 + Decimal(e['annual_effective_rate'])
s = f['stage']
assert months[s['minimum_duration_months'] - 1] == s['complete_at_close']
assert months[s['minimum_duration_months']] == s['usable_from']
assert Decimal(s['monthly_max_fraction'].split('/')[0]) / Decimal(s['monthly_max_fraction'].split('/')[1]) * 24 == 1
assert f['final_commission']['usable_from'] not in months
assert f['final_commission']['operating_months_in_campaign'] == 0
cash = f['cash_gap']
assert cash['due_pence'] - cash['cash_pence'] - cash['finance_pence'] == cash['gap_pence']
d = f['due_guard']
assert date.fromisoformat(d['overdue_due_date']) <= date.fromisoformat(d['close']) < date.fromisoformat(d['future_due_date'])
r = f['reforms']
assert r['annual_slots'] - r['submissions_2010'] == r['remaining_after_reload'] == r['remaining_february'] == 0
assert r['remaining_january_2011'] == r['annual_slots']
s = f['stock']
assert s['opening_homes'] + s['completions'] - s['retirements'] == s['closing_homes']
i = f['income']
assert 12 * i['monthly_real_gbp'] * i['months'] / (i['months'] * i['equivalent_members']) == i['average_annual_real_gbp']

for case in f['tax']['cases']:
    taxable = max(Decimal(0), Decimal(case['gross_gbp']) - values['personal_allowance_under65'])
    basic = min(taxable, values['basic_taxable_band'])
    higher = max(Decimal(0), taxable - values['basic_taxable_band'])
    assert basic * values['income_tax_basic_rate'] + higher * values['income_tax_higher_rate'] == case['tax_gbp']
assert values['public_gross_investment'] - values['public_depreciation'] == values['public_net_investment']
assert values['public_current_receipts'] - values['public_current_expenditure'] - values['public_depreciation'] == values['public_current_surplus']
assert values['public_net_investment'] - values['public_current_surplus'] == values['public_net_borrowing']
print(f'PASS: {len(rows)} evidence records; F01–F12 temporal fixture arithmetic; four tax cases; three fiscal forecast identities.')
print('Documentation arithmetic only: no engine, payroll, calibrated economic or device tests executed.')
