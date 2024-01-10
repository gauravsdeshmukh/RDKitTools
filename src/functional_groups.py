"""Tools to detect functional groups in a molecule."""

from rdkit import Chem

from .constants import func_group_dict

class FGDetector:
    """
    A functional group detector.
    """
    def __init__(self):
        """
        Initialize functional group dictionary.
        """
        self.func_group_dict = func_group_dict

    def post_process(self, count_dict):
        """
        Post process the dictionary of functional group counts.

        Parameters
        ----------
        count_dict: dict
            Dictionary containing functional group counts.

        Returns
        -------
        count_dict: dict
            Processed count_dict
        
        """
        # -O- of ester is also recognized as ether
        count_dict["ether"] -= count_dict["ester"]

        return count_dict


    def detect(self, smiles):
        """
        Count the different functional groups in the given molecule.

        Parameters
        ----------
        smiles: str
            SMILE string for the input molecule.

        Returns
        -------
        count_dict: dict
            Dictionary containing counts of each functional group.
        
        """
        # Initialize empty counts dictionary
        count_dict = {key: 0 for key in self.func_group_dict.keys()}

        # Convert SMILES to RDKit molecule
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            # Add explicit hydrogens
            mol = Chem.AddHs(mol)

            # Get counts
            for (func_group, detector) in self.func_group_dict.items():
                count_dict[func_group] = detector(mol)

        # Post process
        count_dict = self.post_process(count_dict)

        # Return counts
        return count_dict
    

if __name__ == "__main__":
    #### Test case
    # SMILES for t-butylacetic acid
    smiles = "CC(C)(C)CC(=O)O"

    # Get functional groups
    fgd = FGDetector()
    print(fgd.detect(smiles))