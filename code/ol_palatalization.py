"""
Lookup table with information about the presence, absence or uncertainty of OL palatalization in an inherited word.
Creates: ol_palatalization.csv
"""

import pandas as pd
from config import load_corpus, get_output_path

df = load_corpus()

# Dict/df with the presence or absence of OL palatalization
ol_pal_codes = df["palat"].unique().tolist()

# Remove NaN values
ol_pal_codes = [x for x in ol_pal_codes if pd.notna(x)]

ol_pal_name = ['yes', 'no', 'uncertain']

dict_ol_pal = {'ol_pal_id': None,
               'ol_pal_name': ol_pal_name,
               'ol_pal_code': ol_pal_codes}

ol_pal = pd.DataFrame(dict_ol_pal)

# Add id as index (starts from 1)
ol_pal['ol_pal_id'] = range(1, len(ol_pal) + 1)

ol_pal.to_csv(get_output_path('ol_palatalization.csv'), index=False)
print("Created: ol_palatalization.csv")

