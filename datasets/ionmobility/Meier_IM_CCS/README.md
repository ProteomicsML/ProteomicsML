# Meier_IM_CCS

## attributes:
- data type: Peptide ion mobility
- title: Deep learning the collisional cross sections of the peptide universe from a million experimental values
- tag: Meier_IM_CCS
- data publication: https://doi.org/10.1074/mcp.tir118.000900
- ML publication: https://doi.org/10.1038/s41467-021-21352-8
- source dataset identifier: PXD010012, PXD019086, PXD017703
- species: Homo sapiens (Human), Saccharomyces cerevisiae (Baker's yeast)
- size: 718.917 (large)
- format: CSV
- columns: index, Modified sequence, Charge, Mass, Intensity, Retention time, CCS, PT
- mass modifications: unmodified & oxidation & acetylation & carbamidomethyl
- ionmobility_type: TIMS

## data description
MS raw files were analyzed with MaxQuant version 1.6.5.0, which extracts 4D isotope patterns 
(‘features’) and associated MS/MS spectra. The built-in search engine Andromeda74 was used 
to match observed fragment ions to theoretical peptide fragment ion masses derived from in 
silico digests of a reference proteome and a list of 245 potential contaminants using the 
appropriate digestion rules for each proteolytic enzyme (trypsin, LysC or LysN). We allowed 
a maximum of two missing values and required a minimum sequence length of 7 amino acids while 
limiting the maximum peptide mass to 4600 Da. Carbamidomethylation of cysteine was defined as 
a fixed modification, and oxidation of methionine and acetylation of protein N-termini were 
included in the search as variable modifications. Reference proteomes for each organism including 
isoforms were accessed from UniProt (Homo sapiens: 91,618 entries, 2019/05; E. coli: 4403 entries, 
2019/01; C. elegans: 28,403 entries, 2019/01; S. cerevisiae: 6049 entries, 2019/01; D. melanogaster: 
23,304 entries, 2019/01). The synthetic peptide library (ProteomeTools54) was searched against 
the entire human reference proteome. The maximum mass tolerances were set to 20 and 40 ppm for 
precursor and fragment ions, respectively. False discovery rates were controlled at 1% on both 
the peptide spectrum match and protein level with a target-decoy approach. The analyses were 
performed separately for each organism and each set of synthetic peptides (‘proteotypic set’, 
‘SRM atlas’, and ‘missing gene set’). To demonstrate the utility of CCS prediction, we re-analyzed 
three diaPASEF experiments from Meier et al.55 with Spectronaut 14.7.201007.47784 (Biognosys AG), 
replacing experimental ion mobility values in the spectral library with our predictions. Singly 
charged peptide precursors were excluded from this analysis as the neural network was exclusively 
trained with multiply charged peptides.

## sample protocol description:
In bottom-up proteomics, peptides are separated by liquid chromatography with elution 
peak widths in the range of seconds, while mass spectra are acquired in about 100 microseconds
with time-of-fight (TOF) instruments. This allows adding ion mobility as a third dimension of 
separation. Among several formats, trapped ion mobility spectrometry (TIMS) is attractive due 
to its small size, low voltage requirements and high efficiency of ion utilization. We have 
recently demonstrated a scan mode termed parallel accumulation – serial fragmentation (PASEF),
which multiplies the sequencing speed without any loss in sensitivity (Meier et al., PMID: 
26538118). Here we introduce the timsTOF Pro instrument, which optimally implements online 
PASEF. It features an orthogonal ion path into the ion mobility device, limiting the amount
of debris entering the instrument and making it very robust in daily operation. We investigate
different precursor selection schemes for shotgun proteomics to optimally allocate in excess 
of 100 fragmentation events per second. More than 800,000 fragmentation spectra in standard 
120 min LC runs are easily achievable, which can be used for near exhaustive precursor selection
in complex mixtures or re-sequencing weak precursors. MaxQuant identified more than 6,000 proteins
in single run HeLa analyses without matching to a library, and with high quantitative reproducibility
(R > 0.97). Online PASEF achieves a remarkable sensitivity with more than 2,000 proteins identified 
in 30 min runs of only 10 ng HeLa digest. We also show that highly reproducible collisional cross 
sections can be acquired on a large scale (R > 0.99). PASEF on the timsTOF Pro is a valuable addition
to the technological toolbox in proteomics, with a number of unique operating modes that are only
beginning to be explored.

## data anaylsis protocol:
See 'data description'

## comments:
-

