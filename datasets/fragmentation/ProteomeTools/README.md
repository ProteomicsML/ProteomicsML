# ProteomeTools_FI

## attributes:
- data type: Fragmentation intensity
- title: ProteomeTools synthetic peptides
- tag: ProteomeTools_FI
- data publication: https://doi.org/10.1038/nmeth.4153
- ML publication: https://doi.org/10.1038/s41592-019-0426-7
- source dataset identifier: PXD004732
- species: Homo sapiens (human)
- size: Train (4.87 GB). Holdout (250 MB)
- format: hdf5
- columns: 
- mass modifications: unmodified & oxidation
- chromatography_column_type: <unknown>

## data description
The ProteomeTools project aims to derive molecular and digital
tools from the human proteome to facilitate biomedical and life science research.
Here, we describe the generation and multimodal LC-MS/MS analysis of >350,000
synthetic tryptic peptides representing nearly all canonical human gene products. This
resource will be extended to 1.4 million peptides within two years and all data will be
made available to the public in ProteomicsDB.

## sample protocol description:
Tryptic peptides were individually synthesized by solid
phase synthesis, combined into pools of ~1,000 peptides and measured on an Orbitrap
Fusion mass spectrometer. For each peptide pool, an inclusion list was generated to
target peptides for fragmentation in further LC-MS experiments using five
fragmentation methods (HCD, CID, ETD, EThCD, ETciD) with ion trap or Orbitrap
readout and HCD spectra were recorded at 6 different collision energies.

## data anaylsis protocol:
LC-MS runs were individually analyzed using MaxQuant 1.5.3.30.

## comments:
- Tutorial [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ProteomicsML/Fragmentation/blob/main/datasets/ProteomeTools/ProteomeTools%20Fragmentation.ipynb)
- Data on [FigShare](https://figshare.com/articles/dataset/ProteomeTools_-_Prosit_fragmentation_-_Data/6860261)

