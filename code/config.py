"""
Shared configuration for all scripts. Loads the corpus and sets relevant directories
If the directory structure is keept the same, the paths do not need editing.
If not, edit the paths in INPUT_CSV and OUTPUT_DIR to match your local environment.
"""

import os
import pandas as pd
from pathlib import Path
import unicodedata

# =============================================================================
# PATHS - EDIT THESE
# =============================================================================

# Get the directory where THIS script is located
SCRIPT_DIR = Path(__file__).parent.resolve()

# Build paths relative to script location
# Where your input CSV is located
INPUT_CSV = SCRIPT_DIR.parent / "data" / "corpus_olclusters.csv"

# Where the output CSVs will be saved (separate from your code)
OUTPUT_DIR = SCRIPT_DIR.parent / "output"

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_corpus():
    """Load and return the corpus DataFrame."""
    return pd.read_csv(INPUT_CSV, header=0)

def get_output_path(filename):
    """Return the full path for an output file."""
    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    return os.path.join(OUTPUT_DIR, filename)

def set_working_directory(path):
    os.chdir(path)
    
def normalize_for_sorting(s):
    """Normalize strings for alphabetical sorting, ignoring diacritics and symbols."""
    if not isinstance(s, str): # handle NaN
        return ''
    # Handle ñ BEFORE decomposition
    s = s.replace('ñ', 'n~').replace('Ñ', 'N~')
    # Handel * (reconstruction) and parenthesis
    s = s.replace('*', '').replace('(', '').replace(')', '')
    # Decompose characters (é → e + combining acute accent)
    normalized = unicodedata.normalize('NFD', s) # Normalization Form Decomposed
    
    # Remove combining marks (diachritics)
    stripped = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn') # Loops through each character of the normalized string and removes the following diachritic
    return stripped.lower()