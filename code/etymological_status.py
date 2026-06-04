"""
Lookup table with the different specifications for the status of an etymology.
Creates: etymological_status.csv
"""

import pandas as pd
from config import load_corpus, get_output_path

df = load_corpus()

# Dict/df with the different codes 
# Think whether we need better definitions or whether we need to replace the None with 'certain'
etymological_status_code = df["status"].unique().tolist()

# Remove NaN
etymological_status_code = [x for x in etymological_status_code if pd.notna(x)]

etymological_status_name = ['unknown or unclear etymology', 'unclear form of the etymon', 'the etymon does not contain an OL cluster', 'borrowing', 'possible borrowing']

dict_etymological_status = {'etymological_status_id': None,
                            'etymological_status_name': etymological_status_name,
                            'etymological_status_code': etymological_status_code}

etymological_status = pd.DataFrame(dict_etymological_status)

# Add id as index (starts from 1)
etymological_status['etymological_status_id'] = range(1, len(etymological_status) + 1)

etymological_status.to_csv(get_output_path('etymological_status.csv'), index=False)
print("Created: etymological_status.csv")
