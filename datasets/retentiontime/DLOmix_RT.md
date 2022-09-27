---
title: DLOmix
date: last-modified
---
### Download
[![](https://img.shields.io/badge/download-training%20dataset-008080?style=flat-square)](https://github.com/wilhelm-lab/dlomix/blob/develop/example_dataset/proteomTools_test.csv?raw=true)<br>
[![](https://img.shields.io/badge/download-validation%20dataset-008080?style=flat-square)](https://github.com/wilhelm-lab/dlomix/blob/develop/example_dataset/proteomTools_train.csv?raw=true)<br>
[![](https://img.shields.io/badge/download-train/val%20dataset-008080?style=flat-square)](https://github.com/wilhelm-lab/dlomix/blob/develop/example_dataset/proteomTools_train_val.csv?raw=true)<br>
[![](https://img.shields.io/badge/download-testing%20dataset-008080?style=flat-square)](https://github.com/wilhelm-lab/dlomix/blob/develop/example_dataset/proteomTools_val.csv?raw=true)<br>

### Dataset Description
This is a direct subset of the ProteomeTools dataset with computed iRTs based on the PROCAL. 
The total data contains ~27.200 peptides and is mainly useful for teaching purposes
- Training: Containing 27.160 peptides
- Validation: Containing 6.800 peptides
- Testing: Containing 6.000 peptides
- Train/val: Containing 27.200 peptides.

### Attributes
- **title**: DLOmix deep learning in proteomics python framework for retention time
- **dataset tag**: DLOmix_RT
- **data publication**: [ProteomeTools](https://doi.org/10.1038/nmeth.4153)
- **machine learning publication**: [Prosit](https://doi.org/10.1038/nmeth.4153)
- **data source identifier**: PXD004732


- **data type**: retention time
- **format**: CSV
- **columns**: peptide sequence, iRT calibrated retention time
- **[instrument]**: Orbitrap Fusion ETD
- **[organism]**: Homo sapiens (human)
- **[variable modification]**: unmodified
- **[chromatography separation]**: <unknown>
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
- Internal DLOmix tutorial [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wilhelm-lab/dlomix/blob/develop/notebooks/Example_RTModel_Walkthrough_colab.ipynb)
- DLOmix [GitHub](https://github.com/wilhelm-lab/dlomix)


[instrument]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000463
[organism]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0100026
[fixed modifications]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1003021
[variable modification]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1003022
[dissociation method]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000044
[collision energy]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000045 
[mass analyzer type]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000443&lang=en&viewMode=All&siblings=false
[chromatography separation]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1002270&lang=en&viewMode=All&siblings=false
