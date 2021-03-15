"""Split ockovaci mista."""

import pandas as pd

url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/ockovaci-mista.csv"

df = pd.read_csv(url)

months = df['datum'].str[:7].unique()

for month in months:
    df[df['datum'].str[:7] == month].to_csv("ockovaci-mista_" + month + "_v2.csv", index=False)