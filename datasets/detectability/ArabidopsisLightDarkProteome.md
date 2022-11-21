---
title: Arabidopsis PeptideAtlas Light and Dark Proteome
date: last-modified
---
### Downloads
[![](https://img.shields.io/badge/download-training%20dataset-205380?style=flat-square)](http://www.peptideatlas.org/builds/arabidopsis/light_and_dark_protein_list.tsv)<br>

### Dataset Description
From the Arabidopsis PeptideAtlas build (http://www.peptideatlas.org/builds/arabidopsis/)
we have extracted all the "canonical" proteins, which have been observed with at least 2
uniquely mapping peptides of length 9+AA and providing at least 18AA of coverage. We have
also extracted "not observed" proteins that have no peptide detections (that pass
PeptideAtlas's stringent thresholds) at all. Physicochemical properties and RNA-seq-based
properties are also computed and provided in the dataset.

### Attributes
- **title**: Arabidopsis PeptideAtlas Light and Dark Proteome
- **dataset tag**: `detectability/ArabidopsisLightDarkProteome`
- **data publication**: [Plant Cell](https://doi.org/10.1093/plcell/koab211)
- **machine learning publication**: None
- **data source identifier**: 52 PXDs as listed at [PeptideAtlas](https://db.systemsbiology.net/sbeams/cgi/PeptideAtlas/buildDetails?atlas_build_id=510)
- **data type**: protein detectability
- **format**: TSV
- **columns**: `protein_identifier`, `gene_symbol`, `chromosome`,
       `number_of_observations`, `molecular_weight`,
       `gravy_score`, `isoelectric_point`, `rna_detected_percent`,
	   `highest_tpm`, `protein_description`
- **instrument**: various
- **organism**: Arabidopsis thaliana (arabidopsis)
- **fixed modifications**: various
- **variable modification**: various
- **dissociation method**: CID and HCD
- **collision energy**: various
- **mass analyzer type**: various

### Data analysis protocol
52 public datasets were downloaded from ProteomeXchange repositories,
processed through the PeptideAtlas processing pipeline, and protein
categories were computed based on the ensemble data, as described in
[van Wijk et al. 2021](https://doi.org/10.1093/plcell/koab211).
The number of observations is the number of peptide-spectrum matches
in the PeptideAtlas build based on a threshold that aims for a 1%
false dicovery rate at the protein level. The molecular weight,
gravy score (hydrophobicity), and isoelectric point (pI) are
computed in Python via the Pyteomics library. The RNA-seq-based values
are computed based on a re-analysis of over 5000 RNA-seq samples as
described in Kearly et al. (submitted). The metrics are the percentage
of RNA-seq samples with a positive detection of transcripts
corresponding to the protein (a measure of how pervasive the transcripts are),
and the highest RNA abundance in transcripts per million (TPM) in the highest
sample (a measure of the highest possibly abundance at least under some
conditions).

### Comments
- None
