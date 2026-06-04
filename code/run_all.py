"""
Run all normalization scripts in the correct order.

Usage: python run_all.py
"""

import subprocess
import sys
from pathlib import Path
import os
from config import set_working_directory

# Get the directory where THIS script (and the others) are located
SCRIPT_DIR = Path(__file__).parent.resolve()
set_working_directory(SCRIPT_DIR)

# Scripts in order of dependencies
scripts = [
    # No dependencies
    "languages.py",
    "ol_position.py",
    "ol_cluster.py",
    "ol_length.py",
    "ol_type.py",
    "ol_palatalization.py",
    "etymological_status.py",
    "sources.py",
    "root_lang_check.py",
    
    # Depends on languages.csv
    "inherited_words.py",
    
    # Depends on languages.csv and ol_type.csv
    "etyma.py",
]

for script in scripts:
    print(f"\n--- Running {script} ---")
    subprocess.run([sys.executable, script])

print("\n--- Done ---")
