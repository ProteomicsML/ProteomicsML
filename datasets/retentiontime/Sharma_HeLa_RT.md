---
title: Sharma et al. HeLa
date: last-modified
---

### Downloads
[![](https://img.shields.io/badge/download-full%20dataset-008080?style=flat-square)](https://www.kaggle.com/datasets/kirillpe/proteomics-retention-time-prediction/download?datasetVersionNumber=1)

### Dataset Description
The data contains 14.361 peptides from an unknown source, and is used as a kaggle competition dataset.

### Attributes
- **title**: Kirill Pevzner "Proteomics Retention Time Prediction" dataset from Sharma et al. HeLa data from kaggle
- **dataset tag**: Sharma_HeLa_RT
- **data publication**:  <unknown>
- **machine learning publication**: <unknown>
- **data source identifier**: <unknown>

- **data type**: retention time
- **format**: TSV
- **columns**: peptide sequence, uncalibrated elution time
- **[instrument]**:  <unknown>
- **[organism]**: Homo sapiens (human)
- **[fixed modifications]**: <unknown>
- **[variable modification]**: <unknown>
- **[chromatography separation]**:  <unknown>
- **peak measurement**: <unknown>


### Sample Protocol
Unknown sample protocol

### Data Analysis Protocol
This dataset was downloaded from [kaggle](https://www.kaggle.com/datasets/kirillpe/proteomics-retention-time-prediction)
and it is a simple list of peptide sequences and uncalibrated retention times in seconds specific to one dataset.
The pedigree of the data is not well known.

### Comments
- Reference is Sharma et al., but exact publication is unknown
- The kaggle web page lists a filename "mod.txt", but the data archive includes only one file "unmod.txt"
- There are 14,361 data lines in the file (plus 1 header line)
- Header line is "sequence	RT"
- None of the peptides have a mass modification listed
- Presumably this includes only peptides with no mass modification noted in the id, rather than stripped of mods
- Are any peptide sequences repeated?
- The false discovery rate in peptide identifications is not currently known (presumably some are wrong ids)
- This may possibly be the unmodified peptides from PXD000612
- This may possibly be the unmodified peptides from https://pubmed.ncbi.nlm.nih.gov/25159151/
- This is a phospho-enriched dataset. Perhaps only the unmodified peptides are offered



[instrument]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000463
[organism]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0100026
[fixed modifications]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1003021
[variable modification]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1003022
[dissociation method]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000044
[collision energy]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000045 
[mass analyzer type]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000443&lang=en&viewMode=All&siblings=false
[chromatography separation]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1002270&lang=en&viewMode=All&siblings=false
