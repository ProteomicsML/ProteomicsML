# Sharma_HeLa_RT

## attributes:
- data type: Peptide retention time
- title: Kirill Pevzner "Proteomics Retention Time Prediction" dataset from Sharma et al. HeLa data from kaggle
- tag: Sharma_HeLa_RT
- data publication: <unknown>
- ML publication: <unknown>
- source dataset identifier: <unknown>
- species: Homo sapiens (human)
- size: 14361 peptides
- format: TSV
- columns: peptide sequence, uncalibrated elution time
- chromatography_column_type: <unknown>

## data description:
This dataset was downloaded from kaggle (https://www.kaggle.com/datasets/kirillpe/proteomics-retention-time-prediction)
It is a simple list of peptide sequences and uncalibrated retention times in seconds specific to one dataset.
The pedigree of the data is not well known.

## comments:
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










