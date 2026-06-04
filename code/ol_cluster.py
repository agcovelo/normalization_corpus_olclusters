"""
Lookup table describing the cluster contained in an etymon (pl, fl, bl, kl, gl, dl, tl, sl).
Information regarding the length of the obstruents is deleted (see the long_clusters variable) since ol_length will have its own lookup table.
Creates: ol_cluster.csv
"""

import pandas as pd
from config import load_corpus, get_output_path, normalize_for_sorting
import unicodedata

df = load_corpus()

# Dict/df with the specific OL clusters (without regard to the length of the obstruent)
ol_cluster_name = []
long_clusters = ['ffl', 'kkl', 'ppl', 'ttl', 'ggl']

ol_cluster_original = df["OL_cluster"].unique().tolist()

for i in ol_cluster_original:
    if i not in long_clusters:
        ol_cluster_name.append({'ol_cluster': i})
    else:
        continue

ol_cluster = pd.DataFrame(ol_cluster_name)

# Remove NaN values
ol_cluster = ol_cluster[ol_cluster['ol_cluster'].notna()]
ol_cluster = ol_cluster[ol_cluster['ol_cluster'] != 'nan']

# Order alphabetically (ignoring diachritics or special symbols)
ol_cluster.sort_values(by='ol_cluster', key=lambda col: col.map(normalize_for_sorting), inplace=True)

# Add id as index (starts from 1)
ol_cluster.index = range(1, len(ol_cluster) + 1)
ol_cluster.index.name = 'ol_cluster_id'

ol_cluster.to_csv(get_output_path('ol_cluster.csv'))
print("Created: ol_cluster.csv")
