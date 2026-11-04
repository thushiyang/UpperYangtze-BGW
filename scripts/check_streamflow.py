"""Check Figure 2 coverage; optionally recalculate metrics with supplied pairs."""
import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(path):
    with path.open(encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream))


def group(records):
    result=defaultdict(list)
    for row in records:
        result[(row['station_en'],row['period'])].append(row)
    return result


def metrics(records):
    obs=[float(r['observed_m3_s']) for r in records]
    sim=[float(r['simulated_m3_s']) for r in records]
    if not all(math.isfinite(x) for x in obs+sim):
        raise ValueError('Input pairs must be finite and use the same valid months.')
    n=len(obs);mo=sum(obs)/n;ms=sum(sim)/n
    vo=sum((x-mo)**2 for x in obs);vs=sum((x-ms)**2 for x in sim)
    covariance=sum((o-mo)*(s-ms) for o,s in zip(obs,sim))
    error=sum((s-o)**2 for o,s in zip(obs,sim))
    return {'r2':covariance**2/(vo*vs),'nse':1-error/vo,
        'pbias_pct':100*(sum(obs)-sum(sim))/sum(obs),'rmse_m3_s':math.sqrt(error/n)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pairs',type=Path,help='Separately supplied observed/simulated pairs; not bundled.')
    args=parser.parse_args()
    expected={(r['station_en'],r['period']):r for r in read(ROOT/'data/Figure_02_metrics.csv')}
    simulations=group(read(ROOT/'data/Figure_02_simulated.csv'))
    assert len(expected)==len(simulations)==12
    for key,r in expected.items():
        values=simulations[key]
        assert len(values)==int(r['n_months'])
        dates=[x['date'][:7] for x in values]
        assert len(set(dates))==len(dates)
        assert min(dates)==r['start'] and max(dates)==r['end']
        assert all(math.isfinite(float(x['simulated_m3_s'])) for x in values)
    print('PASS: simulation coverage, six stations / twelve periods / 2,808 months.')
    if args.pairs:
        records=[r for r in read(args.pairs) if r.get('observed_m3_s') and r.get('simulated_m3_s')]
        paired=group(records)
        if set(paired)!=set(expected):
            raise ValueError('Expected all twelve station-period groups.')
        for key,values in paired.items():
            if len(values)!=int(expected[key]['n_months']):
                raise ValueError(f'Month count mismatch: {key}')
            for field,value in metrics(values).items():
                if not math.isclose(value,float(expected[key][field]),rel_tol=1e-8,abs_tol=1e-6):
                    raise ValueError(f'Fit mismatch: {key} / {field} / {value}')
        print('PASS: R-squared, NSE, PBIAS and RMSE match twelve archived metric rows.')
    else:
        print('Observations are not bundled; fit metrics and P/R-factor were not recalculated.')


if __name__=='__main__':main()
