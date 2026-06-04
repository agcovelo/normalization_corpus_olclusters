"""
Creates: root_lang_check.csv

Intermediate check file - not a final table.
"""

import pandas as pd
from config import load_corpus, get_output_path

df = load_corpus()

# Find how many unique lang_ids (Lat., Late Lat., etc.) each root has
root_lang_check = df.groupby('root')['etymon_lang'].nunique()
root_lang_check.to_csv(get_output_path('root_lang_check.csv'))
print("Created: root_lang_check.csv")


# #Dict/df roots of the etyma
# root_form = df["root"].unique().tolist()
# etymon_lang = df["etymon_lang"].tolist()

# #Find how many unique lang_ids (Lat., Late Lat., etc.) each root has
# root_lang_check = df.groupby('root')['etymon_lang'].nunique()
# root_lang_check.to_csv('root_lang_check.csv')

# # dict_root = {'root_form': root_form, 'lang_id': etymon_lang}
# # root = pd.DataFrame(dict_root)
# # root['root_id'] = range(1, len(root) + 1)


# # Map the corresponding lang_ids to the lang_codes in the original df
# # lang_to_id = dict(zip(langs["lang_code"], langs["lang_id"]))
# # root["lang_id"] = root["lang_id"].map(lang_to_id).astype("Int64") #Turns the ids into integers and leaves unmatched languages as NA

# # root.to_csv('root.csv', index=False)