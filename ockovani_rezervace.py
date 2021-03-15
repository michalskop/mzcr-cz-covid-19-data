"""Split ockovani registrace."""

import pandas as pd

url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/ockovani-rezervace.csv"

df = pd.read_csv(url)

df = df.sort_values(['datum', 'kraj_nuts_kod', 'ockovaci_misto_id'])

months = df['datum'].str[:7].unique()

for month in months:
    df[df['datum'].str[:7] == month].to_csv("ockovani-rezervace_" + month + "_v1.csv", index=False)