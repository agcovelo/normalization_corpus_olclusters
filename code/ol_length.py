"""
Lookup table with information about the length of the obstruent in OL clusters.
In the original corpus, this information was contained in the column 'OL_cluster'.
Creates: ol_length.csv
"""

import pandas as pd
from config import get_output_path

# Dict/df with the length of the obstruent in the OL cluster
ol_length_name = ['short', 'long']

ol_length_dict = {'ol_length_id': None,
                  'ol_length_name': ol_length_name}

ol_length = pd.DataFrame(ol_length_dict)

# Add id as index (starts from 1)
ol_length['ol_length_id'] = range(1, len(ol_length) + 1)

ol_length.to_csv(get_output_path('ol_length.csv'), index=False)
print("Created: ol_length.csv")
