---
title: Van Puyvelde et al. TWIMS
date: last-modified
---

### Downloads
[![](https://img.shields.io/badge/download-full%20dataset-008080?style=flat-square)](https://github.com/ProteomicsML/ProteomicsML/raw/main/datasets/ionmobility/VanPuyvelde_TWIMS_CCS/TWIMSpeptideCCS.tsv.gz)


### Dataset Description
The data consists of 6.268 PSMs.

### Attributes
- **title**: A comprehensive LFQ benchmark dataset on modern day acquisition strategies in proteomics
- **dataset tag**: VanPuyvelde_TWIMS_CCS
- **data publication**: [Scientific Data](https://doi.org/10.1038/s41597-022-01216-6)
- **machine learning publication**: <unknown>
- **data source identifier**: PXD028735


- **data type**: ion mobility
- **format**: TSV
- **columns**: `Modified sequence` `Charge` `CCS` `Ion Mobility` `Ion Mobility Units` `High Energy` `Ion Mobility Offset`
- **[instrument]**: maXis, timsTOF Pro, 
- **[organism]**: Homo sapiens (Human), Saccharomyces cerevisiae (Baker's yeast), Escherichia coli (E. coli)
- **[fixed modifications]**: <unknown>
- **[variable modification]**:unmodified & oxidation & acetylation & carbamidomethyl
- **ionmobility type**: TWIMS
- **css calibration compounds**: <unknown>


### Sample Protocol
*From the original paper:*

Mass spectrometry-compatible Human K562 (P/N: V6951) and Yeast (P/N: V7461) protein digest extracts were
purchased from Promega (Madison, Wisconsin, United States). Lyophilised MassPrep Escherichia.coli digest
standard (P/N:186003196) was purchased from Waters Corporation (Milford, Massachusetts, United States).
The extracts were reduced with dithiothreitol (DTT), alkylated with iodoacetamide (IAA) and digested with
sequencing grade Trypsin(-Lys C) by the respective manufacturers. The digested protein extracts were reconstituted
in a mixture of 0.1% Formic acid (FA) in water (Biosolve B.V, Valkenswaard, The Netherlands) and spiked with iRT
peptides (Biognosys, Schlieren, Switzerland) at a ratio of 1:20 v/v. Two master samples A and B were created
similar to Navarro et al., each in triplicate, as shown in Fig. 1. Sample A was prepared by mixing Human, Yeast
and E.coli at 65%, 30% and 5% weight for weight (w/w), respectively. Sample B was prepared by mixing Human,
Yeast and E.coli protein digests at 65%, 15%, 20% w/w, respectively. The resulting samples have logarithmic
fold changes (log2FCs) of 0, −1 and 2 for respectively Human, Yeast and E.coli. One sixth of each of the
triplicate master batches of A and B were mixed to create a QC sample, containing 65% w/w Human, 22.5% w/w
Yeast and 12.5% w/w E.coli.

### Data Analysis Protocol
*From the original paper:*

An M-class LC system (Waters Corporation, Milford, MA) was equipped with a 1.7 µm CSH 130 C18 300 µm ×
100 mm column, operating at 5 µL/min with a column temperature of 55 °C. Mobile phase A was UPLC-grade
water containing 0.1% (v/v) FA and 3% DMSO, mobile phase B was ACN containing 0.1% (v/v) FA. Peptides
were separated using a linear gradient of 3−30% mobile phase B over 120 minutes. All experiments were
conducted on a Synapt G2-Si mass spectrometer (Waters Corporation, Wilmslow, UK). The ESI Low Flow probe
capillary voltage was 3 kV, sampling cone 60 V, source offset 60 V, source temperature 80 °C, desolvation
temperature 350 °C, cone gas 80 L/hr, desolvation gas 350 L/hr, and nebulizer pressure 2.5 bar. A lock mass
 reference signal of GluFibrinopeptide B (m/z 785.8426) was sampled every 30 s.

### Comments:
- #


[instrument]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000463
[organism]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0100026
[fixed modifications]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1003021
[variable modification]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1003022
[dissociation method]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000044
[collision energy]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000045 
[mass analyzer type]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000443&lang=en&viewMode=All&siblings=false
[chromatography separation]: https://www.ebi.ac.uk/ols/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1002270&lang=en&viewMode=All&siblings=false
