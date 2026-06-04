"""
Lookup table with information about the position of OL clusters within an etymon: word-initial, postconsonantal, or postvocalic.
Creates: ol_position.csv
"""

import pandas as pd
from config import load_corpus, get_output_path

df = load_corpus()

# Dict/df with the position within the word
ol_pos_codes = df["OL_position"].unique().tolist()
# Remove NaN values
ol_pos_codes = [x for x in ol_pos_codes if pd.notna(x)]

ol_pos_name = ['word-initial', 'postconsonantal', 'postvocalic']

dict_ol_pos = {'ol_pos_id': None,
               'ol_pos_name': ol_pos_name,
               'ol_pos_code': ol_pos_codes}
ol_pos = pd.DataFrame(dict_ol_pos)

# Add id as index (starts from 1)
ol_pos['ol_pos_id'] = range(1, len(ol_pos) + 1)

ol_pos.to_csv(get_output_path('ol_position.csv'), index=False)
print("Created: ol_position.csv")
