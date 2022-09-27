---
title: ProteomeTools
date: last-modified
---
### Downloads
[![](https://img.shields.io/badge/download-training%20dataset-008080?style=flat-square)](https://figshare.com/ndownloader/files/12506534)<br>
[![](https://img.shields.io/badge/download-holdout%20dataset-008080?style=flat-square)](https://figshare.com/ndownloader/files/12785291)

### Dataset Description
The dataset has been divided up into training (250 MB) and holdout (4.87GB) of annotated ms2 spectra.

### Attributes
- **title**: ProteomeTools synthetic peptides
- **dataset tag**: ProteomeTools_FI
- **data publication**: [ProteomeTools](https://doi.org/10.1038/nmeth.4153)
- **machine learning publication**: [Prosit](https://doi.org/10.1038/nmeth.4153)
- **data source identifier**: PXD004732
- **data type**: fragmentation intensity
- **format**: hdf5
- **columns**: <unknown>
- **instrument**: Orbitrap Fusion ETD
- **organism**: Homo sapiens (human)
- **fixed modifications**: <unknown>
- **variable modification**: unmodified
- **dissociation method**: <unknown>
- **collision energy**: 35 and 28
- **mass analyzer type**: ion and orbitrap
- **spectra encoding**: prosit annotation pipeline 

### Sample protocol description
Tryptic peptides were individually synthesized by solid
phase synthesis, combined into pools of ~1,000 peptides and measured on an Orbitrap
Fusion mass spectrometer. For each peptide pool, an inclusion list was generated to
target peptides for fragmentation in further LC-MS experiments using five
fragmentation methods (HCD, CID, ETD, EThCD, ETciD) with ion trap or Orbitrap
readout and HCD spectra were recorded at 6 different collision energies.

### Data analysis protocol
The ProteomeTools project aims to derive molecular and digital
tools from the human proteome to facilitate biomedical and life science research.
Here, we describe the generation and multimodal LC-MS/MS analysis of >350,000
synthetic tryptic peptides representing nearly all canonical human gene products. This
resource will be extended to 1.4 million peptides within two years and all data will be
made available to the public in ProteomicsDB.
LC-MS runs were individually analyzed using MaxQuant 1.5.3.30.

### Comments
- Subset [FigShare](https://figshare.com/articles/dataset/ProteomeTools_-_Prosit_fragmentation_-_Data/6860261)
- Full [FigShare](https://figshare.com/articles/dataset/ProteomeTools_non_tryptic_-_Prosit_fragmentation_-_Data/12937092)
- Trained Model [FigShare](https://figshare.com/articles/dataset/Prosit_-_Model_-_Fragmentation/6965753)
