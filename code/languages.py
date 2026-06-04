"""
Lookup table with information about the languages or linguistic varieties of etyma, roots, and inherited words.
Some languages that appeared in the original corpus are deprecated and now considered Spanish (Sp.) or Portuguese (Pt.), for example Andal. Sp. or Cant. This information is contained in the inherited_word table, where regional infomation about an inherited word is given.
Creates: languages.csv
"""

import pandas as pd
from config import get_output_path, normalize_for_sorting

# Language data
lang_codes = ['Germ.', 'Gaul.', 'Late Lat.', 'Got.', 'u.o.', 'Lat.', 'OFr.', 'OHG', 'Arab.', 'Occ.', 'Fr.', 'Gal.', 'GP', 'Pt.', 'Ast.', 'Sp.', 'OSp.', 'Rib. Arag.', 'Leon.', 'Arag.', 'Montañ. or AL', 'AL', 'Mir.', 'Mozarab.']

langs = ['Germanic', 'Gaulish', 'Late Latin', "Gothic", 'unknown', 'Latin', 'Old French', 'Old High German', 'Arabic', 'Occitan', 'French', 'Galician', 'Galician-Portuguese', 'Portuguese', 'Asturian', 'Spanish', 'Old Spanish', 'Ribagorçan Aragonese', 'Leonese', 'Aragonese', 'Montañese or Astur-Leonese', 'Astur-Leonese', 'Mirandese', 'Mozarabic']

iso_codes = ['gem', None, None, "got", None, 'lat', 'fro', 'goh', 'ara', 'oci', 'fra', 'glg', None, 'por', 'ast', 'spa', 'osp', None, 'ast', 'arg', 'ast', 'ast', 'mwl', 'mxi']

dict_lang = {'lang_id': None,
             'lang_name': langs,
             'lang_code': lang_codes,
             'iso_639_2_3': iso_codes}

langs = pd.DataFrame(dict_lang)

# Order alphabetically (ignoring diachritics or special symbols)
langs.sort_values(by='lang_name', key=lambda col: col.map(normalize_for_sorting), inplace=True)

# Add id as index (starts from 1)
langs["lang_id"] = range(1, len(langs) + 1)

langs.to_csv(get_output_path('languages.csv'), index=False)
print("Created: languages.csv")
