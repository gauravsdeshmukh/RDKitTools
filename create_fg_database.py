"""Script to create a database of functional groups from SMILES data."""

import json
import os
import pandas as pd

from tqdm import tqdm

from src.functional_groups import FGDetector
from src.constants import SMILES_PATH, SAVE_PATH, func_group_dict

# Function to read data from folder
def read_json(filepath):
    """
    Function to get SMILES from JSON.

    Parameters
    ----------
    filepath: str
        Path to the json file

    Returns
    -------
    smiles: str
        SMILES string

    """
    # Read file
    with open(filepath, "r") as f:
        data = json.load(f)

    # Get smiles
    smiles = data["Canonical SMILES"]

    return smiles

# Create empty dataframe to store results
df = pd.DataFrame({"SMILES": [""] * 150000})
for func_group in func_group_dict.keys():
    df[func_group] = [0] * 150000

# Create detectpr
print("Detecting functional groups...")
fgd = FGDetector()

# Go over json files in SMILES path
for root, dirs, files in os.walk(SMILES_PATH):
    for i, fname in enumerate(tqdm(files)):
        fpath = os.path.join(root, fname)
        smiles = read_json(fpath)
        count_dict = fgd.detect(smiles)
        row_dict = {}
        row_dict["SMILES"] = smiles
        row_dict.update(count_dict)
        df.iloc[i, :] = row_dict.values()
        #new_row = pd.Series(count_dict)
        #df = pd.concat([df, new_row], ignore_index=True)
    break
    
# Save results
df = df.loc[df["SMILES"] != "", :]
results_path = SAVE_PATH / "results.csv"

# Remove 0 columns
df = df.loc[:, (df != 0).any(axis=0)]
df.to_csv(results_path)
print("Saved results.")

