"""
Creates: inherited_words.csv
Main table for the inherited_words and their related information, i.e. attestation date, meaning, is_primary, notes, etc.
Requires: languages.csv (run languages.py first)
"""

import pandas as pd
from config import load_corpus, get_output_path, normalize_for_sorting
import unicodedata

# Load corpus table and languages table to get the mapping
df = load_corpus()
langs = pd.read_csv(get_output_path('languages.csv'))

# Create a dictionary with the necessary key:item pairs
inherited_word = df["inherited_form"].tolist() 
lang_variety = df["lang_variety"].tolist()
date = df['date'].tolist()

inherited_word_dict = {'inherited_word_id': None,
                       'inherited_word': inherited_word,
                       'meaning': None,
                       'lang_id': lang_variety,
                       'first_attestation': date,
                       'is_primary': 'yes',
                       'is_regional': 'no',
                       'variety_or_region': None,
                       'notes': None
                       }

# Turn the dictionary into a data frame
inherited_words = pd.DataFrame(inherited_word_dict)

# Replace deprecated linguistic denominations with new ones. 
# The contained regional information will still be visible in the columns is.regional and region/dialect, but it is not longer in the languages lookup table

# Create a dictionary of old labels -> new labels
variety_replacements = {
    'Alav.': 'Sp.',
    'Andal. Sp. ': 'Sp.',
    'Cant.': 'Sp.',
    'Nav.': 'Sp.',
    'Sant.': 'Sp.',
    'Salam.': 'Sp.',
    'Ast., Sant., Burg.': 'Sp.',
    'Pt. Trasm.': 'Pt.',
    'Minh. Pt.': 'Pt.'
}
regions = {
    'Alav.': 'Alava',
    'Andal. Sp. ': 'Andalucia',
    'Cant.': 'Cantabria',
    'Nav.': 'Navarra',
    'Sant.': 'Santander',
    'Salam.': 'Salamanca',
    'Ast., Sant., Burg.': 'Asturias, Santander, Burgos',
    'Pt. Trasm.': 'Tras-os-Montes',
    'Minh. Pt.': 'Minhoto'
}

varieties = ['Alav.', 'Andal. Sp. ','Cant.','Nav.','Sant.','Salam.','Ast., Sant., Burg.','Pt. Trasm.','Minh. Pt.']

# Loop through the regions_dictionary and, if the lang_id value corresponds with the key of the dictionary (the language codes), replace the corresponding value in the column "variety_or_region" with the value of that dictionary
for lang_id, variety_or_region in regions.items(): #.items gives out the key:value of the dictionary
    inherited_words.loc[inherited_words['lang_id'] == lang_id, 'variety_or_region'] = variety_or_region

# Set is.regional to 'yes' if the lang_id corresponds to an element in the varieties list
inherited_words.loc[inherited_words['lang_id'].isin(varieties), 'is_regional'] = 'yes'

# Replace the old labels with new ones in your lang_variety column
inherited_words['lang_id'] = inherited_words['lang_id'].replace(variety_replacements)

# Map the corresponding lang_ids to the lang_codes in the original df
lang_to_id = dict(zip(langs["lang_code"], langs["lang_id"]))
inherited_words["lang_id"] = inherited_words["lang_id"].map(lang_to_id).astype("Int64") #Turns the ids into integers and leaves unmatched languages as NA

# Delete duplicate inherited words from etyma with more than one cluster
# e.g. clāvĭcŭla (1) and (2) result in OSp. llavija.
# Delete "llavija", "llavija", "chauella", "chocallo", "locajo", "landoas", "lancha", lancha", lancha", "fótula" (no subset, the whole row needs to be unique)
# Duplicated items can be found with duplicated = inherited_words[inherited_words.duplicated()]

inherited_words = inherited_words.drop_duplicates()

# Order alphabetically (ignoring diachritics or special symbols)
inherited_words.sort_values(by='inherited_word', key=lambda col: col.map(normalize_for_sorting), inplace=True)

# Add the index once relevant rows have been removed
inherited_words['inherited_word_id'] = range(1, len(inherited_words) + 1)

# Create the csv
inherited_words.to_csv(get_output_path('inherited_words.csv'), index=False)
print("Created: inherited_words.csv")
