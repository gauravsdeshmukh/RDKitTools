"""Constants."""

import rdkit.Chem.Fragments as rcf

from pathlib import Path

# Paths
REPO_PATH = Path(__file__).parents[1]

# Functional group dictionary
func_group_dict = {
    "carb_acid": rcf.fr_COO2,
    "imine": rcf.fr_Imine,
    "amine-1": rcf.fr_NH2,
    "amine-2": rcf.fr_NH1,
    "amine-3": rcf.fr_NH0,
    "amine-4": rcf.fr_quatN,
    "hydroxyl_amine": rcf.fr_N_O,
    "thiol": rcf.fr_SH,
    "aldehyde": rcf.fr_aldehyde,
    "amide": rcf.fr_amide,
    "benzene": rcf.fr_benzene,
    "epoxide": rcf.fr_epoxide,
    "ester": rcf.fr_ester,
    "ether": rcf.fr_ether,
    "halogen": rcf.fr_halogen,
    "imide": rcf.fr_imide,
    "nitrile": rcf.fr_nitrile,
    "isocyanate": rcf.fr_isocyan,
    "ketone": rcf.fr_ketone,
    "furan": rcf.fr_furan,
    "imidazole": rcf.fr_imidazole,
    "oxime": rcf.fr_oxime,
    "phenol": rcf.fr_phenol,
    "phos_acid": rcf.fr_phos_acid,
    "pyridine": rcf.fr_pyridine,
    "urea": rcf.fr_urea,
    "nitro": rcf.fr_nitro,
    "azo": rcf.fr_azo,
    "diazo": rcf.fr_diazo,
    "thiocyan": rcf.fr_thiocyan,
    "isothiocyanate": rcf.fr_isothiocyan,
    "sulfonamide": rcf.fr_sulfonamd,
    "sulfone": rcf.fr_sulfone,
    "sulfide": rcf.fr_sulfide,
    "thiophene": rcf.fr_thiophene,
    "thiazole": rcf.fr_thiazole,
    "tetrazole": rcf.fr_tetrazole,
    "piperidine": rcf.fr_piperdine,
    "piperizine": rcf.fr_piperzine,
    "phos_ester": rcf.fr_phos_ester,
    "oxazole": rcf.fr_oxazole,
    "lactone": rcf.fr_lactone,
    "hydrazine": rcf.fr_hdrzine,
    "hydrazone": rcf.fr_hdrzone,
    "guanidine": rcf.fr_guanido,
}