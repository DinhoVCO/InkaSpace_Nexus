NPJ Microgravity

. 2019 Apr 3;5:9. doi: [10.1038/s41526-019-0070-7](https://doi.org/10.1038/s41526-019-0070-7)

# Spaceflight-induced alternative splicing during seedling development in *Arabidopsis thaliana*

[Nicole S Beisel](https://pubmed.ncbi.nlm.nih.gov/?term=%22Beisel%20NS%22%5BAuthor%5D)

### Nicole S Beisel

1Plant Molecular & Cellular Biology Program, University of Florida, Gainesville, FL USA

Find articles by [Nicole S Beisel](https://pubmed.ncbi.nlm.nih.gov/?term=%22Beisel%20NS%22%5BAuthor%5D)

1, [Jerald Noble](https://pubmed.ncbi.nlm.nih.gov/?term=%22Noble%20J%22%5BAuthor%5D)

### Jerald Noble

1Plant Molecular & Cellular Biology Program, University of Florida, Gainesville, FL USA

Find articles by [Jerald Noble](https://pubmed.ncbi.nlm.nih.gov/?term=%22Noble%20J%22%5BAuthor%5D)

1, [W Brad Barbazuk](https://pubmed.ncbi.nlm.nih.gov/?term=%22Barbazuk%20WB%22%5BAuthor%5D)

### W Brad Barbazuk

1Plant Molecular & Cellular Biology Program, University of Florida, Gainesville, FL USA

2Interdisciplinary Center for Biotechnology Research, University of Florida, Gainesville, FL USA

3Department of Biology, University of Florida, Gainesville, FL USA

4Genetics Institute, University of Florida, Gainesville, FL USA

Find articles by [W Brad Barbazuk](https://pubmed.ncbi.nlm.nih.gov/?term=%22Barbazuk%20WB%22%5BAuthor%5D)

1,2,3,4, [Anna-Lisa Paul](https://pubmed.ncbi.nlm.nih.gov/?term=%22Paul%20AL%22%5BAuthor%5D)

### Anna-Lisa Paul

1Plant Molecular & Cellular Biology Program, University of Florida, Gainesville, FL USA

5Department of Horticultural Sciences, University of Florida, Gainesville, FL USA

Find articles by [Anna-Lisa Paul](https://pubmed.ncbi.nlm.nih.gov/?term=%22Paul%20AL%22%5BAuthor%5D)

1,5, [Robert J Ferl](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ferl%20RJ%22%5BAuthor%5D)

### Robert J Ferl

1Plant Molecular & Cellular Biology Program, University of Florida, Gainesville, FL USA

2Interdisciplinary Center for Biotechnology Research, University of Florida, Gainesville, FL USA

5Department of Horticultural Sciences, University of Florida, Gainesville, FL USA

Find articles by [Robert J Ferl](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ferl%20RJ%22%5BAuthor%5D)

1,2,5,✉

* Author information
* Article notes
* Copyright and License information

1Plant Molecular & Cellular Biology Program, University of Florida, Gainesville, FL USA

2Interdisciplinary Center for Biotechnology Research, University of Florida, Gainesville, FL USA

3Department of Biology, University of Florida, Gainesville, FL USA

4Genetics Institute, University of Florida, Gainesville, FL USA

5Department of Horticultural Sciences, University of Florida, Gainesville, FL USA

✉

Corresponding author.

Received 2018 Sep 18; Accepted 2019 Mar 7; Collection date 2019.

© The Author(s) 2019

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit <http://creativecommons.org/licenses/by/4.0/>.

[PMC Copyright notice](/about/copyright/)

PMCID: PMC6447593  PMID: [30963109](https://pubmed.ncbi.nlm.nih.gov/30963109/)

## Abstract

Plants grown in spaceflight experience novel environmental signals, including those associated with microgravity and ionizing radiation. Spaceflight triggers a response involving transcriptional re-programming and altered cell morphology, though many aspects of this response remain uncharacterized. We analyzed the spaceflight-induced transcriptome with a focus on genes that undergo alternative splicing to examine differential splicing associated with spaceflight—an unstudied characteristic of the molecular response to spaceflight exposure. RNA sequence data obtained during the APEX03 spaceflight experiment that was collected from two *Arabidopsis thaliana* ecotypes at two seedling stages grown onboard the International Space Station, or as ground controls at Kennedy Space Center, were re-examined to detect alternative splicing differences induced by spaceflight. Presence/absence variation analysis was used to identify putative expression-level differences in alternatively spliced isoforms between spaceflight and ground controls and was followed by analysis of significant differential alternative splicing. This study provides the first evidence of a role for alternative splicing in the molecular processes of physiological adaptation to the spaceflight environment.

## Introduction

During growth on the International Space Station (ISS), plants encounter a suite of abiotic stressors largely owing to the effects of microgravity, cosmic radiation, and other less-characterized stresses associated with the spaceflight environment. Similar to observations made in response to terrestrial plant stresses, exposure to the spaceflight environment triggers a unique transcriptional response.[1](#CR1)–[4](#CR4) Patterns of spaceflight-induced gene expression have been analyzed in a variety of experiments carried out onboard the ISS, with focus on dissecting the transcriptome at the resolution of individual genes rather than transcript isoforms.[1](#CR1)–[4](#CR4)

Alternative splicing (AS) is the phenomenon by which exons and introns can be differentially joined together to result in the production of multiple distinct transcript isoforms derived from a single parent gene locus (reviewed in ref. [5](#CR5)). AS greatly enhances the diversity of the eukaryotic transcriptome. In the model plant *Arabidopsis thaliana*, as many as 60% of intron-containing genes undergo AS.[6](#CR6) In addition, unique AS patterns arise in response to terrestrial plant stressors.[5](#CR5),[7](#CR7)–[11](#CR11) To investigate the role of AS during spaceflight adaptation in plants, RNA sequencing data collected during the APEX03 experiment from *A. thaliana* seedlings grown on board the ISS in comparison to seedlings grown as ground controls at Kennedy Space Center (KSC) were analyzed using a bioinformatics pipeline specifically developed to be aware of AS events (adapted from ref. [12](#CR12)).

The APEX03 experiment featured two different *A. thaliana* ecotypes, Columbia-0 (Col-0) and Wassilewskija (WS), and involved RNA sequencing of root tissue from both 4- and 8-day-old seedlings grown on 10 cm2 petri plates containing Phytagel then preserved in RNALater on orbit. These time points were chosen because by 8 days of growth *Arabidopsis* seedlings will transition to photosynthesizing using true leaves, which is a major shift during seedling development. Root morphological differences between Col-0 and WS cultivars have been studied in spaceflight previously: Col-0 is known to exhibit much weaker root skewing in microgravity, compared to the strong rightward root skewing observed in the WS ecotype.[13](#CR13)

Following RNA sequencing, the raw reads were processed using a bioinformatics pipeline designed to analyze the transcriptome with resolution at the level of individual transcript isoforms (Fig. [1a](#Fig1)) (adapted from ref. [12](#CR12)). This pipeline differs from standard pipelines utilized to assess differential gene expression in that three distinct transcript assembly programs are used to maximize the robustness of transcript isoform discovery.[12](#CR12) Presence/absence variation (PAV) of AS isoforms was then performed utilizing extremely stringent criteria to identify the expression level differences in AS isoforms between spaceflight and ground controls. To count an AS isoform as present in each condition, the isoform was required to be expressed at an FPKM (fragments per kilobase of transcript per million mapped reads) ≥10 in all four biological replicates of a given condition and was required to come from a parent gene that undergoes AS as identified by the pipeline used in this analysis. By using a high FPKM value as a strict expression level cutoff and eliminating results with biological variation, lists of AS isoforms strongly present in each condition were generated with high confidence (Supplementary Data File [1](#MOESM2)). Consequentially, AS isoforms considered absent in each condition may not be entirely absent but rather not expressed at a high enough level to be classified as present in this analysis. This PAV analysis resulted in the identification of AS isoforms with expression-level differences between spaceflight and ground control samples in both ecotypes and developmental stages tested (Fig. [1b](#Fig1)). Orthogonal validation of AS isoforms counted as present or absent was performed by re-aligning the RNA sequencing reads to the reference genome utilizing a separate alignment program. Sequencing depth and splice junction coverage were then assessed using Integrative Genomics Viewer[14](#CR14) to experimentally validate a subset of the isoforms counted as present or absent in each condition (Supplementary Fig. [1](#MOESM1)–[4](#MOESM1)). PAV analysis therefore enabled the identification of AS isoforms with expression-level differences in spaceflight, which reflects behavior of the transcriptional machinery within the cell.

### Fig. 1.

[![Fig. 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4444/6447593/f5032c0d9591/41526_2019_70_Fig1_HTML.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=6447593_41526_2019_70_Fig1_HTML.jpg)

[Open in a new tab](figure/Fig1/)

Detection of spaceflight-induced alternatively spliced transcript isoforms. **a** Bioinformatics pipeline utilized to identify all transcript isoforms and significantly differentially spliced genes present in the original RNA sequencing dataset. Steps inside the dashed outline were performed on each individual replicate. See Methods for more detail on gtf merging. **b** Comparison of alternatively spliced isoforms present or absent in spaceflight in both ecotypes and developmental ages tested. **c** Count of differentially alternatively spliced genes and the associated count of transcript isoforms observed in each condition. **d** Comparison of the differentially alternatively spliced genes observed in the Columbia-0 (Col-0) or the Wassilewskija (WS) ecotype background. Differentially alternatively spliced genes observed at both 4- and 8-day time points in either ecotype background were pooled for this analysis. (C Columbia-0, W Wassilewskija, 4 4 days of age, 8 8 days of age. C4 Columbia-0 4 days of age, W8 Wassilewskija 8 days of age)

Specific genes that undergo significant differential AS (dAS) were identified using CuffDiff[15](#CR15) to investigate whether decisions made by the splicing machinery differ in response to spaceflight. In both ecotypes and both developmental stages tested in this analysis, genes that undergo significant dAS between spaceflight and ground control samples were identified (Fig. [1c](#Fig1)). Genes were identified as dAS if the isoform ratio differs significantly between the conditions examined (Supplementary Data File [2](#MOESM3)). A difference in isoform ratio between conditions is indicative of a difference in splicing decision between conditions, which is independent of transcription-level differences.

Interestingly, fewer genes undergo dAS in the Col-0 ecotype background collectively as compared to WS, which is opposite of the pattern observed in the literature between these two ecotypes regarding differentially expressed genes.[2](#CR2) Comparison of the genes that undergo dAS in either the Col-0 or the WS background reveals very little overlap in the identity of the genes alternatively spliced in response to spaceflight (Fig. [1d](#Fig1)). Furthermore, gene ontology analysis does not reveal any obvious conclusions regarding the function or localization of the genes undergoing AS during spaceflight exposure.

An example of dAS between spaceflight and ground controls in both Col-0 and WS is presented as an Integrative Genomics Viewer[14](#CR14) image that visualizes differences in sequencing coverage between AS isoforms of the gene AT2G33770 (Fig. [2a](#Fig2)). This gene locus produces three AS transcript isoforms that utilize the same transcription start site—TCONS\_00029094, TCONS\_00029095, and TCONS\_00029096. One AS isoform, TCONS\_00029094, is only very lowly expressed in all conditions tested. However, AS isoform TCONS\_00029095 is more common in spaceflight samples, whereas AS isoform TCONS\_00029096 is more common in ground control samples (Fig. [2a, b](#Fig2)). This example highlights a difference in pre-mRNA processing in response to spaceflight—a spliceosome-specific behavior as opposed to a difference in transcription.

### Fig. 2.

[![Fig. 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4444/6447593/0cf73d05e012/41526_2019_70_Fig2_HTML.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=6447593_41526_2019_70_Fig2_HTML.jpg)

[Open in a new tab](figure/Fig2/)

Visualization of switch in isoform ratio between spaceflight and ground controls for gene AT2G33770. **a** Screenshot from Integrative Genomics Viewer[16](#CR16) displaying sequencing coverage spanning the AT2G33770 gene model in spaceflight and ground control samples from either the 4-day Columbia-0 (Col-0) or 8-day Wassilewskija (WS) backgrounds. Asterisks indicate exons within the gene model solely present in transcript isoform TCONS\_0029096. Arrows indicate lack of sequencing coverage in spaceflight samples corresponding to the unique exons in TCONS\_0029096. Small numbers in the upper left hand corner of each panel denote the range of the *y* axis scale for each condition. **b** Isoform ratios in spaceflight and ground controls for transcript isoforms TCONS\_0029094, TCONS\_0029095, and TCONS\_0029096 associated with gene AT2G33770 in Col-0 4-day and WS 8-day backgrounds. Isoform ratio was calculated by FPKM (fragments per kilobase of transcript per million mapped reads)

This study represents the first observation of transcriptome-wide spaceflight-induced AS not only in plants but also in any living organism yet exposed to microgravity. The results presented here serve as strong evidence that AS has a role during the molecular adaptation process to the spaceflight environment in higher eukaryotic organisms such as plants and provides methods that can be used to identify AS isoforms from RNA sequencing datasets generated from other spaceflight-exposed organisms. However, the full role of AS during spaceflight adaptation must still be investigated by examining changes in the abundance of AS isoforms present in both conditions, the types of AS events occurring in spaceflight, and the functional implications of AS isoforms present or absent in spaceflight. In addition, it would be interesting to analyze the overlap between spaceflight differentially expressed genes and spaceflight-induced AS isoforms. Dissecting the spaceflight-induced transcriptome with both gene- and AS isoform-level resolution will elucidate better understanding of the molecular mechanisms leveraged by plants to adapt to the radically novel environment, that is, spaceflight.

## Methods

### Data acquisition—APEX03-2 spaceflight experiment

A subset of the data collected during the Advanced Plant Experiment 03-2 (APEX03-2) spaceflight experiment was utilized for this analysis. The APEX03-2 experimental methods have been previously described[16](#CR16) including detailed descriptions of the mission in which the experiment was launched, plant material preparations, and plant growth conditions both onboard the ISS and at KSC where ground controls were comparably grown. For this analysis, the data utilized comes from two wild-type accessions of *Arabidopsis thaliana* (Col-0 and WS) sampled at both 4 and 8 days of age during the experiment.

It should be noted that the APEX03-2 experiment is also referred to as “TAGES-ISA” (Transgenic Gene Expression System-Intracellular Signaling Architecture) by NASA operations nomenclature (<http://www.nasa.gov/mission_pages/station/research/experiments/1059.html>).

### Growth conditions and plant handling

Seeds sown on 10 cm2 petri plates were kept dormant during launch. Germination was initiated after transfer to the Vegetable Production System (VEGGIE) onboard the ISS or at KSC for ground controls. The plates were kept in vertical racks perpendicularly oriented to the light source during growth in VEGGIE. Lighting within the VEGGIE unit was set to provide between 100 and 135 µmoles/m2/s PAR (photosynthetic active radiation). Telemetric data collected on board the ISS during the spaceflight experiment were utilized to precisely mimic the environment onboard the ISS during the ground control experiment, carried out in the ISS Environmental Simulation Chamber at KSC. General methods associated with harvesting plant matter while on orbit for transcriptome analyses, plate de-integration once returned back to KSC, and transport back to the laboratory of the Principal Investigators for analysis has been described in detail for previous spaceflight experiments.[4](#CR4)

### RNA extraction and sequencing

Four biological replicates were analyzed for each condition tested in the APEX03-2 experiment, where one replicate corresponds to the 10–15 plants grown on one petri plate. The plant material constituting each replicate was then subdivided for use in multiple downstream applications. Five to eight individual plants from each replicate of 4-day-old seedlings were combined for RNA extraction. However, to ensure that similar RNA concentrations from replicates containing 8 day-old seedlings were obtained, only 2–3 individual plants from each replicate of 8 day-old seedlings were pooled for RNA extraction. An Olympus dissecting microscope was utilized to separate leaf and root samples, while hypocotyl regions were set aside. Total RNA was extracted from the dissected roots using the Qiashredder and RNAeasy™ kits from QIAGEN (QIAGEN Sciences, MD, USA). Remnant DNA was removed via an on-column digestion utilizing RNase Free DNase (QIAGEN GmbH, Hilden, Germany). RNA quality was analyzed using an Agilent 2100 Bioanalyzer (Agilent Technologies, Santa Clara, CA, USA). A cDNA library was produced using the CloneTech SMART-Seq V4 Ultra Low Input RNA Kit (Clonetech Laboratories, Inc, cat#: 634890). Illumina sequencing libraries were then prepared via the Illumina Nextera DNA Sample Preparation Kit (Cat#: FC-131-1024). Bioanalyzer and quantitative PCR were used to quantify the libraries produced. Pooled equimolar samples were then sequenced using the NextSeq500 instrument in five separate flow cells.

### AS bioinformatics pipeline and downstream processing

Quality control was done to remove low quality reads and bases with Trimmomatic[17](#CR17) using parameters TRAILING:3, SLIDINGWINDOW:4:20, MINLEN:20. Reads were aligned to the *A. thaliana* version 10 reference genome (accessed from <https://genome.jgi.doe.gov>) with Bowtie2 version 2.2.9[18](#CR18) with parameter –fr. Low quality alignments were filtered out by piping the Bowtie2 output into Samtools[19](#CR19) via samtools view –q 30 –b | samtools sort. Picard 2.5.0 (<https://broadinstitute.github.io/picard/>) was used with the parameter REMOVE\_DUPLICATES=true to remove potential optical duplicates from the alignments.

Transcript assemblies were conducted for each sample using three separate transcript assembly programs. Cufflinks[15](#CR15) was used with parameters –library-type fr-firststrand –u -F 0.05–max-intron-length 12000–no-faux-reads utilizing the *A. thaliana* version 9 reference genome and *A. thaliana* version 10 genome annotation (accessed from <https://genome.jgi.doe.gov>) to guide transcript assembly. StringTie[20](#CR20) was used with parameters -f 0.05 -j 2 –rf using the same genome and annotation as Cufflinks to guide assemblies. Trinity[21](#CR21) was used in genome guided mode with parameters –genome\_guided\_bam–genome\_guided\_max\_intron 12000–full\_cleanup–SS\_lib\_type RF–min\_contig\_length 50. The assemblies from Cufflinks and Stringtie were merged using the Stringtie merge function for each sample using parameters -F 1 -f 0.05. PASA[22](#CR22) was used to reconcile this merged assembly and the assembly from Trinity using parameters -C –R -t 〈Trinity fasta output〉 –cufflinks\_gtf 〈merged gtf file〉 -I 12000–ALT\_SPLICE–ALIGNER gmap, blat.

The transcriptome assemblies generated by PASA for each sample were merged with Cuffmerge. The file produced by Cuffmerge was then reformatted to agree with the reference genome annotation format and then compared against the reference annotation using gffcompare (<https://github.com/gpertea/gffcompare>). This merged transcriptome represents all potential transcript isoforms expressed in all of the samples being studied, including both newly discovered isoforms and those previously annotated.

The abundance of transcripts in each sample was then quantified with the rsem-calculate-expression functionality within RSEM[23](#CR23) using default parameters. The FPKM values of each transcript from each sample were parsed from the RSEM output into a matrix. This matrix was used for downstream analysis of PAV of alternatively spliced transcript isoforms. All isoforms expressed from parent genes without a minimum of two unique transcript isoforms identified within the dataset were removed. This category of discarded isoforms represents isoforms that were not produced as a product of AS as identified by the pipeline used in this analysis. In addition, within each condition all isoforms expressed at an FPKM < 10 in at least one out of four replicates were removed from the analysis. Following filtering, lists of spaceflight present, ground control present, and commonly present AS isoforms were generated.

A second round of alignments was done with STAR[24](#CR24) version 2.5.2b using parameters –alignIntronMax 12000–outFilterMismatchNmax 8–sjdbOverhang 100–outSJfilterReads Unique–outSAMmultNmax 1–outFilterType BySJout to generate files for junction spanning alignments. These alignments were filtered for duplicate reads using Picard with the parameter REMOVE\_DUPLICATES=true. STAR allows for the alignment of junction spanning reads, whereas RSEM utilizes Bowtie for alignments, which does not allow for the alignment of these reads. Sequencing depth and splice junction support for a subset of isoforms present or absent in each condition and ecotype was then visualized using Integrative Genomics Viewer[14](#CR14) (Supplementary Fig. [1](#MOESM1)–[4](#MOESM1)).

The alignments from STAR were also used as inputs into Cuffdiff.[15](#CR15) Cuffdiff was run using this merged transcriptome as a reference gtf file to discover differential transcription start site usage between spaceflight and ground controls in both ecotypes and developmental stages tested in this analysis. The transcription start sites of isoforms exhibiting differential splicing were parsed from the splicing.diff file output from Cuffdiff for each condition being tested. The isoforms associated with the transcription start sites were parsed from the isoforms.fpkm\_tracking Cuffdiff output file and the expression, in FPKM, of these isoforms was parsed from the isoforms.read\_group\_tracking Cuffdiff output file. The isoform ratios were then calculated using a Python script for isoforms encoded from the same gene and sharing a transcription start site. All isoforms demonstrating an isoform ratio <0.01 in both spaceflight and ground control samples within a given condition were removed, resulting in the generation of lists of genes and their associated isoforms that undergo differential AS in each condition tested (Supplementary Data File [2](#MOESM3)).

### Reporting Summary

Further information on research design is available in the [Nature Research Reporting Summary](#MOESM4) linked to this article.

## Supplementary information

[Supplemental Figures](/articles/instance/6447593/bin/41526_2019_70_MOESM1_ESM.pdf) (1.6MB, pdf)

[Supplemental Data File 1](/articles/instance/6447593/bin/41526_2019_70_MOESM2_ESM.xlsx) (606KB, xlsx)

[Supplemental Data File 2](/articles/instance/6447593/bin/41526_2019_70_MOESM3_ESM.xlsx) (66KB, xlsx)

[reporting summary](/articles/instance/6447593/bin/41526_2019_70_MOESM4_ESM.pdf) (1.3MB, pdf)

## Acknowledgements

We thank the personnel at Kennedy Space Center and astronauts on board the International Space Station for their assistance with the APEX03 experiment. In addition, we would like to acknowledge Ruth Davenport, Natasha Sng, Jordan Callaham, and Brandon Califar for their helpful discussion and continued support and the University of Florida Research Computing Center. This work was funded by grants NNX12AN69G to R.J.F. and A.-L.P. from NASA Space Life and Physical Sciences, managed through Kennedy Space Center.

## Author contributions

R.J.F. and A.-L.P. designed and completed the spaceflight experiment and RNA sequencing. N.S.B., J.N., and W.B.B. performed the bioinformatics analysis. All authors contributed to writing the paper.

## Data availability

The RNA-seq data reported in this paper are available in GEO under number [GSE95586](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE95586) and in NASA’s GeneLab data repository (<https://genelab-data.ndc.nasa.gov/genelab/>, reference number GLDS-218).

### Competing interests

The authors declare no competing interests.

## Footnotes

**Publisher’s note:** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Supplementary information

**Supplementary information** accompanies the paper on the *npj Microgravity* website (10.1038/s41526-019-0070-7).

## References

* 1.Kwon T, et al. Transcriptional response of Arabidopsis seedlings during spaceflight reveals peroxidase and cell wall remodeling genes associated with root hair development. Am. J. Bot. 2015;102:21–35. doi: 10.3732/ajb.1400458. [[DOI](https://doi.org/10.3732/ajb.1400458)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25587145/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Bot.&title=Transcriptional%20response%20of%20Arabidopsis%20seedlings%20during%20spaceflight%20reveals%20peroxidase%20and%20cell%20wall%20remodeling%20genes%20associated%20with%20root%20hair%20development&author=T%20Kwon&volume=102&publication_year=2015&pages=21-35&pmid=25587145&doi=10.3732/ajb.1400458&)]
* 2.Paul AL, et al. Genetic dissection of the Arabidopsis spaceflight transcriptome: are some responses dispensable for the physiological adaptation of plants to spaceflight? PLoS ONE. 2017;12:e0180186. doi: 10.1371/journal.pone.0180186. [[DOI](https://doi.org/10.1371/journal.pone.0180186)] [[PMC free article](/articles/PMC5491145/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28662188/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20ONE&title=Genetic%20dissection%20of%20the%20Arabidopsis%20spaceflight%20transcriptome:%20are%20some%20responses%20dispensable%20for%20the%20physiological%20adaptation%20of%20plants%20to%20spaceflight?&author=AL%20Paul&volume=12&publication_year=2017&pages=e0180186&pmid=28662188&doi=10.1371/journal.pone.0180186&)]
* 3.Paul AL, et al. Spaceflight transcriptomes: unique responses to a novel environment. Astrobiology. 2012;12:40–56. doi: 10.1089/ast.2011.0696. [[DOI](https://doi.org/10.1089/ast.2011.0696)] [[PMC free article](/articles/PMC3264962/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22221117/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Astrobiology&title=Spaceflight%20transcriptomes:%20unique%20responses%20to%20a%20novel%20environment&author=AL%20Paul&volume=12&publication_year=2012&pages=40-56&pmid=22221117&doi=10.1089/ast.2011.0696&)]
* 4.Paul AL, Zupanska AK, Schultz ER, Ferl RJ. Organ-specific remodeling of the Arabidopsis transcriptome in response to spaceflight. BMC Plant Biol. 2013;13:112. doi: 10.1186/1471-2229-13-112. [[DOI](https://doi.org/10.1186/1471-2229-13-112)] [[PMC free article](/articles/PMC3750915/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23919896/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=Organ-specific%20remodeling%20of%20the%20Arabidopsis%20transcriptome%20in%20response%20to%20spaceflight&author=AL%20Paul&author=AK%20Zupanska&author=ER%20Schultz&author=RJ%20Ferl&volume=13&publication_year=2013&pages=112&pmid=23919896&doi=10.1186/1471-2229-13-112&)]
* 5.Filichkin S, Priest HD, Megraw M, Mockler TC. Alternative splicing in plants: directing traffic at the crossroads of adaptation and environmental stress. Curr. Opin. Plant Biol. 2015;24:125–135. doi: 10.1016/j.pbi.2015.02.008. [[DOI](https://doi.org/10.1016/j.pbi.2015.02.008)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25835141/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Opin.%20Plant%20Biol.&title=Alternative%20splicing%20in%20plants:%20directing%20traffic%20at%20the%20crossroads%20of%20adaptation%20and%20environmental%20stress&author=S%20Filichkin&author=HD%20Priest&author=M%20Megraw&author=TC%20Mockler&volume=24&publication_year=2015&pages=125-135&pmid=25835141&doi=10.1016/j.pbi.2015.02.008&)]
* 6.Marquez Y, Brown JW, Simpson C, Barta A, Kalyna M. Transcriptome survey reveals increased complexity of the alternative splicing landscape in Arabidopsis. Genome Res. 2012;22:1184–1195. doi: 10.1101/gr.134106.111. [[DOI](https://doi.org/10.1101/gr.134106.111)] [[PMC free article](/articles/PMC3371709/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22391557/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genome%20Res.&title=Transcriptome%20survey%20reveals%20increased%20complexity%20of%20the%20alternative%20splicing%20landscape%20in%20Arabidopsis&author=Y%20Marquez&author=JW%20Brown&author=C%20Simpson&author=A%20Barta&author=M%20Kalyna&volume=22&publication_year=2012&pages=1184-1195&pmid=22391557&doi=10.1101/gr.134106.111&)]
* 7.Calixto CPG, et al. Rapid and dynamic alternative splicing impacts the Arabidopsis cold response transcriptome. Plant Cell. 2018;30:1424–1444. doi: 10.1105/tpc.18.00177. [[DOI](https://doi.org/10.1105/tpc.18.00177)] [[PMC free article](/articles/PMC6096597/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29764987/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell&title=Rapid%20and%20dynamic%20alternative%20splicing%20impacts%20the%20Arabidopsis%20cold%20response%20transcriptome&author=CPG%20Calixto&volume=30&publication_year=2018&pages=1424-1444&pmid=29764987&doi=10.1105/tpc.18.00177&)]
* 8.Ling Z, Zhou W, Baldwin IT, Xu S. Insect herbivory elicits genome-wide alternative splicing responses in Nicotiana attenuata. Plant J. 2015;84:228–243. doi: 10.1111/tpj.12997. [[DOI](https://doi.org/10.1111/tpj.12997)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26306554/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20J.&title=Insect%20herbivory%20elicits%20genome-wide%20alternative%20splicing%20responses%20in%20Nicotiana%20attenuata&author=Z%20Ling&author=W%20Zhou&author=IT%20Baldwin&author=S%20Xu&volume=84&publication_year=2015&pages=228-243&pmid=26306554&doi=10.1111/tpj.12997&)]
* 9.Mandadi KK, Scholthof KB. Genome-wide analysis of alternative splicing landscapes modulated during plant-virus interactions in Brachypodium distachyon. Plant Cell. 2015;27:71–85. doi: 10.1105/tpc.114.133991. [[DOI](https://doi.org/10.1105/tpc.114.133991)] [[PMC free article](/articles/PMC4330581/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25634987/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell&title=Genome-wide%20analysis%20of%20alternative%20splicing%20landscapes%20modulated%20during%20plant-virus%20interactions%20in%20Brachypodium%20distachyon&author=KK%20Mandadi&author=KB%20Scholthof&volume=27&publication_year=2015&pages=71-85&pmid=25634987&doi=10.1105/tpc.114.133991&)]
* 10.Thatcher SR, et al. Genome-wide analysis of alternative splicing during development and drought stress in maize. Plant Physiol. 2016;170:586–599. doi: 10.1104/pp.15.01267. [[DOI](https://doi.org/10.1104/pp.15.01267)] [[PMC free article](/articles/PMC4704579/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26582726/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Physiol.&title=Genome-wide%20analysis%20of%20alternative%20splicing%20during%20development%20and%20drought%20stress%20in%20maize&author=SR%20Thatcher&volume=170&publication_year=2016&pages=586-599&pmid=26582726&doi=10.1104/pp.15.01267&)]
* 11.Vitulo N, et al. A deep survey of alternative splicing in grape reveals changes in the splicing machinery related to tissue, stress condition and genotype. BMC Plant Biol. 2014;14:99. doi: 10.1186/1471-2229-14-99. [[DOI](https://doi.org/10.1186/1471-2229-14-99)] [[PMC free article](/articles/PMC4108029/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24739459/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=A%20deep%20survey%20of%20alternative%20splicing%20in%20grape%20reveals%20changes%20in%20the%20splicing%20machinery%20related%20to%20tissue,%20stress%20condition%20and%20genotype&author=N%20Vitulo&volume=14&publication_year=2014&pages=99&pmid=24739459&doi=10.1186/1471-2229-14-99&)]
* 12.Mei W, et al. A comprehensive analysis of alternative splicing in paleopolyploid maize. Front. Plant Sci. 2017;8:694. doi: 10.3389/fpls.2017.00694. [[DOI](https://doi.org/10.3389/fpls.2017.00694)] [[PMC free article](/articles/PMC5423905/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28539927/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=A%20comprehensive%20analysis%20of%20alternative%20splicing%20in%20paleopolyploid%20maize&author=W%20Mei&volume=8&publication_year=2017&pages=694&pmid=28539927&doi=10.3389/fpls.2017.00694&)]
* 13.Paul AL, Amalfitano CE, Ferl RJ. Plant growth strategies are remodeled by spaceflight. BMC Plant Biol. 2012;12:232. doi: 10.1186/1471-2229-12-232. [[DOI](https://doi.org/10.1186/1471-2229-12-232)] [[PMC free article](/articles/PMC3556330/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23217113/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=Plant%20growth%20strategies%20are%20remodeled%20by%20spaceflight&author=AL%20Paul&author=CE%20Amalfitano&author=RJ%20Ferl&volume=12&publication_year=2012&pages=232&pmid=23217113&doi=10.1186/1471-2229-12-232&)]
* 14.Thorvaldsdottir H, Robinson JT, Mesirov JP. Integrative genomics viewer (IGV): high-performance genomics data visualization and exploration. Brief Bioinformatics. 2013;14:178–192. doi: 10.1093/bib/bbs017. [[DOI](https://doi.org/10.1093/bib/bbs017)] [[PMC free article](/articles/PMC3603213/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22517427/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Brief%20Bioinformatics&title=Integrative%20genomics%20viewer%20(IGV):%20high-performance%20genomics%20data%20visualization%20and%20exploration&author=H%20Thorvaldsdottir&author=JT%20Robinson&author=JP%20Mesirov&volume=14&publication_year=2013&pages=178-192&pmid=22517427&doi=10.1093/bib/bbs017&)]
* 15.Trapnell C, et al. Differential gene and transcript expression analysis of RNA-seq experiments with TopHat and Cufflinks. Nat. Protoc. 2012;7:562–578. doi: 10.1038/nprot.2012.016. [[DOI](https://doi.org/10.1038/nprot.2012.016)] [[PMC free article](/articles/PMC3334321/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22383036/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Protoc.&title=Differential%20gene%20and%20transcript%20expression%20analysis%20of%20RNA-seq%20experiments%20with%20TopHat%20and%20Cufflinks&author=C%20Trapnell&volume=7&publication_year=2012&pages=562-578&pmid=22383036&doi=10.1038/nprot.2012.016&)]
* 16.Ferl RJ, Paul AL. The effect of spaceflight on the gravity-sensing auxin gradient of roots: GFP reporter gene microscopy on orbit. NPJ Microgravity. 2016;2:15023. doi: 10.1038/npjmgrav.2015.23. [[DOI](https://doi.org/10.1038/npjmgrav.2015.23)] [[PMC free article](/articles/PMC5515520/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28725721/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=The%20effect%20of%20spaceflight%20on%20the%20gravity-sensing%20auxin%20gradient%20of%20roots:%20GFP%20reporter%20gene%20microscopy%20on%20orbit&author=RJ%20Ferl&author=AL%20Paul&volume=2&publication_year=2016&pages=15023&pmid=28725721&doi=10.1038/npjmgrav.2015.23&)]
* 17.Bolger AM, Lohse M, Usadel B. Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics. 2014;30:2114–2120. doi: 10.1093/bioinformatics/btu170. [[DOI](https://doi.org/10.1093/bioinformatics/btu170)] [[PMC free article](/articles/PMC4103590/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24695404/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=Trimmomatic:%20a%20flexible%20trimmer%20for%20Illumina%20sequence%20data&author=AM%20Bolger&author=M%20Lohse&author=B%20Usadel&volume=30&publication_year=2014&pages=2114-2120&pmid=24695404&doi=10.1093/bioinformatics/btu170&)]
* 18.Langmead B, Salzberg SL. Fast gapped-read alignment with Bowtie 2. Nat. Methods. 2012;9:357–359. doi: 10.1038/nmeth.1923. [[DOI](https://doi.org/10.1038/nmeth.1923)] [[PMC free article](/articles/PMC3322381/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22388286/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Methods&title=Fast%20gapped-read%20alignment%20with%20Bowtie%202&author=B%20Langmead&author=SL%20Salzberg&volume=9&publication_year=2012&pages=357-359&pmid=22388286&doi=10.1038/nmeth.1923&)]
* 19.Li H, et al. The Sequence Alignment/Map format and SAMtools. Bioinformatics. 2009;25:2078–2079. doi: 10.1093/bioinformatics/btp352. [[DOI](https://doi.org/10.1093/bioinformatics/btp352)] [[PMC free article](/articles/PMC2723002/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19505943/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=The%20Sequence%20Alignment/Map%20format%20and%20SAMtools&author=H%20Li&volume=25&publication_year=2009&pages=2078-2079&pmid=19505943&doi=10.1093/bioinformatics/btp352&)]
* 20.Pertea M, et al. StringTie enables improved reconstruction of a transcriptome from RNA-seq reads. Nat. Biotechnol. 2015;33:290–295. doi: 10.1038/nbt.3122. [[DOI](https://doi.org/10.1038/nbt.3122)] [[PMC free article](/articles/PMC4643835/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25690850/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=StringTie%20enables%20improved%20reconstruction%20of%20a%20transcriptome%20from%20RNA-seq%20reads&author=M%20Pertea&volume=33&publication_year=2015&pages=290-295&pmid=25690850&doi=10.1038/nbt.3122&)]
* 21.Grabherr MG, et al. Full-length transcriptome assembly from RNA-Seq data without a reference genome. Nat. Biotechnol. 2011;29:644–652. doi: 10.1038/nbt.1883. [[DOI](https://doi.org/10.1038/nbt.1883)] [[PMC free article](/articles/PMC3571712/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21572440/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=Full-length%20transcriptome%20assembly%20from%20RNA-Seq%20data%20without%20a%20reference%20genome&author=MG%20Grabherr&volume=29&publication_year=2011&pages=644-652&pmid=21572440&doi=10.1038/nbt.1883&)]
* 22.Haas BJ, et al. Improving the Arabidopsis genome annotation using maximal transcript alignment assemblies. Nucleic Acids Res. 2003;31:5654–5666. doi: 10.1093/nar/gkg770. [[DOI](https://doi.org/10.1093/nar/gkg770)] [[PMC free article](/articles/PMC206470/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/14500829/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=Improving%20the%20Arabidopsis%20genome%20annotation%20using%20maximal%20transcript%20alignment%20assemblies&author=BJ%20Haas&volume=31&publication_year=2003&pages=5654-5666&pmid=14500829&doi=10.1093/nar/gkg770&)]
* 23.Li B, Dewey CN. RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome. BMC Bioinformatics. 2011;12:323. doi: 10.1186/1471-2105-12-323. [[DOI](https://doi.org/10.1186/1471-2105-12-323)] [[PMC free article](/articles/PMC3163565/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21816040/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Bioinformatics&title=RSEM:%20accurate%20transcript%20quantification%20from%20RNA-Seq%20data%20with%20or%20without%20a%20reference%20genome&author=B%20Li&author=CN%20Dewey&volume=12&publication_year=2011&pages=323&pmid=21816040&doi=10.1186/1471-2105-12-323&)]
* 24.Dobin A, et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics. 2012;29:15–21. doi: 10.1093/bioinformatics/bts635. [[DOI](https://doi.org/10.1093/bioinformatics/bts635)] [[PMC free article](/articles/PMC3530905/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23104886/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics.&title=STAR:%20ultrafast%20universal%20RNA-seq%20aligner&author=A%20Dobin&volume=29&publication_year=2012&pages=15-21&pmid=23104886&doi=10.1093/bioinformatics/bts635&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

[Supplemental Figures](/articles/instance/6447593/bin/41526_2019_70_MOESM1_ESM.pdf) (1.6MB, pdf)

[Supplemental Data File 1](/articles/instance/6447593/bin/41526_2019_70_MOESM2_ESM.xlsx) (606KB, xlsx)

[Supplemental Data File 2](/articles/instance/6447593/bin/41526_2019_70_MOESM3_ESM.xlsx) (66KB, xlsx)

[reporting summary](/articles/instance/6447593/bin/41526_2019_70_MOESM4_ESM.pdf) (1.3MB, pdf)

### Data Availability Statement

The RNA-seq data reported in this paper are available in GEO under number [GSE95586](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE95586) and in NASA’s GeneLab data repository (<https://genelab-data.ndc.nasa.gov/genelab/>, reference number GLDS-218).