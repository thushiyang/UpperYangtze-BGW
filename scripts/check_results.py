"""Check deposited integrity and selected derived results; no model execution."""
import csv
import hashlib
import math
from collections import defaultdict
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]


def rows(name):
    with (ROOT / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def equal(actual, expected):
    if not math.isclose(float(actual), expected, rel_tol=1e-8, abs_tol=1e-8):
        raise ValueError(f'Calculation mismatch: {actual} != {expected}')


def main():
    checks = 0
    for row in rows('SHA256SUMS.csv'):
        path = ROOT / row['file']
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        if digest != row['sha256'] or path.stat().st_size != int(row['bytes']):
            raise ValueError(f'Integrity mismatch: {row["file"]}')
        checks += 1
    for n in (7,8):
        for row in rows(f'data/Figure_{n:02}.csv'):
            for resource in ('blue_water','green_water'):
                value = row.get(resource+'_mm')
                baseline = row.get(resource+'_mm_baseline')
                change = row.get(resource+'_change_pct')
                if value and baseline and change:
                    equal(change,100*(float(value)/float(baseline)-1))
                    checks += 1
            if n == 8:
                equal(row['f_GW'],float(row['green_water_mm'])/(float(row['blue_water_mm'])+float(row['green_water_mm'])))
                equal(row['delta_GWC'],float(row['f_GW'])-float(row['f_GW_baseline']))
                checks += 2
    for row in rows('data/Figure_10.csv'):
        for resource in ('BW','GW'):
            equal(row[f'delta_{resource}_pct'],100*(float(row[f'{resource}_scenario_mm'])/float(row[f'{resource}_baseline_mm'])-1))
            checks += 1
    for n,prefix in ((13,'blue_water_mm'),(14,'gw_mm')):
        records=rows(f'data/Figure_{n}.csv')
        matched=[r for r in records if r['data_block']=='matched_outcomes']
        groups=defaultdict(list)
        for r in matched:
            y00,y01,y10,y11=[float(r[f'{prefix}_Y{x}']) for x in ('00','01','10','11')]
            for key,value in [('climate',y10-y00),('landuse_historical',y01-y00),
                              ('interaction',y11-y10-y01+y00),('total',y11-y00)]:
                equal(r[key],value)
                checks += 1
            groups[(r['scenario'],r['landuse'],r['scale'],r['region'])].append(float(r['interaction']))
        for r in records:
            if r['data_block']!='interaction_summary':
                continue
            values=groups[(r['scenario'],r['landuse'],r['scale'],r['region'])]
            if len(values)!=6:
                raise ValueError('Expected six matched climate models')
            for k,v in [('median',median(values)),('minimum',min(values)),('maximum',max(values))]:
                equal(r[k],v)
                checks += 1
    for r in rows('data/Figure_15.csv'):
        equal(r['available_water_m3'],0.2*float(r['outlet_Q_volume_m3']))
        equal(r['BWSC'],float(r['consumption_m3'])/float(r['available_water_m3']))
        checks += 2
    print(f'PASS: {checks} file-integrity and selected numerical checks. No SWAT rerun performed.')


if __name__=='__main__':
    main()
