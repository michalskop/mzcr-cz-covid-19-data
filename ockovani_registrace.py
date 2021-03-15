"""Split ockovani registrace."""

import pandas as pd

url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/ockovani-registrace.csv"

df = pd.read_csv(url)

df = df.sort_values(['datum', 'kraj_nuts_kod', 'ockovaci_misto_id', 'vekova_skupina', 'povolani'])

months = df['datum'].str[:9].unique()

for month in months:
    df[df['datum'].str[:9] == month].to_csv("ockovani-registrace_" + month + "_v1.csv", index=False)