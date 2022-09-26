---
title: ProteomeTools
date: last-modified
---


## Downloads
[![](https://img.shields.io/badge/download-small%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Small.csv.gz)<br>
[![](https://img.shields.io/badge/download-medium%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Medium.csv.gz)<br>
[![](https://img.shields.io/badge/download-large%20dataset-205380?style=flat-square)](hhttps://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Large.csv.gz)<br>
[![](https://img.shields.io/badge/download-mixed%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Mixed.csv.gz)<br>
[![](https://img.shields.io/badge/download-oxidation%20dataset-205380?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/retentiontime/ProteomeTools/Oxidation.csv.gz)<br>

## Dataset Description
The full data contains 1.000.000 unmodified peptides and 150.000 oxidized peptides all with MaxQuant scores > 100 split into five groups.

- Small: Containing 100.000 unmodified peptides (good for teaching)
- Medium: Containing 250.000 unmodified peptides (good for validating)
- Large: Containing 250.000 unmodified peptides (good for training)
- Oxidized: Containing 150.000 all oxidized peptides.
- Mixed: Containing 150.000 oxidized and 150.000 unmodified peptides.

## Attributes
- data type: Peptide retention time
- title: ProteomeTools synthetic peptides and iRT calibrated retention times
- tag: ProteomeTools_RT
- data publication: [https://doi.org/10.1038/nmeth.4153](https://doi.org/10.1038/nmeth.4153)
- ML publication: [https://doi.org/10.1038/s41592-019-0426-7](https://doi.org/10.1038/s41592-019-0426-7)
- source dataset identifier: PXD004732
- species: Homo sapiens (human)
- format: CSV
- columns: index, retention time, sequence, modified sequence
- mass modifications: unmodified & oxidation
- chromatography_column_type: <unknown>

## Data description
The ProteomeTools project aims to derive molecular and digital
tools from the human proteome to facilitate biomedical and life science research.
Here, we describe the generation and multimodal LC-MS/MS analysis of >350,000
synthetic tryptic peptides representing nearly all canonical human gene products. This
resource will be extended to 1.4 million peptides within two years and all data will be
made available to the public in ProteomicsDB.

## Sample protocol description
Tryptic peptides were individually synthesized by solid
phase synthesis, combined into pools of ~1,000 peptides and measured on an Orbitrap
Fusion mass spectrometer. For each peptide pool, an inclusion list was generated to
target peptides for fragmentation in further LC-MS experiments using five
fragmentation methods (HCD, CID, ETD, EThCD, ETciD) with ion trap or Orbitrap
readout and HCD spectra were recorded at 6 different collision energies.

## Data analysis protocol
LC-MS runs were individually analyzed using MaxQuant 1.5.3.30.

## Comments
- The full dataset was reduced in size to small, medium, and large sizes
- The original processed data can be found on figshare: [https://figshare.com/projects/prosit/35582](https://figshare.com/projects/prosit/35582)
