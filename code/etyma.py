"""
Creates: etyma.csv
Primary table with information about etyma/original words, containing wordform (PK), meaning, OL_cluster_id (FK), OL_type_id (FK), OL_position, OL_length_id (FK), root_id (FK), notes, etc)

PK = primary key
FK = foreign key

Requires: languages.csv, ol_type.csv, ol_cluster.csv, ol_position.csv, ol_length.csv (run those scripts first)
"""

import pandas as pd
from config import load_corpus, get_output_path, normalize_for_sorting
import unicodedata

df = load_corpus()

# Load lookup tables for foreign key mapping
langs = pd.read_csv(get_output_path('languages.csv'))
ol_type = pd.read_csv(get_output_path('ol_type.csv'))
ol_cluster = pd.read_csv(get_output_path('ol_cluster.csv'))
ol_length = pd.read_csv(get_output_path('ol_length.csv'))
ol_position = pd.read_csv(get_output_path('ol_position.csv'))
root = pd.read_csv(get_output_path('root.csv'))

# Identify the relevant columns in the original corpus and create a dictionary
etymon = df["etymon"].tolist()
etymon_lang = df["etymon_lang"].tolist()
ol_type_etymon = df["OL_type"].tolist()
ol_cluster_etymon = df["OL_cluster"].tolist()
ol_pos_etymon = df["OL_position"].tolist()
ol_length_etymon = df["OL_cluster"].tolist() # there is no ol_length in the original corpus. That information is contained in ol_cluster
root_etymon = df["root"].tolist()

etyma_dict = {'etymon_id': None,
              'etymon': etymon,
              'ol_type_id': ol_type_etymon,
              'ol_cluster_id': ol_cluster_etymon,
              'ol_length_id': ol_length_etymon,
              'ol_pos_id': ol_pos_etymon,
              'root_id': root_etymon,
              'lang_id': etymon_lang,
              'meaning': None,
              'notes': None
              }

# Turn the dictionary onto a pd.data frame
etyma = pd.DataFrame(etyma_dict)

# Remove duplicates (with and without misspellings)
# Remove the labels (1) and (2) to identify several clusters in the same etymon
# Keep only unique values from the column "etymon" and "ol_type_id" since some etyma have two clusters
etyma['etymon'] = etyma['etymon'].str.replace('\(\d+\)', '', regex=True)
etyma = etyma.drop_duplicates(subset=["etymon", "ol_type_id"]) 

# Order alphabetically (ignoring diachritics or special symbols)
etyma.sort_values(by='etymon', key=lambda col: col.map(normalize_for_sorting), inplace=True)

# Add the index once relevant rows have been removed
etyma["etymon_id"] = range(1, len(etyma) + 1)

# Map the corresponding lang_ids to the lang_codes in the original df
lang_to_id = dict(zip(langs["lang_code"], langs["lang_id"]))
etyma["lang_id"] = etyma["lang_id"].map(lang_to_id).astype("Int64") #Turns the ids into integers and leaves unmatched languages as NA

# Map the ol type
ol_type_to_id = dict(zip(ol_type["ol_type_code"], ol_type["ol_type_id"]))
etyma["ol_type_id"] = etyma["ol_type_id"].map(ol_type_to_id).astype("Int64")

# Map the ol clusters
etyma.replace({'ol_cluster_id': ['ffl', 'kkl', 'ppl', 'ttl', 'ggl']}, {'ol_cluster_id': ['fl', 'kl', 'pl', 'tl', 'gl']}, inplace=True) # replace the deprecated long clusters for short clusters. Length of the obstruent is now described in ol_length
ol_cluster_to_id = dict(zip(ol_cluster["ol_cluster"], ol_cluster["ol_cluster_id"]))
etyma["ol_cluster_id"] = etyma["ol_cluster_id"].map(ol_cluster_to_id).astype("Int64")

# Map ol_length
short_clusters = ['fl', 'kl', 'pl', 'tl', 'gl', 'bl', 'dl']
etyma.loc[etyma['ol_length_id'].isin(short_clusters), 'ol_length_id'] = 'short'
etyma.loc[etyma['ol_length_id'].notna() & ~etyma['ol_length_id'].isin(['short']), 'ol_length_id'] = 'long'

ol_length_to_id = dict(zip(ol_length["ol_length_name"], ol_length["ol_length_id"]))
etyma["ol_length_id"] = etyma["ol_length_id"].map(ol_length_to_id).astype("Int64")

# Map the ol position
ol_pos_to_id = dict(zip(ol_position["ol_pos_code"], ol_position["ol_pos_id"]))
etyma["ol_pos_id"] = etyma["ol_pos_id"].map(ol_pos_to_id).astype("Int64")

# Map root
root_to_id = dict(zip(root["root_form"], root["root_id"]))
etyma["root_id"] = etyma["root_id"].map(root_to_id).astype("Int64")

# Change ol_type and ol_pos for īnsŭla: if ol_cluster is indicated as None, then ol_type and ol_pos also need to be None
etyma.loc[etyma['etymon'] == "īnsŭla", 'ol_type_id'] = None
etyma.loc[etyma['etymon'] == "īnsŭla", 'ol_pos_id'] = None

# Create csv
etyma.to_csv(get_output_path('etyma.csv'), index=False)
print("Created: etyma.csv")


