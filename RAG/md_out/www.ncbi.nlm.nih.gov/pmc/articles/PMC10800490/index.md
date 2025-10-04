Front Plant Sci

. 2024 Jan 8;14:1308713. doi: [10.3389/fpls.2023.1308713](https://doi.org/10.3389/fpls.2023.1308713)

# Conserved plant transcriptional responses to microgravity from two consecutive spaceflight experiments

[Eric S Land](https://pubmed.ncbi.nlm.nih.gov/?term=%22Land%20ES%22%5BAuthor%5D)

### Eric S Land

1
Department of Plant and Microbial Biology, North Carolina State University, Raleigh, NC, United States

Find articles by [Eric S Land](https://pubmed.ncbi.nlm.nih.gov/?term=%22Land%20ES%22%5BAuthor%5D)

1, [James Sheppard](https://pubmed.ncbi.nlm.nih.gov/?term=%22Sheppard%20J%22%5BAuthor%5D)

### James Sheppard

2
Department of Molecular and Structural Biochemistry, North Carolina State University, Raleigh, NC, United States

Find articles by [James Sheppard](https://pubmed.ncbi.nlm.nih.gov/?term=%22Sheppard%20J%22%5BAuthor%5D)

2, [Colleen J Doherty](https://pubmed.ncbi.nlm.nih.gov/?term=%22Doherty%20CJ%22%5BAuthor%5D)

### Colleen J Doherty

2
Department of Molecular and Structural Biochemistry, North Carolina State University, Raleigh, NC, United States

Find articles by [Colleen J Doherty](https://pubmed.ncbi.nlm.nih.gov/?term=%22Doherty%20CJ%22%5BAuthor%5D)

2, [Imara Y Perera](https://pubmed.ncbi.nlm.nih.gov/?term=%22Perera%20IY%22%5BAuthor%5D)

### Imara Y Perera

1
Department of Plant and Microbial Biology, North Carolina State University, Raleigh, NC, United States

Find articles by [Imara Y Perera](https://pubmed.ncbi.nlm.nih.gov/?term=%22Perera%20IY%22%5BAuthor%5D)

1,\*

* Author information
* Article notes
* Copyright and License information

1
Department of Plant and Microbial Biology, North Carolina State University, Raleigh, NC, United States

2
Department of Molecular and Structural Biochemistry, North Carolina State University, Raleigh, NC, United States

Edited by: Francisco Javier Medina, Spanish National Research Council (CSIC), Spain

Reviewed by: Patrick H. Masson, University of Wisconsin-Madison, United States

Sabrina Li San Chin, University of Wisconsin-Madison, United States

✉

\*Correspondence: Imara Y. Perera, iperera@ncsu.edu

Received 2023 Oct 7; Accepted 2023 Dec 12; Collection date 2023.

Copyright © 2024 Land, Sheppard, Doherty and Perera

This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

[PMC Copyright notice](/about/copyright/)

PMCID: PMC10800490  PMID: [38259952](https://pubmed.ncbi.nlm.nih.gov/38259952/)

## Abstract

### Introduction

Understanding how plants adapt to the space environment is essential, as plants will be a valuable component of long duration space missions. Several spaceflight experiments have focused on transcriptional profiling as a means of understanding plant adaptation to microgravity. However, there is limited overlap between results from different experiments. Differences in experimental conditions and hardware make it difficult to find a consistent response across experiments and to distinguish the primary effects of microgravity from other spaceflight effects.

### Methods

Plant Signaling (PS) and Plant RNA Regulation (PRR) were two separate spaceflight experiments conducted on the International Space Station utilizing the European Modular Cultivation System (EMCS). The EMCS provided a lighted environment for plant growth with centrifugal capabilities providing an onboard 1 *g* control.

### Results and discussion

An RNA-Seq analysis of shoot samples from PS and PRR revealed a significant overlap of genes differentially expressed in microgravity between the two experiments. Relative to onboard 1 *g* controls, genes involved in transcriptional regulation, shoot development, and response to auxin and light were upregulated in microgravity in both experiments. Conversely, genes involved in defense response, abiotic stress, Ca++ signaling, and cell wall modification were commonly downregulated in both datasets. The downregulation of stress responses in microgravity in these two experiments is interesting as these pathways have been previously observed as upregulated in spaceflight compared to ground controls. Similarly, we have observed many stress response genes to be upregulated in the 1 *g* onboard control compared to ground reference controls; however these genes were specifically downregulated in microgravity. In addition, we analyzed the sRNA landscape of the 1 *g* and microgravity (μ *g*) shoot samples from PRR. We identified three miRNAs (miR319c, miR398b, and miR8683) which were upregulated in microgravity, while several of their corresponding target genes were found to be downregulated in microgravity. Interestingly, the downregulated target genes are enriched in those encoding chloroplast-localized enzymes and proteins. These results uncover microgravity unique transcriptional changes and highlight the validity and importance of an onboard 1 *g* control.

**Keywords:** transcriptional profiling, adaptation to spaceflight, Arabidopsis, microgravity (μ*g*), plants

## 1. Introduction

As an essential part of life support systems for long-duration space missions, plants supplement food as well as purify the air and water ([Fu et al., 2016](#B18); [De Micco et al., 2023](#B15)). Future colonization efforts will require the ability to grow plants in unfamiliar environments. However, the space environment poses challenges to growing plants. In addition to the difficulties of providing essential requirements for plant growth (light, water, nutrients, etc.), growing plants in space requires the mitigation of unfavorable factors such as altered gas composition, lack of convective currents, and cosmic radiation.

It is important to understand the molecular mechanisms that regulate plant adaptations to space. Toward that goal, several spaceflight experiments have examined the global transcriptional changes of plants grown on the International Space Station (ISS). One caveat to these studies is that until recently, lighted habitats for plant experimentation were limited; for ease of handling and setup, several experiments were carried out in Biological Research In Canisters hardware (BRICs), where plants were grown in the dark. Another point of concern is that many spaceflight experiments have employed hardware-matched experiments on Earth as controls; however, it is difficult to replicate all of the stresses that plants may face on the ISS on the ground.

Further, while several transcriptional datasets have been generated (accessible through the NASA GeneLab data repository), differences in plant age, tissue type, and growth conditions confound efforts to separate primary responses to microgravity from other spaceflight related stress responses ([Manzano et al., 2022](#B36); [Olanrewaju et al., 2023](#B50)). A recent meta-analysis by Barker et al. clearly illustrates some of these confounding effects ([Barker et al., 2023](#B5)). The authors showed that the analysis method (RNA-Seq vs. microarrays) was a principal factor leading to variability between datasets as was the hardware utilized for the spaceflight experiments. Nevertheless, focusing only on experiments conducted in BRIC hardware helped uncover common responses. Namely, oxidative stress, heat shock, cell wall dynamics, hypoxia, and ROS signaling were Gene Ontology annotations enriched in spaceflight compared to ground controls. A transcriptional profiling study of 12 day-old Arabidopsis seedlings grown in the Advanced Biological Research System (ABRS) hardware found organ-specific gene expression changes between leaves, hypocotyls, and roots ([Paul et al., 2013](#B51)). Although each tissue exhibited unique responses, cell wall remodeling, touch response, and pathogen responses were common themes among the genes differentially expressed in space.

Plant growth is highly responsive to external cues. Two critical cues –light and gravity– have profound influences on the direction and magnitude of plant growth. Plant roots grow down with the gravity vector (positive gravitropism), while the stems grow opposite to the gravity vector (negative gravitropism) and toward light (positive phototropism). On earth, light and gravity work in combination to direct the orientation of the primary axes of growth as well as root and shoot branching and leaf angle, enabling efficient nutrient acquisition and light capture. The relative contribution of each of these cues in regulating plant growth is difficult to disentangle on Earth, where gravity is a constant; the ISS provides an ideal platform to answer such fundamental questions.

The European Modular Cultivation System (EMCS) was one of the controlled environment plant growth habitats operational on the ISS for many years ([Brinckmann, 1999](#B8); [Kittang et al., 2014](#B27)). In addition to providing lighting, regulated air circulation, and ethylene scrubbing, the EMCS was unique in that it consisted of two centrifuge rotors within a growth chamber. Rotor speeds could be varied to impart *g* levels ranging from 0 - 2 *g*. The EMCS, therefore, afforded researchers the ability to conduct a simultaneous 1 *g* control in space as well as to specifically query the effects of partial gravity.

Spaceflight experiments utilizing EMCS hardware have attempted to uncouple light and gravity stimuli ([Millar et al., 2010](#B41); [Vandenbrink et al., 2016](#B73)). Some experiments have examined the transcriptional response of plants to partial *g* levels. We previously reported that a subset of genes differentially expressed in microgravity respond to incremental increases in *g* levels ([Sheppard et al., 2021](#B61)). Other researchers have compared differences in gene expression between Lunar or Martian gravity and onboard 1 *g* controls ([Herranz et al., 2019](#B20); [Villacampa et al., 2021](#B76)). These types of experiments can inform us on plant responses to extraterrestrial habitats and will be important for aiding with long term colonization efforts.

In this study, we compare the transcriptional response of Arabidopsis shoots from two independent spaceflight experiments conducted on the ISS. In both experiments, Arabidopsis seedlings were grown for 5-6 days in the EMCS. The results revealed considerable overlap between the two experiments despite differences in the experimental setup. Furthermore, onboard 1 *g* controls facilitated the identification of microgravity-specific differences in gene expression.

## 2. Materials and methods

### 2.1. Preflight ground testing

Prior to flight build, optimization was carried out at North Carolina State University with a focus on seed stock viability, experimental protocols, and downstream sample recovery and processing. *Arabidopsis thaliana* Col-0 seed stocks were carefully screened to obtain an average germination of ≥99%, and dissection and processing protocols were developed to recover ≥1μg RNA from ≤3mg input tissue with a high degree of RNA integrity. Seed storage tests were carried out to ensure the viability of sterilized seeds for at least a 6 month period. Preflight testing for Plant Signaling (PS) included a Schedule Test and Operations Verification Test (OVT) at the Norwegian User Support and Operations Center (N-USOC, Trondheim, Norway), in an Engineering Reference Module (ERM-1). Similarly, ahead of the Plant RNA Regulation (PRR) spaceflight, an Experiment Verification Test (EVT) at NASA Ames Research Center (ARC) in an EMCS ground facility (ERM-2), and an Operations Verification Test (OVT) in the EMCS Engineering Reference Module (ERM-1) at N-USOC were carried out. All preflight and flight preparations for seed, media, and hardware assembly were carried out at NASA ARC.

### 2.2. Flight experiment preparation

PS and PRR were carried out in the EMCS using the experimental unique equipment (EUE)s which are the TROPI-like seed cassettes previously described ([Kiss et al., 2009](#B26); [Vandenbrink and Kiss, 2019](#B75)). Whatman #3 blotter paper and black-gridded PES membrane (PALL life Sciences Cat. No. 65561) were cut to fit the seed cassettes. Blotter papers were pre-soaked in 0.5X MS media, pH 5.7 (without sucrose) and allowed to dry. Blotter papers and membranes were sterilized by autoclaving. Seeds were surface sterilized and allowed to dry for 2 hours. Healthy viable seeds were selected under a dissecting microscope and attached to the gridded membrane using guar gum. Seeds were positioned with micropyles pointing down (away from lights) with 27 seeds/membrane. Gridded seeded membranes were attached to prepared blotters with guar gum and fixed to cassette base plates. Cassette covers were installed and sealed with foil tape (3M). A total of 80 cassettes were prepared for each experiment. Seed cassettes were assembled for flight at NASA ARC and loaded into experimental containers (ECs) approximately 4 weeks prior to the scheduled flight.

### 2.3. Spaceflight

Onboard the ISS, ECs were loaded into the EMCS by the attending astronaut. Each EC contained 5 seed cassettes for a total of 4 ECs (20 seed cassettes)/centrifuge rotor. Experiments were initiated by hydration, controlled remotely. The experimental timelines for PS and PRR are shown in [**Figure 1**](#f1). Both experiments were illuminated by white LEDs along the shoot side of the cassettes, and both experiments consisted of two replicate experimental runs. PS was carried out under continuous light, while PRR employed a long-day light regime (16h light/8h dark). Images were obtained from cameras located within the EMCS chamber. EMCS environmental parameters for PS were set at 21% O2 and a constant seedling temperature of 24°C. For PS, the ambient cabin air was purged from the EMCS chamber prior to each experimental run so that CO2 levels gradually increased to equilibrate with the cabin (beginning ~370 ppm and equilibrating to ~760 ppm). EMCS environmental parameters for PRR were set at 21% O2, 24°C daytime seedling temperature, and 21°C nighttime seedling temperature. Due to constraints with the upmass of air gas canisters, the EMCS chamber was not purged prior to each run of PRR; chamber CO2 for the duration of PRR was similar to the ISS cabin (~3000 ppm). In both PS and PRR, environmental factors were monitored by real-time telemetry to record O2, CO2, seedling temperature, and relative humidity. At the end of the experiments, seed cassettes were removed from the ECs, with 1 *g* cassettes handled first, and frozen immediately in the onboard -80°C freezer (MELFI). Seed cassettes remained frozen onboard the ISS. Samples were maintained at cryogenic temperature during return via Space-X Dragon, after splashdown, and until delivery to the laboratory. Samples were then stored at -80°C until processing for RNA.

#### Figure 1.

[![Figure 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/838077b63a6c/fpls-14-1308713-g001.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g001.jpg)

[Open in a new tab](figure/f1/)

Experimental Timelines of Plant Signaling (PS) and Plant RNA Regulation (PRR). Seed cassettes were prepared with dry seed and installed into the EMCS hardware on board the ISS. Experiments were initiated by remote hydration (blue arrows), and the two rotors were actuated according to the schedule shown with regular imaging (black arrows). Plant signaling **(A)** employed a constant light schedule while Plant RNA Regulation **(B)** was conducted under a 16/8 hour light/dark schedule, with two staggered hydration events allowing for the simultaneous harvest of 4 day and 6 day old seedlings at the end of the experiment.

### 2.4. Ground reference controls

For both PS and PRR, ground reference experiments were carried out in the ERM-2 at NASA-ARC, using flight build spares and matching environmental parameters to the flight experiments. Briefly, this hardware was designed to replicate environmental conditions experienced aboard the ISS to include temperature, gas composition, and provide comparable support to the flight hardware. Experimental containers (ECs) were positioned in the ERM in an upright position such that seedlings grew vertically, with lighting provided within each seed cassette from above the germinating seedlings, similar to the flight configuration.

### 2.5. RNA isolation

All analyzed shoot samples for the 1 *g* controls were from seed cassettes in position 3 of each EC. For PS, position 3 corresponded to 0.76 *g* and for PRR position 3 corresponded to 1 *g* ([**Supplementary Figure 1**](#SF1)). For each RNA isolation, seed cassettes were processed singly as follows. A single seed cassette was retrieved from the freezer, and the cover was removed. The cassette base was placed on a chilled platform, and RNA-later (Thermo Fisher Cat. No. AM7021) was added. The seedlings were dissected into root and shoot fractions and stored at 4°C in RNA-later for 24 hours, followed by storage at -20°C until RNA isolation. RNA was isolated from each shoot sample using the RNAqueous Micro kit (Applied Biosystems Cat No. AM1931). RNA recovery and integrity were monitored by Bioanalyzer (Agilent 2100). For the PRR shoot samples, the RNA isolation protocol was modified in order to retain the small RNA fraction as well.

### 2.6. Illumina sequencing

Each sample for Illumina Sequencing consisted of RNA isolated from a single seed cassette (each containing 27 seedlings) and each treatment/condition consisted of 3-4 replicates each. PS library preparation and sequencing were carried out by the Genomic Sciences Laboratory at North Carolina State University (Raleigh, NC) as described previously ([Sheppard et al., 2021](#B61)). Libraries were prepared using the ultra-directional library prep kit (New England Biolabs, Ipswich, MA, USA). Sequencing was carried out on 3 lanes of Illumina HiSeq2500 (125 bp single end reads). For PRR, Library preparation and Illumina sequencing for RNA and small RNA (sRNA) was carried out by Novogene Corporation Inc. (Sacramento, CA).

### 2.7. Data processing and analysis

Raw reads were cleaned up to remove adapters and reads shorter than 50 reads by cutadapt ([Martin, 2011](#B38)). Quality control was evaluated by FastQC ([Andrews, 2010](#B3)) to ensure adapters were removed. Reads were aligned using HiSat2 ([Kim et al., 2019](#B25)) to the Arabidopsis genome using TAIR10 ([Lamesch et al., 2012](#B30)) and Araport11 ([Cheng et al., 2017](#B11)) genome annotations (downloaded 08/2018). Read counts per feature were generated using HTseq-Count ([Anders et al., 2015](#B2)). Differential gene expression was determined using DESeq2 ([Love et al., 2014](#B34)). Features with one count or less in any sample were discarded. Differentially expressed genes were filtered on p-values. For the individual analyses of PS and PRR, the significance cutoff was padj <0.05 and for the combined analyses, the cutoff was padj < 0.01. Each sample and condition was represented by 3-4 replicates. Normalized DESeq2 counts tables were visualized as heatmaps using the R package pheatmap (version 1.0.12), clustering by column and scaling by row.

To determine whether overlap between individually analyzed PS and PRR DE gene lists were significant and non-random, hypergeometric distribution hypothesis testing was carried out using the phyper function of the R programming language. These analyses assumed a total genome size of 33,603 genes. Similarly, enrichment for HY5 targets in µ *g* DEG lists obtained from the combined PS/PRR dataset was analyzed by the same function, assuming 3,894 putative HY5 binding targets within the genome ([Lee et al., 2007](#B31)).

To identify potential upstream regulatory sequences present in the DEGs, a 4th order Markov background model was constructed using the 1kb regions of DNA upstream of all genes found to be differentially regulated in µ *g*. Using this model as a background control, MEME analysis ([Bailey et al., 2015](#B4)) examined the 500 bp regions upstream of upregulated genes using the parameters “-mod anr -minw 6 -maxw 8 -p 4 -nmotifs 10 -dna -revcomp” to elicit enriched motifs.

Gene Ontology (GO) annotation and enrichment was queried using agriGO2 ([Tian et al., 2017](#B71)), ExPath2.0 ([Tseng et al., 2020](#B72)), PANTHER18.0 ([Thomas et al., 2022](#B70)), and PlantGSAD ([Ma et al., 2022](#B35)).

PCA variance analysis was performed using variance stabilized counts from the DESeq dds object in ggplot2; this was limited to the top five hundred transcripts ranked by variance. Data was captured from the plotPCA function using ggplot\_build. To determine the significance of the correlation between the variables of Age and Gravity Condition and the principal components, we used the package PCAtools R package ([Blighe and Lun, 2023](#B6)). The function eigencorplot was used to visualize and test the significance of the correlation between these two variables and the top six principal components ([**Supplementary Figure 2**](#SF2)). The comparison was made using Pearson’s correlation, with pairwise.complete.obs, so that the correlation between each pair is evaluated using all paired data for each variable. The Benjamini and Hochberg multiple testing correction was applied.

### 2.8. Data availability

Raw sequence files and metadata for PS and PRR are available at the NASA data repository GeneLab under the accession numbers OSD-223 and OSD-437.

## 3. Results

### 3.1. Experimental setup and growth parameters

To minimize the impact of handling and transport, seeds were dry-mounted on membranes and remained dormant until hydration at the initiation of each experimental run. The dry seed configuration with an on-orbit hydration also eliminated the need for late loading and allowed for flexibility in the event of flight scrubbing or delayed experiment initiation. Following hydration and illumination, seedlings from PS and PRR germinated with high frequency ([**Supplementary Table 1**](#SM1)) and exhibited nominal growth across each run of both experiments. Differences in experimental design ([**Figure 1**](#f1)) included the presence/absence of a day/night cycle, total experiment length, and centrifugal profiles. Notably, PS incorporated 48 hours of initial 1 *g* treatment at the start of the experiment. For the later experiment, PRR, the μ *g* rotor remained stationary for the entire duration of the experiment. A morphological difference was observed between these experiments, characterized by a largely uniform orientation of seedling roots in PS, in contrast to the more disordered growth patterns observed in PRR ([**Figure 2**](#f2)). This difference could be due to the initial gravitational cue provided to all seedlings in PS, the presence of a day/night cycle in PRR, or a combination of the two. Despite a small degree of variation from seed cassette to seed cassette, each experiment provided a sufficient amount of healthy plant tissue for downstream analysis, and only those cassettes which exhibited nominal growth and development were selected for downstream analysis ([**Supplementary Figure 3**](#SF3)).

#### Figure 2.

[![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/e82e7d043295/fpls-14-1308713-g002.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g002.jpg)

[Open in a new tab](figure/f2/)

Representative Images of Plant Signaling and Plant RNA Regulation Seed Cassettes. Representative images of seedling morphology across µ *g* and 1 *g* conditions taken at the end of each experiment. Digital JPEGs are displayed directly as downlinked from EMCS hardware without alteration. Note that the camera configuration which allowed for close-up imaging provided two images of each seed cassette (left and right side), with partial overlap of each captured image (scale bar = 0.5 cm).

### 3.2. Differentially expressed genes

The individual DE-Seq2 analyses of PS and PRR yielded a significant number of genes that were differentially expressed between microgravity (μ *g*) and the onboard (1 *g*) control. In total, we identified 1,819 and 1,792 differentially expressed genes (DEGs) in PS, and PRR, respectively. The overlap between the two experiments for both μ *g* upregulated and μ *g* downregulated DEG lists was significant ([**Table 1**](#T1)). Both experiments shared 178 genes upregulated in µ *g* and 399 genes downregulated in µ *g*. GO annotation revealed enrichment of the GO terms, “Regulation of Transcription” and “Auxin Signaling” in the common µ *g* upregulated genes. “Cell Wall” and “Response to Stress” were GO terms enriched in the common µ *g* downregulated genes.

#### Table 1.

Hypergeometric distribution hypothesis testing of overlap between DE genes identified by individual analysis of Plant Signaling (PS) and Plant RNA Regulation (PRR).

|  | PS | PRR | Overlap | Hypergeometric Test p-value |
| --- | --- | --- | --- | --- |
| **Total DEGs (WT Shoot)** | 1819 | 1792 |  |  |
| **Upregulated in micro *g*** | 510 | 599 | 178 | 9.97E-185 |
| **Downregulated in micro *g*** | 1309 | 1193 | 399 | 1.63E-272 |

[Open in a new tab](table/T1/)

To further compare the two experiments, RNA-Seq reads from PS and PRR were re-analyzed in a combined study to impart increased statistical power. DE-Seq2 analysis of this combined dataset revealed 1,112 genes upregulated in µ *g* and 1,429 genes downregulated in µ *g* ([**Supplementary Table 2**](#SM1)). It should be noted that >99% of DEGs identified as common to the two individual datasets listed above were similarly identified by this combined analysis. Additionally, this analysis further reinforced the enrichment categories initially observed by individual analyses. [**Table 2**](#T2) lists the major enriched GO terms for DEGs up- and downregulated in µ *g*.

#### Table 2.

GO enrichment analysis of genes differentially regulated in microgravity.

| Genes upregulated in microgravity | | | | | |
| --- | --- | --- | --- | --- | --- |
| Biological Process | | | | | |
| GO Accession | Description | query item | background item | p-value | FDR |
| **GO:0016192** | vesicle-mediated transport | 52 | 397 | 1.30E-13 | 3.00E-10 |
| **GO:0048193** | Golgi vesicle transport | 23 | 108 | 2.80E-10 | 1.10E-07 |
| **GO:0006355** | regulation of transcription, DNA-templated | 155 | 2443 | 1.80E-10 | 7.70E-08 |
| **GO:0048367** | shoot system development | 64 | 896 | 1.70E-06 | 0.00019 |
| **GO:0009734** | auxin-activated signaling pathway | 23 | 190 | 2.80E-06 | 0.00026 |
| **GO:0009733** | response to auxin | 36 | 407 | 5.30E-06 | 0.00042 |
| Cellular Compartment | | | | | |
| **GO:0044431** | Golgi apparatus part | 83 | 567 | 8.10E-24 | 6.90E-21 |
| **GO:0005794** | Golgi apparatus | 123 | 1182 | 8.60E-23 | 3.60E-20 |
| **GO:0012505** | endomembrane system | 175 | 2143 | 1.90E-21 | 5.40E-19 |
| **GO:0005802** | trans-Golgi network | 45 | 256 | 5.20E-16 | 1.10E-13 |
| **GO:0005634** | nucleus | 487 | 9924 | 1.80E-13 | 1.70E-11 |
| Genes downregulated in microgravity | | | | | |
| --- | --- | --- | --- | --- | --- |
| GO Accession | Description | query item | background item | p-value | FDR |
| Biological Process | | | | | |
| **GO:0006950** | response to stress | 340 | 3506 | 1.60E-34 | 4.10E-31 |
| **GO:0006952** | defense response | 172 | 1566 | 7.80E-22 | 5.80E-19 |
| **GO:0009607** | response to biotic stimulus | 116 | 1253 | 1.60E-10 | 3.80E-08 |
| **GO:0023052** | signaling | 162 | 1997 | 3.90E-10 | 7.20E-08 |
| **GO:0009414** | response to water deprivation | 49 | 347 | 3.70E-10 | 7.10E-08 |
| **GO:0006970** | response to osmotic stress | 69 | 636 | 3.60E-09 | 5.20E-07 |
| **GO:0009266** | response to temperature stimulus | 63 | 559 | 4.70E-09 | 6.30E-07 |
| **GO:0009737** | response to abscisic acid | 62 | 578 | 3.30E-08 | 4.20E-06 |
| **GO:0009651** | response to salt stress | 59 | 574 | 2.60E-07 | 2.90E-05 |
| **GO:0009409** | response to cold | 45 | 384 | 2.70E-07 | 2.90E-05 |
| **GO:0071554** | cell wall organization or biogenesis | 61 | 704 | 2.50E-05 | 0.0018 |
| Cellular Compartment | | | | | |
| **GO:0009536** | plastid | 293 | 4213 | 1.80E-10 | 2.10E-08 |
| **GO:0009507** | chloroplast | 289 | 4148 | 2.10E-10 | 2.10E-08 |
| **GO:0009579** | thylakoid | 66 | 584 | 1.80E-09 | 1.50E-07 |
| **GO:0005618** | cell wall | 68 | 706 | 3.00E-07 | 1.10E-05 |

[Open in a new tab](table/T2/)

#### 3.2.1. Genes upregulated in μ *g*, compared to 1 *g* in space

##### 3.2.1.1. Transcription factors

Similar to the individual studies, the combined results for PS and PRR show strong enrichment of genes associated with DNA transcription. In total, 159 Transcription Factors (TFs) as identified by Pruneda-Paz et al. ([Pruneda-Paz et al., 2014](#B55)) were upregulated in µ *g* ([**Supplementary Table 3**](#SM1)). The majority of these TFs are involved in regulating shoot meristem and leaf growth and are associated with organ patterning, leaf development, and photomorphogenesis. Specifically, *SPCH*, *WOX3*, *TCP22*, *GATA2*, *HFR1*, several *GRF*s, as well as TFs mediating auxin responses and brassinosteroid (BR) signaling were upregulated in the μ *g* condition relative to 1 *g* controls. The upregulated list also included 8 TFs belonging to the Apetala2/Ethylene response factor (AP2/ERF) superfamily, of which cytokinin response factors (CRF4 and CRF5) and Aintegumenta (ANT) play established roles in cell proliferation and embryo, cotyledon and leaf development ([Mizukami and Fischer, 2000](#B42); [Rashotte et al., 2006](#B56)).

##### 3.2.1.2. Other transcriptional regulators

Among the DEGs upregulated in μ *g*, 7 genes with potential epigenetic regulatory function were noted. Of these, 5 genes encoded SET domain containing histone methyltransferases including 3 members of the SUVH family ([Naumann et al., 2005](#B46)). Genome wide methylation changes leading to altered transcriptional profiles have been reported in response to spaceflight ([Zhou et al., 2019](#B86); [Paul et al., 2021](#B53)).

##### 3.2.1.3. Auxin related genes

Another conserved category that was prominent in the combined analysis is auxin transport and signaling ([**Table 3**](#T3)); this group includes 2 auxin efflux carriers (*PIN3* and *PIN4*), six auxin response factors (*ARF*s), and 11 small auxin upregulated (*SAUR*) genes.

###### Table 3.

Auxin related genes up regulated in microgravity.

| Gene ID | Log2 Fold Change | padj | Symbol | Description |
| --- | --- | --- | --- | --- |
| **AT1G70940** | 0.4567 | 1.46E-03 | *PIN3* | Auxin efflux regulator |
| **AT3G26810** | 0.2620 | 7.66E-03 | *AFB2* | Auxin F-box protein |
| **AT2G33310** | 0.4547 | 3.04E-04 | *IAA13* | Auxin induced protein |
| **AT1G12820** | 0.3672 | 3.25E-03 | *AFB3* | Auxin signaling F-box protein |
| **AT1G31880** | 0.7857 | 5.47E-03 | *BRX* | BRX family protein |
| **AT5G47750** | 0.2417 | 2.70E-03 | *D6PKL2* | D6PK family protein kinase |
| **AT1G16510** | 1.5668 | 6.93E-08 | *SAUR41* | Clade III SAUR gene |
| **AT3G62150** | 0.6457 | 2.42E-03 | *ABCB21* | ATP-binding cassette transporter |
| **AT5G60450** | 0.4424 | 9.39E-03 | *ARF4* | Auxin response factor |
| **AT1G59750** | 0.3375 | 8.86E-05 | *ARF1* | Auxin response factor |
| **AT1G30330** | 0.8869 | 6.11E-06 | *ARF6* | Auxin response factor |
| **AT1G15750** | 0.2680 | 6.81E-05 | *TPL* | WUS-interacting protein |
| **AT2G01420** | 0.5521 | 1.34E-04 | *PIN4* | Auxin efflux carrier |
| **AT5G59430** | 0.4832 | 2.88E-03 | *TRP1* | Telomere repeat binding protein |
| **AT1G77850** | 0.5913 | 9.30E-07 | *ARF17* | Auxin response factor |
| **AT3G62980** | 0.3926 | 2.95E-04 | *TIR1* | Auxin receptor |
| **AT1G19220** | 0.4469 | 9.25E-03 | *ARF19* | Auxin response factor |
| **AT3G59900** | 0.7563 | 9.71E-04 | *ARGOS* | Auxin-Regulated Gene Involved in Organ Size |
| **AT5G47370** | 1.8362 | 5.23E-13 | *HAT2* | Homeobox-leucine zipper |
| **AT4G32280** | 2.6829 | 2.07E-08 | *IAA29* | Auxin induced protein |
| **AT4G37580** | 1.2138 | 1.91E-04 | *HLS1* | Putative N-acetyltransferase |
| **AT4G30080** | 0.6009 | 2.40E-04 | *ARF16* | Auxin response factor |
| **AT4G38850** | 1.6286 | 2.91E-04 | *SAUR15* | SAUR-like auxin-responsive protein |
| **AT3G16500** | 1.0398 | 2.51E-10 | *PAP1* | Phytochrome-associated protein |
| **AT5G24520** | 0.3512 | 1.89E-03 | *TTG1* | WD40 repeat containing protein |
| **AT5G12050** | 1.0703 | 4.08E-06 | *BG1* | Rho GTPase-activating protein |
| **AT2G45210** | 1.2634 | 1.12E-04 | *SAUR36* | SAUR-like auxin-responsive protein |
| **AT4G34770** | 0.9559 | 5.70E-03 | *SAUR1* | SAUR-like auxin-responsive protein |
| **AT4G38825** | 2.1098 | 3.04E-05 | *SAUR13* | SAUR-like auxin-responsive protein |
| **AT4G38840** | 0.8468 | 3.04E-05 | *SAUR14* | SAUR-like auxin-responsive protein |
| **AT4G38860** | 1.3374 | 3.72E-09 | *SAUR16* | SAUR-like auxin-responsive protein |
| **AT1G75580** | 1.5290 | 7.84E-06 | *SAUR51* | SAUR-like auxin-responsive protein |
| **AT3G60690** | 1.0297 | 3.73E-03 | *SAUR59* | SAUR-like auxin-responsive protein |
| **AT5G20820** | 3.1398 | 9.25E-04 | *SAUR76* | SAUR-like auxin-responsive protein |
| **AT4G36110** | 1.7236 | 2.51E-04 | *SAUR9* | SAUR-like auxin-responsive protein |
| **AT1G69160** | 0.8261 | 4.53E-03 | *BGL1* | BIG GRAIN like protein |
| **AT2G42620** | 0.6706 | 2.67E-05 | *MAX2* | F-box leucine-rich repeat family protein |
| **AT5G08560** | 0.2504 | 5.05E-03 | *WDR26* | WD40 repeat containing protein |

[Open in a new tab](table/T3/)

*SAUR*s were among the more highly upregulated genes in µ *g*, with 9 of the 11 induced more than 2-fold. *SAUR*s were first characterized as rapidly induced in response to auxin, although a few *SAUR*s are repressed by auxin ([Ren and Gray, 2015](#B58)). Of the 11 *SAUR*s identified in this dataset, 10 are induced by auxin; *SAUR15* and *SAUR16* may also be induced by Gibberellic acid (GA) and Brassinosteroids ([Ren and Gray, 2015](#B58)). SAURs 13-16 are classified as lirSAURs ([Sun et al., 2016](#B67)) that are light-regulated in cotyledons and hypocotyls and directly interact with phytochrome interacting factors (PIF)s ([Dong et al., 2019](#B16)). Overexpression of *SAUR36* and *SAUR41* increases cell expansion and promotes hypocotyl elongation ([Chae et al., 2012](#B10); [Stamm and Kumar, 2013](#B66)). SAUR36 is implicated in leaf growth senescence ([Hou et al., 2013](#B21)), and SAUR76 may act as a negative regulator of leaf expansion by regulating cell division ([Markakis et al., 2013](#B37)). SAUR15 is involved in the shade avoidance response and is a potential target of PIF4. Interestingly, *SAUR15* expression has been shown to increase on the lower flank of inflorescence stems 30 min following gravistimulation ([Taniguchi et al., 2014](#B68)).

We also detected 6 *ARF*s upregulated in µ *g*. In general, ARFs are TFs that are bound by Aux/IAA repressors and remain inactive in the absence of auxin. This repression is relieved in the presence of auxin, promoting transcriptional activation of auxin-responsive downstream genes. Three of the *ARF*s detected in this dataset (*ARF1*, *ARF4* and *ARF19*) are implicated in leaf development, while ARF6 and ARF17 play a role in flowering ([Cancé et al., 2022](#B9); [Li et al., 2023](#B33)).

##### 3.2.1.4. Vesicle transport genes

Interestingly, the combined analysis of genes enriched in µ *g* identified a third enriched group –genes involved vesicle-mediated transport– that was not detected in the individual analyses of each experiment. This category consists of approximately 50 genes, including those encoding for members of the coat protein (COP) complex, Sec23/24 protein transport, and several proteins associated with Golgi and the endomembrane system ([Hwang and Robinson, 2009](#B22)). The enrichment of vesicle transport is consistent with observation that shoot growth and developmental processes appear to be altered under µ *g*.

Not surprisingly, given the enrichment of biological processes described above involving vesicle transport, auxin responses, and transcriptional regulators, the cellular compartments overrepresented in the µ *g* upregulated dataset are Golgi and the nucleus ([**Table 2**](#T2)).

##### 3.2.1.5. Promoter analysis of genes upregulated in µ *g*

To examine whether any *cis*-regulatory elements may be associated with the genes upregulated in the µ *g* condition relative to onboard 1 *g* controls, we analyzed regions upstream of the transcript initiation site using Multiple Expectation maximizations for Motif Elicitation (MEME) software. A consensus sequence, 5’-GGCCCA-3’, was returned as the top result of this query, with an E-value of 3.7E-12 ([**Figure 3A**](#f3)). There were 258 occurrences of this motif in 174 unique genes (15.6% of total input genes). Further, this motif predominantly occurred in the -100 to -0 bp region upstream of transcript initiation sites, as seen in the density analysis ([**Figure 3B**](#f3)). This motif, also known as ‘Up1’’(GGCCCAWWW) or ‘‘Site II element’’ (TGGGCY), is overrepresented in the -200 to -1 bp region of Arabidopsis transcripts ([Molina and Grotewold, 2005](#B43); [Davis et al., 2012](#B14)). Additionally, this sequence has been identified as a binding site of the TB1, CYCLOIDEA, PCF (TCP) plant-specific family of transcription factors ([Viola et al., 2011](#B77)). Arabidopsis TCP proteins regulate many aspects of development including cell cycle control, leaf morphology, senescence as well as defense responses ([Aguilar Martinez and Sinha, 2013](#B1); [Li, 2015](#B32)). Consistent with the enrichment of this element upstream of genes upregulated in µ *g*, a class I TCP (*TCP22*) was found to be upregulated in µ *g* ([**Supplementary Table 3**](#SM1)).

###### Figure 3.

[![Figure 3](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/7b62768b9074/fpls-14-1308713-g003.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g003.jpg)

[Open in a new tab](figure/f3/)

Consensus Sequence and Distribution of the Site II Element Enriched in Promoter Regions of Upregulated Transcripts. **(A)** Sequence analysis of the 500 bp region upstream of µ *g* upregulated transcripts showed an enrichment for the motif identified as the Site II element. **(B)** Density analysis of the distribution of this motif within the analyzed region indicates a probability density maxima at -70bp relative to transcriptional start sites (right). The position of individual occurrences of this motif within the analyzed regions is plotted along the x-axis (blue dots), visualized with an artificial spread across the y-axis.

#### 3.2.2. Genes downregulated in µ *g*, compared to 1 *g* in space

The combined analysis of PS and PRR indicated that responses to stress (both abiotic and biotic) were highly enriched in genes downregulated in µ *g* ([**Table 2**](#T2)), consistent with what was observed in each individual experiment. This overall dampening of stress response genes includes a downregulation of genes encoding several members of Cytochrome P450 family, 14 Glutathione S-transferases, and members of a MATE efflux family involved in detoxification. In addition, we detected an enrichment of plastid-associated genes as well as several involved in cell wall organization.

##### 3.2.2.1. Transcription factors

The µ *g* downregulated DEGs include 120 TFs ([**Supplementary Table 4**](#SM1)). Unlike the upregulated TFs, which were associated with developmental responses, the downregulated TFs are primarily involved in regulating stress responses ([**Figure 4**](#f4)). The downregulated TFs include those implicated in biotic stress and plant defense ([Ng et al., 2018](#B47)) and those involved in abiotic stresses, including osmotic and temperature stress. As is illustrated in [**Figure 4**](#f4), the functions of these downregulated TFs are distinct with limited overlap with those of the upregulated TFs. While 4-5 GO terms show some overlap, these categories are most significant in the downregulated TFs. Further analysis within the overlapping categories show for instance that the auxin and ABA related terms in the upregulated TF group are involved with growth while the downregulated TF genes in these groups contain those that regulate stress as described below.

###### Figure 4.

[![Figure 4](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/3e6f5914e3e4/fpls-14-1308713-g004.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g004.jpg)

[Open in a new tab](figure/f4/)

Functional comparison of transcription factors differentially expressed in microgravity. Differentially regulated transcription factor gene lists were analyzed for enrichment by PlantGSAD. Following GO enrichment, Singular Enrichment Analyses (SEA)s were compared by SEACOMPARE to identify common and/or unique GO categories using the online tool in PlantGSAD. The p values for GO categories were generated by the SEACOMPARE tool and represent the significance of the GO terms. The color progression from yellow to red represents increasing significance while the gray bars are not significant.

The largest groups of TF downregulated in µ *g* are 15 ethylene response factors (ERF)s and 12 WRKY TFs ([Phukan et al., 2016](#B54)). The WRKY TFs in our dataset appear to function chiefly in abiotic or biotic stress responses. The ERFs include 7 dehydration responsive element-binding (DREB) subfamily A members including CBF2, ([Shinozaki and Yamaguchi-Shinozaki, 2000](#B62); [Novillo et al., 2004](#B49)) and 8 AP2/ERF family TFs ([Srivastava and Kumar, 2019](#B65)). The downregulated TF list also includes 4 heat stress TFs, several MYB and NAC family TFs, and calmodulin binding transcriptional activators (CAMTA)s.

##### 3.2.2.2. Biotic stress and defense related genes

Among the genes downregulated in µ *g*, approximately 200 genes were associated with plant defense and response to biotic stimuli. This category includes 24 disease-resistance proteins, different classes of receptor-like protein kinases, and several WRKY TFs. Of interest, it has been reported that WRKY18, WRKY40 and WRKY60 (which are represented in our dataset) form a cluster that work either synergistically or antagonistically in response to bacterial or necrotrophic pathogens ([Xu et al., 2006](#B81); [Schön et al., 2013](#B60)).

##### 3.2.2.3. Abiotic stress related genes

In addition to the downregulation of genes involved in biotic stress responses, we also detected approximately 140 downregulated genes associated with the responses to temperature stimulus and ABA-mediated regulation of osmotic stress ([**Supplementary Table 5**](#SM1)). Song et al. carried out a time series of RNA-Seq experiments and large-scale ChIP-Seq focused on 21 ABA-responsive TFs ([Song et al., 2016](#B63)). This study revealed a TF hierarchical network regulating ABA responses in Arabidopsis. Interestingly, 9 of these 21 TFs (namely, *NFY-B2*, *NFY-C2*, *GBF3*, *MYB44*, *DIV2*, *HB7*, *NAC032*, *NAC102* and *RD26*) are downregulated in our dataset.

##### 3.2.2.4. Calcium signaling related genes

Given the enhancement in stress responses, it is not surprising that approximately 40 genes involved in calcium signaling were downregulated in µ *g* ([**Table 4**](#T4)). This category includes calcium binding proteins, calcium-dependent protein kinases (CDPK)s, calmodulin-binding proteins and TFs, CBL-interacting protein kinases, and cyclic nucleotide gated ion channels (CNGC)s.

###### Table 4.

Ca++ related genes downregulated in microgravity.

| Gene ID | Log2 Fold Change | padj | Symbol | Description |
| --- | --- | --- | --- | --- |
| **AT4G17615** | -0.5692 | 1.08E-03 | *CBL1* | Calcineurin B-like protein 1 |
| **AT5G66650** | -1.4308 | 3.72E-04 | *CMCU* | Calcium uniporter protein 3 |
| **AT4G32060** | -0.5073 | 3.60E-04 | *MICU* | Calcium uptake protein, mitochondrial |
| **AT5G54590** | -0.6115 | 5.94E-03 | *CRLK1* | Calcium/calmodulin-regulated receptor-like kinase |
| **AT5G37770** | -1.7365 | 4.38E-09 | *CML24* | Calcium-binding protein |
| **AT5G42380** | -2.7770 | 8.69E-03 | *CML37* | Calcium-binding protein |
| **AT5G49480** | -1.0429 | 5.98E-06 | *CP1* | Calcium-binding protein |
| **AT2G46600** | -2.6536 | 8.42E-14 | *KIC* | Calcium-binding protein |
| **AT4G27280** | -3.6521 | 2.59E-10 | *KRP1* | Calcium-binding protein |
| **AT5G54490** | -2.2801 | 3.69E-06 | *PBP1* | Calcium-binding protein |
| **AT3G14590** | -1.1538 | 2.31E-04 | *NTMC2T6.2* | Calcium-dependent lipid-binding family protein |
| **AT4G21940** | -0.8663 | 2.51E-03 | *CPK15* | Calcium-dependent protein kinase |
| **AT5G66210** | -1.7608 | 1.82E-09 | *CPK28* | Calcium-dependent protein kinase |
| **AT1G76040** | -0.9149 | 3.36E-03 | *CPK29* | Calcium-dependent protein kinase |
| **AT3G57530** | -1.9357 | 1.37E-11 | *CPK32* | Calcium-dependent protein kinase |
| **AT4G09570** | -0.4804 | 3.47E-03 | *CPK4* | Calcium-dependent protein kinase |
| **AT1G27770** | -1.8644 | 2.82E-11 | *ACA1* | Calcium-transporting ATPase |
| **AT2G41010** | -1.5839 | 2.42E-12 | *CAMBP25* | Calmodulin-binding protein |
| **AT5G62570** | -1.4615 | 3.55E-08 | *CBP60A* | Calmodulin-binding protein |
| **AT2G24300** | -1.0421 | 3.92E-03 | *CBP60E* | Calmodulin-binding protein |
| **AT5G26920** | -2.8406 | 1.07E-06 | *CBP60G* | Calmodulin-binding protein |
| **AT5G64220** | -0.4456 | 1.03E-04 | *CAMTA2* | Calmodulin-binding transcription activator |
| **AT2G22300** | -0.5213 | 1.30E-03 | *CAMTA3* | Calmodulin-binding transcription activator |
| **AT1G67310** | -0.4575 | 3.13E-05 | *CAMTA4* | Calmodulin-binding transcription activator |
| **AT2G41100** | -1.4492 | 5.29E-06 | *CML12* | Calmodulin-like protein |
| **AT2G43290** | -1.7077 | 5.75E-14 | *CML5* | Calmodulin-like protein |
| **AT3G51920** | -0.8321 | 5.20E-06 | *CML9* | Calmodulin-like protein |
| **AT1G01130** | -0.9225 | 5.87E-05 | *CIPK* | CBL-interacting serine/threonine-protein kinase |
| **AT2G30360** | -0.7795 | 9.29E-05 | *CIPK11* | CBL-interacting serine/threonine-protein kinase |
| **AT5G01820** | -0.7076 | 1.98E-03 | *CIPK14* | CBL-interacting serine/threonine-protein kinase |
| **AT1G48260** | -0.7532 | 6.49E-03 | *CIPK17* | CBL-interacting serine/threonine-protein kinase |
| **AT5G07070** | -0.7082 | 5.74E-05 | *CIPK2* | CBL-interacting serine/threonine-protein kinase |
| **AT3G19100** | -0.4980 | 3.52E-04 | *CRK2* | CDPK-related kinase |
| **AT5G53130** | -1.2025 | 1.84E-07 | *CNGC1* | Cyclic nucleotide-gated ion channel |
| **AT5G54250** | -0.8611 | 5.00E-05 | *CNGC4* | Cyclic nucleotide-gated ion channel |

[Open in a new tab](table/T4/)

#### 3.2.3. Non-coding RNAs

Natural antisense transcripts (NAT)s are antisense sequences which may overlap in part with protein coding (sense) transcripts. This sense-antisense pairing can lead to regulation of the sense transcript ([Wight and Werner, 2013](#B79)). A negative correlation in expression (i.e. NAT up and sense transcript down) may be indicative of gene silencing; however, NATs may also enhance sense transcript expression by regulating mRNA stability and/or translation ([Reis and Poirier, 2021](#B57)).

Among the DEGs in µ *g*, we found 42 upregulated NATs and 30 downregulated NATs. Interestingly, we observe a negative correlation between NAT expression and the overlapping sense transcripts for 29 of the 42 upregulated NATs suggesting a possible means of repression of these genes. Among these are several genes encoding for chloroplastic proteins, defense related proteins and the TF *MYB44* ([**Supplementary Table 6**](#SM1)). Additionally, we observed that the expression of 20 of the overlapping sense transcripts for the 30 downregulated NATs are upregulated under µ *g* ([**Supplementary Table 6**](#SM1)).

### 3.3. Microgravity versus the space environment

Perhaps the most striking aspect of the DEGs that are downregulated in both PS and PRR is that > 400 genes are associated with stress responses. This included a strong enrichment of biotic stress response (in particular, response to bacteria and chitin) and genes known to respond to many abiotic stresses, including salt and temperature. Curiously, these responses have been reported as upregulated in spaceflight experiments compared to ground controls. It is not surprising that the space environment poses several challenges to plants and many of these are not easy to measure or replicate on the ground. Although our focus in both PS and PRR spaceflights was the direct comparison of µ *g* with the onboard 1 *g* control, we also carried out ground controls where EMCS chamber conditions were matched in the ground reference module ERM-2. An examination of the DEGs between 1 *g* in space and ground controls revealed that many of these stress response-related genes were actually upregulated in 1 *g* compared to the ground. These observations indicate that the space environment (excluding µ *g*) enhanced the expression of these stress-related genes. However, this group of genes was specifically downregulated in µ *g* compared to 1 *g* suggesting that microgravity masks the induction of these genes in the space environment. Representative heat maps for select defense-related genes are shown in [**Figure 5**](#f5) ([**Supplementary Table 7**](#SM1)). As an example of an abiotic stress response, heat maps for a set of genes involved in salt stress are shown in [**Figure 6**](#f6) ([**Supplementary Table 8**](#SM1)). These heat maps clearly illustrate that the stress-related genes showed higher levels of expression in the spaceflight 1 *g* condition compared to either µ *g* or the ground controls. Since the 1 *g* and µ *g* experiments were conducted on two rotors held in the same chamber at the same time, we can be confident that all other “space-related” stimuli were shared between the two, and that the primary difference between them was the µ *g* treatment. The differences between 1 *g* and the ground control samples, would include all other effects of the space environment, excluding microgravity. It is clear that many of these genes would not have been detected as differentially expressed in the absence of the on board 1 *g* control and these results reveal that this control is critical in order to identify µ *g* specific changes.

#### Figure 5.

[![Figure 5](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/0964ead77412/fpls-14-1308713-g005.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g005.jpg)

[Open in a new tab](figure/f5/)

Expression profiles of DEG subsets across 1 *g*, µ *g*, and ground control conditions. DESeq2 normalized counts (two replicates for each condition) of defense DEG subsets were visualized as heatmaps by the R package pheatmap. Data presented are clustered by column (dendrogram, top), and scaled by row.

#### Figure 6.

[![Figure 6](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/f91a1a7a5a2f/fpls-14-1308713-g006.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g006.jpg)

[Open in a new tab](figure/f6/)

Expression profiles of DEG subsets across 1 *g*, µ *g*, and ground control conditions. DESeq2 normalized counts (two replicates for each condition) of salt stress DEG subsets were visualized as heatmaps by the R package pheatmap. Data presented are clustered by column (dendrogram, top), and scaled by row.

#### 3.3.1. Micro RNAs detected and their target genes

In addition to mRNA profiling, the PRR spaceflight experiment included sequencing of small RNAs (sRNA)s which revealed that several micro RNAs (miRNA)s were differentially regulated in µ *g* compared to 1 *g* and ground controls. miRNAs act to regulate gene expression either by the cleavage of their target mRNAs, or by repression of translation or DNA methylation ([Song et al., 2019](#B64)).

We identified 3 miRNAs –miR319c, miR863-5p and miR398b-3p– that were upregulated in µ *g* ([**Figure 7A**](#f7)). Both miR863 and miR398b are found in Arabidopsis leaves and seedlings ([Meng et al., 2012](#B40)). The miR398 family was shown to target Cu++ and Zn++ dismutase enzymes in response to Cu++ deficiency ([Yamasaki et al., 2007](#B82)) and the miR319 family is involved in the regulation of leaf shape via their interaction with TCP TFs ([Bresso et al., 2018](#B7)). Although the specific targets listed in these publications were not represented in our dataset, we did detect several putative miRNA targets. Correlation analysis of miR319c and miR863-5p and their predicted mRNA targets detected in our dataset are shown in [**Figure 7B**](#f7) ([**Supplementary Table 9**](#SM1)). It can be seen that many of the predicted targets were coordinately downregulated in µ *g*, consistent with repression by these miRNAs. The miR319c cluster of downregulated targets include several defense-related genes and 12 of the 22 miR398b-3p target genes encode for chloroplastic enzymes and proteins. Interestingly, overall 38% of the downregulated miR319c, miR863-5p and miR398b-3p target gene products are localized in the plastid.

##### Figure 7.

[![Figure 7](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/9c2f6eaddebf/fpls-14-1308713-g007.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g007.jpg)

[Open in a new tab](figure/f7/)

Differentially expressed miRNAs and their target genes. **(A)** Heatmap showing the expression of differentially regulated miRNAs. **(B)** Correlation of expression between miR863-5p and miR319c and their putative targets. Squares denote the miRNAs and circles represent the miRNA target genes. Red and green represent up and down regulation, respectively.

Two miRNAs, miR156f-3p and miR5654-3p were upregulated in 1 *g* relative to µ *g* ([**Figure 7A**](#f7)) with coordinate down regulation of 14-16 of their predicted targets in 1 *g* ([**Supplementary Table 9**](#SM1)). The miR156 family is closely associated with and regulates several Squamosa Promoter binding Like (SPL) TFs and is important for regulating phase transitions such as the progression from juvenile to adult stages and flowering time ([Wang and Wang, 2015](#B78)). Most recently, miR156 has been shown to modulate seedling growth in response to temperature and light changes via its interaction with SPL9 ([Sang et al., 2023](#B59)). Coincidentally, *SPL9* expression is downregulated in 1 *g* in our dataset along with other targets of miR156f-3p, which are related to auxin and ethylene signaling.

We also observed that both µ *g* and 1 *g* seedlings had higher expression of miR398b-3p compared to ground control and 4 miR398b-3p target genes were coordinately downregulated in both µ *g* and 1 *g* compared with ground, including two TFs, *GTE11* and *ATRX-like-protein*.

#### 3.3.2. Day 4 versus day 6: a possible interaction between µ *g* responses and development

The experimental design of PRR with staggered hydration allowed for some samples to be initiated 48h later, yielding two time points (Day 4 and Day 6) from the same experiment. Our major focus was on DEGs detected at Day 6, described in the preceding sections. Comparing the effects of microgravity on the Day 4 and Day 6 plants revealed interactions between plant developmental stage and microgravity. These interactions are apparent in the PCA plot of the PRR Day 4 and 6 flight samples ([**Figure 8A**](#f8)). Principal component 1 primarily separated Day 4 and Day 6 samples under 1 *g* (p<0.05). Principal component 2 separated 1 *g* and µ *g* at either day (p<0.001). However, there was little separation between the Day 4 and Day 6 samples in µ *g* in the first principal component ([**Figure 8A**](#f8)).

##### Figure 8.

[![Figure 8](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d3e3/10800490/e17578d18c2f/fpls-14-1308713-g008.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=10800490_fpls-14-1308713-g008.jpg)

[Open in a new tab](figure/f8/)

Comparison of Expression Profiles at Day 4 and Day 6. **(A)** Principal component analysis (PCA) of the PRR flight samples. Filled and open symbols represent µ *g* and 1 *g*, respectively (black circles, Day 4; red circles, Day 6). **(B)** Representative examples of individual genes that show similar patterns of expression between 1 *g* and µ *g*, at Day 4 and Day 6. **(C)** Representative examples of individual genes showing higher expression uniquely at Day 4 in 1 *g*. DESeq2 normalized counts were visualized using ggplot2.

Examination of the DEGs at Day 4 revealed that a much smaller fraction of genes were differentially regulated in µ *g* at Day 4 (compared with the DEGs detected at Day 6). In total, at Day 4 there were 406 DEGs (75 up and 331 down in µ *g* compared to 1 *g*). Many of these DEGs (~ 40% of the up- and 60% of downregulated genes in µ *g*) at Day 4 were shared with the Day 6 data. A majority of the 210 genes commonly downregulated in µ *g* at both Day 4 and Day 6, were related to abiotic and biotic stresses as described previously. This finding indicates that µ *g* specific downregulation of stress responses occurs as early as Day 4 and is common between the two times sampled. Genes associated with cell wall organization were also found to be downregulated at both days. Examples of genes which exhibit similar downregulation in microgravity at both Day 4 and 6 are depicted in [**Figure 8B**](#f8).

We also observed that several genes were uniquely downregulated in µ *g* at Day 4 only. Scatter plots of representative genes in this group clearly indicate that the differential expression observed at Day 4 did not persist at Day 6 ([**Figure 8C**](#f8)).

Taken together, these results suggest that the developmental window the samples are in could influence the observed transcription response profiles and point to interactions between µ *g* and the developmental stage.

## 4. Discussion

### 4.1. Conserved and unique transcriptional changes in microgravity

The PS and PRR spaceflight experiments were designed to examine early seedling development and responses to microgravity. To answer these questions, we utilized the EMCS facility with a rotor configuration selected to provide µ *g* and an onboard 1 *g* control. The two experiments were conducted at different times and had different lighting regimes as well as some other differences in set up as outlined in [**Figure 1**](#f1). Despite these differences, there was considerable parity between the DEGs in µ *g* between the two experiments. Genes upregulated in µ *g* compared to the 1 *g* control were primarily involved in leaf and shoot development. The majority of the upregulated TFs function to regulate these processes and the enrichment in auxin and vesicle transport also support growth processes. In contrast, there appears to be a substantial downregulation of both biotic and abiotic stress responses in µ *g*. Defense related genes were overrepresented and most of the downregulated TFs function in mediating plant stress responses ([**Figure 4**](#f4)). Additionally, we identified specific miRNAs that were differentially regulated in microgravity with coordinate regulation of their putative targets.

The large-scale downregulation in microgravity of stress-response related genes in the PS and PRR flight experiments are somewhat at odds with other experiments where flight responses are compared to a ground control on Earth. In fact, we find that genes reported as upregulated in spaceflight appear to be downregulated in our datasets. For instance, 70 genes that were upregulated in spaceflight in BRIC19 ([Choi et al., 2019](#B12)) are downregulated in µ *g* in our dataset. Many of these common genes are associated with response to stress and hypoxia.

We do however find more overlap in responses if we examine RNA-Seq datasets from other EMCS spaceflight experiments which utilized onboard 1 *g* controls. The Seedling Growth experiments (SG2 and SG3) were conducted in the EMCS; however these experiments included photostimulation with either unidirectional blue ([Herranz et al., 2019](#B20); [Vandenbrink et al., 2019](#B74)) or red ([Villacampa et al., 2021](#B76)) light for the final 48h of the experimental timeline. Although there was almost no overlap in DEGs upregulated in µ *g*; we do detect considerable overlap with µ *g* downregulated genes as well as genes downregulated in low (<0.1) *g* ([Herranz et al., 2019](#B20)). Comparing our results to Herranz et al. shows that 54 genes were commonly downregulated in µ *g*. Furthermore, 143 genes downregulated in low *g* were shared with genes downregulated in µ *g* in our data. Even more pronounced is the similarity in enriched GO terms for genes downregulated in µ *g* and low *g* compared to 1 *g* ([Herranz et al., 2019](#B20)) and the genes downregulated in µ *g* in the PS/PRR data. These include, response to stimulus, response to abiotic stimulus and response to stress. Genes downregulated in µ *g* in with the red light photostimulation ([Villacampa et al., 2021](#B76)) were enriched in the GO categories response to bacterium and fungus. Taken together these results further reinforce the idea that both biotic and abiotic stress responses appear to be specifically downregulated in µ *g*. This regulation would not have been detected without the onboard 1 *g* condition for comparison and these results point to the value of having an onboard 1 *g* control.

At least 4 different Arabidopsis ecotypes have been flown in space including Col-0, Ler, Ws and Cvi ([Paul et al., 2017](#B52); [Choi et al., 2019](#B12)). Interestingly, the Col-0 ecotype was found to be more responsive to the spaceflight environment compared to both Ws and Ler with more DEGs detected overall. A direct comparison of our results (on light grown Col-0 shoots) with the previous studies is hampered by the fact that they utilized either root tips or etiolated whole seedlings. Nevertheless, when we compare our findings with other spaceflight experiments, we find that two common features stand out; many experiments have reported altered expression of genes involved in cell wall modification and photosynthesis/plastid related genes. Two unexpected findings of our experiments are the potential regulation by the transcription factor Elongated Hypocotyl 5(HY5) and the altered expression of a few gravitropism related genes.

#### 4.1.1. Cell wall related genes

Genes involved in remodeling of plant cell walls have been reported to be differentially expressed in previous spaceflight experiments ([Paul et al., 2013](#B51); [Kwon et al., 2015](#B29); [Johnson et al., 2017](#B24); [Choi et al., 2019](#B12); [Nakashima et al., 2023](#B45)). Glycomic analysis of spaceflight plant samples have shown changes in cell wall glycans, consistent with spaceflight related modification of cell walls ([Johnson et al., 2017](#B24); [Nakashima et al., 2023](#B45)). Similar to these previous reports, we also observed that genes involved in cell wall modification are overrepresented in our datasets; particularly we found approximately 100 genes associated with cell wall organization and modification downregulated in µ *g*. These included genes encoding for several members of the xyloglucan endotransglucosylase (XTH) family, expansins, peroxidases, pectin esterases and polygalacturonases. These cell wall proteins are involved in cell wall polymer rearrangement which occurs during cell elongation ([Irshad et al., 2008](#B23)). The individual genes in these enzyme categories however, were not conserved between our dataset and the previous reports; probably due to differences in tissue type, age and growth conditions. We also found cellulose synthase-like genes and 6 genes encoding for dirigent proteins which are involved in lignin biosynthesis to be downregulated in µ *g*.

#### 4.1.2. Chloroplast and photosynthesis related genes

The mis-regulation or altered regulation of photosynthesis related genes has been reported for many spaceflight experiments including those that focused on seedlings grown in the dark ([Kwon et al., 2015](#B29); [Kruse et al., 2020](#B28)). The investigators who conducted the EMCS experiments SG2 and SG3, (Vandenbrink et al., Herranz et al., and Villacampa et al.) reported that genes involved in photosynthesis were enriched in both µ *g* upregulated and µ *g* downregulated datasets. We did not detect photosynthesis related genes upregulated in µ *g* in either PS or PRR, perhaps due to the differences in the lighting regime compared with the SG series of experiments. However, we do see enrichment for genes involved in photosynthesis and plastid function downregulated in µ *g*. Plastid localization was an enriched GO term for cellular localization accounting for approximately 300 genes in the µ *g* downregulated category of our dataset. Genes encoding for subunits of the NADPH complex, LHCA and photosystem I and II core were downregulated in µ *g* in both PS and PRR. We also found that several of the µ *g* downregulated miRNA targets were associated with plastids. Since many of these spaceflight studies have focused on young Arabidopsis seedlings, it is not clear if the altered regulation of genes associated with photosynthesis and chloroplast function would persist in fully grown plants. Whether such adjustments continue to maturity and how they may impact the photosynthetic capacity of plants will need to be evaluated in future spaceflight experiments.

#### 4.1.3. HY5 target genes

Genes differentially expressed in µ *g* in both PS and PRR were significantly enriched for HY5 target genes. HY5 is a central regulator of photomorphogenesis and may directly or indirectly affect the expression of approximately one third of the Arabidopsis genome ([Lee et al., 2007](#B31); [Gangappa and Botto, 2016](#B19)). HY5 is involved in integrating light and hormonal signals to regulate developmental processes in plants. In addition to a major role in light mediated signaling, HY5 is implicated in nutrient uptake and utilization, biosynthesis of secondary metabolites and response to fluctuations in temperature ([Xiao et al., 2021](#B80)). HY5 targets were significantly enriched in the genes upregulated in µ *g* (hypergeometric test, *p*=2.45e-11). The µ *g* upregulated HY5 targets were associated with organ development, light responses and auxin transport. We also found a significant enrichment of HY5 targets in the genes downregulated in µ *g* (hypergeometric test, *p*=1.698e-120). Many of the downregulated HY5 targets were involved in abiotic and biotic stress responses.

#### 4.1.4. Gravitropism related genes

Curiously, we found some gravitropism related genes to be upregulated in µ *g*. Among these, the TF Shoot Gravitropism 5 (*SGR5*) was upregulated in µ *g* at both Day 4 and Day 6. SGR5 was first described as being important for the gravitropic response of Arabidopsis inflorescence stems ([Yamauchi et al., 1997](#B83)). Further studies showed that SGR5 is localized in the shoot endodermis and that amyloplast sedimentation in the shoot endodermis is slower in the *sgr5* mutant ([Morita et al., 2006](#B44); [Tanimoto et al., 2008](#B69)). SGR5 is also known as Indeterminate Domain 15 (IDD15). The IDD TFs IDD14, IDD15 and IDD16 have been shown to work cooperatively to regulate auxin transport in the shoot and play a role in aerial tissue development and gravitropic responses ([Cui et al., 2013](#B13)). We found *IDD14* to be upregulated in µ *g*, as well as another gene involved in regulating gravitropic response – *LAZY1*. *LAZY1* is expressed primarily in shoots of young seedlings and the early stages of the hypocotyl gravitropism were affected in a *lazy1* mutant ([Yoshihara and Spalding, 2017](#B84)). The LAZY proteins are thought to act early in the gravity signaling cascade by transmitting positional information on amyloplast sedimentation upstream of auxin redistribution ([Nishimura et al., 2023](#B48)). The upregulation of these genes under µ *g* maybe related to their roles in regulating auxin flow; a closer look at their localization and dynamics under microgravity would be informative.

### 4.2. The Influence of developmental stage on observed transcriptional responses

The differences in gene expression between µ *g* and 1 *g* at Day 4 and Day 6 in PRR, revealed that many more genes were responsive to µ *g* at Day 6 than at Day 4. Since the Day 4 and Day 6 samples for each condition were obtained from the same rotor and collected at the same time, these differences suggest that the developmental stage of the seedlings can have a profound effect on observed transcriptional responses. The variation between Day 4 and Day 6 samples grown in 1 *g* and µ *g*, was also evident in the PCA plot where principal component 1, (which captured 53% of the variation between samples), clearly separated the Day 4 and Day 6 samples at 1 *g*; however, this separation was not observed in samples grown under the µ *g* condition. This indicates that differences in gene expression between the Day 4 and Day 6 samples in 1 *g* are either masked or not present in µ *g*. A possible explanation for this observation is that there are differences between 1 *g* and µ *g* grown seedlings in their developmental progression.

To determine if there were delays in germination between 1 *g* and µ *g* that could result in altered development we examined germination time by interrogating the sequential series of images obtained throughout the PRR experiment. We found no difference in the timing of the first occurrence of radicle emergence between µ *g* and 1 *g* seedlings. We conclude that there was no delay in germination under µ *g*; additionally, growth at Day 6 ([**Figure 3**](#f3)) was similar between µ *g* and 1 *g* conditions. Although we did not see gross differences in growth, given the short timeframe of this experiment, we cannot rule out that there may be subtle changes which could become more pronounced as the plants mature. Longer duration experiments with a finer resolution of time points would be required to fully characterize and understand the regulatory underpinnings for these differences.

### 4.3. Lessons learned for future spaceflight experiments

#### 4.3.1. Long term plant experiments

The PS and PRR experiments were focused on a narrow window of the Arabidopsis life cycle; the TROPI seed cassettes and EC arrangement only supported short duration experiments. Therefore we cannot extrapolate or assume that the transcriptional response to microgravity seen in these experiments would be universally applicable to long duration plant experiments on the ISS. Furthermore the seed cassettes provide a controlled optimal environment for seedling growth with sufficient lighting, moisture and humidity without inherent spaceflight associated limitations of water delivery that are manifest in larger plant growth habitats. Long term experiments where plants are grown from seed to maturity are needed to characterize critical stages in plant development. This approach will lead to a better understanding of the physiology of plant adaptations to the space environment.

#### 4.3.2. Multiple bioreplicates

Both PS and PRR included two experimental runs or bioreplicates. Although the replicates for each spaceflight were carried out back to back in the same hardware, and from the same flight builds, we detected run to run variation in responses. Run to run variation may be caused by other spaceflight related conditions that could differ on a day to day basis on the ISS. While this disparity did not overshadow the major transcriptional changes that were conserved between the PS and PRR experiments, it could be misleading if results from only a single experiment are considered. This underscores the importance of being able to conduct replicate spaceflight experiments.

#### 4.3.3. Combined OMIC approaches

We acknowledge that single-time-point studies are snapshots of “steady-state” transcriptional profiles which, on their own, are not sufficient to capture the full range and continuum of regulation. However, single-time-point transcriptional studies are valuable in that they can help identify key transcriptional regulators and they offer the first signs of pathways which may be altered. The inclusion of sRNA profiling in combination with RNA-Seq can provide clues on an additional layer of post transcriptional regulation and upcoming spaceflight experiments are likely to incorporate both these forms of analyses. While the proteome may be a more direct readout of response, spaceflight experiments frequently have insufficient amounts of tissue for large scale proteomic studies; additional hurdles include the cost and the paucity of well annotated reference protein databases. Only a few flight experiments to date, have taken a proteomic approach ([Ferl et al., 2014](#B17); [Mazars et al., 2014](#B39); [Zhang et al., 2015](#B85); [Kruse et al., 2020](#B28)), and fewer still have been able to include both proteomic and transcriptomic analyses ([Kruse et al., 2020](#B28)). Moving forward it will be important to employ multiple OMICs approaches to study a spaceflight experiment. The larger plant habitats on the ISS such as Veggie and the Advanced Plant Habitat (APH) can better support these endeavors. Ultimately, the biochemical and metabolic status of the plants will be indicative of their adaptations to their new environment.

## Data availability statement

The datasets presented in this study can be found in online repositories. The names of the repository/repositories and accession number(s) can be found below: NASA GeneLab data repository, OSD-223 and OSD-437.

## Author contributions

EL: Investigation, Writing – original draft, Writing – review & editing, Methodology, Visualization, Software. JS: Methodology, Writing – original draft, Data curation, Formal analysis. CD: Formal analysis, Methodology, Writing – original draft, Writing – review & editing, Supervision. IP: Writing – original draft, Writing – review & editing, Conceptualization, Funding acquisition, Investigation, Project administration, Supervision, Data curation.

## Acknowledgments

We gratefully acknowledge our payload teams at NASA-Ames Research Center for their guidance and help making these experiments possible, especially Robert Bowman, Marianne Steele, Gwo-Shing Sun, David Heathcote, Kris Vogelsong and John Rask. Thanks also to the N-USOC in Trondheim, Norway for their cooperation and help during the on orbit experiments as well as the schedule tests and OVTs. We thank Caroline Smith for her work on pre flight testing and flight build for the PS experiment. Library preparation and RNA-Seq for PS was carried out at the Genomics Science Laboratory at North Carolina State University and for PRR by Novogene Corporation Inc. We also thank NASA astronauts Mike Fossum and Kate Rubins for conducting the on-orbit operations on the ISS.

## Funding Statement

The author(s) declare financial support was received for the research, authorship, and/or publication of this article. This work was funded by NASA (Grant Nos. NNX10AM72G and NNX15AB07G to IP).

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: <https://www.frontiersin.org/articles/10.3389/fpls.2023.1308713/full#supplementary-material>

[Click here for additional data file.](/articles/instance/10800490/bin/Image_1.tif) (8.2MB, tif)

[Click here for additional data file.](/articles/instance/10800490/bin/Image_2.tif) (2.2MB, tif)

[Click here for additional data file.](/articles/instance/10800490/bin/Image_3.tif) (9.2MB, tif)

[Click here for additional data file.](/articles/instance/10800490/bin/Table_1.xlsx) (433.2KB, xlsx)

[Click here for additional data file.](/articles/instance/10800490/bin/Table_2.docx) (18.8KB, docx)

## References

1. Aguilar Martinez J., Sinha N. (2013). Analysis of the role of Arabidopsis class I TCP genes AtTCP7, AtTCP8, AtTCP22, and AtTCP23 in leaf development. Front. Plant Sci. 4. doi:  10.3389/fpls.2013.00406
    [[DOI](https://doi.org/10.3389/fpls.2013.00406)] [[PMC free article](/articles/PMC3797442/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24137171/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci&title=Analysis%20of%20the%20role%20of%20Arabidopsis%20class%20I%20TCP%20genes%20AtTCP7,%20AtTCP8,%20AtTCP22,%20and%20AtTCP23%20in%20leaf%20development&author=J.%20Aguilar%20Martinez&author=N.%20Sinha&volume=4&publication_year=2013&pmid=24137171&doi=10.3389/fpls.2013.00406&)]
2. Anders S., Pyl P. T., Huber W. (2015). HTSeq-A Python framework to work with high-throughput sequencing data. Bioinformatics
   31 (2), 166–169. doi:  10.1093/bioinformatics/btu638
    [[DOI](https://doi.org/10.1093/bioinformatics/btu638)] [[PMC free article](/articles/PMC4287950/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25260700/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=HTSeq-A%20Python%20framework%20to%20work%20with%20high-throughput%20sequencing%20data&author=S.%20Anders&author=P.%20T.%20Pyl&author=W.%20Huber&volume=31&issue=2&publication_year=2015&pages=166-169&pmid=25260700&doi=10.1093/bioinformatics/btu638&)]
3. Andrews S. (2010). “‘FastQC: a quality control tool for high throughput sequence data,” in Babraham Bioinformatics (Cambridge, United Kingdom: Babraham Institute; ). [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Babraham%20Bioinformatics&author=S.%20Andrews&publication_year=2010&)]
4. Bailey T. L., Johnson J., Grant C. E., Noble W. S. (2015). The MEME suite. Nucleic Acids Res.
   43 (W1), W39–W49. doi:  10.1093/nar/gkv416
    [[DOI](https://doi.org/10.1093/nar/gkv416)] [[PMC free article](/articles/PMC4489269/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25953851/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=The%20MEME%20suite&author=T.%20L.%20Bailey&author=J.%20Johnson&author=C.%20E.%20Grant&author=W.%20S.%20Noble&volume=43&issue=W1&publication_year=2015&pages=W39-W49&pmid=25953851&doi=10.1093/nar/gkv416&)]
5. Barker R., Kruse C. P. S., Johnson C., Saravia-Butler A., Fogle H., Chang H.-S., et al. (2023). Meta-analysis of the space flight and microgravity response of the Arabidopsis plant transcriptome. NPJ Microgravity
   9 (1), 21. doi:  10.1038/s41526-023-00247-6
    [[DOI](https://doi.org/10.1038/s41526-023-00247-6)] [[PMC free article](/articles/PMC10027818/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36941263/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=Meta-analysis%20of%20the%20space%20flight%20and%20microgravity%20response%20of%20the%20Arabidopsis%20plant%20transcriptome&author=R.%20Barker&author=C.%20P.%20S.%20Kruse&author=C.%20Johnson&author=A.%20Saravia-Butler&author=H.%20Fogle&volume=9&issue=1&publication_year=2023&pages=21&pmid=36941263&doi=10.1038/s41526-023-00247-6&)]
6. Blighe K., Lun A. (2023) PCAtools: PCAtools: Everything Principal Components Analysis. Available at: <https://bioconductor.org/packages/PCAtools>.
7. Bresso E. G., Chorostecki U., Rodriguez R. E., Palatnik J. F., Schommer C. (2018). Spatial control of gene expression by miR319-regulated TCP transcription factors in leaf development. Plant Physiol.
   176 (2), 1694–1708. doi:  10.1104/pp.17.00823
    [[DOI](https://doi.org/10.1104/pp.17.00823)] [[PMC free article](/articles/PMC5813565/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29133375/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Physiol.&title=Spatial%20control%20of%20gene%20expression%20by%20miR319-regulated%20TCP%20transcription%20factors%20in%20leaf%20development&author=E.%20G.%20Bresso&author=U.%20Chorostecki&author=R.%20E.%20Rodriguez&author=J.%20F.%20Palatnik&author=C.%20Schommer&volume=176&issue=2&publication_year=2018&pages=1694-1708&pmid=29133375&doi=10.1104/pp.17.00823&)]
8. Brinckmann E. (1999). Spaceflight opportunities on the ISS for plant research–the ESA perspective. Adv. space Res.
   24 (6), 779–788. doi:  10.1016/s0273-1177(99)00413-5
    [[DOI](https://doi.org/10.1016/s0273-1177%2899%2900413-5)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11542623/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Adv.%20space%20Res.&title=Spaceflight%20opportunities%20on%20the%20ISS%20for%20plant%20research%E2%80%93the%20ESA%20perspective&author=E.%20Brinckmann&volume=24&issue=6&publication_year=1999&pages=779-788&pmid=11542623&doi=10.1016/s0273-1177(99)00413-5&)]
9. Cancé C., Martin-Arevalillo R., Boubekeur K., Dumas R. (2022). “Auxin response factors are keys to the many auxin doors,” in New Phytologist, vol. 235. (John Wiley & Sons, Ltd; ), 402–419. doi:  10.1111/nph.18159
    [[DOI](https://doi.org/10.1111/nph.18159)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/35434800/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=New%20Phytologist&author=C.%20Canc%C3%A9&author=R.%20Martin-Arevalillo&author=K.%20Boubekeur&author=R.%20Dumas&publication_year=2022&)]
10. Chae K., Isaacs C. G., Reeves P. H., Maloney G. S., Muday G. K., Nagpal P., et al. (2012). “Arabidopsis SMALL AUXIN UP RNA63 promotes hypocotyl and stamen filament elongation,” in The Plant Journal, vol. 71. (John Wiley & Sons, Ltd; ), 684–697. doi:  10.1111/j.1365-313X.2012.05024.x
     [[DOI](https://doi.org/10.1111/j.1365-313X.2012.05024.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22507274/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The%20Plant%20Journal&author=K.%20Chae&author=C.%20G.%20Isaacs&author=P.%20H.%20Reeves&author=G.%20S.%20Maloney&author=G.%20K.%20Muday&publication_year=2012&)]
11. Cheng C.-Y., Krishnakumar V., Chan A. P., Thibaud-Nissen F., Schobel S., Town C. D. (2017). Araport11: a complete reannotation of the Arabidopsis thaliana reference genome. Plant J.
    89 (4), 789–804. doi:  10.1111/tpj.13415
     [[DOI](https://doi.org/10.1111/tpj.13415)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27862469/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20J.&title=Araport11:%20a%20complete%20reannotation%20of%20the%20Arabidopsis%20thaliana%20reference%20genome&author=C.-Y.%20Cheng&author=V.%20Krishnakumar&author=A.%20P.%20Chan&author=F.%20Thibaud-Nissen&author=S.%20Schobel&volume=89&issue=4&publication_year=2017&pages=789-804&pmid=27862469&doi=10.1111/tpj.13415&)]
12. Choi W. G., Barker R. J., Kim S. H., Swanson S. J., Gilroy S. (2019). Variation in the transcriptome of different ecotypes of Arabidopsis thaliana reveals signatures of oxidative stress in plant responses to spaceflight. Am. J. Bot.
    106 (1), 123–136. doi:  10.1002/ajb2.1223
     [[DOI](https://doi.org/10.1002/ajb2.1223)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30644539/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Bot.&title=Variation%20in%20the%20transcriptome%20of%20different%20ecotypes%20of%20Arabidopsis%20thaliana%20reveals%20signatures%20of%20oxidative%20stress%20in%20plant%20responses%20to%20spaceflight&author=W.%20G.%20Choi&author=R.%20J.%20Barker&author=S.%20H.%20Kim&author=S.%20J.%20Swanson&author=S.%20Gilroy&volume=106&issue=1&publication_year=2019&pages=123-136&pmid=30644539&doi=10.1002/ajb2.1223&)]
13. Cui D., Zhao J., Jing Y., Fan M., Liu J., Wang Z., et al. (2013). The arabidopsis IDD14, IDD15, and IDD16 cooperatively regulate lateral organ morphogenesis and gravitropism by promoting Auxin biosynthesis and transport. PLoS Genet.
    9 (9), e1003759. doi:  10.1371/journal.pgen.1003759
     [[DOI](https://doi.org/10.1371/journal.pgen.1003759)] [[PMC free article](/articles/PMC3764202/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24039602/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20Genet.&title=The%20arabidopsis%20IDD14,%20IDD15,%20and%20IDD16%20cooperatively%20regulate%20lateral%20organ%20morphogenesis%20and%20gravitropism%20by%20promoting%20Auxin%20biosynthesis%20and%20transport&author=D.%20Cui&author=J.%20Zhao&author=Y.%20Jing&author=M.%20Fan&author=J.%20Liu&volume=9&issue=9&publication_year=2013&pages=e1003759&pmid=24039602&doi=10.1371/journal.pgen.1003759&)]
14. Davis I. W., Benninger C., Benfey P. N., Elich T. (2012). POWRS: position-sensitive motif discovery. PLoS One
    7 (7), e40373. doi:  10.1371/journal.pone.0040373
     [[DOI](https://doi.org/10.1371/journal.pone.0040373)] [[PMC free article](/articles/PMC3390389/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22792292/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=POWRS:%20position-sensitive%20motif%20discovery&author=I.%20W.%20Davis&author=C.%20Benninger&author=P.%20N.%20Benfey&author=T.%20Elich&volume=7&issue=7&publication_year=2012&pages=e40373&pmid=22792292&doi=10.1371/journal.pone.0040373&)]
15. De Micco V., Amitrano C., Mastroleo F., Aronne G., Battistelli A., Carnero-Diaz E., et al. (2023). Plant and microbial science and technology as cornerstones to Bioregenerative Life Support Systems in space. NPJ Microgravity
    9 (1), 69. doi:  10.1038/s41526-023-00317-9
     [[DOI](https://doi.org/10.1038/s41526-023-00317-9)] [[PMC free article](/articles/PMC10449850/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/37620398/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=Plant%20and%20microbial%20science%20and%20technology%20as%20cornerstones%20to%20Bioregenerative%20Life%20Support%20Systems%20in%20space&author=V.%20De%20Micco&author=C.%20Amitrano&author=F.%20Mastroleo&author=G.%20Aronne&author=A.%20Battistelli&volume=9&issue=1&publication_year=2023&pages=69&pmid=37620398&doi=10.1038/s41526-023-00317-9&)]
16. Dong J., Sun N., Yang J., Deng Z., Lan J., Qin G., et al. (2019). The transcription factors TCP4 and PIF3 antagonistically regulate organ-specific light induction of SAUR genes to modulate cotyledon opening during de-etiolation in Arabidopsis. Plant Cell
    31 (5), 1155–1170. doi:  10.1105/tpc.18.00803
     [[DOI](https://doi.org/10.1105/tpc.18.00803)] [[PMC free article](/articles/PMC6533013/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30914467/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell&title=The%20transcription%20factors%20TCP4%20and%20PIF3%20antagonistically%20regulate%20organ-specific%20light%20induction%20of%20SAUR%20genes%20to%20modulate%20cotyledon%20opening%20during%20de-etiolation%20in%20Arabidopsis&author=J.%20Dong&author=N.%20Sun&author=J.%20Yang&author=Z.%20Deng&author=J.%20Lan&volume=31&issue=5&publication_year=2019&pages=1155-1170&pmid=30914467&doi=10.1105/tpc.18.00803&)]
17. Ferl R. J., Koh J., Denison F., Paul A.-L. (2014). “Spaceflight induces specific alterations in the proteomes of arabidopsis,” in Astrobiology, vol. 15. (Mary Ann Liebert, Inc., publishers; ), 32–56. doi:  10.1089/ast.2014.1210
     [[DOI](https://doi.org/10.1089/ast.2014.1210)] [[PMC free article](/articles/PMC4290804/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25517942/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Astrobiology&author=R.%20J.%20Ferl&author=J.%20Koh&author=F.%20Denison&author=A.-L.%20Paul&publication_year=2014&)]
18. Fu Y., Li L., Xie B., Dong C., Wang M., Jia B., et al. (2016). “How to establish a bioregenerative life support system for long-term crewed missions to the moon or mars,” in Astrobiology, vol. 16. (United States: ), 925–936. doi:  10.1089/ast.2016.1477
     [[DOI](https://doi.org/10.1089/ast.2016.1477)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27912029/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Astrobiology&author=Y.%20Fu&author=L.%20Li&author=B.%20Xie&author=C.%20Dong&author=M.%20Wang&publication_year=2016&)]
19. Gangappa S. N., Botto J. F. (2016). The multifaceted roles of HY5 in plant growth and development. Mol. Plant
    9 (10), 1353–1365. doi:  10.1016/j.molp.2016.07.002
     [[DOI](https://doi.org/10.1016/j.molp.2016.07.002)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27435853/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol.%20Plant&title=The%20multifaceted%20roles%20of%20HY5%20in%20plant%20growth%20and%20development&author=S.%20N.%20Gangappa&author=J.%20F.%20Botto&volume=9&issue=10&publication_year=2016&pages=1353-1365&pmid=27435853&doi=10.1016/j.molp.2016.07.002&)]
20. Herranz R., Vandenbrink J. P., Villacampa A., Manzano A., Poehlman W. L., Feltus F. A., et al. (2019). RNAseq analysis of the response of Arabidopsis thaliana to fractional gravity under blue-light stimulation during spaceflight. Front. Plant Sci.
    10, 1–11. doi:  10.3389/fpls.2019.01529
     [[DOI](https://doi.org/10.3389/fpls.2019.01529)] [[PMC free article](/articles/PMC6889863/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31850027/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=RNAseq%20analysis%20of%20the%20response%20of%20Arabidopsis%20thaliana%20to%20fractional%20gravity%20under%20blue-light%20stimulation%20during%20spaceflight&author=R.%20Herranz&author=J.%20P.%20Vandenbrink&author=A.%20Villacampa&author=A.%20Manzano&author=W.%20L.%20Poehlman&volume=10&publication_year=2019&pages=1-11&pmid=31850027&doi=10.3389/fpls.2019.01529&)]
21. Hou K., Wu W., Gan S.-S. (2013). SAUR36, a SMALL AUXIN UP RNA gene, is involved in the promotion of leaf senescence in Arabidopsis. Plant Physiol.
    161 (2), 1002–1009. doi:  10.1104/pp.112.212787
     [[DOI](https://doi.org/10.1104/pp.112.212787)] [[PMC free article](/articles/PMC3560998/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23250625/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Physiol.&title=SAUR36,%20a%20SMALL%20AUXIN%20UP%20RNA%20gene,%20is%20involved%20in%20the%20promotion%20of%20leaf%20senescence%20in%20Arabidopsis&author=K.%20Hou&author=W.%20Wu&author=S.-S.%20Gan&volume=161&issue=2&publication_year=2013&pages=1002-1009&pmid=23250625&doi=10.1104/pp.112.212787&)]
22. Hwang I., Robinson D. G. (2009). Transport vesicle formation in plant cells. Curr. Opin. Plant Biol.
    12 (6), 660–669. doi:  10.1016/j.pbi.2009.09.012
     [[DOI](https://doi.org/10.1016/j.pbi.2009.09.012)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19854098/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Opin.%20Plant%20Biol.&title=Transport%20vesicle%20formation%20in%20plant%20cells&author=I.%20Hwang&author=D.%20G.%20Robinson&volume=12&issue=6&publication_year=2009&pages=660-669&pmid=19854098&doi=10.1016/j.pbi.2009.09.012&)]
23. Irshad M., Canut H., Borderies G., Pont-Lezica R., Jamet E. (2008). A new picture of cell wall protein dynamics in elongating cells of Arabidopsis thaliana: Confirmed actors and newcomers. BMC Plant Biol.
    8 (1), 94. doi:  10.1186/1471-2229-8-94
     [[DOI](https://doi.org/10.1186/1471-2229-8-94)] [[PMC free article](/articles/PMC2551616/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18796151/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=A%20new%20picture%20of%20cell%20wall%20protein%20dynamics%20in%20elongating%20cells%20of%20Arabidopsis%20thaliana:%20Confirmed%20actors%20and%20newcomers&author=M.%20Irshad&author=H.%20Canut&author=G.%20Borderies&author=R.%20Pont-Lezica&author=E.%20Jamet&volume=8&issue=1&publication_year=2008&pages=94&pmid=18796151&doi=10.1186/1471-2229-8-94&)]
24. Johnson C. M., Subramanian A., Pattathil S., Correll M. J., Kiss J. Z. (2017). Comparative transcriptomics indicate changes in cell wall organization and stress response in seedlings during spaceflight. Am. J. Bot.
    104 (8), 1219–1231. doi:  10.3732/ajb.1700079
     [[DOI](https://doi.org/10.3732/ajb.1700079)] [[PMC free article](/articles/PMC5821596/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28827451/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Bot.&title=Comparative%20transcriptomics%20indicate%20changes%20in%20cell%20wall%20organization%20and%20stress%20response%20in%20seedlings%20during%20spaceflight&author=C.%20M.%20Johnson&author=A.%20Subramanian&author=S.%20Pattathil&author=M.%20J.%20Correll&author=J.%20Z.%20Kiss&volume=104&issue=8&publication_year=2017&pages=1219-1231&pmid=28827451&doi=10.3732/ajb.1700079&)]
25. Kim D., Paggi J. M., Park C., Bennett C., Salzberg S. L. (2019). Graph-based genome alignment and genotyping with HISAT2 and HISAT-genotype. Nat. Biotechnol.
    37 (8), 907–915. doi:  10.1038/s41587-019-0201-4
     [[DOI](https://doi.org/10.1038/s41587-019-0201-4)] [[PMC free article](/articles/PMC7605509/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31375807/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=Graph-based%20genome%20alignment%20and%20genotyping%20with%20HISAT2%20and%20HISAT-genotype&author=D.%20Kim&author=J.%20M.%20Paggi&author=C.%20Park&author=C.%20Bennett&author=S.%20L.%20Salzberg&volume=37&issue=8&publication_year=2019&pages=907-915&pmid=31375807&doi=10.1038/s41587-019-0201-4&)]
26. Kiss J. Z., Kumar P., Millar K. D.L., Edelmann R. E., Correll M. J. (2009). Operations of a spaceflight experiment to investigate plant tropisms. Adv. Space Res.
    44 (8), 879–886. doi:  10.1016/j.asr.2009.06.007
     [[DOI](https://doi.org/10.1016/j.asr.2009.06.007)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Adv.%20Space%20Res.&title=Operations%20of%20a%20spaceflight%20experiment%20to%20investigate%20plant%20tropisms&author=J.%20Z.%20Kiss&author=P.%20Kumar&author=K.%20D.L.%20Millar&author=R.%20E.%20Edelmann&author=M.%20J.%20Correll&volume=44&issue=8&publication_year=2009&pages=879-886&doi=10.1016/j.asr.2009.06.007&)]
27. Kittang A.-I., Iversen T.-H., Fossum K. R., Mazars C., Carnero-Diaz E., Boucheron-Dubuisson E., et al. (2014). Exploration of plant growth and development using the European Modular Cultivation System facility on the International Space Station. Plant Biol. (Stuttgart Germany)
    16 (3), 528–538. doi:  10.1111/plb.12132
     [[DOI](https://doi.org/10.1111/plb.12132)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24433330/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Biol.%20(Stuttgart%20Germany)&title=Exploration%20of%20plant%20growth%20and%20development%20using%20the%20European%20Modular%20Cultivation%20System%20facility%20on%20the%20International%20Space%20Station&author=A.-I.%20Kittang&author=T.-H.%20Iversen&author=K.%20R.%20Fossum&author=C.%20Mazars&author=E.%20Carnero-Diaz&volume=16&issue=3&publication_year=2014&pages=528-538&pmid=24433330&doi=10.1111/plb.12132&)]
28. Kruse C. P. S., Meyers A. D., Basu P., Hutchinson S., Luesse D. R., Wyatt S. E. (2020). Spaceflight induces novel regulatory responses in Arabidopsis seedling as revealed by combined proteomic and transcriptomic analyses. BMC Plant Biol.
    20 (1), 237. doi:  10.1186/s12870-020-02392-6
     [[DOI](https://doi.org/10.1186/s12870-020-02392-6)] [[PMC free article](/articles/PMC7251690/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32460700/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=Spaceflight%20induces%20novel%20regulatory%20responses%20in%20Arabidopsis%20seedling%20as%20revealed%20by%20combined%20proteomic%20and%20transcriptomic%20analyses&author=C.%20P.%20S.%20Kruse&author=A.%20D.%20Meyers&author=P.%20Basu&author=S.%20Hutchinson&author=D.%20R.%20Luesse&volume=20&issue=1&publication_year=2020&pages=237&pmid=32460700&doi=10.1186/s12870-020-02392-6&)]
29. Kwon T., Sparks J. A., Nakashima J., Allen S. N., Tang Y., Blancaflor E. B. (2015). “Transcriptional response of Arabidopsis seedlings during spaceflight reveals peroxidase and cell wall remodeling genes associated with root hair development,” in American Journal of Botany, vol. 102. (John Wiley & Sons, Ltd; ), 21–35. doi:  10.3732/ajb.1400458
     [[DOI](https://doi.org/10.3732/ajb.1400458)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25587145/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=American%20Journal%20of%20Botany&author=T.%20Kwon&author=J.%20A.%20Sparks&author=J.%20Nakashima&author=S.%20N.%20Allen&author=Y.%20Tang&publication_year=2015&)]
30. Lamesch P., Berardini T. Z., Li D., Swarbreck D., Wilks C., Sasidharan R., et al. (2012). The Arabidopsis Information Resource (TAIR): improved gene annotation and new tools. Nucleic Acids Res.
    40 (D1), D1202–D1210. doi:  10.1093/nar/gkr1090
     [[DOI](https://doi.org/10.1093/nar/gkr1090)] [[PMC free article](/articles/PMC3245047/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22140109/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=The%20Arabidopsis%20Information%20Resource%20(TAIR):%20improved%20gene%20annotation%20and%20new%20tools&author=P.%20Lamesch&author=T.%20Z.%20Berardini&author=D.%20Li&author=D.%20Swarbreck&author=C.%20Wilks&volume=40&issue=D1&publication_year=2012&pages=D1202-D1210&pmid=22140109&doi=10.1093/nar/gkr1090&)]
31. Lee J., He K., Stolc V., Lee H., Figueroa P., Gao Y., et al. (2007). Analysis of transcription factor HY5 genomic binding sites revealed its hierarchical role in light regulation of development. Plant Cell
    19 (3), 731–749. doi:  10.1105/tpc.106.047688
     [[DOI](https://doi.org/10.1105/tpc.106.047688)] [[PMC free article](/articles/PMC1867377/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17337630/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell&title=Analysis%20of%20transcription%20factor%20HY5%20genomic%20binding%20sites%20revealed%20its%20hierarchical%20role%20in%20light%20regulation%20of%20development&author=J.%20Lee&author=K.%20He&author=V.%20Stolc&author=H.%20Lee&author=P.%20Figueroa&volume=19&issue=3&publication_year=2007&pages=731-749&pmid=17337630&doi=10.1105/tpc.106.047688&)]
32. Li S. (2015). “The Arabidopsis thaliana TCP transcription factors: A broadening horizon beyond development,” in Plant Signaling & Behavior, vol. 10. (Taylor & Francis; ). doi:  10.1080/15592324.2015.1044192
     [[DOI](https://doi.org/10.1080/15592324.2015.1044192)] [[PMC free article](/articles/PMC4622585/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26039357/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Plant%20Signaling%20&%20Behavior&author=S.%20Li&publication_year=2015&)]
33. Li Y., Han S., Qi Y. (2023). “Advances in structure and function of auxin response factor in plants,” in Journal of Integrative Plant Biology, vol. 65. (John Wiley & Sons, Ltd; ), 617–632. doi:  10.1111/jipb.13392
     [[DOI](https://doi.org/10.1111/jipb.13392)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36263892/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Journal%20of%20Integrative%20Plant%20Biology&author=Y.%20Li&author=S.%20Han&author=Y.%20Qi&publication_year=2023&)]
34. Love M. I., Huber W., Anders S. (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol.
    15 (12), 550. doi:  10.1186/s13059-014-0550-8
     [[DOI](https://doi.org/10.1186/s13059-014-0550-8)] [[PMC free article](/articles/PMC4302049/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25516281/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genome%20Biol.&title=Moderated%20estimation%20of%20fold%20change%20and%20dispersion%20for%20RNA-seq%20data%20with%20DESeq2&author=M.%20I.%20Love&author=W.%20Huber&author=S.%20Anders&volume=15&issue=12&publication_year=2014&pages=550&pmid=25516281&doi=10.1186/s13059-014-0550-8&)]
35. Ma X., Yan H., Yang J., Liu Y., Li Z., Sheng M., et al. (2022). PlantGSAD: a comprehensive gene set annotation database for plant species. Nucleic Acids Res.
    50 (D1), D1456–D1467. doi:  10.1093/nar/gkab794
     [[DOI](https://doi.org/10.1093/nar/gkab794)] [[PMC free article](/articles/PMC8728169/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34534340/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=PlantGSAD:%20a%20comprehensive%20gene%20set%20annotation%20database%20for%20plant%20species&author=X.%20Ma&author=H.%20Yan&author=J.%20Yang&author=Y.%20Liu&author=Z.%20Li&volume=50&issue=D1&publication_year=2022&pages=D1456-D1467&pmid=34534340&doi=10.1093/nar/gkab794&)]
36. Manzano A., Carnero-Diaz E., Herranz R., Medina F. J. (2022). Recent transcriptomic studies to elucidate the plant adaptive response to spaceflight and to simulated space environments. iScience
    25 (8), 104687. doi:  10.1016/j.isci.2022.104687
     [[DOI](https://doi.org/10.1016/j.isci.2022.104687)] [[PMC free article](/articles/PMC9287483/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/35856037/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=iScience&title=Recent%20transcriptomic%20studies%20to%20elucidate%20the%20plant%20adaptive%20response%20to%20spaceflight%20and%20to%20simulated%20space%20environments&author=A.%20Manzano&author=E.%20Carnero-Diaz&author=R.%20Herranz&author=F.%20J.%20Medina&volume=25&issue=8&publication_year=2022&pages=104687&pmid=35856037&doi=10.1016/j.isci.2022.104687&)]
37. Markakis M. N., Boron A. K., Van Loock B., Saini K., Cirera S., Verbelen J.-P., et al. (2013). Characterization of a small Auxin-up RNA (SAUR)-like gene involved in Arabidopsis thaliana development. PloS One
    8 (11), e82596. doi:  10.1371/journal.pone.0082596
     [[DOI](https://doi.org/10.1371/journal.pone.0082596)] [[PMC free article](/articles/PMC3842426/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24312429/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20One&title=Characterization%20of%20a%20small%20Auxin-up%20RNA%20(SAUR)-like%20gene%20involved%20in%20Arabidopsis%20thaliana%20development&author=M.%20N.%20Markakis&author=A.%20K.%20Boron&author=B.%20Van%20Loock&author=K.%20Saini&author=S.%20Cirera&volume=8&issue=11&publication_year=2013&pages=e82596&pmid=24312429&doi=10.1371/journal.pone.0082596&)]
38. Martin M. (2011). Cutadapt removes adapter sequences from high-throughput sequencing reads. EMBnet. journal
    17 (1), 10–12. doi:  10.14806/ej.17.1.200. *Next Generation Sequencing Data Analysis*. [[DOI](https://doi.org/10.14806/ej.17.1.200)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=EMBnet.%20journal&title=Cutadapt%20removes%20adapter%20sequences%20from%20high-throughput%20sequencing%20reads&author=M.%20Martin&volume=17&issue=1&publication_year=2011&doi=10.14806/ej.17.1.200&)]
39. Mazars C., Brière C., Grat S., Pichereaux C., Rossignol M., Pereda-Loth V., et al. (2014). “Microsome-associated proteome modifications of Arabidopsis seedlings grown on board the International Space Station reveal the possible effect on plants of space stresses other than microgravity,” in Plant Signaling & Behavior. 9, e29637. doi:  10.4161/psb.29637
     [[DOI](https://doi.org/10.4161/psb.29637)] [[PMC free article](/articles/PMC4205128/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25763699/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Signaling%20&%20Behavior&title=Microsome-associated%20proteome%20modifications%20of%20Arabidopsis%20seedlings%20grown%20on%20board%20the%20International%20Space%20Station%20reveal%20the%20possible%20effect%20on%20plants%20of%20space%20stresses%20other%20than%20microgravity&author=C.%20Mazars&author=C.%20Bri%C3%A8re&author=S.%20Grat&author=C.%20Pichereaux&author=M.%20Rossignol&volume=9&publication_year=2014&pages=e29637&pmid=25763699&doi=10.4161/psb.29637&)]
40. Meng Y., Shao C., Ma X., Wang H., Chen M. (2012). Expression-based functional investigation of the organ-specific microRNAs in Arabidopsis. PloS One
    7 (11), e50870. doi:  10.1371/journal.pone.0050870
     [[DOI](https://doi.org/10.1371/journal.pone.0050870)] [[PMC free article](/articles/PMC3511311/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23226412/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20One&title=Expression-based%20functional%20investigation%20of%20the%20organ-specific%20microRNAs%20in%20Arabidopsis&author=Y.%20Meng&author=C.%20Shao&author=X.%20Ma&author=H.%20Wang&author=M.%20Chen&volume=7&issue=11&publication_year=2012&pages=e50870&pmid=23226412&doi=10.1371/journal.pone.0050870&)]
41. Millar K. D. L., Kumar P., Correll M. J., Mullen J. L., Hangarter R. P., Edelmann R. E., et al. (2010). “A novel phototropic response to red light is revealed in microgravity,” in The New phytologist, vol. 186. (England: ), 648–656. doi:  10.1111/j.1469-8137.2010.03211.x
     [[DOI](https://doi.org/10.1111/j.1469-8137.2010.03211.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20298479/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The%20New%20phytologist&author=K.%20D.%20L.%20Millar&author=P.%20Kumar&author=M.%20J.%20Correll&author=J.%20L.%20Mullen&author=R.%20P.%20Hangarter&publication_year=2010&)]
42. Mizukami Y., Fischer R. L. (2000). “Plant organ size control: AINTEGUMENTA regulates growth and cell numbers during organogenesis,” in Proceedings of the National Academy of Sciences of the United States of America, United States, Vol. 97. 942–947. doi:  10.1073/pnas.97.2.942
     [[DOI](https://doi.org/10.1073/pnas.97.2.942)] [[PMC free article](/articles/PMC15435/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/10639184/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?Mizukami%20Y.,%20Fischer%20R.%20L.%20(2000).%20%E2%80%9CPlant%20organ%20size%20control:%20AINTEGUMENTA%20regulates%20growth%20and%20cell%20numbers%20during%20organogenesis,%E2%80%9D%20in%20Proceedings%20of%20the%20National%20Academy%20of%20Sciences%20of%20the%20United%20States%20of%20America,%20United%20States,%20Vol.%2097.%20942%E2%80%93947.%20doi:%C2%A0%2010.1073/pnas.97.2.942)]
43. Molina C., Grotewold E. (2005). Genome wide analysis of Arabidopsis core promoters. BMC Genomics
    6 (1), 25. doi:  10.1186/1471-2164-6-25
     [[DOI](https://doi.org/10.1186/1471-2164-6-25)] [[PMC free article](/articles/PMC554773/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15733318/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Genomics&title=Genome%20wide%20analysis%20of%20Arabidopsis%20core%20promoters&author=C.%20Molina&author=E.%20Grotewold&volume=6&issue=1&publication_year=2005&pages=25&pmid=15733318&doi=10.1186/1471-2164-6-25&)]
44. Morita M. T., Sakaguchi K., Kiyose S., Taira K., Kato T., Nakamura M., et al. (2006). “A C2H2-type zinc finger protein, SGR5, is involved in early events of gravitropism in Arabidopsis inflorescence stems,” in The Plant Journal, vol. 47. (John Wiley & Sons, Ltd; ), 619–628. doi:  10.1111/j.1365-313X.2006.02807.x
     [[DOI](https://doi.org/10.1111/j.1365-313X.2006.02807.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16813575/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The%20Plant%20Journal&author=M.%20T.%20Morita&author=K.%20Sakaguchi&author=S.%20Kiyose&author=K.%20Taira&author=T.%20Kato&publication_year=2006&)]
45. Nakashima J., Pattathil S., Avci U., Chin S., Alan Sparks J., Hahn M. G., et al. (2023). Glycome profiling and immunohistochemistry uncover changes in cell walls of Arabidopsis thaliana roots during spaceflight. NPJ Microgravity
    9 (1), 68. doi:  10.1038/s41526-023-00312-0
     [[DOI](https://doi.org/10.1038/s41526-023-00312-0)] [[PMC free article](/articles/PMC10444889/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/37608048/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=Glycome%20profiling%20and%20immunohistochemistry%20uncover%20changes%20in%20cell%20walls%20of%20Arabidopsis%20thaliana%20roots%20during%20spaceflight&author=J.%20Nakashima&author=S.%20Pattathil&author=U.%20Avci&author=S.%20Chin&author=J.%20Alan%20Sparks&volume=9&issue=1&publication_year=2023&pages=68&pmid=37608048&doi=10.1038/s41526-023-00312-0&)]
46. Naumann K., Fischer A., Hofmann I., Krauss V., Phalke S., Irmler K., et al. (2005). Pivotal role of AtSUVH2 in heterochromatic histone methylation and gene silencing in Arabidopsis. EMBO J.
    24 (7), 1418–1429. doi:  10.1038/sj.emboj.7600604
     [[DOI](https://doi.org/10.1038/sj.emboj.7600604)] [[PMC free article](/articles/PMC1142535/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15775980/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=EMBO%20J.&title=Pivotal%20role%20of%20AtSUVH2%20in%20heterochromatic%20histone%20methylation%20and%20gene%20silencing%20in%20Arabidopsis&author=K.%20Naumann&author=A.%20Fischer&author=I.%20Hofmann&author=V.%20Krauss&author=S.%20Phalke&volume=24&issue=7&publication_year=2005&pages=1418-1429&pmid=15775980&doi=10.1038/sj.emboj.7600604&)]
47. Ng D. W., Abeysinghe J. K., Kamali M. (2018). Regulating the regulators: the control of transcription factors in plant defense signaling. Int. J. Mol. Sci. doi:  10.3390/ijms19123737
     [[DOI](https://doi.org/10.3390/ijms19123737)] [[PMC free article](/articles/PMC6321093/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30477211/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci&title=Regulating%20the%20regulators:%20the%20control%20of%20transcription%20factors%20in%20plant%20defense%20signaling&author=D.%20W.%20Ng&author=J.%20K.%20Abeysinghe&author=M.%20Kamali&publication_year=2018&pmid=30477211&doi=10.3390/ijms19123737&)]
48. Nishimura T., Mori S., Shikata H., Nakamura M., Hashiguchi Y., Abe Y., et al. (2023). “Cell polarity linked to gravity sensing is generated by LZY translocation from statoliths to the plasma membrane,” in Science, vol. 381. (American Association for the Advancement of Science; ), 1006–1010. doi:  10.1126/science.adh9978
     [[DOI](https://doi.org/10.1126/science.adh9978)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/37561884/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Science&author=T.%20Nishimura&author=S.%20Mori&author=H.%20Shikata&author=M.%20Nakamura&author=Y.%20Hashiguchi&publication_year=2023&)]
49. Novillo F., Alonso J. M., Ecker J. R., Salinas J. (2004). “CBF2/DREB1C is a negative regulator of CBF1/DREB1B and CBF3/DREB1A expression and plays a central role in stress tolerance in Arabidopsis,” in Proceedings of the National Academy of Sciences, vol. 101. (National Acad Sciences; ), 3985–3990. [[DOI](https://doi.org/10.1073/pnas.0303029101)] [[PMC free article](/articles/PMC374356/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15004278/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Proceedings%20of%20the%20National%20Academy%20of%20Sciences&author=F.%20Novillo&author=J.%20M.%20Alonso&author=J.%20R.%20Ecker&author=J.%20Salinas&publication_year=2004&)]
50. Olanrewaju G. O., Kruse C. P. S., Wyatt S. E. (2023). Functional meta-analysis of the proteomic responses of Arabidopsis seedlings to the spaceflight environment reveals multi-dimensional sources of variability across spaceflight experiments. Int. J. Mol. Sci. doi:  10.3390/ijms241914425
     [[DOI](https://doi.org/10.3390/ijms241914425)] [[PMC free article](/articles/PMC10573023/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/37833871/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci&title=Functional%20meta-analysis%20of%20the%20proteomic%20responses%20of%20Arabidopsis%20seedlings%20to%20the%20spaceflight%20environment%20reveals%20multi-dimensional%20sources%20of%20variability%20across%20spaceflight%20experiments&author=G.%20O.%20Olanrewaju&author=C.%20P.%20S.%20Kruse&author=S.%20E.%20Wyatt&publication_year=2023&pmid=37833871&doi=10.3390/ijms241914425&)]
51. Paul A.-L., et al. (2013). ‘Organ-specific remodeling of the Arabidopsis transcriptome in response to spaceflight. BMC Plant Biol.
    13 (1), 112. doi:  10.1186/1471-2229-13-112
     [[DOI](https://doi.org/10.1186/1471-2229-13-112)] [[PMC free article](/articles/PMC3750915/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23919896/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=%E2%80%98Organ-specific%20remodeling%20of%20the%20Arabidopsis%20transcriptome%20in%20response%20to%20spaceflight&author=A.-L.%20Paul&volume=13&issue=1&publication_year=2013&pages=112&pmid=23919896&doi=10.1186/1471-2229-13-112&)]
52. Paul A. L., Zupanska A. K., Schultz E. R., Ferl R. J. (2017). Genetic dissection of the Arabidopsis spaceflight transcriptome: Are some responses dispensable for the physiological adaptation of plants to spaceflight? PLoS One
    12 (6), 1–24. doi:  10.1371/journal.pone.0180186
     [[DOI](https://doi.org/10.1371/journal.pone.0180186)] [[PMC free article](/articles/PMC5491145/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28662188/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Genetic%20dissection%20of%20the%20Arabidopsis%20spaceflight%20transcriptome:%20Are%20some%20responses%20dispensable%20for%20the%20physiological%20adaptation%20of%20plants%20to%20spaceflight&author=A.%20L.%20Paul&author=A.%20K.%20Zupanska&author=E.%20R.%20Schultz&author=R.%20J.%20Ferl&volume=12&issue=6&publication_year=2017&pages=1-24&pmid=28662188&doi=10.1371/journal.pone.0180186&)]
53. Paul A.-L., Haveman N., Califar B., Ferl R. J. (2021). ‘Epigenomic regulators elongator complex subunit 2 and methyltransferase 1 differentially condition the spaceflight response in Arabidopsis. Front. Plant Sci. 12. doi:  10.3389/fpls.2021.691790
     [[DOI](https://doi.org/10.3389/fpls.2021.691790)] [[PMC free article](/articles/PMC8475764/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34589093/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci&title=%E2%80%98Epigenomic%20regulators%20elongator%20complex%20subunit%202%20and%20methyltransferase%201%20differentially%20condition%20the%20spaceflight%20response%20in%20Arabidopsis&author=A.-L.%20Paul&author=N.%20Haveman&author=B.%20Califar&author=R.%20J.%20Ferl&volume=12&publication_year=2021&pmid=34589093&doi=10.3389/fpls.2021.691790&)]
54. Phukan U. J., Jeena G. S., Shukla R. K. (2016). WRKY transcription factors: molecular regulation and stress responses in plants. Front. Plant Sci.
    7, 760. doi:  10.3389/fpls.2016.00760
     [[DOI](https://doi.org/10.3389/fpls.2016.00760)] [[PMC free article](/articles/PMC4891567/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27375634/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=WRKY%20transcription%20factors:%20molecular%20regulation%20and%20stress%20responses%20in%20plants&author=U.%20J.%20Phukan&author=G.%20S.%20Jeena&author=R.%20K.%20Shukla&volume=7&publication_year=2016&pages=760&pmid=27375634&doi=10.3389/fpls.2016.00760&)]
55. Pruneda-Paz J. L., Breton G., Nagel D. H., Kang S. E., Bonaldi K., Doherty C. J., et al. (2014). A genome-scale resource for the functional characterization of Arabidopsis transcription factors. Cell Rep.
    8 (2), 622–632. doi:  10.1016/j.celrep.2014.06.033
     [[DOI](https://doi.org/10.1016/j.celrep.2014.06.033)] [[PMC free article](/articles/PMC4125603/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25043187/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Rep.&title=A%20genome-scale%20resource%20for%20the%20functional%20characterization%20of%20Arabidopsis%20transcription%20factors&author=J.%20L.%20Pruneda-Paz&author=G.%20Breton&author=D.%20H.%20Nagel&author=S.%20E.%20Kang&author=K.%20Bonaldi&volume=8&issue=2&publication_year=2014&pages=622-632&pmid=25043187&doi=10.1016/j.celrep.2014.06.033&)]
56. Rashotte A. M., Mason M. G., Hutchison C. E., Ferreira F. J., Schaller G. E., Kieber J. J. (2006). “A subset of Arabidopsis AP2 transcription factors mediates cytokinin responses in concert with a two-component pathway,” in Proceedings of the National Academy of Sciences of the United States of America, United States, Vol. 103. 11081–11085. doi:  10.1073/pnas.0602038103
     [[DOI](https://doi.org/10.1073/pnas.0602038103)] [[PMC free article](/articles/PMC1544176/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16832061/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?Rashotte%20A.%20M.,%20Mason%20M.%20G.,%20Hutchison%20C.%20E.,%20Ferreira%20F.%20J.,%20Schaller%20G.%20E.,%20Kieber%20J.%20J.%20(2006).%20%E2%80%9CA%20subset%20of%20Arabidopsis%20AP2%20transcription%20factors%20mediates%20cytokinin%20responses%20in%20concert%20with%20a%20two-component%20pathway,%E2%80%9D%20in%20Proceedings%20of%20the%20National%20Academy%20of%20Sciences%20of%20the%20United%20States%20of%20America,%20United%20States,%20Vol.%20103.%2011081%E2%80%9311085.%20doi:%C2%A0%2010.1073/pnas.0602038103)]
57. Reis R. S., Poirier Y. (2021). Making sense of the natural antisense transcript puzzle. Trends Plant Sci.
    26 (11), 1104–1115. doi:  10.1016/j.tplants.2021.07.004
     [[DOI](https://doi.org/10.1016/j.tplants.2021.07.004)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34303604/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Trends%20Plant%20Sci.&title=Making%20sense%20of%20the%20natural%20antisense%20transcript%20puzzle&author=R.%20S.%20Reis&author=Y.%20Poirier&volume=26&issue=11&publication_year=2021&pages=1104-1115&pmid=34303604&doi=10.1016/j.tplants.2021.07.004&)]
58. Ren H., Gray W. M. (2015). SAUR proteins as effectors of hormonal and environmental signals in plant growth. Mol. Plant
    8 (8), 1153–1164. doi:  10.1016/j.molp.2015.05.003
     [[DOI](https://doi.org/10.1016/j.molp.2015.05.003)] [[PMC free article](/articles/PMC5124491/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25983207/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol.%20Plant&title=SAUR%20proteins%20as%20effectors%20of%20hormonal%20and%20environmental%20signals%20in%20plant%20growth&author=H.%20Ren&author=W.%20M.%20Gray&volume=8&issue=8&publication_year=2015&pages=1153-1164&pmid=25983207&doi=10.1016/j.molp.2015.05.003&)]
59. Sang Q., Fan L., Liu T., Qiu Y., Du J., Mo B., et al. (2023). MicroRNA156 conditions auxin sensitivity to enable growth plasticity in response to environmental changes in Arabidopsis. Nat. Commun.
    14 (1), 1449. doi:  10.1038/s41467-023-36774-9
     [[DOI](https://doi.org/10.1038/s41467-023-36774-9)] [[PMC free article](/articles/PMC10033679/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36949101/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Commun.&title=MicroRNA156%20conditions%20auxin%20sensitivity%20to%20enable%20growth%20plasticity%20in%20response%20to%20environmental%20changes%20in%20Arabidopsis&author=Q.%20Sang&author=L.%20Fan&author=T.%20Liu&author=Y.%20Qiu&author=J.%20Du&volume=14&issue=1&publication_year=2023&pages=1449&pmid=36949101&doi=10.1038/s41467-023-36774-9&)]
60. Schön M., Töller A., Diezel C., Roth C., Westphal L., Wiermer M., et al. (2013). “Analyses of wrky18 wrky40 Plants Reveal Critical Roles of SA/EDS1 Signaling and Indole-Glucosinolate Biosynthesis for Golovinomyces orontii Resistance and a Loss-of Resistance Towards Pseudomonas syringae pv. tomato AvrRPS4,” in Molecular Plant-Microbe Interactions®, vol. 26. (Scientific Societies; ), 758–767. doi:  10.1094/MPMI-11-12-0265-R
     [[DOI](https://doi.org/10.1094/MPMI-11-12-0265-R)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23617415/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Molecular%20Plant-Microbe%20Interactions%C2%AE&author=M.%20Sch%C3%B6n&author=A.%20T%C3%B6ller&author=C.%20Diezel&author=C.%20Roth&author=L.%20Westphal&publication_year=2013&)]
61. Sheppard J., Land E. S., Toennisson T. A., Doherty C. J., Perera I. Y. (2021). Uncovering transcriptional responses to fractional gravity in Arabidopsis roots. Life. 11. doi:  10.3390/life11101010
     [[DOI](https://doi.org/10.3390/life11101010)] [[PMC free article](/articles/PMC8539686/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34685382/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Life&title=Uncovering%20transcriptional%20responses%20to%20fractional%20gravity%20in%20Arabidopsis%20roots&author=J.%20Sheppard&author=E.%20S.%20Land&author=T.%20A.%20Toennisson&author=C.%20J.%20Doherty&author=I.%20Y.%20Perera&volume=11&publication_year=2021&pmid=34685382&doi=10.3390/life11101010&)]
62. Shinozaki K., Yamaguchi-Shinozaki K. (2000). Molecular responses to dehydration and low temperature: differences and cross-talk between two stress signaling pathways. Curr. Opin. Plant Biol.
    3 (3), 217–223. doi:  10.1016/S1369-5266(00)80068-0
     [[DOI](https://doi.org/10.1016/S1369-5266%2800%2980068-0)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/10837265/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Opin.%20Plant%20Biol.&title=Molecular%20responses%20to%20dehydration%20and%20low%20temperature:%20differences%20and%20cross-talk%20between%20two%20stress%20signaling%20pathways&author=K.%20Shinozaki&author=K.%20Yamaguchi-Shinozaki&volume=3&issue=3&publication_year=2000&pages=217-223&pmid=10837265&doi=10.1016/S1369-5266(00)80068-0&)]
63. Song L., Huang S. C., Wise A., Castanon R., Nery J. R., Chen H., et al. (2016). “A transcription factor hierarchy defines an environmental stress response network,” in Science, vol. 354. (American Association for the Advancement of Science; ), aag1550. doi:  10.1126/science.aag1550
     [[DOI](https://doi.org/10.1126/science.aag1550)] [[PMC free article](/articles/PMC5217750/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27811239/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Science&author=L.%20Song&author=S.%20C.%20Huang&author=A.%20Wise&author=R.%20Castanon&author=J.%20R.%20Nery&publication_year=2016&)]
64. Song X., Li Y., Cao X., Qi Y. (2019). MicroRNAs and their regulatory roles in plant–environment interactions’, *annual review of plant biology*
    . Annu. Rev.
    70 (1), 489–525. doi:  10.1146/annurev-arplant-050718-100334
     [[DOI](https://doi.org/10.1146/annurev-arplant-050718-100334)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30848930/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Annu.%20Rev.&title=MicroRNAs%20and%20their%20regulatory%20roles%20in%20plant%E2%80%93environment%20interactions%E2%80%99,%20annual%20review%20of%20plant%20biology&author=X.%20Song&author=Y.%20Li&author=X.%20Cao&author=Y.%20Qi&volume=70&issue=1&publication_year=2019&pages=489-525&pmid=30848930&doi=10.1146/annurev-arplant-050718-100334&)]
65. Srivastava R., Kumar R. (2019). The expanding roles of APETALA2/Ethylene Responsive Factors and their potential applications in crop improvement. Briefings Funct. Genomics
    18 (4), 240–254. doi:  10.1093/bfgp/elz001
     [[DOI](https://doi.org/10.1093/bfgp/elz001)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30783669/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Briefings%20Funct.%20Genomics&title=The%20expanding%20roles%20of%20APETALA2/Ethylene%20Responsive%20Factors%20and%20their%20potential%20applications%20in%20crop%20improvement&author=R.%20Srivastava&author=R.%20Kumar&volume=18&issue=4&publication_year=2019&pages=240-254&pmid=30783669&doi=10.1093/bfgp/elz001&)]
66. Stamm P., Kumar P. P. (2013). Auxin and gibberellin responsive Arabidopsis SMALL AUXIN UP RNA36 regulates hypocotyl elongation in the light. Plant Cell Rep.
    32 (6), 759–769. doi:  10.1007/s00299-013-1406-5
     [[DOI](https://doi.org/10.1007/s00299-013-1406-5)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23503980/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell%20Rep.&title=Auxin%20and%20gibberellin%20responsive%20Arabidopsis%20SMALL%20AUXIN%20UP%20RNA36%20regulates%20hypocotyl%20elongation%20in%20the%20light&author=P.%20Stamm&author=P.%20P.%20Kumar&volume=32&issue=6&publication_year=2013&pages=759-769&pmid=23503980&doi=10.1007/s00299-013-1406-5&)]
67. Sun N., Wang J., Gao Z., Dong J., He H., Terzaghi W., et al. (2016). “Arabidopsis SAURs are critical for differential light regulation of the development of various organs,” in Proceedings of the National Academy of Sciences of the United States of America, United States, Vol. 113. 6071–6076. doi:  10.1073/pnas.1604782113
     [[DOI](https://doi.org/10.1073/pnas.1604782113)] [[PMC free article](/articles/PMC4889401/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27118848/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?Sun%20N.,%20Wang%20J.,%20Gao%20Z.,%20Dong%20J.,%20He%20H.,%20Terzaghi%20W.,%20et%20al.%20(2016).%20%E2%80%9CArabidopsis%20SAURs%20are%20critical%20for%20differential%20light%20regulation%20of%20the%20development%20of%20various%20organs,%E2%80%9D%20in%20Proceedings%20of%20the%20National%20Academy%20of%20Sciences%20of%20the%20United%20States%20of%20America,%20United%20States,%20Vol.%20113.%206071%E2%80%936076.%20doi:%C2%A0%2010.1073/pnas.1604782113)]
68. Taniguchi M., Nakamura M., Tasaka M., Morita M. T. (2014). “Identification of gravitropic response indicator genes in Arabidopsis inflorescence stems,” in Plant Signaling & Behavior, vol. 9. (Taylor & Francis; ). doi:  10.4161/psb.29570
     [[DOI](https://doi.org/10.4161/psb.29570)] [[PMC free article](/articles/PMC4203507/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25763694/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Plant%20Signaling%20&%20Behavior&author=M.%20Taniguchi&author=M.%20Nakamura&author=M.%20Tasaka&author=M.%20T.%20Morita&publication_year=2014&)]
69. Tanimoto M., Tremblay R., Colasanti J. (2008). Altered gravitropic response, amyloplast sedimentation and circumnutation in the Arabidopsisshoot gravitropism 5 mutant are associated with reduced starch levels. Plant Mol. Biol.
    67 (1), 57–69. doi:  10.1007/s11103-008-9301-0
     [[DOI](https://doi.org/10.1007/s11103-008-9301-0)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18259878/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Mol.%20Biol.&title=Altered%20gravitropic%20response,%20amyloplast%20sedimentation%20and%20circumnutation%20in%20the%20Arabidopsisshoot%20gravitropism%205%20mutant%20are%20associated%20with%20reduced%20starch%20levels&author=M.%20Tanimoto&author=R.%20Tremblay&author=J.%20Colasanti&volume=67&issue=1&publication_year=2008&pages=57-69&pmid=18259878&doi=10.1007/s11103-008-9301-0&)]
70. Thomas P. D., Ebert D., Muruganujan A., Mushayahama T., Albou L.-P., Mi H. (2022). “PANTHER: Making genome-scale phylogenetics accessible to all,” in Protein Science, vol. 31. (John Wiley & Sons, Ltd; ), 8–22. doi:  10.1002/pro.4218
     [[DOI](https://doi.org/10.1002/pro.4218)] [[PMC free article](/articles/PMC8740835/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34717010/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Protein%20Science&author=P.%20D.%20Thomas&author=D.%20Ebert&author=A.%20Muruganujan&author=T.%20Mushayahama&author=L.-P.%20Albou&publication_year=2022&)]
71. Tian T., Liu Y., Yan H., You Q., Yi X., Du Z., et al. (2017). A’griGO v2.0: a GO analysis toolkit for the agricultural community 2017 update. Nucleic Acids Res.
    45 (W1), W122–W129. doi:  10.1093/nar/gkx382
     [[DOI](https://doi.org/10.1093/nar/gkx382)] [[PMC free article](/articles/PMC5793732/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28472432/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=A%E2%80%99griGO%20v2.0:%20a%20GO%20analysis%20toolkit%20for%20the%20agricultural%20community%202017%20update&author=T.%20Tian&author=Y.%20Liu&author=H.%20Yan&author=Q.%20You&author=X.%20Yi&volume=45&issue=W1&publication_year=2017&pages=W122-W129&pmid=28472432&doi=10.1093/nar/gkx382&)]
72. Tseng K.-C., Li G.-Z., Hung Y.-C., Chow C.-N., Wu N.-Y., Chien Y.-Y., et al. (2020). EXPath 2.0: an updated database for integrating high-throughput gene expression data with biological pathways. Plant Cell Physiol.
    61 (10), 1818–1827. doi:  10.1093/pcp/pcaa115
     [[DOI](https://doi.org/10.1093/pcp/pcaa115)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32898258/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell%20Physiol.&title=EXPath%202.0:%20an%20updated%20database%20for%20integrating%20high-throughput%20gene%20expression%20data%20with%20biological%20pathways&author=K.-C.%20Tseng&author=G.-Z.%20Li&author=Y.-C.%20Hung&author=C.-N.%20Chow&author=N.-Y.%20Wu&volume=61&issue=10&publication_year=2020&pages=1818-1827&pmid=32898258&doi=10.1093/pcp/pcaa115&)]
73. Vandenbrink J. P., Herranz R., Medina F. J., Edelmann R. E., Kiss J. Z. (2016). A novel blue-light phototropic response is revealed in roots of Arabidopsis thaliana in microgravity. Planta
    244 (6), 1201–1215. doi:  10.1007/s00425-016-2581-8
     [[DOI](https://doi.org/10.1007/s00425-016-2581-8)] [[PMC free article](/articles/PMC5748516/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27507239/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Planta&title=A%20novel%20blue-light%20phototropic%20response%20is%20revealed%20in%20roots%20of%20Arabidopsis%20thaliana%20in%20microgravity&author=J.%20P.%20Vandenbrink&author=R.%20Herranz&author=F.%20J.%20Medina&author=R.%20E.%20Edelmann&author=J.%20Z.%20Kiss&volume=244&issue=6&publication_year=2016&pages=1201-1215&pmid=27507239&doi=10.1007/s00425-016-2581-8&)]
74. Vandenbrink J. P., Herranz R., Poehlman W. L., Alex Feltus F., Villacampa A., Ciska M., et al. (2019). RNA-seq analyses of Arabidopsis thaliana seedlings after exposure to blue-light phototropic stimuli in microgravity. Am. J. Bot.
    106 (11), 1466–1476. doi:  10.1002/ajb2.1384
     [[DOI](https://doi.org/10.1002/ajb2.1384)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31709515/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Bot.&title=RNA-seq%20analyses%20of%20Arabidopsis%20thaliana%20seedlings%20after%20exposure%20to%20blue-light%20phototropic%20stimuli%20in%20microgravity&author=J.%20P.%20Vandenbrink&author=R.%20Herranz&author=W.%20L.%20Poehlman&author=F.%20Alex%20Feltus&author=A.%20Villacampa&volume=106&issue=11&publication_year=2019&pages=1466-1476&pmid=31709515&doi=10.1002/ajb2.1384&)]
75. Vandenbrink J. P., Kiss J. Z. (2019). “Preparation of a spaceflight experiment to study tropisms in arabidopsis seedlings on the international space station BT - phototropism: methods and protocols,” in Phototropism Methods and Protocols. Ed. Yamamoto K. T.(New York, NY:
    Springer New York; ), 207–214. doi:  10.1007/978-1-4939-9015-3\_17
     [[DOI](https://doi.org/10.1007/978-1-4939-9015-3_17)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30694478/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Phototropism%20Methods%20and%20Protocols&author=J.%20P.%20Vandenbrink&author=J.%20Z.%20Kiss&publication_year=2019&)]
76. Villacampa A., Ciska M., Manzano A., Vandenbrink J. P., Kiss J. Z., Herranz R., et al. (2021). From spaceflight to MARS G-levels: Adaptive response of a. thaliana seedlings in a reduced gravity environment is enhanced by red-light photostimulation. Int. J. Mol. Sci.
    22 (2), 1–27. doi:  10.3390/ijms22020899
     [[DOI](https://doi.org/10.3390/ijms22020899)] [[PMC free article](/articles/PMC7830483/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33477454/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci.&title=From%20spaceflight%20to%20MARS%20G-levels:%20Adaptive%20response%20of%20a.%20thaliana%20seedlings%20in%20a%20reduced%20gravity%20environment%20is%20enhanced%20by%20red-light%20photostimulation&author=A.%20Villacampa&author=M.%20Ciska&author=A.%20Manzano&author=J.%20P.%20Vandenbrink&author=J.%20Z.%20Kiss&volume=22&issue=2&publication_year=2021&pages=1-27&pmid=33477454&doi=10.3390/ijms22020899&)]
77. Viola I. L., Uberti Manassero N. G., Ripoll R., Gonzalez D. H. (2011). The Arabidopsis class I TCP transcription factor AtTCP11 is a developmental regulator with distinct DNA-binding properties due to the presence of a threonine residue at position 15 of the TCP domain. Biochem. J.
    435 (1), 143–155. doi:  10.1042/BJ20101019
     [[DOI](https://doi.org/10.1042/BJ20101019)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21241251/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Biochem.%20J.&title=The%20Arabidopsis%20class%20I%20TCP%20transcription%20factor%20AtTCP11%20is%20a%20developmental%20regulator%20with%20distinct%20DNA-binding%20properties%20due%20to%20the%20presence%20of%20a%20threonine%20residue%20at%20position%2015%20of%20the%20TCP%20domain&author=I.%20L.%20Viola&author=N.%20G.%20Uberti%20Manassero&author=R.%20Ripoll&author=D.%20H.%20Gonzalez&volume=435&issue=1&publication_year=2011&pages=143-155&pmid=21241251&doi=10.1042/BJ20101019&)]
78. Wang H., Wang H. (2015). The miR156/SPL Module, a Regulatory Hub and Versatile Toolbox, Gears up Crops for Enhanced Agronomic Traits. Mol. Plant
    8 (5), 677–688. doi:  10.1016/j.molp.2015.01.008
     [[DOI](https://doi.org/10.1016/j.molp.2015.01.008)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25617719/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol.%20Plant&title=The%20miR156/SPL%20Module,%20a%20Regulatory%20Hub%20and%20Versatile%20Toolbox,%20Gears%20up%20Crops%20for%20Enhanced%20Agronomic%20Traits&author=H.%20Wang&author=H.%20Wang&volume=8&issue=5&publication_year=2015&pages=677-688&pmid=25617719&doi=10.1016/j.molp.2015.01.008&)]
79. Wight M., Werner A. (2013). “The functions of natural antisense transcripts,” in Essays in Biochemistry, vol. 54 . Eds. Lindsay M. A., Griffiths-Jones S., 91–101. doi:  10.1042/bse0540091
     [[DOI](https://doi.org/10.1042/bse0540091)] [[PMC free article](/articles/PMC4284957/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23829529/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Essays%20in%20Biochemistry&author=M.%20Wight&author=A.%20Werner&publication_year=2013&)]
80. Xiao Y., Chu L., Zhang Y., Bian Y., Xiao J., Xu D. (2021). “HY5: A pivotal regulator of light-dependent development in higher plants,” in Frontiers in plant science, vol. 12. (Switzerland: ), 800989. doi:  10.3389/fpls.2021.800989
     [[DOI](https://doi.org/10.3389/fpls.2021.800989)] [[PMC free article](/articles/PMC8801436/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/35111179/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Frontiers%20in%20plant%20science&author=Y.%20Xiao&author=L.%20Chu&author=Y.%20Zhang&author=Y.%20Bian&author=J.%20Xiao&publication_year=2021&)]
81. Xu X., Chen C., Fan B., Chen Z. (2006). Physical and functional interactions between pathogen-induced Arabidopsis WRKY18, WRKY40, and WRKY60 transcription factors. Plant Cell
    18 (5), 1310–1326. doi:  10.1105/tpc.105.037523
     [[DOI](https://doi.org/10.1105/tpc.105.037523)] [[PMC free article](/articles/PMC1456877/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16603654/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell&title=Physical%20and%20functional%20interactions%20between%20pathogen-induced%20Arabidopsis%20WRKY18,%20WRKY40,%20and%20WRKY60%20transcription%20factors&author=X.%20Xu&author=C.%20Chen&author=B.%20Fan&author=Z.%20Chen&volume=18&issue=5&publication_year=2006&pages=1310-1326&pmid=16603654&doi=10.1105/tpc.105.037523&)]
82. Yamasaki H., Abdel-Ghany S. E., Cohu C. M., Kobayashi Y., Shikanai T., Pilon M. (2007). Regulation of copper homeostasis by micro-RNA in Arabidopsis. J. Biol. Chem.
    282 (22), 16369–16378. doi:  10.1074/jbc.M700138200
     [[DOI](https://doi.org/10.1074/jbc.M700138200)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17405879/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Biol.%20Chem.&title=Regulation%20of%20copper%20homeostasis%20by%20micro-RNA%20in%20Arabidopsis&author=H.%20Yamasaki&author=S.%20E.%20Abdel-Ghany&author=C.%20M.%20Cohu&author=Y.%20Kobayashi&author=T.%20Shikanai&volume=282&issue=22&publication_year=2007&pages=16369-16378&pmid=17405879&doi=10.1074/jbc.M700138200&)]
83. Yamauchi Y., Fukaki H., Fujisawa H., Tasaka M. (1997). Mutations in the SGR4, SGR5 and SGR6 loci of Arabidopsis thaliana alter the shoot gravitropism. Plant Cell Physiol.
    38 (5), 530–535. doi:  10.1093/oxfordjournals.pcp.a029201
     [[DOI](https://doi.org/10.1093/oxfordjournals.pcp.a029201)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/9210330/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell%20Physiol.&title=Mutations%20in%20the%20SGR4,%20SGR5%20and%20SGR6%20loci%20of%20Arabidopsis%20thaliana%20alter%20the%20shoot%20gravitropism&author=Y.%20Yamauchi&author=H.%20Fukaki&author=H.%20Fujisawa&author=M.%20Tasaka&volume=38&issue=5&publication_year=1997&pages=530-535&pmid=9210330&doi=10.1093/oxfordjournals.pcp.a029201&)]
84. Yoshihara T., Spalding E. P. (2017). LAZY genes mediate the effects of gravity on Auxin gradients and plant architecture. Plant Physiol.
    175 (2), 959–969. doi:  10.1104/pp.17.00942
     [[DOI](https://doi.org/10.1104/pp.17.00942)] [[PMC free article](/articles/PMC5619908/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28821594/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Physiol.&title=LAZY%20genes%20mediate%20the%20effects%20of%20gravity%20on%20Auxin%20gradients%20and%20plant%20architecture&author=T.%20Yoshihara&author=E.%20P.%20Spalding&volume=175&issue=2&publication_year=2017&pages=959-969&pmid=28821594&doi=10.1104/pp.17.00942&)]
85. Zhang Y., Wang L., Xie J., Zheng H. (2015). Differential protein expression profiling of Arabidopsis thaliana callus under microgravity on board the Chinese SZ-8 spacecraft. Planta. Germany
    241 (2), 475–488. doi:  10.1007/s00425-014-2196-x
     [[DOI](https://doi.org/10.1007/s00425-014-2196-x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25374148/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Planta.%20Germany&title=Differential%20protein%20expression%20profiling%20of%20Arabidopsis%20thaliana%20callus%20under%20microgravity%20on%20board%20the%20Chinese%20SZ-8%20spacecraft&author=Y.%20Zhang&author=L.%20Wang&author=J.%20Xie&author=H.%20Zheng&volume=241&issue=2&publication_year=2015&pages=475-488&pmid=25374148&doi=10.1007/s00425-014-2196-x&)]
86. Zhou M., Sng N. J., LeFrois C. E., Paul A.-L., Ferl R. J. (2019). Epigenomics in an extraterrestrial environment: organ-specific alteration of DNA methylation and gene expression elicited by spaceflight in Arabidopsis thaliana. BMC Genomics
    20 (1), 205. doi:  10.1186/s12864-019-5554-z
     [[DOI](https://doi.org/10.1186/s12864-019-5554-z)] [[PMC free article](/articles/PMC6416986/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30866818/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Genomics&title=Epigenomics%20in%20an%20extraterrestrial%20environment:%20organ-specific%20alteration%20of%20DNA%20methylation%20and%20gene%20expression%20elicited%20by%20spaceflight%20in%20Arabidopsis%20thaliana&author=M.%20Zhou&author=N.%20J.%20Sng&author=C.%20E.%20LeFrois&author=A.-L.%20Paul&author=R.%20J.%20Ferl&volume=20&issue=1&publication_year=2019&pages=205&pmid=30866818&doi=10.1186/s12864-019-5554-z&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

[Click here for additional data file.](/articles/instance/10800490/bin/Image_1.tif) (8.2MB, tif)

[Click here for additional data file.](/articles/instance/10800490/bin/Image_2.tif) (2.2MB, tif)

[Click here for additional data file.](/articles/instance/10800490/bin/Image_3.tif) (9.2MB, tif)

[Click here for additional data file.](/articles/instance/10800490/bin/Table_1.xlsx) (433.2KB, xlsx)

[Click here for additional data file.](/articles/instance/10800490/bin/Table_2.docx) (18.8KB, docx)

### Data Availability Statement

Raw sequence files and metadata for PS and PRR are available at the NASA data repository GeneLab under the accession numbers OSD-223 and OSD-437.

The datasets presented in this study can be found in online repositories. The names of the repository/repositories and accession number(s) can be found below: NASA GeneLab data repository, OSD-223 and OSD-437.