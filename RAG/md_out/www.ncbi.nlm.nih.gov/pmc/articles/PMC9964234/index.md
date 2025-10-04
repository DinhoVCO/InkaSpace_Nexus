Life (Basel)

. 2023 Feb 18;13(2):576. doi: [10.3390/life13020576](https://doi.org/10.3390/life13020576)

# Designing a Novel Monitoring Approach for the Effects of Space Travel on Astronauts’ Health

[Anurag Sakharkar](https://pubmed.ncbi.nlm.nih.gov/?term=%22Sakharkar%20A%22%5BAuthor%5D)

### Anurag Sakharkar

1College of Arts and Science, University of Saskatchewan, 9 Campus Drive, Saskatoon, SK S7N 5A5, Canada

Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Visualization

Find articles by [Anurag Sakharkar](https://pubmed.ncbi.nlm.nih.gov/?term=%22Sakharkar%20A%22%5BAuthor%5D)

1, [Jian Yang](https://pubmed.ncbi.nlm.nih.gov/?term=%22Yang%20J%22%5BAuthor%5D)

### Jian Yang

2College of Pharmacy and Nutrition, University of Saskatchewan, 107 Wiggins Road, Saskatoon, SK S7N 5E5, Canada

Conceptualization, Methodology, Validation, Formal analysis, Investigation, Resources, Data curation, Writing – review & editing, Supervision, Project administration, Funding acquisition

Find articles by [Jian Yang](https://pubmed.ncbi.nlm.nih.gov/?term=%22Yang%20J%22%5BAuthor%5D)

2,\*

Editors: Claudia Pacelli, Francesca Ferranti, Marta del Bianco

* Author information
* Article notes
* Copyright and License information

1College of Arts and Science, University of Saskatchewan, 9 Campus Drive, Saskatoon, SK S7N 5A5, Canada

2College of Pharmacy and Nutrition, University of Saskatchewan, 107 Wiggins Road, Saskatoon, SK S7N 5E5, Canada

\*

Correspondence: jian.yang@usask.ca

#### Roles

**Anurag Sakharkar**: Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Visualization

**Jian Yang**: Conceptualization, Methodology, Validation, Formal analysis, Investigation, Resources, Data curation, Writing – review & editing, Supervision, Project administration, Funding acquisition

**Claudia Pacelli**: Academic Editor

**Francesca Ferranti**: Academic Editor

**Marta del Bianco**: Academic Editor

Received 2023 Jan 9; Revised 2023 Feb 2; Accepted 2023 Feb 6; Collection date 2023 Feb.

© 2023 by the authors.

Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (<https://creativecommons.org/licenses/by/4.0/>).

[PMC Copyright notice](/about/copyright/)

PMCID: PMC9964234  PMID: [36836933](https://pubmed.ncbi.nlm.nih.gov/36836933/)

## Abstract

Space exploration and extraterrestrial civilization have fascinated humankind since the earliest days of human history. It was only in the last century that humankind finally began taking significant steps towards these goals by sending astronauts into space, landing on the moon, and building the International Space Station. However, space voyage is very challenging and dangerous, and astronauts are under constant space radiation and microgravity. It has been shown that astronauts are at a high risk of developing a broad range of diseases/disorders. Thus, it is critical to develop a rapid and effective assay to monitor astronauts’ health in space. In this study, gene expression and correlation patterns were analyzed for 10 astronauts (8 male and 2 female) using the publicly available microarray dataset E-GEOD-74708. We identified 218 differentially expressed genes between In-flight and Pre-flight and noticed that space travel decreased genome regulation and gene correlations across the entire genome, as well as individual signaling pathways. Furthermore, we systematically developed a shortlist of 32 genes that could be used to monitor astronauts’ health during space travel. Further studies, including microgravity experiments, are warranted to optimize and validate the proposed assay.

**Keywords:** space biology, diagnostic assay, health, transcriptome, space flight

## 1. Introduction

“Space: the final frontier.” [[1](#B1-life-13-00576)]. Every fan of the American science fiction TV series Star Trek is likely to remember this cardinal line of the opening monologue. Indeed, space exploration and extraterrestrial civilization have continually fascinated humankind; however, it was only in the last century that humankind finally took a solid step forward by sending astronauts into space and landing on the moon [[2](#B2-life-13-00576),[3](#B3-life-13-00576)]. In the 21st century, humankind has made another great leap forward in space exploration: expediting the International Space Station (ISS) program [[4](#B4-life-13-00576)], sending unmanned rovers to seek signs of life on Mars [[5](#B5-life-13-00576),[6](#B6-life-13-00576)], and starting private space ventures [[7](#B7-life-13-00576),[8](#B8-life-13-00576)]. In addition, NASA (The National Aeronautics and Space Administration) is planning to send astronauts back to the moon in 2024 and to Mars in the 2030s [[9](#B9-life-13-00576)]. Through all these endeavors, we have seen the twilight of crewed space missions going beyond our harbor (Earth) and into deep space.

Space travel is challenging, dangerous, and full of uncertainty. Astronauts are under sustained microgravity and cosmic radiation. Prolonged exposure to microgravity and cosmic radiation has been shown to cause a series of health problems, including loss of muscle mass [[10](#B10-life-13-00576),[11](#B11-life-13-00576)], reduced bone density [[12](#B12-life-13-00576),[13](#B13-life-13-00576)], compromised immune responses [[14](#B14-life-13-00576),[15](#B15-life-13-00576)], impaired renal functions [[16](#B16-life-13-00576)], neurological system irresponsiveness [[17](#B17-life-13-00576),[18](#B18-life-13-00576)], and development of cardiovascular diseases [[19](#B19-life-13-00576),[20](#B20-life-13-00576)]. Furthermore, microgravity and cosmic radiation can cause several types of cancer, such as leukemia, likely due to compromised immunity [[21](#B21-life-13-00576)]. However, studies under simulated microgravity also show that microgravity affects cell proliferation and apoptosis and can change cancer cells into less malignant phenotypes [[22](#B22-life-13-00576),[23](#B23-life-13-00576),[24](#B24-life-13-00576)]. These studies indicate that the impact of microgravity and cosmic radiation on human health is profound, and it is unlikely that this impact is due to changes in one gene or a small group of genes. Therefore, genomic, transcriptomic, and/or proteomic studies are crucial to fully understand the effects of microgravity and cosmic radiation on human health. These studies can lead to the development of effective strategies to monitor, prevent, and/or alleviate the effects on human health caused by space travel.

Approximately 12 years ago, NASA and JAXA (Japan Aerospace Exploration Agency) undertook a microarray study on 10 astronauts (8 male and 2 female) who had a six-month mission at the ISS [[25](#B25-life-13-00576)]. Terada et al. used qPCR to confirm that space flight changed gene expression in astronauts [[25](#B25-life-13-00576)]. Several genes, including *FGF18*, *ANGPTL7*, and *COMP*, were upregulated and might play a role in inhibiting cell proliferation in hair follicles. However, they neither discussed the potential effects of the differentially expressed genes on the astronauts’ health nor provided any strategy to monitor these effects. Thus, in the current study, we reanalyzed this microarray dataset, conceptualized a method that could monitor the effects of space travel on astronauts’ health, and searched for potential intervention options.

## 2. Materials and Methods

### 2.1. Data Acquisition

Microarray dataset E-GEOD-74708, which is the largest publicly available space gene expression dataset, was downloaded from the NASA GeneLab Database (<https://genelab-data.ndc.nasa.gov/genelab>, accessed on 15 March 2021). It contains gene expression profiles for 10 astronauts (8 male and 2 female) that stayed in the ISS between July 2009 and February 2013. For each astronaut, 2 profiles were collected at each of the three time points, Pre-flight (prior to departing for the ISS), In-flight (while staying at the ISS), and Post-flight (after return to the ground).

### 2.2. Data Processing

Individual gene expression profiles were combined into three DataFrames: Pre-flight, In-flight, and Post-flight using the Pandas package (version 1.3.0) in Python [[26](#B26-life-13-00576)]. These DataFrames were analyzed for possible outliers and verified for accuracy. Gene expression readings with null values were removed. Then, Agilent IDs in the data were mapped to gene names using the Ensembl BioMart database (<https://www.ensembl.org/biomart/martview>, accessed on 15 March 2021).

### 2.3. DEG Identification and Signaling Pathway Analysis

Differentially expressed genes (DEGs: ∣log2FC∣ ≥ 3.00 and *p* < 0.05) were identified between the In-flight and the Pre-flight DataFrames using the DEGseq package (version 1.42.0) in R [[27](#B27-life-13-00576)]. The Likelihood Ratio Test (LRT) function was applied in the calculation. No DEGs were identified between the Post-flight and the In-flight DataFrames. The DEGs between In-flight and Pre-flight were then subjected to signaling pathway analysis using the InnateDB tool [[28](#B28-life-13-00576)].

### 2.4. Calculation of Gene Pair Correlation Matrices

Pairwise Pearson correlation coefficient matrices for the 3 gene expression DataFrames were calculated using formula r=Σ (xi−x\_) (yi−y\_)Σ (xi−x\_)2 Σ(yi−y\_)2. The correlation matrices were subsequently transferred to be visualized using an R platform. To analyze gene pair correlations for the signaling pathways, the expression profiles of the genes for the pathways were extracted from the DataFrames to produce the DataFrame subsets. For each signaling pathway, pairwise Pearson correlation coefficients were calculated and visualized as outlined above between the In-flight and Pre-flight subsets and between the Post-flight and In-flight subsets. Positive and negative correlations were represented in blue and red, respectively. Additionally, gene pair correlation coefficient differentials, ΔCC (In-Pre) = CCIn-flight – CCPre-flight and ΔCC (Post-In) = CCPost-flight – CCIn-flight were calculated by matrix subtraction between the In-flight and Pre-flight subsets and between the Post-flight and In-flight subsets. These were subsequently visualized with correlation difference plots with positive and negative ΔCCs shown in green and red, respectively.

### 2.5. Protein–Protein Interaction Network and Disease Network Constructions

The BioGrid database [[29](#B29-life-13-00576)] and DisGeNET database [[30](#B30-life-13-00576)] were downloaded in March 2021 to create a protein–protein interaction (PPI) network and extract the disease interaction information, respectively, for the DEGs. The networks were then constructed using Python and visualized using Cytoscape [[31](#B31-life-13-00576)].

### 2.6. Drug and miRNA Screenings

The Drugbank [[32](#B32-life-13-00576)] and miRTARBase [[33](#B33-life-13-00576)] databases were also downloaded in March 2021 to extract the drug and miRNA interaction information for the DEGs. The networks were subsequently constructed using Python and visualized using Cytoscape. From these two networks, we identified potential drugs and miRNAs targeting the 32 genes that were identified to be used in a rapid RT2-PCR assay for space travel.

## 3. Results and Discussion

### 3.1. Differentially Expressed Genes (DEGs)

NASA and JAXA undertook Study GLDS-174: “Effects of a closed space environment on gene expression in hair follicles of astronauts in the International Space Station” between 2009 and 2013. Hair follicles were chosen for this study because they are the easiest attainable and noninvasive samples that are understood to be representative of most large-scale changes in the body [[25](#B25-life-13-00576)]. However, Terada et al. only reported the expression of selected genes in this study and did not undertake further analysis [[25](#B25-life-13-00576)]. To better understand how space travel affects astronauts’ health, we downloaded the microarray dataset (E-GEOD-74708) from the NASA GeneLab open data repository. The microarray dataset includes gene expression information for three stages: Pre-flight (6 months to 2 weeks before launch), In-flight (while staying in the ISS), and Post-flight (2 days to 3 months after returning from the ISS). We then analyzed the dataset for gene expression and gene pair correlation. Using cut-off criteria of ∣log2FC∣ ≥ 3.00 and *p* < 0.05, 218 DEGs were identified between In-flight and Pre-flight ([Supplementary File S1: DEG\_list.xls](#app1-life-13-00576)). The top 20 up- and downregulated genes are summarized in [Table 1](#life-13-00576-t001). However, no DEGs were detected between Post-flight and In-flight, suggesting that the astronauts may need a longer time than current guidelines for the body to adjust to the ground environment. Furthermore, astronauts have a much higher risk of developing various types of diseases than normal people and precautionary measures are critical to protect their health after returning to ground.

#### Table 1.

Top 20 up- and down-regulated DEGs (differentially expressed genes) between In-flight and Pre-flight. The cut-off criteria for DEGs are ∣log2FC∣ ≥ 3.00 and *p* < 0.05.

| Up-Regulated Genes | | | Down-Regulated Genes | | |
| --- | --- | --- | --- | --- | --- |
| Gene Name | Log2FC | *p*-Value | Gene Name | Log2FC | *p*-Value |
| *LIMCH1* | 7.59 | 0.03 | *NFATC1* | −10.40 | 0.00 |
| *IER3* | 7.45 | 0.03 | *KIDINS220* | −10.35 | 0.03 |
| *ZNF664* | 6.57 | 0.03 | *ZCCHC9* | −7.82 | 0.00 |
| *NDUFA1* | 6.27 | 0.03 | *IGSF9* | −6.08 | 0.03 |
| *[AL391650.1](https://www.ncbi.nlm.nih.gov/nuccore/AL391650.1)* | 5.28 | 0.03 | *HSD11B1L* | −5.76 | 0.00 |
| *TUBGCP5* | 5.07 | 0.03 | *CLTB* | −5.69 | 0.00 |
| *GAPVD1* | 5.03 | 0.03 | *YIPF2* | −5.68 | 0.03 |
| *AARS2* | 4.81 | 0.03 | *BTBD9* | −5.49 | 0.00 |
| *AC004080.5* | 4.77 | 0.03 | *LINC00668* | −5.41 | 0.00 |
| *NAA60* | 4.72 | 0.03 | *[AL096711.2](https://www.ncbi.nlm.nih.gov/nuccore/AL096711.2)* | −4.97 | 0.03 |
| *IGBP1P1* | 4.41 | 0.03 | *EIF4E2* | −4.97 | 0.03 |
| *FANCD2* | 4.28 | 0.03 | *SHE* | −4.41 | 0.03 |
| *AMT* | 4.20 | 0.03 | *HOXC4* | −4.27 | 0.00 |
| *PNPLA4* | 4.11 | 0.03 | *THBS3* | −4.17 | 0.00 |
| *RABGAP1* | 4.10 | 0.03 | *PGM2L1* | −3.95 | 0.00 |
| *MAPKAPK5* | 3.89 | 0.03 | *TCEANC* | −3.93 | 0.03 |
| *DFFBP1* | 3.83 | 0.03 | *ARHGAP9* | −3.91 | 0.00 |
| *STAG1* | 3.71 | 0.03 | *ZNF451* | −3.80 | 0.03 |
| *SPON2* | 3.62 | 0.04 | *NCEH1* | −3.73 | 0.00 |
| *CHN1* | 3.59 | 0.04 | *[AC010531.1](https://www.ncbi.nlm.nih.gov/nuccore/AC010531.1)* | −3.71 | 0.03 |

[Open in a new tab](table/life-13-00576-t001/)

As expected, the DEGs between In-flight and Pre-flight regulate a broad spectrum of biological and physiological functions. For example, the most up-regulated gene *LIMCH1*, encoding LIM and calponin-homology domains 1, activates the non-muscle myosin Iia complex, stabilizes focal adhesion, and inhibits cell migration [[34](#B34-life-13-00576),[35](#B35-life-13-00576)]. Thus, the upregulation of *LIMCH1* may explain observations that microgravity exposure can change cancer cells into less malignant phenotypes [[22](#B22-life-13-00576),[23](#B23-life-13-00576),[24](#B24-life-13-00576)]. The second most up-regulated gene *IER3* encodes Immediate Early Response 3 and regulates cell apoptosis [[36](#B36-life-13-00576)], inflammation [[37](#B37-life-13-00576)], and tumorigenesis [[38](#B38-life-13-00576)]. Upregulation of *IER3* has been observed in several types of cancer and may regulate cancer progression [[39](#B39-life-13-00576),[40](#B40-life-13-00576)]. This implies another possible reason, other than radiation exposure, that increases the risk of astronauts developing cancer during a prolonged period of space travel. The most down-regulated gene, *NFATC1,* encodes Nuclear Factor of Activated T Cells 1 and plays an important role in osteoblast differentiation [[41](#B41-life-13-00576)], osteoclastogenesis [[42](#B42-life-13-00576)], T-cell differentiation [[43](#B43-life-13-00576)], lymphatic endothelial development [[44](#B44-life-13-00576)], cardiac valve morphogenesis [[45](#B45-life-13-00576)], and tumorigenesis [[46](#B46-life-13-00576)]. The downregulation of *NFATC1* may result in osteoporosis, immunocompromised conditions, and prostate cancer in astronauts during a prolonged space stay. The second most down-regulated gene, *KIDINS220*, encoding Kinase D Interacting Substrate 220, modulates the development and function of the nerve and cardiovascular systems [[47](#B47-life-13-00576),[48](#B48-life-13-00576)]. The downregulation of *KIDINS220* may contribute to the development of neurological disorders and cardiovascular diseases in astronauts. In summary, the large variation of the biological processes regulated by the DEGs provides a valuable resource of genes for us to develop a rapid assay kit (~20–30 genes) to monitor astronauts’ health conditions in space. However, it is noteworthy that the three genes reported by Terada et al., *FGF18*, *ANGPTL7*, and *COMP*, are not in the aforementioned DEG list because they failed to meet the cut-off criteria.

### 3.2. Gene Pair Correlations

As mentioned above, the effect of space travel on an astronaut’s health is comprehensive and involves the regulation of many genes. It is also well-known that any biological, physiological, or pathophysiological change requires a delicate coordination of multiple genes. Therefore, we decided to carry out a gene pair correlation analysis for the whole genome (30,645 transcripts for 23,115 genes) among the Pre-flight, In-flight, and Post-flight expression profiles. As shown in [Figure 1](#life-13-00576-f001)A, the genes are highly correlated in the Pre-flight, which is consistent with previous studies showing that gene expressions are correlated in normal human tissues [[49](#B49-life-13-00576)]. Upon staying in the ISS for an extended period of 6 months, the genome significantly lost its regulation of the gene expression and gene coordination was scrambled ([Figure 1](#life-13-00576-f001)B). Our previous studies have shown that loss of gene pair correlations is a hallmark of carcinogenesis and/or cancer progression [[50](#B50-life-13-00576),[51](#B51-life-13-00576),[52](#B52-life-13-00576)]. Therefore, loss of coordination of gene expression, other than cosmic radiation and compromised immune system, is likely to be another factor that increases the risk of cancer development in astronauts. Analysis of the Post-flight dataset showed that returning to ground did not significantly improve genome regulation and coordination of gene expression ([Figure 1](#life-13-00576-f001)C), implying that the effect of space travel on human health is more profound and longer lasting than currently thought. Extended care is necessary for astronauts to minimize the risk of disease development. As we progress towards crewed missions into outer space (for example, to the Moon and Mars) and other prolonged space stays, it is critical to develop rapid approaches to monitor genome regulation and establish corresponding protocols to alleviate the effects of space travel on human health. Another important question that needs to be addressed is whether the human body could establish a new “routine” for prolonged space stays and what this would look like in terms of astronauts’ health. We speculate that loss of gene expression coordination might also be responsible for other diseases/conditions astronauts experience, such as muscle loss and compromised immune system. Extensive further studies in space biomedicine and space pharmacology are warranted to prepare us for longer-term outer space exploration.

#### Figure 1.

[![Figure 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8a9b/9964234/9b254aa52d38/life-13-00576-g001.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9964234_life-13-00576-g001.jpg)

[Open in a new tab](figure/life-13-00576-f001/)

Gene pair correlations of the whole genome (30,645 transcripts for 23,115 genes) for 10 astronauts during Pre-flight (**A**), In-flight (**B**), and Post-flight (**C**). Positive and negative correlations are represented in blue and red, respectively.

### 3.3. Signaling Pathway and Disease Network of the DEGs

Because DEGs are the most altered genes during a biological process, we conducted a signaling pathway analysis of the 218 DEGs between In-flight and Pre-flight to figure out which biological functions are regulated by these genes. The top 11 signaling pathways were identified to be signal transduction, immune system, gene expression, metabolism, metabolism of proteins, generic transcription pathway, developmental biology, metabolism of lipids and lipoproteins, axon guidance, innate immune system, and disease ([Table 2](#life-13-00576-t002)). In total, 48 genes were found to be involved in the regulation of these top 11 signaling pathways. Moreover, it is obvious that most of these DEGs are involved in the regulation of multiple signaling pathways, and that these signaling pathways regulate a broad range of biological, physiological, and/or pathophysiological processes. This analysis reconfirms that space travel imposes comprehensive effects on the human system rather than affecting an individual organ or tissue.

#### Table 2.

Differentially expressed genes (DEGs) present in the top 11 signaling pathways.

| Signaling Pathways | Gene Names |
| --- | --- |
| Signal transduction | *ARHGAP9*, *CCL2*, *CCNC*, *CHN1*, *CLTB*, *COL4A4*, *CREB1*, *CRHR1*, *CTNNBIP1*, *HIF1A*, *KIDINS220*, *NFATC1*, *PDPK1*, *SOS2*, *THBS3*, *YES1* |
| Immune system | *ATF2*, *BIRC2*, *CREB1*, *EIF4E2*, *IL7*, *NFATC1*, *PDPK1*, *UBA5*, *UBR4*, *XAF1*, *YES1* |
| Gene expression | *AARS2*, *CCNC*, *RRN3*, *ZNF184*, *ZNF253*, *ZNF529*, *ZNF606*, *ZNF664*, *ZNF699*, *ZNF711* |
| Metabolism | *ACSL4*, *ARSK*, *CCNC*, *GM2A*, *GPT*, *HACL1*, *NDUFA1*, *PIKFYVE*, *PSAT1* |
| Metabolism of proteins | *ARSK*, *CCL2*, *DPP4*, *GNE*, *MAGT1*, *PCSK1*, *SPON2*, *XRN2* |
| Generic transcription pathway | *CCNC*, *ZNF184*, *ZNF253*, *ZNF529*, *ZNF606*, *ZNF664*, *ZNF699*, *ZNF711* |
| Developmental biology | *CCNC*, *CLTB*, *COL4A4*, *CREB1*, *SCN2B*, *SOS2*, *YES1* |
| Metabolism of lipids and lipoproteins | *ACSL4*, *ARSK*, *CCNC*, *GM2A*, *HACL1*, *PIKFYVE* |
| Axon guidance | *CLTB*, *COL4A4*, *CREB1*, *SCN2B*, *SOS2*, *YES1* |
| Innate immune system | *ATF2*, *BIRC2*, *CREB1*, *NFATC1*, *PDPK1*, *YES1* |
| Disease | *CCNC*, *CHMP4C*, *CREB1*, *CTNNBIP1*, *HIF1A*, *PDPK1* |

[Open in a new tab](table/life-13-00576-t002/)

We further analyzed the disease network for the 218 DEGs between the In-flight and Pre-flight expression profiles to identify the major disease/disorder conditions associated with space travel ([Supplementary File S2: Disease\_DEG.xls](#app1-life-13-00576)). As shown in [Table 3](#life-13-00576-t003), the top 20 disease/disorder conditions can broadly be divided into three categories: neoplasia/carcinoma, neurological disorder, and liver function, with the top three conditions being malignant neoplasm of the breast, colorectal carcinoma, and malignant neoplasm of the prostate. More DEGs were associated with tumor development than other diseases/disorders. In 2019, Reynolds et al. reported the effect of space radiation on astronauts’ death using a statistical analysis [[53](#B53-life-13-00576)]. Of the astronauts who traveled to space between 1960 and 2018, 53 NASA astronauts have died, with 16 of those deaths (30.2%) being caused by cancer. Nevertheless, their study indicates that space radiation does not strongly impact the mortality of astronauts. This implies that weakened genome regulation (i.e., reduced gene expression correlation) is likely to be another key factor, in addition to compromised immune function, in causing tumor development in astronauts. However, these tumors may be less malignant or even benign [[22](#B22-life-13-00576),[23](#B23-life-13-00576),[24](#B24-life-13-00576)]. Moreover, consistent with previous studies [[54](#B54-life-13-00576),[55](#B55-life-13-00576)], our results showed that space travel significantly affects astronauts’ liver function and liver metabolism. Key genes identified from our analysis, such as *GPT* and *UBA5*, might serve as valuable monitoring biomarkers of astronauts’ liver function and even possible medical intervention points to protect astronauts’ health. Because liver is a major organ for drug metabolism, a systematic space pharmacology study is needed to establish drug profiles—including dosing, ADMET (absorption, distribution, metabolism, excretion, and toxicity), and even formulation—in preparation for future voyages into outer space. Space drug usage based on current information may be less effective or even detrimental to astronauts’ health.

#### Table 3.

Top 20 disease/disorder conditions and their respectively associated DEGs based on disease network analysis of 218 DEGs between In-flight and Pre-flight.

| Disease/Disorder | Genes |
| --- | --- |
| Malignant Neoplasm of Breast | *THBS3*, *UBR4*, *ATF2*, *NBN*, *CRHR1*, *AREG*, *HIF1A*, *PDPK1*, *COL7A1*, *ZNF404*, *BIRC2* |
| Colorectal Carcinoma | *POSTN*, *SACS*, *FANCG*, *XAF1*, *ACSL4*, *INTS13*, *COL7A1*, *NFATC1*, *C12ORF76*, *NDUFA1* |
| Malignant Neoplasm of Prostate | *GREB1*, *HMGN5*, *SPON2*, *HIF1A*, *CRYL1*, *CASZ1*, *ACSL4*, *NBN* |
| Prostatic Neoplasms | *CASZ1*, *NBN*, *GREB1*, *HIF1A*, *CRYL1*, *ACSL4*, *SPON2*, *HMGN5* |
| Schizophrenia | *PSAT1*, *BTBD9*, *CFAP65*, *CREB1*, *CCL2*, *HSPA12A*, *DKK3*, *VRK2* |
| Breast Carcinoma | *BIRC2*, *COL7A1*, *ZNF404*, *HIF1A*, *AREG*, *CRHR1*, *PDPK1* |
| Mammary Carcinoma, Human | *AREG*, *COL7A1*, *HIF1A*, *CRHR1*, *ZNF404*, *PDPK1*, *BIRC2* |
| Mammary Neoplasms | *AREG*, *COL7A1*, *PDPK1*, *ZNF404*, *CRHR1*, *HIF1A*, *BIRC2* |
| Mammary Neoplasms, Human | *ZNF404*, *COL7A1*, *PDPK1*, *CRHR1*, *BIRC2*, *HIF1A*, *AREG* |
| Unipolar Depression | *CCL2*, *PEA15*, *HIF1A*, *CRHR1*, *CREB1*, *ACSL4* |
| Liver Cirrhosis, Experimental | *GPT*, *TM6SF1*, *SGCB*, *ARHGAP9*, *CCL2* |
| Major Depressive Disorder | *HIF1A*, *CRHR1*, *PEA15*, *CCL2*, *CREB1* |
| Non-small Cell Lung Carcinoma | *E2F8*, *PSAT1*, *AREG*, *HIF1A*, *COL7A1* |
| Bipolar Disorder | *HIF1A*, *CRHR1*, *CREB1*, *HMGXB4* |
| Chemical And Drug Induced Liver Injury | *HACL1*, *GPT*, *UBA5*, *CCL2* |
| Chemical-induced Liver Toxicity | *HACL1*, *UBA5*, *GPT*, *CCL2* |
| Depressive Disorder | *CREB1*, *CRHR1*, *DPP4*, *ACSL4* |
| Disease Exacerbation | *COL7A1*, *E2F8*, *ATF2*, *HIF1A* |
| Drug-induced Acute Liver Injury | *GPT*, *HACL1*, *CCL2*, *UBA5* |
| Drug-induced Liver Disease | *HACL1*, *GPT*, *CCL2*, *UBA5* |

[Open in a new tab](table/life-13-00576-t003/)

### 3.4. Design of a Rapid Assay for Space Travel

Any biological or physiological process requires a delicate regulation of genes, including gene expression levels, interactions, and correlations. However, most genomics/genetic studies are focused on gene expression level rather than gene pair correlation. Although gene co-expressions and protein co-localizations are commonly studied in biomedical research, our research laboratory, to the best of our knowledge, is the first to apply gene pair correlation coefficient (a mathematical term) to describe and explain biological and medical questions [[50](#B50-life-13-00576),[51](#B51-life-13-00576),[52](#B52-life-13-00576)]. Thus, to design a rapid assay to monitor astronauts’ health, we selected a set of genes with expression levels and gene pair correlations significantly altered by space travel.

We calculated gene pair correlation coefficients (designated as CC) of the DEGs associated with the top 11 signaling pathways for the Pre-flight, In-flight, and Post-flight datasets, and analyzed the gene pair correlation coefficient differentials (designated as ΔCC) between the In-flight and Pre-flight and between the Post-flight and In-flight ([Figure 2](#life-13-00576-f002)). The changes in gene pair CCs between the In-flight and Pre-flight datasets were obvious for every signaling pathway, except the generic transcription pathway. However, the changes between Post-flight and In-flight CCs were minimal. Thus, using ∣ΔCC∣ > 0.70 as a cut-off, we identified gene pairs with their correlation coefficients significantly altered between the In-flight and Pre-flight datasets and summarized them in [Table 4](#life-13-00576-t004). These gene pairs were then classified into four categories based on changes in correlation coefficients: Category 1—positive to more/less positive (highlighted in blue), Category 2—positive to negative (highlighted in green), Category 3—negative to positive (highlighted in brown), and Category 4—negative to more/less negative (highlighted in red). It is noteworthy that Categories 2 and 3 contained more gene pairs than Categories 1 and 4, implying that many genes lost their coordination and even started counteractive processes in space. This observation supports previous studies that found that spaceflight significantly affects gene expression and homeostasis [[56](#B56-life-13-00576)]. This dramatic change in gene expression coordination is thought to affect normal biological and physiological functions in the human body and is likely detrimental to astronauts’ health.

#### Figure 2.

[![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8a9b/9964234/a82bc1dd77f0/life-13-00576-g002a.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9964234_life-13-00576-g002a.jpg)

[![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8a9b/9964234/4c92777e7db8/life-13-00576-g002b.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9964234_life-13-00576-g002b.jpg)

[![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8a9b/9964234/e1cdfdd7e5d9/life-13-00576-g002c.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9964234_life-13-00576-g002c.jpg)

[Open in a new tab](figure/life-13-00576-f002/)

Gene pair correlations ((**1**): Pre-flight, (**2**): In-flight, and (**3**): Post-flight) and differentials of gene pair correlations (**4**): between In-flight and Pre-flight and (**5**): between Post-flight and In-flight for the differentially expressed genes (DEGs) in the top 11 signaling pathways. The top 11 signaling pathways are signal transduction, immune system, gene expression, metabolism, metabolism of proteins, generic transcription pathway, developmental biology, metabolism of lipids and lipoproteins, axon guidance, innate immune system, and disease. The top 11 signaling pathways were identified from InnateDB analysis of the 218 DEGs (∣log2FC∣ ≥ 3.00 and *p* < 0.05). Positive and negative gene pair correlations are represented in blue and red, respectively; and positive and negative differentials of gene pair correlations are represented in green and red, respectively.

#### Table 4.

Gene pairs with significantly altered correlation coefficients between In-flight and Pre-flight (i.e., ∣ΔCC (CCIn-flight – CCPre-flight)∣ > 0.70) in the top 11 signaling pathways identified from signaling pathway analysis of the 218 DEGs between In-flight and Pre-flight. Gene pairs with correlation coefficients changed from positive to less/more positive (Category 1), positive to negative (Category 2), negative to positive (Category 3), and negative to less/more negative (Category 4) were highlighted in blue, green, brown, and red, respectively.

| GENE PAIRS | CCPre-flight | CCIn-flight | ΔCC |
| --- | --- | --- | --- |
| **Signal transduction** | | | |
| **ARHGAP9–COL4A4** | *−0.51* | *0.28* | *0.79* |
| **ARHGAP9–THBS3** | *0.39* | *−0.48* | *−0.87* |
| **CCL2–COL4A4** | *−0.95* | *−0.07* | *0.88* |
| **CCL2–CREB1** | *0.93* | *−0.09* | *−1.02* |
| **CCL2–CRHR1** | *0.68* | *−0.11* | *−0.79* |
| **CCL2–THBS3** | *0.68* | *−0.19* | *−0.87* |
| **CCNC–COL4A4** | *0.46* | *−0.65* | *−1.11* |
| **CCNC–CRHR1** | *−0.58* | *0.65* | *1.23* |
| **CCNC–THBS3** | *−0.41* | *0.34* | *0.75* |
| **CHN1–CRHR1** | *0.43* | *−0.59* | *−1.02* |
| **CHN1–HIF1A** | *−0.36* | *0.34* | *0.70* |
| **COL4A4–CREB1** | *−0.93* | *−0.03* | *0.90* |
| **COL4A4–NFATC1** | *−0.77* | *0.50* | *1.27* |
| **COL4A4–PDPK1** | *0.41* | *−0.50* | *−0.91* |
| **CREB1–CRHR1** | *0.80* | *−0.03* | *−0.83* |
| **CREB1–THBS3** | *0.79* | *0.05* | *−0.74* |
| **CRHR1–KIDINS220** | *0.59* | *−0.14* | *−0.73* |
| **CRHR1–NFATC1** | *0.83* | *−0.47* | *−1.30* |
| **CRHR1–PDPK1** | *−0.57* | *0.34* | *0.91* |
| **CRHR1–YES1** | *0.40* | *−0.71* | *−1.11* |
| **CTNNBIP1–NFATC1** | *0.07* | *0.85* | *0.78* |
| **KIDINS220–PDPK1** | *−0.74* | *0.30* | *1.04* |
| **KIDINS220–SOS2** | *−0.86* | *0.29* | *1.15* |
| **KIDINS220–YES1** | *0.70* | *0.00* | *−0.70* |
| **NFATC1–THBS3** | *0.72* | *−0.34* | *−1.06* |
| **PDPK1–SOS2** | *0.63* | *−0.22* | *−0.85* |
| **SOS2–YES1** | *−0.61* | *0.17* | *0.78* |
| **Immune system** | | | |
| **ATF2–NFATC1** | *−0.03* | *−0.75* | *−0.72* |
| **BIRC2–PDPK1** | *−0.73* | *0.13* | *0.86* |
| **CREB1–EIF4E2** | *−0.94* | *0.07* | *1.01* |
| **CREB1–IL7** | *0.91* | *−0.03* | *−0.94* |
| **CREB1–UBR4** | *0.90* | *−0.28* | *−1.18* |
| **CREB1–XAF1** | *0.71* | *−0.03* | *−0.74* |
| **EIF4E2–IL7** | *−0.87* | *0.10* | *0.97* |
| **EIF4E2–NFATC1** | *−0.87* | *0.46* | *1.33* |
| **EIF4E2–UBR4** | *−0.95* | *0.40* | *1.35* |
| **EIF4E2–XAF1** | *−0.72* | *0.10* | *0.82* |
| **IL7–UBR4** | *0.88* | *−0.34* | *−1.22* |
| **NFATC1–UBR4** | *0.85* | *−0.18* | *−1.03* |
| **PDPK1–UBR4** | *−0.55* | *0.34* | *0.89* |
| **UBA5–UBR4** | *0.59* | *−0.27* | *−0.86* |
| **UBR4–XAF1** | *0.88* | *−0.16* | *−1.04* |
| **UBR4–YES1** | *0.35* | *−0.59* | *−0.94* |
| **Gene expression** | | | |
| **AARS2–ZNF253** | *−0.57* | *0.23* | *0.80* |
| **AARS2–ZNF606** | *−0.91* | *0.21* | *1.12* |
| **AARS2–ZNF711** | *−0.60* | *0.31* | *0.91* |
| **RRN3–ZNF184** | *−0.51* | *0.34* | *0.85* |
| **RRN3–ZNF606** | *−0.06* | *0.87* | *0.93* |
| **RRN3–ZNF711** | *−0.22* | *0.50* | *0.72* |
| **Metabolism** | | | |
| **ACSL4–ARSK** | *0.56* | *−0.66* | *−1.22* |
| **ACSL4–CCNC** | *0.75* | *−0.74* | *−1.49* |
| **ACSL4–GPT** | *−0.66* | *0.85* | *1.61* |
| **ACSL4–NDUFA1** | *0.81* | *0.05* | *−0.76* |
| **ACSL4–PIKFYVE** | *−0.22* | *0.69* | *0.91* |
| **ARSK–GM2A** | *0.48* | *−0.34* | *−0.82* |
| **CCNC–GM2A** | *0.65* | *−0.44* | *−1.09* |
| **CCNC–PSAT1** | *0.88* | *−0.23* | *−1.11* |
| **GPT–NDUFA1** | *−0.59* | *0.24* | *0.83* |
| **GPT–PIKFYVE** | *−0.05* | *0.79* | *0.84* |
| **GPT–PSAT1** | *−0.65* | *0.46* | *1.11* |
| **Metabolism of proteins** | | | |
| **ARSK–DPP4** | *−0.27* | *0.57* | *0.84* |
| **CCL2–DPP4** | *0.79* | *−0.26* | *−1.05* |
| **CCL2–PCSK1** | *0.90* | *−0.16* | *−1.06* |
| **CCL2–SPON2** | *0.77* | *−0.03* | *−0.80* |
| **DPP4–GNE** | *0.74* | *−0.21* | *−0.95* |
| **DPP4–MAGT1** | *−0.57* | *0.37* | *0.94* |
| **MAGT1–PCSK1** | *−0.85* | *0.21* | *1.06* |
| **PCSK1–SPON2** | *0.84* | *0.01* | *−0.83* |
| **Developmental biology** | | | |
| **CCNC–COL4A4** | *0.46* | *−0.65* | *−1.11* |
| **CLTB–SCN2B** | *−0.39* | *0.37* | *0.76* |
| **COL4A4–CREB1** | *−0.93* | *−0.03* | *0.90* |
| **SOS2–YES1** | *−0.61* | *0.17* | *0.78* |
| **Metabolism of lipids and lipoproteins** | | | |
| **ACSL4–ARSK** | *0.56* | *−0.66* | *−1.22* |
| **ACSL4–CCNC** | *0.75* | *−0.74* | *−1.49* |
| **ACSL4–PIKFYVE** | *−0.22* | *0.69* | *0.91* |
| **ARSK–GM2A** | *0.48* | *−0.34* | *−0.82* |
| **CCNC–GM2A** | *0.65* | *−0.44* | *−1.09* |
| **Axon guidance** | | | |
| **CLTB–SCN2B** | *−0.39* | *0.37* | *0.76* |
| **COL4A4–CREB1** | *−0.93* | *−0.03* | *0.90* |
| **SOS2–YES1** | *−0.61* | *0.17* | *0.78* |
| **Innate immune system** | | | |
| **ATF2–NFATC1** | *−0.03* | *−0.75* | *−0.72* |
| **BIRC2–PDPK1** | *−0.73* | *0.13* | *0.86* |
| **Disease** | | | |
| **CCNC–CHMP4C** | *0.60* | *−0.38* | *−0.98* |
| **CHMP4C–CREB1** | *−0.85* | *0.31* | *1.16* |
| **CHMP4C–PDPK1** | *0.44* | *−0.63* | *−1.07* |

[Open in a new tab](table/life-13-00576-t004/)

In a previous study, correlation was classified into three categories based on correlation coefficients: strong (0.68 ≤ ∣CC∣ ≤ 1.00), moderate (0.36 ≤ ∣CC∣ ≤ 0.67), and weak (∣CC∣ ≤ 0.35) [[57](#B57-life-13-00576)]. To increase the sensitivity of the assay for space travel, it is rational to only include gene pairs with correlations changing from strong to weak, weak to strong, or strong to opposite strong with ∣ΔCC∣ > 0.70. Using this guideline, we identified the following gene pairs: 12 gene pairs from signal transduction, 11 gene pairs from immune system, 2 gene pairs from gene expression, 5 gene pairs from metabolism, 6 gene pairs from metabolism of proteins, 1 gene pair from developmental biology, 2 gene pairs from metabolism of lipids and lipoprotein, 1 gene pair from axon guidance, 2 gene pairs from innate immune system, and 1 gene pair from disease ([Table 5](#life-13-00576-t005)). In total, 32 genes were selected, and they are *AARS2*, *ACSL4*, *ATF2*, *BIRC2*, *CCL2*, *CCNC*, *CHMP4C*, *COL4A4*, *CREB1*, *CRHR1*, *CTNNBIP1*, *DPP4*, *EIF4E2*, *GNE*, *GPT*, *IL7*, *KIDINS220*, *MAGT1*, *NDUFA1*, *NFATC1*, *PCSK1*, *PDPK1*, *PIKFYVE*, *PSAT1*, *RRN3*, *SOS2*, *SPON2*, *THBS3*, *UBR4*, *XAF1*, *YES1*, and *ZNF606*.

#### Table 5.

Gene pairs with criteria of ∣ΔCC∣ > 0.70 and correlation changing from strong to weak, weak to strong, or strong to opposite strong from the top 11 signaling pathways.

| Signaling Pathways | Gene Pairs |
| --- | --- |
| Signal transduction | *CCL2–COL4A4*, *CCL2*–*CREB1*, *CCL2*–*CRHR1*, *CCL2*–*THBS3*, *COL4A4*–*CREB1*, *CREB1*–*CRHR1*, *CREB1*–*THBS3*, *CTNNBIP1*–*NFATC1*, *KIDINS220*–*PDPK1*, *KIDINS220*–*SOS2*, *KIDINS220*–*YES1*, *NFATC1*–*THBS3* |
| Immune system | *ATF2*–*NFATC1*, *BIRC2*–*PDPK1*, *CREB1*–*EIF4E2*, *CREB1*–IL7, *CREB1*–*UBR4*, *CREB1*–*XAF1*, *EIF4E2*–*IL7*, *EIF4E2*–*XAF1*, *IL7*–*UBR4*, *NFATC1*–*UBR4*, *UBR4*–*XAF1* |
| Gene expression | *AARS2*–*ZNF606*, *RRN3*–*ZNF606* |
| Metabolism | *ACSL4*–*CCNC*, *ACSL4*–*NDUFA1*, *ACSL4*–*PIKFYVE*, *CCNC*–*PSAT1*, *GPT*–*PIKFYVE* |
| Metabolism of proteins | *CCL2*–*DPP4*, *CCL2*–*PCSK1*, *CCL2*–*SPON2*, *DPP4*–*GNE*, *MAGT1*–*PCSK1*, *PCSK1*–*SPON2* |
| Developmental biology | *COL4A4*–*CREB1* |
| Metabolism of lipids and lipoproteins | *ACSL4*–*CCNC*, *ACSL4*–*PIKFYVE* |
| Axon guidance | *COL4A4*–*CREB1* |
| Innate immune system | *ATF2*–*NFATC1*, *BIRC2*–*PDPK1* |
| Disease | *CHMP4C*–*CREB1* |

[Open in a new tab](table/life-13-00576-t005/)

To get a global view of the 32 genes regulating biological functions, we constructed the protein–protein interaction (PPI), disease-gene, drug-gene, and miRNA-gene networks for the 218 DEGs and labelled the 32 genes in the networks ([Supplementary Figure S1](#app1-life-13-00576)). Genes that were present in the 32-gene list but not in the networks were not labelled. Most of the 32 identified genes have high degrees of connectivity and are likely to be biological hubs. Thus, we propose that an RT2-PCR assay of these 32 genes could be a novel, effective, and comparatively cheap way to continuously monitor astronauts’ health in space. Validation of this assay under microgravity simulation conditions is warranted for further optimization of the gene list before sending an assay kit for practical tests in space. Finally, we extracted the drug molecules (both approved and experimental, listed in [Supplementary File S3: Drug\_list.xls](#app1-life-13-00576)) and miRNAs (listed in [Supplementary File S4: miRNA\_list.xls](#app1-life-13-00576)) that potentially target these 32 genes from the drug-gene and miRNA-gene networks. These drugs and miRNAs could be applied as possible medical interventions for health conditions associated with space travel.

## 4. Conclusions

In this study, we analyzed the effects of space travel on gene expression and correlation using the publicly available microarray dataset E-GEOD-74708, and systematically developed a shortlist of genes for a novel rapid assay that could be used to monitor astronauts’ health in space. However, this study faces a few limitations. First, the sample size (10 astronauts) is small due to the nature of space travel and unstandardized space biology research. More sample collection is needed to optimize the monitoring assay. Secondly, there were only two female astronauts in the microarray dataset. To get better representation and higher accuracy in the analysis, more gene expression profiles from a diverse population of astronauts should be obtained. Future studies in simulated microgravity conditions will allow for the optimization and validation of the proposed assay. It is noteworthy that this assay may address only one facet of a complete monitoring and treatment approach for astronauts’ health in space. In practice, other factors such as biomarkers and physiological metrics should also be included in the approach. Despite these drawbacks, our current study proposes a new strategy to develop genome-based rapid assays. This strategy could also be applied to other research fields such as cancer diagnostic assays.

## Supplementary Materials

The following supporting information can be downloaded at: <https://www.mdpi.com/article/10.3390/life13020576/s1>, File S1: DEG\_list.xls; File S2: Disease\_DEG.xls; File S3: Drug\_list.xls; File S4: miRNA\_list.xls; Supplementary Figure S1: Protein-protein interaction (A), disease-gene (B), drug-gene (C) and miRNA-gene (D) networks for the 218 differentially expressed genes (DEGs) between Pre-flight and In-flight gene expression datasets collected from 10 astronauts (8 males and 2 females). Nodes with higher degrees of connectivity were shown in larger size and darker color. Genes identified for the rapid RT2-PCR assay kit were labelled in the networks. Genes *CCNC, CTNNBIP1, EIF4E2* and *RRN3* are not present in the disease-gene network; genes *BIRC2, CCNC, CHMP4C, CTNNBIP1, EIF4E2, IL7, KIDINS220, MAGT1, PIKFYVE, RRN3, SOS2, SPON2, THBS3, XAF1* and *ZNF606* are not present in the drug-gene network; and genes *CRHR1, DPP4, GPT* and *SPON2* are not present in the miRNA-gene network, respectively.

[Click here for additional data file.](/articles/instance/9964234/bin/life-13-00576-s001.zip) (2.3MB, zip)

## Author Contributions

Conceptualization, J.Y.; methodology, A.S. and J.Y.; software, A.S.; validation, A.S. and J.Y.; formal analysis, A.S. and J.Y.; investigation, A.S. and J.Y.; resources, J.Y.; data curation, A.S. and J.Y.; writing—original draft preparation, A.S.; writing—review and editing, J.Y.; visualization, A.S. and J.Y.; supervision, J.Y.; project administration, J.Y.; funding acquisition, J.Y. All authors have read and agreed to the published version of the manuscript.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

Not applicable.

## Conflicts of Interest

The authors declare no conflict of interest.

## Funding Statement

The APC was funded by a President’s NSERC Research Fund from the University of Saskatchewan (Saskatoon, Saskatchewan, Canada), grant number 424844 (J.Y.).

## Footnotes

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

## References

* 1.Fontana D.C., Roddenberry G. Star Trek: The Next Generation 1; 1987. [(accessed on 7 February 2023)]. Available online: <http://www.leethomson.myzen.co.uk/Star_Trek/2_The_Next_Generation/Star_Trek_-_The_Next_Generation_Season_1/Star_Trek_-_The_Next_Generation_1x01-102_-_Encounter_at_Farpoint.pdf>.
* 2.Cole M.D. Vostok 1: First Human in Space. Enslow Publishing LLC; New York, NY, USA: 1995.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Vostok%201:%20First%20Human%20in%20Space&author=M.D.%20Cole&publication_year=1995&)]
* 3.Loff S. Apollo 11 Mission Overview, NASA. [(accessed on 24 March 2022)];2015 Available online: <https://www.nasa.gov/mission_pages/apollo/missions/apollo11.html>.
* 4.Garcia M. International Space Station. NASA. [(accessed on 24 March 2022)];2015 Available online: <https://www.nasa.gov/mission_pages/station/main>.
* 5.Greicius T. Mars Perseverance Rover. NASA. [(accessed on 24 March 2022)];2016 Available online: <https://www.nasa.gov/perseverance>.
* 6.Mars Exploration Program. Mars Curiosity Rover. NASA. [(accessed on 24 March 2022)];2021 Available online: <https://mars.nasa.gov/msl/>
* 7.Loff S. Commercial Space Transportation. NASA. [(accessed on 24 March 2022)];2015 Available online: <https://www.nasa.gov/exploration/commercial>.
* 8.Guzman A. Low-Earth Orbit Economy. NASA. [(accessed on 24 March 2022)];2021 Available online: <https://www.nasa.gov/leo-economy>.
* 9.Gateway, NASA. [(accessed on 24 March 2022)];2019 Available online: <https://www.nasa.gov/gateway>.
* 10.Gopalakrishnan R., Genc K.O., Rice A.J., Lee S.M., Evans H.J., Maender C.C., Ilaslan H., Cavanagh P.R. Muscle volume, strength, endurance, and exercise loads during 6-month missions in space. Aviat. Space Environ. Med. 2010;81:91–102. doi: 10.3357/ASEM.2583.2010. [[DOI](https://doi.org/10.3357/ASEM.2583.2010)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20131648/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Aviat.%20Space%20Environ.%20Med.&title=Muscle%20volume,%20strength,%20endurance,%20and%20exercise%20loads%20during%206-month%20missions%20in%20space&author=R.%20Gopalakrishnan&author=K.O.%20Genc&author=A.J.%20Rice&author=S.M.%20Lee&author=H.J.%20Evans&volume=81&publication_year=2010&pages=91-102&pmid=20131648&doi=10.3357/ASEM.2583.2010&)]
* 11.Trappe S., Costill D., Gallagher P., Creer A., Peters J.R., Evans H., Riley D.A., Fitts R.H. Exercise in space: Human skeletal muscle after 6 months aboard the International Space Station. J. Appl. Physiol. 2009;106:1159–1168. doi: 10.1152/japplphysiol.91578.2008. [[DOI](https://doi.org/10.1152/japplphysiol.91578.2008)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19150852/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Appl.%20Physiol.&title=Exercise%20in%20space:%20Human%20skeletal%20muscle%20after%206%20months%20aboard%20the%20International%20Space%20Station&author=S.%20Trappe&author=D.%20Costill&author=P.%20Gallagher&author=A.%20Creer&author=J.R.%20Peters&volume=106&publication_year=2009&pages=1159-1168&pmid=19150852&doi=10.1152/japplphysiol.91578.2008&)]
* 12.Vogel J.M., Whittle M.W. Proceedings: Bone mineral content changes in the Skylab astronauts. Am. J. Roentgenol. 1976;126:1296–1297. doi: 10.2214/ajr.126.6.1296. [[DOI](https://doi.org/10.2214/ajr.126.6.1296)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/179415/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Roentgenol.&title=Proceedings:%20Bone%20mineral%20content%20changes%20in%20the%20Skylab%20astronauts&author=J.M.%20Vogel&author=M.W.%20Whittle&volume=126&publication_year=1976&pages=1296-1297&pmid=179415&doi=10.2214/ajr.126.6.1296&)]
* 13.Vico L., Hargens A. Skeletal changes during and after spaceflight. Nat. Rev. Rheumatol. 2018;14:229–245. doi: 10.1038/nrrheum.2018.37. [[DOI](https://doi.org/10.1038/nrrheum.2018.37)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29559713/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Rev.%20Rheumatol.&title=Skeletal%20changes%20during%20and%20after%20spaceflight&author=L.%20Vico&author=A.%20Hargens&volume=14&publication_year=2018&pages=229-245&pmid=29559713&doi=10.1038/nrrheum.2018.37&)]
* 14.Akiyama T., Horie K., Hinoi E., Hiraiwa M., Kato A., Maekawa Y., Takahashi A., Furukawa S. How does spaceflight affect the acquired immune system? NPJ Microgravity. 2020;6:14. doi: 10.1038/s41526-020-0104-1. [[DOI](https://doi.org/10.1038/s41526-020-0104-1)] [[PMC free article](/articles/PMC7206142/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32411817/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=How%20does%20spaceflight%20affect%20the%20acquired%20immune%20system?&author=T.%20Akiyama&author=K.%20Horie&author=E.%20Hinoi&author=M.%20Hiraiwa&author=A.%20Kato&volume=6&publication_year=2020&pages=14&pmid=32411817&doi=10.1038/s41526-020-0104-1&)]
* 15.Crucian B.E., Choukèr A., Simpson R.J., Mehta S., Marshall G., Smith S.M., Zwart S.R., Heer M., Ponomarev S., Whitmire A., et al. Immune System Dysregulation During Spaceflight: Potential Countermeasures for Deep Space Exploration Missions. Front. Immunol. 2018;9:1437. doi: 10.3389/fimmu.2018.01437. [[DOI](https://doi.org/10.3389/fimmu.2018.01437)] [[PMC free article](/articles/PMC6038331/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30018614/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Immunol.&title=Immune%20System%20Dysregulation%20During%20Spaceflight:%20Potential%20Countermeasures%20for%20Deep%20Space%20Exploration%20Missions&author=B.E.%20Crucian&author=A.%20Chouk%C3%A8r&author=R.J.%20Simpson&author=S.%20Mehta&author=G.%20Marshall&volume=9&publication_year=2018&pages=1437&pmid=30018614&doi=10.3389/fimmu.2018.01437&)]
* 16.Smith S.M., Heer M., Shackelford L.C., Sibonga J.D., Spatz J., Pietrzyk R.A., Hudson E.K., Zwart S.R. Bone metabolism and renal stone risk during International Space Station missions. Bone. 2015;81:712–720. doi: 10.1016/j.bone.2015.10.002. [[DOI](https://doi.org/10.1016/j.bone.2015.10.002)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26456109/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bone&title=Bone%20metabolism%20and%20renal%20stone%20risk%20during%20International%20Space%20Station%20missions&author=S.M.%20Smith&author=M.%20Heer&author=L.C.%20Shackelford&author=J.D.%20Sibonga&author=J.%20Spatz&volume=81&publication_year=2015&pages=712-720&pmid=26456109&doi=10.1016/j.bone.2015.10.002&)]
* 17.Roy-O’Reilly M., Mulavara A., Williams T. A review of alterations to the brain during spaceflight and the potential relevance to crew in long-duration space exploration. NPJ Microgravity. 2021;7:5. doi: 10.1038/s41526-021-00133-z. [[DOI](https://doi.org/10.1038/s41526-021-00133-z)] [[PMC free article](/articles/PMC7887220/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33594073/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=A%20review%20of%20alterations%20to%20the%20brain%20during%20spaceflight%20and%20the%20potential%20relevance%20to%20crew%20in%20long-duration%20space%20exploration&author=M.%20Roy-O%E2%80%99Reilly&author=A.%20Mulavara&author=T.%20Williams&volume=7&publication_year=2021&pages=5&pmid=33594073&doi=10.1038/s41526-021-00133-z&)]
* 18.Kalb R., Solomon D. Space exploration, Mars, and the nervous system. Arch. Neurol. 2007;64:485–490. doi: 10.1001/archneur.64.4.485. [[DOI](https://doi.org/10.1001/archneur.64.4.485)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17420309/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Arch.%20Neurol.&title=Space%20exploration,%20Mars,%20and%20the%20nervous%20system&author=R.%20Kalb&author=D.%20Solomon&volume=64&publication_year=2007&pages=485-490&pmid=17420309&doi=10.1001/archneur.64.4.485&)]
* 19.Vernice N.A., Meydan C., Afshinnekoo E., Mason C.E. Long-term spaceflight and the cardiovascular system. Precis. Clin. Med. 2020;3:284–291. doi: 10.1093/pcmedi/pbaa022. [[DOI](https://doi.org/10.1093/pcmedi/pbaa022)] [[PMC free article](/articles/PMC7757439/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33391848/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Precis.%20Clin.%20Med.&title=Long-term%20spaceflight%20and%20the%20cardiovascular%20system&author=N.A.%20Vernice&author=C.%20Meydan&author=E.%20Afshinnekoo&author=C.E.%20Mason&volume=3&publication_year=2020&pages=284-291&pmid=33391848&doi=10.1093/pcmedi/pbaa022&)]
* 20.Hughson R.L., Helm A., Durante M. Heart in space: Effect of the extraterrestrial environment on the cardiovascular system. Nat. Rev. Cardiol. 2018;15:167–180. doi: 10.1038/nrcardio.2017.157. [[DOI](https://doi.org/10.1038/nrcardio.2017.157)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29053152/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Rev.%20Cardiol.&title=Heart%20in%20space:%20Effect%20of%20the%20extraterrestrial%20environment%20on%20the%20cardiovascular%20system&author=R.L.%20Hughson&author=A.%20Helm&author=M.%20Durante&volume=15&publication_year=2018&pages=167-180&pmid=29053152&doi=10.1038/nrcardio.2017.157&)]
* 21.Cucinotta F.A., Schimmerling W., Wilson J.W., Peterson L.E., Badhwar G.D., Saganti P.B., Dicello J.F. Space radiation cancer risks and uncertainties for Mars missions. Radiat. Res. 2001;156:682–688. doi: 10.1667/0033-7587(2001)156[0682:SRCRAU]2.0.CO;2. [[DOI](https://doi.org/10.1667/0033-7587%282001%29156%5B0682%3ASRCRAU%5D2.0.CO;2)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11604093/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Space%20radiation%20cancer%20risks%20and%20uncertainties%20for%20Mars%20missions&author=F.A.%20Cucinotta&author=W.%20Schimmerling&author=J.W.%20Wilson&author=L.E.%20Peterson&author=G.D.%20Badhwar&volume=156&publication_year=2001&pages=682-688&pmid=11604093&doi=10.1667/0033-7587(2001)156%5B0682:SRCRAU%5D2.0.CO;2&)]
* 22.Ahn C.B., Lee J.H., Han D.G., Kang H.W., Lee S.H., Lee J.I., Son K.H., Lee J.W. Simulated microgravity with floating environment promotes migration of non-small cell lung cancers. Sci. Rep. 2019;9:14553. doi: 10.1038/s41598-019-50736-6. [[DOI](https://doi.org/10.1038/s41598-019-50736-6)] [[PMC free article](/articles/PMC6787256/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31601869/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Simulated%20microgravity%20with%20floating%20environment%20promotes%20migration%20of%20non-small%20cell%20lung%20cancers&author=C.B.%20Ahn&author=J.H.%20Lee&author=D.G.%20Han&author=H.W.%20Kang&author=S.H.%20Lee&volume=9&publication_year=2019&pages=14553&pmid=31601869&doi=10.1038/s41598-019-50736-6&)]
* 23.Lewis M.L., Reynolds J.L., Cubano L.A., Hatton J.P., Lawless B.D., Piepmeier E.H. Spaceflight alters microtubules and increases apoptosis in human lymphocytes (Jurkat) FASEB J. 1998;12:1007–1018. doi: 10.1096/fasebj.12.11.1007. [[DOI](https://doi.org/10.1096/fasebj.12.11.1007)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/9707173/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=FASEB%20J.&title=Spaceflight%20alters%20microtubules%20and%20increases%20apoptosis%20in%20human%20lymphocytes%20(Jurkat)&author=M.L.%20Lewis&author=J.L.%20Reynolds&author=L.A.%20Cubano&author=J.P.%20Hatton&author=B.D.%20Lawless&volume=12&publication_year=1998&pages=1007-1018&pmid=9707173&doi=10.1096/fasebj.12.11.1007&)]
* 24.Krüger M., Melnik D., Kopp S., Buken C., Sahana J., Bauer J., Wehland M., Hemmersbach R., Corydon T.J., Infanger M., et al. Fighting Thyroid Cancer with Microgravity Research. Int. J. Mol. Sci. 2019;20:2553. doi: 10.3390/ijms20102553. [[DOI](https://doi.org/10.3390/ijms20102553)] [[PMC free article](/articles/PMC6566201/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31137658/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci.&title=Fighting%20Thyroid%20Cancer%20with%20Microgravity%20Research&author=M.%20Kr%C3%BCger&author=D.%20Melnik&author=S.%20Kopp&author=C.%20Buken&author=J.%20Sahana&volume=20&publication_year=2019&pages=2553&pmid=31137658&doi=10.3390/ijms20102553&)]
* 25.Terada M., Seki M., Takahashi R., Yamada S., Higashibata A., Majima H.J., Sudoh M., Mukai C., Ishioka N. Effects of a Closed Space Environment on Gene Expression in Hair Follicles of Astronauts in the International Space Station. PloS one. 2016;11:e0150801. doi: 10.1371/journal.pone.0150801. [[DOI](https://doi.org/10.1371/journal.pone.0150801)] [[PMC free article](/articles/PMC4814050/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27029003/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20one&title=Effects%20of%20a%20Closed%20Space%20Environment%20on%20Gene%20Expression%20in%20Hair%20Follicles%20of%20Astronauts%20in%20the%20International%20Space%20Station&author=M.%20Terada&author=M.%20Seki&author=R.%20Takahashi&author=S.%20Yamada&author=A.%20Higashibata&volume=11&publication_year=2016&pages=e0150801&pmid=27029003&doi=10.1371/journal.pone.0150801&)]
* 26.McKinney W. Data Structures for Statistical Computing in python; Proceedings of the Python in Science Conference; Austin TX, USA. 28–30 June 2010. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20Python%20in%20Science%20Conference&title=Data%20Structures%20for%20Statistical%20Computing%20in%20python&author=W.%20McKinney&)]
* 27.Wang L., Feng Z., Wang X., Wang X., Zhang X. DEGseq: An R package for identifying differentially expressed genes from RNA-seq data. Bioinformatics. 2010;26:136–138. doi: 10.1093/bioinformatics/btp612. [[DOI](https://doi.org/10.1093/bioinformatics/btp612)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19855105/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=DEGseq:%20An%20R%20package%20for%20identifying%20differentially%20expressed%20genes%20from%20RNA-seq%20data&author=L.%20Wang&author=Z.%20Feng&author=X.%20Wang&author=X.%20Wang&author=X.%20Zhang&volume=26&publication_year=2010&pages=136-138&pmid=19855105&doi=10.1093/bioinformatics/btp612&)]
* 28.Lynn D.J., Winsor G.L., Chan C., Richard N., Laird M.R., Barsky A., Gardy J.L., Roche F.M., Chan T.H., Shah N., et al. InnateDB: Facilitating systems-level analyses of the mammalian innate immune response. Mol. Syst. Biol. 2008;4:218. doi: 10.1038/msb.2008.55. [[DOI](https://doi.org/10.1038/msb.2008.55)] [[PMC free article](/articles/PMC2564732/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18766178/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol.%20Syst.%20Biol.&title=InnateDB:%20Facilitating%20systems-level%20analyses%20of%20the%20mammalian%20innate%20immune%20response&author=D.J.%20Lynn&author=G.L.%20Winsor&author=C.%20Chan&author=N.%20Richard&author=M.R.%20Laird&volume=4&publication_year=2008&pages=218&pmid=18766178&doi=10.1038/msb.2008.55&)]
* 29.Stark C., Breitkreutz B.J., Reguly T., Boucher L., Breitkreutz A., Tyers M. BioGRID: A general repository for interaction datasets. Nucleic Acids Res. 2006;34:D535–D539. doi: 10.1093/nar/gkj109. [[DOI](https://doi.org/10.1093/nar/gkj109)] [[PMC free article](/articles/PMC1347471/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16381927/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=BioGRID:%20A%20general%20repository%20for%20interaction%20datasets&author=C.%20Stark&author=B.J.%20Breitkreutz&author=T.%20Reguly&author=L.%20Boucher&author=A.%20Breitkreutz&volume=34&publication_year=2006&pages=D535-D539&pmid=16381927&doi=10.1093/nar/gkj109&)]
* 30.Piñero J., Ramírez-Anguita J.M., Saüch-Pitarch J., Ronzano F., Centeno E., Sanz F., Furlong L.I. The DisGeNET knowledge platform for disease genomics: 2019 update. Nucleic Acids Res. 2020;48:D845–D855. doi: 10.1093/nar/gkz1021. [[DOI](https://doi.org/10.1093/nar/gkz1021)] [[PMC free article](/articles/PMC7145631/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31680165/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=The%20DisGeNET%20knowledge%20platform%20for%20disease%20genomics:%202019%20update&author=J.%20Pi%C3%B1ero&author=J.M.%20Ram%C3%ADrez-Anguita&author=J.%20Sa%C3%BCch-Pitarch&author=F.%20Ronzano&author=E.%20Centeno&volume=48&publication_year=2020&pages=D845-D855&pmid=31680165&doi=10.1093/nar/gkz1021&)]
* 31.Shannon P., Markiel A., Ozier O., Baliga N.S., Wang J.T., Ramage D., Amin N., Schwikowski B., Ideker T. Cytoscape: A software environment for integrated models of biomolecular interaction networks. Genome Res. 2003;13:2498–2504. doi: 10.1101/gr.1239303. [[DOI](https://doi.org/10.1101/gr.1239303)] [[PMC free article](/articles/PMC403769/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/14597658/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genome%20Res.&title=Cytoscape:%20A%20software%20environment%20for%20integrated%20models%20of%20biomolecular%20interaction%20networks&author=P.%20Shannon&author=A.%20Markiel&author=O.%20Ozier&author=N.S.%20Baliga&author=J.T.%20Wang&volume=13&publication_year=2003&pages=2498-2504&pmid=14597658&doi=10.1101/gr.1239303&)]
* 32.Wishart D.S., Knox C., Guo A.C., Shrivastava S., Hassanali M., Stothard P., Chang Z., Woolsey J. DrugBank: A comprehensive resource for in silico drug discovery and exploration. Nucleic Acids Res. 2006;34:D668–D672. doi: 10.1093/nar/gkj067. [[DOI](https://doi.org/10.1093/nar/gkj067)] [[PMC free article](/articles/PMC1347430/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16381955/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=DrugBank:%20A%20comprehensive%20resource%20for%20in%20silico%20drug%20discovery%20and%20exploration&author=D.S.%20Wishart&author=C.%20Knox&author=A.C.%20Guo&author=S.%20Shrivastava&author=M.%20Hassanali&volume=34&publication_year=2006&pages=D668-D672&pmid=16381955&doi=10.1093/nar/gkj067&)]
* 33.Huang H.Y., Lin Y.C., Li J., Huang K.Y., Shrestha S., Hong H.C., Tang Y., Chen Y.G., Jin C.N., Yu Y., et al. miRTarBase 2020: Updates to the experimentally validated microRNA-target interaction database. Nucleic Acids Res. 2020;48:D148–D154. doi: 10.1093/nar/gkz896. [[DOI](https://doi.org/10.1093/nar/gkz896)] [[PMC free article](/articles/PMC7145596/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31647101/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=miRTarBase%202020:%20Updates%20to%20the%20experimentally%20validated%20microRNA-target%20interaction%20database&author=H.Y.%20Huang&author=Y.C.%20Lin&author=J.%20Li&author=K.Y.%20Huang&author=S.%20Shrestha&volume=48&publication_year=2020&pages=D148-D154&pmid=31647101&doi=10.1093/nar/gkz896&)]
* 34.Lin Y.H., Zhen Y.Y., Chien K.Y., Lee I.C., Lin W.C., Chen M.Y., Pai L.M. LIMCH1 regulates nonmuscle myosin-II activity and suppresses cell migration. Mol. Bio. Cell. 2017;28:1054–1065. doi: 10.1091/mbc.e15-04-0218. [[DOI](https://doi.org/10.1091/mbc.e15-04-0218)] [[PMC free article](/articles/PMC5391182/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28228547/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol.%20Bio.%20Cell&title=LIMCH1%20regulates%20nonmuscle%20myosin-II%20activity%20and%20suppresses%20cell%20migration&author=Y.H.%20Lin&author=Y.Y.%20Zhen&author=K.Y.%20Chien&author=I.C.%20Lee&author=W.C.%20Lin&volume=28&publication_year=2017&pages=1054-1065&pmid=28228547&doi=10.1091/mbc.e15-04-0218&)]
* 35.Aguilar-Cuenca R., Juanes-García A., Vicente-Manzanares M. Myosin II in mechanotransduction: Master and commander of cell migration, morphogenesis, and cancer. Cell Mol. Life Sci. 2013;71:479–492. doi: 10.1007/s00018-013-1439-5. [[DOI](https://doi.org/10.1007/s00018-013-1439-5)] [[PMC free article](/articles/PMC11113847/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23934154/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Mol.%20Life%20Sci.&title=Myosin%20II%20in%20mechanotransduction:%20Master%20and%20commander%20of%20cell%20migration,%20morphogenesis,%20and%20cancer&author=R.%20Aguilar-Cuenca&author=A.%20Juanes-Garc%C3%ADa&author=M.%20Vicente-Manzanares&volume=71&publication_year=2013&pages=479-492&pmid=23934154&doi=10.1007/s00018-013-1439-5&)]
* 36.Schilling D., Pittelkow M.R., Kumar R. IEX-1, an immediate early gene, increases the rate of apoptosis in keratinocytes. Oncogene. 2001;20:7992–7997. doi: 10.1038/sj.onc.1204965. [[DOI](https://doi.org/10.1038/sj.onc.1204965)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11753682/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Oncogene&title=IEX-1,%20an%20immediate%20early%20gene,%20increases%20the%20rate%20of%20apoptosis%20in%20keratinocytes&author=D.%20Schilling&author=M.R.%20Pittelkow&author=R.%20Kumar&volume=20&publication_year=2001&pages=7992-7997&pmid=11753682&doi=10.1038/sj.onc.1204965&)]
* 37.Arlt A., Schäfer H. Role of the immediate early response 3 (IER3) gene in cellular stress response, inflammation and tumorigenesis. Eur. J. Cell Biol. 2011;90:545–552. doi: 10.1016/j.ejcb.2010.10.002. [[DOI](https://doi.org/10.1016/j.ejcb.2010.10.002)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21112119/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Eur.%20J.%20Cell%20Biol.&title=Role%20of%20the%20immediate%20early%20response%203%20(IER3)%20gene%20in%20cellular%20stress%20response,%20inflammation%20and%20tumorigenesis&author=A.%20Arlt&author=H.%20Sch%C3%A4fer&volume=90&publication_year=2011&pages=545-552&pmid=21112119&doi=10.1016/j.ejcb.2010.10.002&)]
* 38.Ustyugova I.V., Zhi L., Abramowitz J., Birnbaumer L., Wu M.X. IEX-1 deficiency protects against colonic cancer. Mol. Cancer Res. 2012;10:760–767. doi: 10.1158/1541-7786.MCR-11-0556. [[DOI](https://doi.org/10.1158/1541-7786.MCR-11-0556)] [[PMC free article](/articles/PMC3465947/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22550081/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol.%20Cancer%20Res.&title=IEX-1%20deficiency%20protects%20against%20colonic%20cancer&author=I.V.%20Ustyugova&author=L.%20Zhi&author=J.%20Abramowitz&author=L.%20Birnbaumer&author=M.X.%20Wu&volume=10&publication_year=2012&pages=760-767&pmid=22550081&doi=10.1158/1541-7786.MCR-11-0556&)]
* 39.Akilov O.E., Wu M.X., Ustyugova I.V., Falo L.D., Geskin L.J. Resistance of Sézary cells to TNF-α-induced apoptosis is mediated in part by a loss of TNFR1 and a high level of the IER3 expression. Exp. Dermatol. 2012;21:287–292. doi: 10.1111/j.1600-0625.2012.01452.x. [[DOI](https://doi.org/10.1111/j.1600-0625.2012.01452.x)] [[PMC free article](/articles/PMC3306129/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22417305/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Exp.%20Dermatol.&title=Resistance%20of%20S%C3%A9zary%20cells%20to%20TNF-%CE%B1-induced%20apoptosis%20is%20mediated%20in%20part%20by%20a%20loss%20of%20TNFR1%20and%20a%20high%20level%20of%20the%20IER3%20expression&author=O.E.%20Akilov&author=M.X.%20Wu&author=I.V.%20Ustyugova&author=L.D.%20Falo&author=L.J.%20Geskin&volume=21&publication_year=2012&pages=287-292&pmid=22417305&doi=10.1111/j.1600-0625.2012.01452.x&)]
* 40.Rasmussen L.M., Frederiksen K.S., Din N., Galsgaard E., Christensen L., Berchtold M.W., Panina S. Prolactin and oestrogen synergistically regulate gene expression and proliferation of breast cancer cells. Endocr. Relat. Cancer. 2010;17:809–822. doi: 10.1677/ERC-09-0326. [[DOI](https://doi.org/10.1677/ERC-09-0326)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20601496/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Endocr.%20Relat.%20Cancer&title=Prolactin%20and%20oestrogen%20synergistically%20regulate%20gene%20expression%20and%20proliferation%20of%20breast%20cancer%20cells&author=L.M.%20Rasmussen&author=K.S.%20Frederiksen&author=N.%20Din&author=E.%20Galsgaard&author=L.%20Christensen&volume=17&publication_year=2010&pages=809-822&pmid=20601496&doi=10.1677/ERC-09-0326&)]
* 41.Bergamin L.S., Penolazzi L., Lambertini E., Falzoni S., Sarti A.C., Molle C.M., Gendron F.P., De Bonis P., Di Virgilio F., Piva R. Expression and function of the P2X7 receptor in human osteoblasts: The role of NFATc1 transcription factor. J. Cell Physiol. 2021;236:641–652. doi: 10.1002/jcp.29891. [[DOI](https://doi.org/10.1002/jcp.29891)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32583512/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Cell%20Physiol.&title=Expression%20and%20function%20of%20the%20P2X7%20receptor%20in%20human%20osteoblasts:%20The%20role%20of%20NFATc1%20transcription%20factor&author=L.S.%20Bergamin&author=L.%20Penolazzi&author=E.%20Lambertini&author=S.%20Falzoni&author=A.C.%20Sarti&volume=236&publication_year=2021&pages=641-652&pmid=32583512&doi=10.1002/jcp.29891&)]
* 42.Winslow M.M., Pan M., Starbuck M., Gallo E.M., Deng L., Karsenty G., Crabtree G.R. Calcineurin/NFAT signaling in osteoblasts regulates bone mass. Dev. Cell. 2006;10:771–782. doi: 10.1016/j.devcel.2006.04.006. [[DOI](https://doi.org/10.1016/j.devcel.2006.04.006)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16740479/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Dev.%20Cell&title=Calcineurin/NFAT%20signaling%20in%20osteoblasts%20regulates%20bone%20mass&author=M.M.%20Winslow&author=M.%20Pan&author=M.%20Starbuck&author=E.M.%20Gallo&author=L.%20Deng&volume=10&publication_year=2006&pages=771-782&pmid=16740479&doi=10.1016/j.devcel.2006.04.006&)]
* 43.Klein-Hessling S., Muhammad K., Klein M., Pusch T., Rudolf R., Flöter J., Qureischi M., Beilhack A., Vaeth M., Kummerow C., et al. NFATc1 controls the cytotoxicity of CD8+ T cells. Nat. Commun. 2017;8:511. doi: 10.1038/s41467-017-00612-6. [[DOI](https://doi.org/10.1038/s41467-017-00612-6)] [[PMC free article](/articles/PMC5593830/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28894104/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Commun.&title=NFATc1%20controls%20the%20cytotoxicity%20of%20CD8+%20T%20cells&author=S.%20Klein-Hessling&author=K.%20Muhammad&author=M.%20Klein&author=T.%20Pusch&author=R.%20Rudolf&volume=8&publication_year=2017&pages=511&pmid=28894104&doi=10.1038/s41467-017-00612-6&)]
* 44.Kulkarni R.M., Greenberg J.M., Akeson A.L. NFATc1 regulates lymphatic endothelial development. Mech. Dev. 2009;126:350–365. doi: 10.1016/j.mod.2009.02.003. [[DOI](https://doi.org/10.1016/j.mod.2009.02.003)] [[PMC free article](/articles/PMC2680470/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19233265/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mech.%20Dev.&title=NFATc1%20regulates%20lymphatic%20endothelial%20development&author=R.M.%20Kulkarni&author=J.M.%20Greenberg&author=A.L.%20Akeson&volume=126&publication_year=2009&pages=350-365&pmid=19233265&doi=10.1016/j.mod.2009.02.003&)]
* 45.Chang C.P., Neilson J.R., Bayle J.H., Gestwicki J.E., Kuo A., Stankunas K., Graef I.A., Crabtree G.R. A field of myocardial-endocardial NFAT signaling underlies heart valve morphogenesis. Cell. 2004;118:649–663. doi: 10.1016/j.cell.2004.08.010. [[DOI](https://doi.org/10.1016/j.cell.2004.08.010)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15339668/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell&title=A%20field%20of%20myocardial-endocardial%20NFAT%20signaling%20underlies%20heart%20valve%20morphogenesis&author=C.P.%20Chang&author=J.R.%20Neilson&author=J.H.%20Bayle&author=J.E.%20Gestwicki&author=A.%20Kuo&volume=118&publication_year=2004&pages=649-663&pmid=15339668&doi=10.1016/j.cell.2004.08.010&)]
* 46.Xu W., Gu J., Ren Q., Shi Y., Xia Q., Wang J., Wang S., Wang Y., Wang J. NFATC1 promotes cell growth and tumorigenesis in ovarian cancer up-regulating c-Myc through ERK1/2/p38 MAPK signal pathway. Tumour Biol. 2016;37:4493–4500. doi: 10.1007/s13277-015-4245-x. [[DOI](https://doi.org/10.1007/s13277-015-4245-x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26501422/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Tumour%20Biol.&title=NFATC1%20promotes%20cell%20growth%20and%20tumorigenesis%20in%20ovarian%20cancer%20up-regulating%20c-Myc%20through%20ERK1/2/p38%20MAPK%20signal%20pathway&author=W.%20Xu&author=J.%20Gu&author=Q.%20Ren&author=Y.%20Shi&author=Q.%20Xia&volume=37&publication_year=2016&pages=4493-4500&pmid=26501422&doi=10.1007/s13277-015-4245-x&)]
* 47.Cesca F., Yabe A., Spencer-Dene B., Arrigoni A., Al-Qatari M., Henderson D., Phillips H., Koltzenburg M., Benfenati F., Schiavo G. Kidins220/ARMS is an essential modulator of cardiovascular and nervous system development. Cell Death Dis. 2011;2:e226. doi: 10.1038/cddis.2011.108. [[DOI](https://doi.org/10.1038/cddis.2011.108)] [[PMC free article](/articles/PMC3223693/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22048169/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Death%20Dis.&title=Kidins220/ARMS%20is%20an%20essential%20modulator%20of%20cardiovascular%20and%20nervous%20system%20development&author=F.%20Cesca&author=A.%20Yabe&author=B.%20Spencer-Dene&author=A.%20Arrigoni&author=M.%20Al-Qatari&volume=2&publication_year=2011&pages=e226&pmid=22048169&doi=10.1038/cddis.2011.108&)]
* 48.Cesca F., Yabe A., Spencer-Dene B., Scholz-Starke J., Medrihan L., Maden C.H., Gerhardt H., Orriss I.R., Baldelli P., Al-Qatari M., et al. Kidins220/ARMS mediates the integration of the neurotrophin and VEGF pathways in the vascular and nervous systems. Cell Death Differ. 2012;19:194–208. doi: 10.1038/cdd.2011.141. [[DOI](https://doi.org/10.1038/cdd.2011.141)] [[PMC free article](/articles/PMC3263493/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22048155/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Death%20Differ.&title=Kidins220/ARMS%20mediates%20the%20integration%20of%20the%20neurotrophin%20and%20VEGF%20pathways%20in%20the%20vascular%20and%20nervous%20systems&author=F.%20Cesca&author=A.%20Yabe&author=B.%20Spencer-Dene&author=J.%20Scholz-Starke&author=L.%20Medrihan&volume=19&publication_year=2012&pages=194-208&pmid=22048155&doi=10.1038/cdd.2011.141&)]
* 49.van Dam S., Võsa U., van der Graaf A., Franke L., de Magalhães J.P. Gene co-expression analysis for functional classification and gene-disease predictions. Brief. Bioinform. 2018;19:575–592. doi: 10.1093/bib/bbw139. [[DOI](https://doi.org/10.1093/bib/bbw139)] [[PMC free article](/articles/PMC6054162/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28077403/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Brief.%20Bioinform.&title=Gene%20co-expression%20analysis%20for%20functional%20classification%20and%20gene-disease%20predictions&author=S.%20van%20Dam&author=U.%20V%C3%B5sa&author=A.%20van%20der%20Graaf&author=L.%20Franke&author=J.P.%20de%20Magalh%C3%A3es&volume=19&publication_year=2018&pages=575-592&pmid=28077403&doi=10.1093/bib/bbw139&)]
* 50.Sakharkar M.K., Dhillon S.K., Chidambaram S.B., Essa M.M., Yang J. Gene Pair Correlation Coefficients in Sphingolipid Metabolic Pathway as a Potential Prognostic Biomarker for Breast Cancer. Cancers. 2020;12:1747. doi: 10.3390/cancers12071747. [[DOI](https://doi.org/10.3390/cancers12071747)] [[PMC free article](/articles/PMC7409333/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32630169/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cancers&title=Gene%20Pair%20Correlation%20Coefficients%20in%20Sphingolipid%20Metabolic%20Pathway%20as%20a%20Potential%20Prognostic%20Biomarker%20for%20Breast%20Cancer&author=M.K.%20Sakharkar&author=S.K.%20Dhillon&author=S.B.%20Chidambaram&author=M.M.%20Essa&author=J.%20Yang&volume=12&publication_year=2020&pages=1747&pmid=32630169&doi=10.3390/cancers12071747&)]
* 51.Sakharkar M.K., Dhillon S.K., Rajamanickam K., Heng B., Braidy N., Guillemin G.J., Yang J. Alteration in Gene Pair Correlations in Tryptophan Metabolism as a Hallmark in Cancer Diagnosis. Int. J. Tryptophan Res. 2020;13:1178646920977013. doi: 10.1177/1178646920977013. [[DOI](https://doi.org/10.1177/1178646920977013)] [[PMC free article](/articles/PMC7734567/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33354111/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Tryptophan%20Res.&title=Alteration%20in%20Gene%20Pair%20Correlations%20in%20Tryptophan%20Metabolism%20as%20a%20Hallmark%20in%20Cancer%20Diagnosis&author=M.K.%20Sakharkar&author=S.K.%20Dhillon&author=K.%20Rajamanickam&author=B.%20Heng&author=N.%20Braidy&volume=13&publication_year=2020&pages=1178646920977013&pmid=33354111&doi=10.1177/1178646920977013&)]
* 52.Sakharkar M.K., Rajamanickam K., Ji S., Dhillon S.K., Yang J. Pairwise correlation of genes involved in glucose metabolism: A potential diagnostic marker of cancer? Genes Cancer. 2021;12:69–76. doi: 10.18632/genesandcancer.216. [[DOI](https://doi.org/10.18632/genesandcancer.216)] [[PMC free article](/articles/PMC8211569/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34163562/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genes%20Cancer&title=Pairwise%20correlation%20of%20genes%20involved%20in%20glucose%20metabolism:%20A%20potential%20diagnostic%20marker%20of%20cancer?&author=M.K.%20Sakharkar&author=K.%20Rajamanickam&author=S.%20Ji&author=S.K.%20Dhillon&author=J.%20Yang&volume=12&publication_year=2021&pages=69-76&pmid=34163562&doi=10.18632/genesandcancer.216&)]
* 53.Reynolds R.J., Bukhtiyarov I.V., Tikhonova G.I., Day S.M., Ushakov I.B., Gorchakova T. Contrapositive logic suggests space radiation not having a strong impact on mortality of US astronauts and Soviet and Russian cosmonauts. Sci. Rep. 2019;9:8583. doi: 10.1038/s41598-019-44858-0. [[DOI](https://doi.org/10.1038/s41598-019-44858-0)] [[PMC free article](/articles/PMC6609703/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31273231/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Contrapositive%20logic%20suggests%20space%20radiation%20not%20having%20a%20strong%20impact%20on%20mortality%20of%20US%20astronauts%20and%20Soviet%20and%20Russian%20cosmonauts&author=R.J.%20Reynolds&author=I.V.%20Bukhtiyarov&author=G.I.%20Tikhonova&author=S.M.%20Day&author=I.B.%20Ushakov&volume=9&publication_year=2019&pages=8583&pmid=31273231&doi=10.1038/s41598-019-44858-0&)]
* 54.Beheshti A., Chakravarty K., Fogle H., Fazelinia H., Silveira W., Boyko V., Polo S.L., Saravia-Butler A.M., Hardiman G., Taylor D., et al. Multi-omics analysis of multiple missions to space reveal a theme of lipid dysregulation in mouse liver. Sci. Rep. 2019;9:19195. doi: 10.1038/s41598-019-55869-2. [[DOI](https://doi.org/10.1038/s41598-019-55869-2)] [[PMC free article](/articles/PMC6915713/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31844325/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Multi-omics%20analysis%20of%20multiple%20missions%20to%20space%20reveal%20a%20theme%20of%20lipid%20dysregulation%20in%20mouse%20liver&author=A.%20Beheshti&author=K.%20Chakravarty&author=H.%20Fogle&author=H.%20Fazelinia&author=W.%20Silveira&volume=9&publication_year=2019&pages=19195&pmid=31844325&doi=10.1038/s41598-019-55869-2&)]
* 55.Kurosawa R., Sugimoto R., Imai H., Atsuji K., Yamada K., Kawano Y., Ohtsu I., Suzuki K. Impact of spaceflight and artificial gravity on sulfur metabolism in mouse liver: Sulfur metabolomic and transcriptomic analysis. Sci. Rep. 2021;11:21786. doi: 10.1038/s41598-021-01129-1. [[DOI](https://doi.org/10.1038/s41598-021-01129-1)] [[PMC free article](/articles/PMC8575787/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34750416/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Impact%20of%20spaceflight%20and%20artificial%20gravity%20on%20sulfur%20metabolism%20in%20mouse%20liver:%20Sulfur%20metabolomic%20and%20transcriptomic%20analysis&author=R.%20Kurosawa&author=R.%20Sugimoto&author=H.%20Imai&author=K.%20Atsuji&author=K.%20Yamada&volume=11&publication_year=2021&pages=21786&pmid=34750416&doi=10.1038/s41598-021-01129-1&)]
* 56.Garrett-Bakelman F.E., Darshi M., Green S.J., Gur R.C., Lin L., Macias B.R., McKenna M.J., Meydan C., Mishra T., Nasrini J., et al. The NASA Twins Study: A multidimensional analysis of a year-long human spaceflight. Science. 2019;364:eaau8650. doi: 10.1126/science.aau8650. [[DOI](https://doi.org/10.1126/science.aau8650)] [[PMC free article](/articles/PMC7580864/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30975860/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Science&title=The%20NASA%20Twins%20Study:%20A%20multidimensional%20analysis%20of%20a%20year-long%20human%20spaceflight&author=F.E.%20Garrett-Bakelman&author=M.%20Darshi&author=S.J.%20Green&author=R.C.%20Gur&author=L.%20Lin&volume=364&publication_year=2019&pages=eaau8650&pmid=30975860&doi=10.1126/science.aau8650&)]
* 57.Taylor R. Interpretation of the correlation coefficient: A basic review. J. Diagn. Med. Sonogr. 1990;6:35–39. doi: 10.1177/875647939000600106. [[DOI](https://doi.org/10.1177/875647939000600106)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Diagn.%20Med.%20Sonogr.&title=Interpretation%20of%20the%20correlation%20coefficient:%20A%20basic%20review&author=R.%20Taylor&volume=6&publication_year=1990&pages=35-39&doi=10.1177/875647939000600106&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

[Click here for additional data file.](/articles/instance/9964234/bin/life-13-00576-s001.zip) (2.3MB, zip)

### Data Availability Statement

Not applicable.