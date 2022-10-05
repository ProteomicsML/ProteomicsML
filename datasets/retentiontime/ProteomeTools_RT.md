---
title: ProteomeTools
date: last-modified
---

### Downloads
[![](https://img.shields.io/badge/download-small%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Small.csv.gz)<br>
[![](https://img.shields.io/badge/download-medium%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Medium.csv.gz)<br>
[![](https://img.shields.io/badge/download-large%20dataset-205380?style=flat-square)](hhttps://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Large.csv.gz)<br>
[![](https://img.shields.io/badge/download-mixed%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Mixed.csv.gz)<br>
[![](https://img.shields.io/badge/download-oxidation%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Oxidation.csv.gz)<br>

### Dataset Descriptions
The full data contains 1.000.000 unmodified peptides and 150.000 oxidized peptides all with MaxQuant scores > 100 (as described in Prosit paper) split into five groups. <br>
- Small: Containing 100.000 unmodified peptides (good for teaching) <br>
- Medium: Containing 250.000 unmodified peptides (good for validating) <br>
- Large: Containing 250.000 unmodified peptides (good for training) <br>
- Oxidized: Containing 150.000 all oxidized peptides. <br>
- Mixed: Containing 150.000 oxidized and 150.000 unmodified peptides. <br>


### Attributes
* **title**: ProteomeTools synthetic peptides and iRT calibrated retention times
* **dataset tag**: ProteomeTools_RT
* **data publication**: [ProteomeTools](https://doi.org/10.1038/nmeth.4153)
* **machine learning publication**: [Prosit](https://doi.org/10.1038/nmeth.4153)
* **data source identifier**: PXD004732
- **data type**: retention time
- **format**: CSV
- **columns**: `index`, `retention time`, `sequence`, `modified`, `sequence`
- **instrument**: Orbitrap Fusion ETD
- **organism**: Homo sapiens (human)
- **variable modification**: unmodified & oxidation
- **chromatography separation**: <unknown>
- **peak measurement**: <unknown>


### Sample Protocol
Tryptic peptides were individually synthesized by solid
phase synthesis, combined into pools of ~1,000 peptides and measured on an Orbitrap
Fusion mass spectrometer. For each peptide pool, an inclusion list was generated to
target peptides for fragmentation in further LC-MS experiments using five
fragmentation methods (HCD, CID, ETD, EThCD, ETciD) with ion trap or Orbitrap
readout and HCD spectra were recorded at 6 different collision energies.

### Data Analysis Protocol
The ProteomeTools project aims to derive molecular and digital
tools from the human proteome to facilitate biomedical and life science research.
Here, we describe the generation and multimodal LC-MS/MS analysis of >350,000
synthetic tryptic peptides representing nearly all canonical human gene products. This
resource will be extended to 1.4 million peptides within two years and all data will be
made available to the public in ProteomicsDB.

### Comments
- #

