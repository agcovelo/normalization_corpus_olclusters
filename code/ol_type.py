"""
Lookup table with information about the type of OL cluster in the etyma: the clusters can be either primary (etymological) or secondary (formed through syncope of the intervening vowel)
Creates: ol_type.csv
"""

import pandas as pd
from config import load_corpus, get_output_path

df = load_corpus()

# Dict/df with the OL type, e.g. primary/etymological or secondary/after syncope
ol_type_codes = df["OL_type"].unique().tolist()
# Remove NaN values
ol_type_codes = [x for x in ol_type_codes if pd.notna(x)]

ol_type_name = ['primary or etymological', 'secondary (after syncope)']

dict_ol_type = {'ol_type_id': None,
                'ol_type_name': ol_type_name,
                'ol_type_code': ol_type_codes}
ol_type = pd.DataFrame(dict_ol_type)

# Add id as index (starts from 1)
ol_type['ol_type_id'] = range(1, len(ol_type) + 1)

ol_type.to_csv(get_output_path('ol_type.csv'), index=False)
print("Created: ol_type.csv")
