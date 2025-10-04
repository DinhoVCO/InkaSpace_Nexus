PLoS One

. 2021 Oct 12;16(10):e0250715. doi: [10.1371/journal.pone.0250715](https://doi.org/10.1371/journal.pone.0250715)

# RNAseq and RNA molecular barcoding reveal differential gene expression in cortical bone following hindlimb unloading in female mice

[Jordan M Spatz](https://pubmed.ncbi.nlm.nih.gov/?term=%22Spatz%20JM%22%5BAuthor%5D)

### Jordan M Spatz

1Center for Advanced Orthopedic Studies, Beth Israel Deaconess Medical Center, Boston, Massachusetts, United States of America

2University of California San Francisco School of Medicine, San Francisco, California, United States of America

3Harvard Medical School, Boston, Massachusetts, United States of America

Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Writing – review & editing

Find articles by [Jordan M Spatz](https://pubmed.ncbi.nlm.nih.gov/?term=%22Spatz%20JM%22%5BAuthor%5D)

1,2,3,#, [Frank C Ko](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ko%20FC%22%5BAuthor%5D)

### Frank C Ko

1Center for Advanced Orthopedic Studies, Beth Israel Deaconess Medical Center, Boston, Massachusetts, United States of America

3Harvard Medical School, Boston, Massachusetts, United States of America

Data curation, Formal analysis, Investigation, Methodology, Visualization, Writing – original draft, Writing – review & editing

Find articles by [Frank C Ko](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ko%20FC%22%5BAuthor%5D)

1,3,#, [Ugur M Ayturk](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ayturk%20UM%22%5BAuthor%5D)

### Ugur M Ayturk

3Harvard Medical School, Boston, Massachusetts, United States of America

4Boston Children’s Hospital, Boston, Massachusetts, United States of America

Data curation, Formal analysis, Investigation, Methodology, Writing – review & editing

Find articles by [Ugur M Ayturk](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ayturk%20UM%22%5BAuthor%5D)

3,4, [Matthew L Warman](https://pubmed.ncbi.nlm.nih.gov/?term=%22Warman%20ML%22%5BAuthor%5D)

### Matthew L Warman

3Harvard Medical School, Boston, Massachusetts, United States of America

4Boston Children’s Hospital, Boston, Massachusetts, United States of America

Formal analysis, Funding acquisition, Methodology, Supervision, Writing – review & editing

Find articles by [Matthew L Warman](https://pubmed.ncbi.nlm.nih.gov/?term=%22Warman%20ML%22%5BAuthor%5D)

3,4, [Mary L Bouxsein](https://pubmed.ncbi.nlm.nih.gov/?term=%22Bouxsein%20ML%22%5BAuthor%5D)

### Mary L Bouxsein

1Center for Advanced Orthopedic Studies, Beth Israel Deaconess Medical Center, Boston, Massachusetts, United States of America

3Harvard Medical School, Boston, Massachusetts, United States of America

Conceptualization, Funding acquisition, Investigation, Methodology, Supervision, Writing – original draft, Writing – review & editing

Find articles by [Mary L Bouxsein](https://pubmed.ncbi.nlm.nih.gov/?term=%22Bouxsein%20ML%22%5BAuthor%5D)

1,3,\*

Editor: Jung-Eun Kim5

* Author information
* Article notes
* Copyright and License information

1Center for Advanced Orthopedic Studies, Beth Israel Deaconess Medical Center, Boston, Massachusetts, United States of America

2University of California San Francisco School of Medicine, San Francisco, California, United States of America

3Harvard Medical School, Boston, Massachusetts, United States of America

4Boston Children’s Hospital, Boston, Massachusetts, United States of America

5Kyungpook National University School of Medicine, REPUBLIC OF KOREA

**Competing Interests:** No authors have competing interests.

✉

\* E-mail: mbouxsei@bidmc.harvard.edu

#

Contributed equally.

#### Roles

**Jordan M Spatz**: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Writing – review & editing

**Frank C Ko**: Data curation, Formal analysis, Investigation, Methodology, Visualization, Writing – original draft, Writing – review & editing

**Ugur M Ayturk**: Data curation, Formal analysis, Investigation, Methodology, Writing – review & editing

**Matthew L Warman**: Formal analysis, Funding acquisition, Methodology, Supervision, Writing – review & editing

**Mary L Bouxsein**: Conceptualization, Funding acquisition, Investigation, Methodology, Supervision, Writing – original draft, Writing – review & editing

**Jung-Eun Kim**: Editor

Received 2021 Jan 6; Accepted 2021 Apr 12; Collection date 2021.

© 2021 Spatz et al

This is an open access article distributed under the terms of the [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

[PMC Copyright notice](/about/copyright/)

PMCID: PMC8509868  PMID: [34637435](https://pubmed.ncbi.nlm.nih.gov/34637435/)

## Abstract

Disuse-induced bone loss is seen following spinal cord injury, prolonged bed rest, and exposure to microgravity. We performed whole transcriptomic profiling of cortical bone using RNA sequencing (RNAseq) and RNA molecular barcoding (NanoString) on a hindlimb unloading (HLU) mouse model to identify genes whose mRNA transcript abundances change in response to disuse. Eleven-week old female C57BL/6 mice were exposed to ambulatory loading or HLU for 7 days (n = 8/group). Total RNA from marrow-flushed femoral cortical bone was analyzed on HiSeq and NanoString platforms. The expression of several previously reported genes associated with Wnt signaling and metabolism was altered by HLU. Furthermore, the increased abundance of transcripts, such as Pfkfb3 and Mss51, after HLU imply these genes also have roles in the cortical bone’s response to altered mechanical loading. Our study demonstrates that an unbiased approach to assess the whole transcriptomic profile of cortical bone can reveal previously unidentified mechanosensitive genes and may eventually lead to novel targets to prevent disuse-induced osteoporosis.

## Introduction

Mechanical loading plays an important role during musculoskeletal development and maintenance. Reduced mechanical loading from extended immobilization, spinal cord injury, or spaceflight leads to decreased bone mass and mineral density in humans, which increases susceptibility to skeletal fractures. Biological mechanisms underlying skeletal deterioration due to reduced mechanical loading have been studied using hindlimb unloading rodent models, which demonstrated altered Wnt or IGF signaling or Rank/Rankl/Opg pathway [[1](#pone.0250715.ref001)–[5](#pone.0250715.ref005)]. These studies led to several clinical studies that explored the usage of existing or newly developed pharmacological therapies to counter immobilization or spaceflight induced bone loss [[6](#pone.0250715.ref006),[7](#pone.0250715.ref007)].

While prior studies in rodent models demonstrated signaling pathways that contribute to skeletal loss from reduced mechanical loading, limited candidate gene approached precluded exploration of other novel pathways that may also play an important role. Recent advances in whole transcriptome RNA deep sequencing (RNAseq) allow comprehensive, quantitative, and unbiased view of the complete RNA transcriptome. This high-throughput approach can allow identification novel pathways that are altered in response to reduced mechanical loading in rodent models. Prior studies in transgenic mice or mice that underwent increased mechanical loading successfully demonstrated alterations in novel pathways in osteocytes using RNAseq [[8](#pone.0250715.ref008),[9](#pone.0250715.ref009)]. However, no studies to date examined whole transcriptome profile of osteocytes from mice that underwent reduced mechanical loading.

Thus, we examined the complete RNA transcriptome in cortical bone from mice that underwent hindlimb unloading for 7 days, with the goal of identifying novel mechanosensitive pathways that respond to mechanical unloading. We validated our RNAseq results by a highly sensitive RNA molecular barcoding technologies (NanoString) examining 60 panel genes.

## Material and methods

### Hindlimb unloading

Eleven-week old, female C57Bl/6J mice were randomly assigned to hindlimb unloading (HLU) or normal weightbearing (Cont) (n = 8/group). The HLU group underwent hindlimb unloading for 7 days according to the previously published studies [[10](#pone.0250715.ref010)–[15](#pone.0250715.ref015)]. In brief, under isoflurane anesthesia, the mouse tail was taped to a freely rotating harness connected to a wheel that moved along the central axis of the custom-made cage. The harness was adjusted such that the mouse could not touch its hind limbs to the floor or the walls of the cage. Mice were maintained on a 12/12 hour light/dark cycle, had ad libitum access to standard laboratory rodent chow and water, and were sacrificed by CO2 inhalation at the end of the experiment. All animal procedures were approved by and performed in accordance with the guidelines of the Beth Israel Deaconess Medical Center Institutional Animal Care and Use Committee.

### RNAseq

After cutting the ends of bones and flushing marrow with 10 ml phosphate-buffered saline, the cortical bone was placed in an Eppendorf tube and immediately snap-frozen in liquid nitrogen. Subsequently, Trizol was added while the bone is maintained frozen in an eppendorf tube placed in a liquid nitrogen bath, homogenized in the same eppendorf tube with the Fastprep24 machine (MP Biomdicals), and subsequently total RNA was isolated and purified using manufacture recommendations for the PureLink RNA kit (Life Technologies). Using this isolation technique, we routinely obtain 3–6 ug per sample total RNA that has high quality RNA integrity numbers (RIN, Aigilent Technologies) > 7.5 [[9](#pone.0250715.ref009)]. RNA sequencing libraries were prepared using TruSeq RNA Sample Preparation Kit (v2, Illumina, San Diego, CA) per manufacturer recommendations using 500 ng/sample total RNA [[8](#pone.0250715.ref008)]. Samples were multiplexed (n = 8 per lane) for sequencing on a HiSeq (Illumina) platform and reads were aligned to reference genome (Tophat2). Differential gene expression was analyzed by DESeq2 and relevant biological processes associated with differentially expressed genes were analyzed by Gene Set Enrichment Analysis according to studies by Subramanian et al. [[8](#pone.0250715.ref008),[16](#pone.0250715.ref016)–[18](#pone.0250715.ref018)].

### Nanostring

To validate our set of differentially regulated genes identified by RNASeq. and to perform targeted gene discovery in our unloading model using the limiting amount of total RNA (3–6 ug/sample) we isolated from murine femurs, we used a NanoString nCounter codeset of sixty differentially expressed genes ([Table 1](#pone.0250715.t001)) with 6 housekeeping genes (Actb, Abcf1, B2m, Gapdh, Pol42A, Sirt4). In brief, the nCounter gene codeset contains a matched pair 3′ biotinylated capture probe and a 5′reporter probe tagged with a fluorescent barcode, for each of 236 transcripts. Probes are hybridized to 100 ng of total RNA for 19 h at 65°C, after which excess capture and reporter probes are removed and transcript-specific ternary complexes are immobilized on a streptavidin-coated cartridge. Subsequently, all solution manipulations are carried out using the NanoString preparation station robotic fluids handling platform. Data collection is carried out with the nCounter Digital Analyzer to count individual fluorescent barcodes and quantify target RNA molecules present in each sample. Normalization was carried based on a standard curve constructed using spike in exogenous control constructs and the 6 housekeeping genes included in the codeset [[19](#pone.0250715.ref019)].

#### Table 1. Differentially expressed genes in the control and hindlimb unloaded (HLU) mouse cortical bone assessed by NanoString.

| Molecular Pathways | Selected Genes | Differentially Expressed Genes | HLU vs. Control (Fold Change) | p-value |
| --- | --- | --- | --- | --- |
| Mesenchymal stem cell (MSC) fate determination and differentiation | Abi3bp, Fabp4, Apod |  |  |  |
| Osteoblast function and differentiation | Aspn, Alpl, Bmpr1a, Dkk1, Fzd4, Tgfb1-3, Runx2, Tob1, Opg, Spp1, Sp7, Sparc, Bglap, Myoc, Col1a1, Col1a2, Col3a1, Den, Serpinfl, Sfrp2, Sfrp4, Wnt16, Wnt9a, Wnt5a, Wnt4, Wisp2, Zfyve9, Snca, Bmp4 | Fzd4 Sfrp2 Sfrp4 Spp1 Bmp4 | 1.6 1.7 1.7 1.5 1.4 | 0.03 0.05 0.009 0.02 0.02 |
| Osteocyte function and differentiation | Sost, Mef2C, Mepe, Postn, Phex, Npy | Npy | 1.2 | 0.04 |
| Osteoclast function and differentiation | Ctsk, Tnfsfl1(Rankl), Trap (Acp5) |  |  |  |
| Extracellular matrix proteases | Mmp2, Mmp3, Mmp10, Mmp13, Mmp14, Mmp15 | Mmp3 Mmp13 | 1.8 1.6 | 0.007 0.01 |
| Protease inhibitors | Timp1, Timp2 | Timp1 | 1.5 | 0.02 |
| Cell cycle control, mitochondria, energy balance | Mss51, Scd1, Pfkfb3 | Scd1 Pfkfb3 | 2.0 1.8 | 0.01 0.004 |
| Housekeeping genes | Actb, Abcf1, B2m, Gapdh, Pol42A, Sirt4 |  |  |  |

[Open in a new tab](table/pone.0250715.t001/)

## Results

Hindlimb unloading did not alter the quality of RNAseq data. For both groups, individual specimens yielded ~22 million reads with high unique mapping rates (79% for controls and 81% for HLU). RNAseq analysis of cortical bone mRNA from control and HLU mice, without correcting for multiple hypothesis testing, identified 723 genes whose transcript abundances increased ≥ 1.2-fold and 610 genes whose transcript abundances decreased ≥ 1.2-fold. After considering genes whose transcript abundances changed by 1.2-fold and correcting for multiple hypothesis testing (p < 0.1), 8 genes demonstrated increased transcript abundance and 5 genes demonstrated decreased transcript abundance following HLU. Gene set enrichment analysis using these 13 differentially expressed genes pointed to several metabolic processes, monosaccharide metabolism (Pfkfb3, Igfbp5, p < 0.01), peptidase inhibition (Stfa1, Stfa2, p < 0.01), and cellular protein metabolism (Stfa2, Stfa1, Igfbp5, p < 0.01). Wnt signaling was also implicated ([Fig 1](#pone.0250715.g001)).

### Fig 1. Selected KEGG pathway and gene ontology of biological process altered in cortical bone from hindlimb unloaded mice and the effects of HLU on Wnt signaling and Pfkfb3.

[![Fig 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7e22/8509868/279c8c1e1155/pone.0250715.g001.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=8509868_pone.0250715.g001.jpg)

[Open in a new tab](figure/pone.0250715.g001/)

Transcript abundances measured by RNAseq and Nanostring were similar in control mice (Pearson’s R = 0.90, p < 0.0001, [Fig 2A](#pone.0250715.g002)). Changes in transcript abundance between control and HLU mice also correlated significantly between the RNAseq and Nanostring datasets (Pearson’s R = 0.76, p < 0.0001, [Fig 2B](#pone.0250715.g002)). Importantly, Nanostring confirmed alterations seen with RNAseq in transcripts associated with Wnt signaling and cell metabolism ([Table 1](#pone.0250715.t001), [Fig 3](#pone.0250715.g003)). Scd1 (2-fold, p = 0.01), Pfkfb3 (1.8-fold, p = 0.003), and Fzd4 (1.6-fold, p = 0.03) were all upregulated in cortical bone isolated from hindlimb unloaded mouse. In addition to these genes, we identified Mmp3 (1.8-fold, p = 0.007), Sfrp2 (1.7-fold, p = 0.05), Sfrp4 (1.7-fold, p = 0.009), Mmp13 (1.6-fold, p = 0.01), Bmp4 (1.4-fold, p = 0.02), Timp1 (1.5-fold, p = 0.02), Npy (1.2-fold, p = 0.04), and Spp1 (1.5-fold, p = 0.02) genes to be upregulated in the hindlimb unloaded mouse cortical bone. No downregulated genes were detected.

### Fig 2. Correlation between Nanostring and RNAseq transcript abundance in controls (A) and changes in abundance between control and HLU mice (B) with 95% confidence bands of the best-fit line.

[![Fig 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7e22/8509868/d42738713900/pone.0250715.g002.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=8509868_pone.0250715.g002.jpg)

[Open in a new tab](figure/pone.0250715.g002/)

### Fig 3. Cell metabolism and Wnt signaling associated transcripts whose abundance changed between control and HLU mice, as assessed by RNAseq and Nanostring analysis.

[![Fig 3](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7e22/8509868/6d5c9141ee13/pone.0250715.g003.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=8509868_pone.0250715.g003.jpg)

[Open in a new tab](figure/pone.0250715.g003/)

## Discussion

Our RNAseq dataset provides an unbiased approach for identifying genes whose transcripts change in response to mechanical unloading of cortical bone. We identified novel genes (e.g., Mss51, Pfkfb3) related to cell cycle, mitochondria, and cellular energy balance that were differentially regulated by HLU.

While mitochondria are typically reduced in size as osteoblasts transition to osteocytes, histopathological studies demonstrate enlarged mitochondria in osteocytes from rats immobilized for ten days [[20](#pone.0250715.ref020)]. Further, in mice with impaired osteocyte autophagy, enlarged mitochondria are observed as well, and associated with decreased trabecular and cortical bone [[21](#pone.0250715.ref021)]. Imbalance in osteocyte mitochondrial redox can disrupt the canalicular network and lead to bone loss [[22](#pone.0250715.ref022)]. Further studies are needed to determine whether the genes we identified may sense altered mechanical loading through a similar mechanism that regulates cellular energy balance in bone.

Prior studies have also demonstrated that microgravity causes alterations to glycolysis pathways in a variety of cells, including osteoblasts [[23](#pone.0250715.ref023),[24](#pone.0250715.ref024)]. Importantly, our data show that Pfkfb3, which controls the concentration of fructose 2,6-bisphosphate, a potent allosteric activator of PFK1, is significantly upregulated after HLU. Recent evidence supports the concept that Pfkfb3 provides a signaling mechanism for Wnt3A, altering osteoblast differentiation [[25](#pone.0250715.ref025)]. Pfkfb3 was also identified de-novo in a gene enrichment analysis of circulating monocytes in patients with osteoporosis, further suggesting a possible role in modulating the bone microenvironment in the setting of low bone density [[26](#pone.0250715.ref026)]. Our study adds to the evidence that Pfkfb3 may influence bone metabolism in the context of microgravity, disuse-induced bone loss and osteoporosis.

Mss51 has not been demonstrated to be involved during skeletal development or homeostasis, but recently published study suggests that Mss51 may be involved in bone adaptation following mechanical loading [[27](#pone.0250715.ref027)]. The alteration in Mss51 appears to be mediated by focal adhesion kinase, which has been shown to be responsive to mechanical loading via fluid flow shear stress in osteoblasts [[28](#pone.0250715.ref028),[29](#pone.0250715.ref029)]. Mechanical loading likely alters cell-matrix environment, thereby allowing integrins to initiate intracellular signaling to promote bone adaptation. Hindlimb unloading in rats also decreases focal adhesions in mesenchymal stromal cells [[30](#pone.0250715.ref030)], which will have resulted in increased Mss51 [[27](#pone.0250715.ref027)]. These studies demonstrate that while Mss51 is conventionally known to be involved during cell metabolism and energy balance, the gene may also be responsive to mechanical loading/unloading via changes in cell-matrix environment.

Prior studies of hindlimb unloading in rodents have reported that several signaling pathways such as Wnt and Rankl/Opg are altered in osteoblasts and osteocytes following mechanical unloading [[31](#pone.0250715.ref031)–[34](#pone.0250715.ref034)]. While our study demonstrated that Wnt signaling is implicated to be involved, we did not find that sclerostin or Rankl/Opg to be altered following hindlimb unloading. There are several possible factors that may have contributed to differences in study findings. First, it is possible that methodological differences (RNAseq vs. RT-qPCR) used to assess transcript levels contributed to different outcomes. Second, while we carefully removed bone marrow, surrounding soft tissues, and both ends of bone, the cortical bone lining cells may have contributed to heterogeneity of cell population, leading to blunted effects on several signaling pathways known to be altered by hindlimb unloading in osteocytes or osteoblasts. In addition, whereas we examined day 7 of unloading, earlier time points may be needed to observe robust differences in gene expression due to unloading. Prior studies have demonstrated that bones from 6 to 9 months old rats are more responsive to hindlimb unloading than 28 to 32 months old rats, likely due to increased Bmp2 and Igf1 in younger animals [[35](#pone.0250715.ref035),[36](#pone.0250715.ref036)]. Finally, hindlimb unloading has been shown to affect other physiologic systems in female 11-week-old mice, such as loss of muscle and increased corticosterone metabolites [[37](#pone.0250715.ref037)], which has been shown to inhibit bone formation [[38](#pone.0250715.ref038)]. Altogether, a variety of factors can contribute to inconsistencies in gene expression across studies. Additional suitably powered and well-controlled studies are needed to resolve reported discrepancies among studies.

We used only female mice, thus precluding analysis of possible sexual dimorphism in mechanosensitive genes. We selected the 7-day timepoint based on our prior studies, but recognize the limitation of this approach which precludes determining the time-course of gene-expression changes. This early timepoint may have led to minimal changes in osteogenic genes in our studies. However, our ability to identify novel genes that may initiate osteogenic responses later, not previously associated with disuse-induced bone loss provides rationale for future studies with multiple timepoints to expand upon the current findings. While there was excellent correlation between the measurements performed with two methods ([Fig 2](#pone.0250715.g002)), Nanostring detected more differentially expressed genes than RNAseq ([Fig 3](#pone.0250715.g003)). Therefore, although Nanostring can sample a limited, pre-determined portion of cortical bone transcriptome, it can serve as a powerful approach towards identifying mild changes (<2-fold) in transcript abundance.

Our gene expression approach comparing cortical bone gene expression in HLU and normally loaded mice successfully revealed previously known and unknown genes. Future mechanistic studies examining the functional role of metabolic genes revealed from our study may identify novel mechanosensitive pathways responsible for microgravity- and disuse-induced bone loss. Elucidating these pathways may lead to therapeutic interventions to treat bone loss and prevent fracture risk associated with microgravity, spinal cord injury, or extended bed rest.

## Supporting information

S1 File. Nanostring supple.

(XLSX)

[Click here for additional data file.](/articles/instance/8509868/bin/pone.0250715.s001.xlsx) (21.1KB, xlsx)

S2 File. RNAseq supple.

(CSV)

[Click here for additional data file.](/articles/instance/8509868/bin/pone.0250715.s002.csv) (7.1MB, csv)

## Data Availability

The data underlying the results are provided as [Supporting information](#sec008) files, and the transcriptomic profile data has been deposited to Gene Expression Omnibus database (accession number GSE169292).

## Funding Statement

This work supported by funding from National Aeronautics and Space Administration (NNX10AE39G) and from the National Institutes of Health (R21AR057522 and R01AR053237). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## References

* 1.Robling A. G., Niziolek P. J., Baldridge L. A., Condon K. W., Allen M. R., Alam I., et al. (2008) Mechanical stimulation of bone in vivo reduces osteocyte expression of Sost/sclerostin. *J Biol Chem*
  283, 5866–5875. doi: 10.1074/jbc.M705092200
   [[DOI](https://doi.org/10.1074/jbc.M705092200)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18089564/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Biol%20Chem&title=Mechanical%20stimulation%20of%20bone%20in%20vivo%20reduces%20osteocyte%20expression%20of%20Sost/sclerostin&author=A.%20G.%20Robling&author=P.%20J.%20Niziolek&author=L.%20A.%20Baldridge&author=K.%20W.%20Condon&author=M.%20R.%20Allen&volume=283&publication_year=2008&pages=5866-5875&pmid=18089564&doi=10.1074/jbc.M705092200&)]
* 2.Sakata T., Wang Y., Halloran B. P., Elalieh H. Z., Cao J., and Bikle D. D. (2004) Skeletal unloading induces resistance to insulin-like growth factor-I (IGF-I) by inhibiting activation of the IGF-I signaling pathways. *J Bone Miner Res*
  19, 436–446. doi: 10.1359/JBMR.0301241
   [[DOI](https://doi.org/10.1359/JBMR.0301241)] [[PMC free article](/articles/PMC10720400/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15040832/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=Skeletal%20unloading%20induces%20resistance%20to%20insulin-like%20growth%20factor-I%20(IGF-I)%20by%20inhibiting%20activation%20of%20the%20IGF-I%20signaling%20pathways&author=T.%20Sakata&author=Y.%20Wang&author=B.%20P.%20Halloran&author=H.%20Z.%20Elalieh&author=J.%20Cao&volume=19&publication_year=2004&pages=436-446&pmid=15040832&doi=10.1359/JBMR.0301241&)]
* 3.Spatz J. M., Wein M. N., Gooi J. H., Qu Y., Garr J. L., Liu S., et al. (2015) The Wnt Inhibitor Sclerostin Is Up-regulated by Mechanical Unloading in Osteocytes in Vitro. *J Biol Chem*
  290, 16744–16758. doi: 10.1074/jbc.M114.628313
   [[DOI](https://doi.org/10.1074/jbc.M114.628313)] [[PMC free article](/articles/PMC4505423/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25953900/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Biol%20Chem&title=The%20Wnt%20Inhibitor%20Sclerostin%20Is%20Up-regulated%20by%20Mechanical%20Unloading%20in%20Osteocytes%20in%20Vitro&author=J.%20M.%20Spatz&author=M.%20N.%20Wein&author=J.%20H.%20Gooi&author=Y.%20Qu&author=J.%20L.%20Garr&volume=290&publication_year=2015&pages=16744-16758&pmid=25953900&doi=10.1074/jbc.M114.628313&)]
* 4.Cabahug-Zuckerman P., Frikha-Benayed D., Majeska R. J., Tuthill A., Yakar S., Judex S., et al. (2016) Osteocyte Apoptosis Caused by Hindlimb Unloading is Required to Trigger Osteocyte RANKL Production and Subsequent Resorption of Cortical and Trabecular Bone in Mice Femurs. *J Bone Miner Res*
  31, 1356–1365. doi: 10.1002/jbmr.2807
   [[DOI](https://doi.org/10.1002/jbmr.2807)] [[PMC free article](/articles/PMC5488280/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26852281/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=Osteocyte%20Apoptosis%20Caused%20by%20Hindlimb%20Unloading%20is%20Required%20to%20Trigger%20Osteocyte%20RANKL%20Production%20and%20Subsequent%20Resorption%20of%20Cortical%20and%20Trabecular%20Bone%20in%20Mice%20Femurs&author=P.%20Cabahug-Zuckerman&author=D.%20Frikha-Benayed&author=R.%20J.%20Majeska&author=A.%20Tuthill&author=S.%20Yakar&volume=31&publication_year=2016&pages=1356-1365&pmid=26852281&doi=10.1002/jbmr.2807&)]
* 5.Ko F. C., Van Vliet M., Ellman R., Grasso D., Brooks D. J., Spatz J. M., et al. (2017) Treatment With a Soluble Bone Morphogenetic Protein Type 1A Receptor (BMPR1A) Fusion Protein Increases Bone Mass and Bone Formation in Mice Subjected to Hindlimb Unloading. *JBMR Plus*
  1, 66–72. doi: 10.1002/jbm4.10012
   [[DOI](https://doi.org/10.1002/jbm4.10012)] [[PMC free article](/articles/PMC6124165/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30283882/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=JBMR%20Plus&title=Treatment%20With%20a%20Soluble%20Bone%20Morphogenetic%20Protein%20Type%201A%20Receptor%20(BMPR1A)%20Fusion%20Protein%20Increases%20Bone%20Mass%20and%20Bone%20Formation%20in%20Mice%20Subjected%20to%20Hindlimb%20Unloading&author=F.%20C.%20Ko&author=M.%20Van%20Vliet&author=R.%20Ellman&author=D.%20Grasso&author=D.%20J.%20Brooks&volume=1&publication_year=2017&pages=66-72&pmid=30283882&doi=10.1002/jbm4.10012&)]
* 6.Leblanc A., Matsumoto T., Jones J., Shapiro J., Lang T., Shackelford L., et al. (2013) Bisphosphonates as a supplement to exercise to protect bone during long-duration spaceflight. *Osteoporos Int*
  24, 2105–2114. doi: 10.1007/s00198-012-2243-z
   [[DOI](https://doi.org/10.1007/s00198-012-2243-z)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23334732/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Osteoporos%20Int&title=Bisphosphonates%20as%20a%20supplement%20to%20exercise%20to%20protect%20bone%20during%20long-duration%20spaceflight&author=A.%20Leblanc&author=T.%20Matsumoto&author=J.%20Jones&author=J.%20Shapiro&author=T.%20Lang&volume=24&publication_year=2013&pages=2105-2114&pmid=23334732&doi=10.1007/s00198-012-2243-z&)]
* 7.Gifre L., Vidal J., Carrasco J. L., Muxi A., Portell E., Monegal A., et al. (2016) Denosumab increases sublesional bone mass in osteoporotic individuals with recent spinal cord injury. *Osteoporos Int*
  27, 405–410. doi: 10.1007/s00198-015-3333-5
   [[DOI](https://doi.org/10.1007/s00198-015-3333-5)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26423406/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Osteoporos%20Int&title=Denosumab%20increases%20sublesional%20bone%20mass%20in%20osteoporotic%20individuals%20with%20recent%20spinal%20cord%20injury&author=L.%20Gifre&author=J.%20Vidal&author=J.%20L.%20Carrasco&author=A.%20Muxi&author=E.%20Portell&volume=27&publication_year=2016&pages=405-410&pmid=26423406&doi=10.1007/s00198-015-3333-5&)]
* 8.Ayturk U. M., Jacobsen C. M., Christodoulou D. C., Gorham J., Seidman J. G., Seidman C. E., et al. (2013) An RNA-seq protocol to identify mRNA expression changes in mouse diaphyseal bone: applications in mice with bone property altering Lrp5 mutations. *J Bone Miner Res*
  28, 2081–2093. doi: 10.1002/jbmr.1946
   [[DOI](https://doi.org/10.1002/jbmr.1946)] [[PMC free article](/articles/PMC3743099/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23553928/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=An%20RNA-seq%20protocol%20to%20identify%20mRNA%20expression%20changes%20in%20mouse%20diaphyseal%20bone:%20applications%20in%20mice%20with%20bone%20property%20altering%20Lrp5%20mutations&author=U.%20M.%20Ayturk&author=C.%20M.%20Jacobsen&author=D.%20C.%20Christodoulou&author=J.%20Gorham&author=J.%20G.%20Seidman&volume=28&publication_year=2013&pages=2081-2093&pmid=23553928&doi=10.1002/jbmr.1946&)]
* 9.Kelly N. H., Schimenti J. C., Ross F. P., and van der Meulen M. C. (2016) Transcriptional profiling of cortical versus cancellous bone from mechanically-loaded murine tibiae reveals differential gene expression. *Bone*
  86, 22–29. doi: 10.1016/j.bone.2016.02.007
   [[DOI](https://doi.org/10.1016/j.bone.2016.02.007)] [[PMC free article](/articles/PMC4833881/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26876048/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bone&title=Transcriptional%20profiling%20of%20cortical%20versus%20cancellous%20bone%20from%20mechanically-loaded%20murine%20tibiae%20reveals%20differential%20gene%20expression&author=N.%20H.%20Kelly&author=J.%20C.%20Schimenti&author=F.%20P.%20Ross&author=M.%20C.%20van%20der%20Meulen&volume=86&publication_year=2016&pages=22-29&pmid=26876048&doi=10.1016/j.bone.2016.02.007&)]
* 10.Ellman R., Grasso D. J., van Vliet M., Brooks D. J., Spatz J. M., Conlon C., et al. (2014) Combined effects of botulinum toxin injection and hind limb unloading on bone and muscle. *Calcif Tissue Int*
  94, 327–337. doi: 10.1007/s00223-013-9814-7
   [[DOI](https://doi.org/10.1007/s00223-013-9814-7)] [[PMC free article](/articles/PMC3921683/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24240478/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Calcif%20Tissue%20Int&title=Combined%20effects%20of%20botulinum%20toxin%20injection%20and%20hind%20limb%20unloading%20on%20bone%20and%20muscle&author=R.%20Ellman&author=D.%20J.%20Grasso&author=M.%20van%20Vliet&author=D.%20J.%20Brooks&author=J.%20M.%20Spatz&volume=94&publication_year=2014&pages=327-337&pmid=24240478&doi=10.1007/s00223-013-9814-7&)]
* 11.Globus R. K., Bikle D. D., and Morey-Holton E. (1986) The temporal response of bone to unloading. *Endocrinology*
  118, 733–742. doi: 10.1210/endo-118-2-733
   [[DOI](https://doi.org/10.1210/endo-118-2-733)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/3943489/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Endocrinology&title=The%20temporal%20response%20of%20bone%20to%20unloading&author=R.%20K.%20Globus&author=D.%20D.%20Bikle&author=E.%20Morey-Holton&volume=118&publication_year=1986&pages=733-742&pmid=3943489&doi=10.1210/endo-118-2-733&)]
* 12.Iwaniec U. T., Wronski T. J., Amblard D., Nishimura Y., van der Meulen M. C., Wade C. E., et al. (2005) Effects of disrupted beta1-integrin function on the skeletal response to short-term hindlimb unloading in mice. *J Appl Physiol*
  98, 690–696. doi: 10.1152/japplphysiol.00689.2004
   [[DOI](https://doi.org/10.1152/japplphysiol.00689.2004)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15465888/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Appl%20Physiol&title=Effects%20of%20disrupted%20beta1-integrin%20function%20on%20the%20skeletal%20response%20to%20short-term%20hindlimb%20unloading%20in%20mice&author=U.%20T.%20Iwaniec&author=T.%20J.%20Wronski&author=D.%20Amblard&author=Y.%20Nishimura&author=M.%20C.%20van%20der%20Meulen&volume=98&publication_year=2005&pages=690-696&pmid=15465888&doi=10.1152/japplphysiol.00689.2004&)]
* 13.Kurokouchi K., Ito T., Ohmori S., Kanda K., Murata Y., and Seo H. (1995) Changes in the markers of bone metabolism following skeletal unloading. *Environmental medicine*: *annual report of the Research Institute of Environmental Medicine*, *Nagoya University*
  39, 21–24.  [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11540541/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Environmental%20medicine:%20annual%20report%20of%20the%20Research%20Institute%20of%20Environmental%20Medicine,%20Nagoya%20University&title=Changes%20in%20the%20markers%20of%20bone%20metabolism%20following%20skeletal%20unloading&author=K.%20Kurokouchi&author=T.%20Ito&author=S.%20Ohmori&author=K.%20Kanda&author=Y.%20Murata&volume=39&publication_year=1995&pages=21-24&pmid=11540541&)]
* 14.Spatz J. M., Ellman R., Cloutier A. M., Louis L., van Vliet M., Suva L. J., et al. (2013) Sclerostin antibody inhibits skeletal deterioration due to reduced mechanical loading. *J Bone Miner Res*
  28, 865–874. doi: 10.1002/jbmr.1807
   [[DOI](https://doi.org/10.1002/jbmr.1807)] [[PMC free article](/articles/PMC4076162/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23109229/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=Sclerostin%20antibody%20inhibits%20skeletal%20deterioration%20due%20to%20reduced%20mechanical%20loading&author=J.%20M.%20Spatz&author=R.%20Ellman&author=A.%20M.%20Cloutier&author=L.%20Louis&author=M.%20van%20Vliet&volume=28&publication_year=2013&pages=865-874&pmid=23109229&doi=10.1002/jbmr.1807&)]
* 15.Zhong N., Garman R. A., Squire M. E., Donahue L. R., Rubin C. T., Hadjiargyrou M., and Judex S. (2005) Gene expression patterns in bone after 4 days of hind-limb unloading in two inbred strains of mice. *Aviation*, *Space*, *and Environmental Medicine*
  76, 530–535.  [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15945395/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Aviation,%20Space,%20and%20Environmental%20Medicine&title=Gene%20expression%20patterns%20in%20bone%20after%204%20days%20of%20hind-limb%20unloading%20in%20two%20inbred%20strains%20of%20mice&author=N.%20Zhong&author=R.%20A.%20Garman&author=M.%20E.%20Squire&author=L.%20R.%20Donahue&author=C.%20T.%20Rubin&volume=76&publication_year=2005&pages=530-535&pmid=15945395&)]
* 16.Ogata H., Goto S., Sato K., Fujibuchi W., Bono H., and Kanehisa M. (1999) KEGG: Kyoto Encyclopedia of Genes and Genomes. *Nucleic Acids Res*
  27, 29–34. doi: 10.1093/nar/27.1.29
   [[DOI](https://doi.org/10.1093/nar/27.1.29)] [[PMC free article](/articles/PMC148090/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/9847135/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res&title=KEGG:%20Kyoto%20Encyclopedia%20of%20Genes%20and%20Genomes&author=H.%20Ogata&author=S.%20Goto&author=K.%20Sato&author=W.%20Fujibuchi&author=H.%20Bono&volume=27&publication_year=1999&pages=29-34&pmid=9847135&doi=10.1093/nar/27.1.29&)]
* 17.Subramanian A., Tamayo P., Mootha V. K., Mukherjee S., Ebert B. L., Gillette M. A., et al. (2005) Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. *Proc Natl Acad Sci U S A*
  102, 15545–15550. doi: 10.1073/pnas.0506580102
   [[DOI](https://doi.org/10.1073/pnas.0506580102)] [[PMC free article](/articles/PMC1239896/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16199517/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proc%20Natl%20Acad%20Sci%20U%20S%20A&title=Gene%20set%20enrichment%20analysis:%20a%20knowledge-based%20approach%20for%20interpreting%20genome-wide%20expression%20profiles&author=A.%20Subramanian&author=P.%20Tamayo&author=V.%20K.%20Mootha&author=S.%20Mukherjee&author=B.%20L.%20Ebert&volume=102&publication_year=2005&pages=15545-15550&pmid=16199517&doi=10.1073/pnas.0506580102&)]
* 18.Subramanian A., Kuehn H., Gould J., Tamayo P., and Mesirov J. P. (2007) GSEA-P: a desktop application for Gene Set Enrichment Analysis. *Bioinformatics*
  23, 3251–3253. doi: 10.1093/bioinformatics/btm369
   [[DOI](https://doi.org/10.1093/bioinformatics/btm369)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17644558/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=GSEA-P:%20a%20desktop%20application%20for%20Gene%20Set%20Enrichment%20Analysis&author=A.%20Subramanian&author=H.%20Kuehn&author=J.%20Gould&author=P.%20Tamayo&author=J.%20P.%20Mesirov&volume=23&publication_year=2007&pages=3251-3253&pmid=17644558&doi=10.1093/bioinformatics/btm369&)]
* 19.Kulkarni M. M. (2011) Digital multiplexed gene expression analysis using the NanoString nCounter system. *Curr Protoc Mol Biol* Chapter
  25, Unit25B 10. doi: 10.1002/0471142727.mb25b10s94
   [[DOI](https://doi.org/10.1002/0471142727.mb25b10s94)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21472696/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr%20Protoc%20Mol%20Biol%20Chapter&title=Digital%20multiplexed%20gene%20expression%20analysis%20using%20the%20NanoString%20nCounter%20system&author=M.%20M.%20Kulkarni&volume=25&publication_year=2011&pmid=21472696&doi=10.1002/0471142727.mb25b10s94&)]
* 20.Palumbo C., Palazzini S., Zaffe D., and Marotti G. (1990) Osteocyte differentiation in the tibia of newborn rabbit: an ultrastructural study of the formation of cytoplasmic processes. *Acta Anat (Basel)*
  137, 350–358. doi: 10.1159/000146907
   [[DOI](https://doi.org/10.1159/000146907)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/2368590/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Acta%20Anat%20(Basel)&title=Osteocyte%20differentiation%20in%20the%20tibia%20of%20newborn%20rabbit:%20an%20ultrastructural%20study%20of%20the%20formation%20of%20cytoplasmic%20processes&author=C.%20Palumbo&author=S.%20Palazzini&author=D.%20Zaffe&author=G.%20Marotti&volume=137&publication_year=1990&pages=350-358&pmid=2368590&doi=10.1159/000146907&)]
* 21.Piemontese M., Onal M., Xiong J., Han L., Thostenson J. D., Almeida M., et al. (2016) Low bone mass and changes in the osteocyte network in mice lacking autophagy in the osteoblast lineage. *Sci Rep*
  6, 24262. doi: 10.1038/srep24262
   [[DOI](https://doi.org/10.1038/srep24262)] [[PMC free article](/articles/PMC4827128/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27064143/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci%20Rep&title=Low%20bone%20mass%20and%20changes%20in%20the%20osteocyte%20network%20in%20mice%20lacking%20autophagy%20in%20the%20osteoblast%20lineage&author=M.%20Piemontese&author=M.%20Onal&author=J.%20Xiong&author=L.%20Han&author=J.%20D.%20Thostenson&volume=6&publication_year=2016&pages=24262&pmid=27064143&doi=10.1038/srep24262&)]
* 22.Kobayashi K., Nojiri H., Saita Y., Morikawa D., Ozawa Y., Watanabe K., et al. (2015) Mitochondrial superoxide in osteocytes perturbs canalicular networks in the setting of age-related osteoporosis. *Sci Rep*
  5, 9148. doi: 10.1038/srep09148
   [[DOI](https://doi.org/10.1038/srep09148)] [[PMC free article](/articles/PMC5376208/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25779629/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci%20Rep&title=Mitochondrial%20superoxide%20in%20osteocytes%20perturbs%20canalicular%20networks%20in%20the%20setting%20of%20age-related%20osteoporosis&author=K.%20Kobayashi&author=H.%20Nojiri&author=Y.%20Saita&author=D.%20Morikawa&author=Y.%20Ozawa&volume=5&publication_year=2015&pages=9148&pmid=25779629&doi=10.1038/srep09148&)]
* 23.Michaletti A., Gioia M., Tarantino U., and Zolla L. (2017) Effects of microgravity on osteoblast mitochondria: a proteomic and metabolomics profile. *Sci Rep*
  7, 15376. doi: 10.1038/s41598-017-15612-1
   [[DOI](https://doi.org/10.1038/s41598-017-15612-1)] [[PMC free article](/articles/PMC5684136/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29133864/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci%20Rep&title=Effects%20of%20microgravity%20on%20osteoblast%20mitochondria:%20a%20proteomic%20and%20metabolomics%20profile&author=A.%20Michaletti&author=M.%20Gioia&author=U.%20Tarantino&author=L.%20Zolla&volume=7&publication_year=2017&pages=15376&pmid=29133864&doi=10.1038/s41598-017-15612-1&)]
* 24.Wang Y., Chen Z. H., Yin C., Ma J. H., Li D. J., Zhao F., et al. (2015) GeneChip expression profiling reveals the alterations of energy metabolism related genes in osteocytes under large gradient high magnetic fields. *PLoS One*
  10, e0116359. doi: 10.1371/journal.pone.0116359
   [[DOI](https://doi.org/10.1371/journal.pone.0116359)] [[PMC free article](/articles/PMC4312085/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25635858/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=GeneChip%20expression%20profiling%20reveals%20the%20alterations%20of%20energy%20metabolism%20related%20genes%20in%20osteocytes%20under%20large%20gradient%20high%20magnetic%20fields&author=Y.%20Wang&author=Z.%20H.%20Chen&author=C.%20Yin&author=J.%20H.%20Ma&author=D.%20J.%20Li&volume=10&publication_year=2015&pages=e0116359&pmid=25635858&doi=10.1371/journal.pone.0116359&)]
* 25.Esen E., Chen J., Karner C. M., Okunade A. L., Patterson B. W., and Long F. (2013) WNT-LRP5 signaling induces Warburg effect through mTORC2 activation during osteoblast differentiation. *Cell Metab*
  17, 745–755. doi: 10.1016/j.cmet.2013.03.017
   [[DOI](https://doi.org/10.1016/j.cmet.2013.03.017)] [[PMC free article](/articles/PMC3653292/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23623748/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Metab&title=WNT-LRP5%20signaling%20induces%20Warburg%20effect%20through%20mTORC2%20activation%20during%20osteoblast%20differentiation&author=E.%20Esen&author=J.%20Chen&author=C.%20M.%20Karner&author=A.%20L.%20Okunade&author=B.%20W.%20Patterson&volume=17&publication_year=2013&pages=745-755&pmid=23623748&doi=10.1016/j.cmet.2013.03.017&)]
* 26.Xiao H., Shan L., Zhu H., and Xue F. (2012) Detection of significant pathways in osteoporosis based on graph clustering. *Mol Med Rep*
  6, 1325–1332. doi: 10.3892/mmr.2012.1082
   [[DOI](https://doi.org/10.3892/mmr.2012.1082)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22992777/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Mol%20Med%20Rep&title=Detection%20of%20significant%20pathways%20in%20osteoporosis%20based%20on%20graph%20clustering&author=H.%20Xiao&author=L.%20Shan&author=H.%20Zhu&author=F.%20Xue&volume=6&publication_year=2012&pages=1325-1332&pmid=22992777&doi=10.3892/mmr.2012.1082&)]
* 27.Sato T., Verma S., Andrade C. D. C., Omeara M., Campbell N., Wang J. S., et al. (2020) A FAK/HDAC5 signaling axis controls osteocyte mechanotransduction. *Nat Commun*
  11, 3282
  doi: 10.1038/s41467-020-17099-3
   [[DOI](https://doi.org/10.1038/s41467-020-17099-3)] [[PMC free article](/articles/PMC7329900/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32612176/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat%20Commun&title=A%20FAK/HDAC5%20signaling%20axis%20controls%20osteocyte%20mechanotransduction&author=T.%20Sato&author=S.%20Verma&author=C.%20D.%20C.%20Andrade&author=M.%20Omeara&author=N.%20Campbell&volume=11&publication_year=2020&pages=3282&pmid=32612176&doi=10.1038/s41467-020-17099-3&)]
* 28.Castillo A. B., Blundo J. T., Chen J. C., Lee K. L., Yereddi N. R., Jang E., et al. (2012) Focal adhesion kinase plays a role in osteoblast mechanotransduction in vitro but does not affect load-induced bone formation in vivo. *PLoS One*
  7, e43291. doi: 10.1371/journal.pone.0043291
   [[DOI](https://doi.org/10.1371/journal.pone.0043291)] [[PMC free article](/articles/PMC3448625/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23028449/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Focal%20adhesion%20kinase%20plays%20a%20role%20in%20osteoblast%20mechanotransduction%20in%20vitro%20but%20does%20not%20affect%20load-induced%20bone%20formation%20in%20vivo&author=A.%20B.%20Castillo&author=J.%20T.%20Blundo&author=J.%20C.%20Chen&author=K.%20L.%20Lee&author=N.%20R.%20Yereddi&volume=7&publication_year=2012&pages=e43291&pmid=23028449&doi=10.1371/journal.pone.0043291&)]
* 29.Santos A., Bakker A. D., Zandieh-Doulabi B., de Blieck-Hogervorst J. M., and Klein-Nulend J. (2010) Early activation of the beta-catenin pathway in osteocytes is mediated by nitric oxide, phosphatidyl inositol-3 kinase/Akt, and focal adhesion kinase. *Biochem Biophys Res Commun*
  391, 364–369. doi: 10.1016/j.bbrc.2009.11.064
   [[DOI](https://doi.org/10.1016/j.bbrc.2009.11.064)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19913504/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Biochem%20Biophys%20Res%20Commun&title=Early%20activation%20of%20the%20beta-catenin%20pathway%20in%20osteocytes%20is%20mediated%20by%20nitric%20oxide,%20phosphatidyl%20inositol-3%20kinase/Akt,%20and%20focal%20adhesion%20kinase&author=A.%20Santos&author=A.%20D.%20Bakker&author=B.%20Zandieh-Doulabi&author=J.%20M.%20de%20Blieck-Hogervorst&author=J.%20Klein-Nulend&volume=391&publication_year=2010&pages=364-369&pmid=19913504&doi=10.1016/j.bbrc.2009.11.064&)]
* 30.Qian X., Zhang C., Chen G., Tang Z., Liu Q., Chen J., et al. (2014) Effects of BMP-2 and FGF2 on the osteogenesis of bone marrow-derived mesenchymal stem cells in hindlimb-unloaded rats. *Cell Biochem Biophys*
  70, 1127–1136. doi: 10.1007/s12013-014-0032-3
   [[DOI](https://doi.org/10.1007/s12013-014-0032-3)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24880437/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Biochem%20Biophys&title=Effects%20of%20BMP-2%20and%20FGF2%20on%20the%20osteogenesis%20of%20bone%20marrow-derived%20mesenchymal%20stem%20cells%20in%20hindlimb-unloaded%20rats&author=X.%20Qian&author=C.%20Zhang&author=G.%20Chen&author=Z.%20Tang&author=Q.%20Liu&volume=70&publication_year=2014&pages=1127-1136&pmid=24880437&doi=10.1007/s12013-014-0032-3&)]
* 31.Moriishi T., Fukuyama R., Ito M., Miyazaki T., Maeno T., Kawai Y., et al. (2012) Osteocyte network; a negative regulatory system for bone mass augmented by the induction of Rankl in osteoblasts and Sost in osteocytes at unloading. *PLoS One*
  7, e40143. doi: 10.1371/journal.pone.0040143
   [[DOI](https://doi.org/10.1371/journal.pone.0040143)] [[PMC free article](/articles/PMC3387151/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22768243/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Osteocyte%20network;%20a%20negative%20regulatory%20system%20for%20bone%20mass%20augmented%20by%20the%20induction%20of%20Rankl%20in%20osteoblasts%20and%20Sost%20in%20osteocytes%20at%20unloading&author=T.%20Moriishi&author=R.%20Fukuyama&author=M.%20Ito&author=T.%20Miyazaki&author=T.%20Maeno&volume=7&publication_year=2012&pages=e40143&pmid=22768243&doi=10.1371/journal.pone.0040143&)]
* 32.Jing D., Cai J., Wu Y., Shen G., Li F., Xu Q., et al. (2014) Pulsed electromagnetic fields partially preserve bone mass, microarchitecture, and strength by promoting bone formation in hindlimb-suspended rats. *J Bone Miner Res*
  29, 2250–2261. doi: 10.1002/jbmr.2260
   [[DOI](https://doi.org/10.1002/jbmr.2260)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24753111/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=Pulsed%20electromagnetic%20fields%20partially%20preserve%20bone%20mass,%20microarchitecture,%20and%20strength%20by%20promoting%20bone%20formation%20in%20hindlimb-suspended%20rats&author=D.%20Jing&author=J.%20Cai&author=Y.%20Wu&author=G.%20Shen&author=F.%20Li&volume=29&publication_year=2014&pages=2250-2261&pmid=24753111&doi=10.1002/jbmr.2260&)]
* 33.Gerbaix M., Vico L., Ferrari S. L., and Bonnet N. (2015) Periostin expression contributes to cortical bone loss during unloading. *Bone*
  71, 94–100. doi: 10.1016/j.bone.2014.10.011
   [[DOI](https://doi.org/10.1016/j.bone.2014.10.011)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25445447/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bone&title=Periostin%20expression%20contributes%20to%20cortical%20bone%20loss%20during%20unloading&author=M.%20Gerbaix&author=L.%20Vico&author=S.%20L.%20Ferrari&author=N.%20Bonnet&volume=71&publication_year=2015&pages=94-100&pmid=25445447&doi=10.1016/j.bone.2014.10.011&)]
* 34.Rucci N., Capulli M., Piperni S. G., Cappariello A., Lau P., Frings-Meuthen P., et al. (2015) Lipocalin 2: a new mechanoresponding gene regulating bone homeostasis. *J Bone Miner Res*
  30, 357–368. doi: 10.1002/jbmr.2341
   [[DOI](https://doi.org/10.1002/jbmr.2341)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25112732/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=Lipocalin%202:%20a%20new%20mechanoresponding%20gene%20regulating%20bone%20homeostasis&author=N.%20Rucci&author=M.%20Capulli&author=S.%20G.%20Piperni&author=A.%20Cappariello&author=P.%20Lau&volume=30&publication_year=2015&pages=357-368&pmid=25112732&doi=10.1002/jbmr.2341&)]
* 35.Cunningham H. C., West D. W. D., Baehr L. M., Tarke F. D., Baar K., Bodine S. C., et al. (2018) Age-dependent bone loss and recovery during hindlimb unloading and subsequent reloading in rats. *BMC Musculoskelet Disord*
  19, 223. doi: 10.1186/s12891-018-2156-x
   [[DOI](https://doi.org/10.1186/s12891-018-2156-x)] [[PMC free article](/articles/PMC6052521/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30021585/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Musculoskelet%20Disord&title=Age-dependent%20bone%20loss%20and%20recovery%20during%20hindlimb%20unloading%20and%20subsequent%20reloading%20in%20rats&author=H.%20C.%20Cunningham&author=D.%20W.%20D.%20West&author=L.%20M.%20Baehr&author=F.%20D.%20Tarke&author=K.%20Baar&volume=19&publication_year=2018&pages=223&pmid=30021585&doi=10.1186/s12891-018-2156-x&)]
* 36.Perrien D. S., Akel N. S., Dupont-Versteegden E. E., Skinner R. A., Siegel E. R., Suva L. J., et al. (2007) Aging alters the skeletal response to disuse in the rat. *Am J Physiol Regul Integr Comp Physiol*
  292, R988–996. doi: 10.1152/ajpregu.00302.2006
   [[DOI](https://doi.org/10.1152/ajpregu.00302.2006)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17068163/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am%20J%20Physiol%20Regul%20Integr%20Comp%20Physiol&title=Aging%20alters%20the%20skeletal%20response%20to%20disuse%20in%20the%20rat&author=D.%20S.%20Perrien&author=N.%20S.%20Akel&author=E.%20E.%20Dupont-Versteegden&author=R.%20A.%20Skinner&author=E.%20R.%20Siegel&volume=292&publication_year=2007&pages=R988-996&pmid=17068163&doi=10.1152/ajpregu.00302.2006&)]
* 37.Ellman R., Spatz J., Cloutier A., Palme R., Christiansen B. A., and Bouxsein M. L. (2013) Partial reductions in mechanical loading yield proportional changes in bone density, bone architecture, and muscle mass. *J Bone Miner Res*
  28, 875–885. doi: 10.1002/jbmr.1814
   [[DOI](https://doi.org/10.1002/jbmr.1814)] [[PMC free article](/articles/PMC4118556/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23165526/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Bone%20Miner%20Res&title=Partial%20reductions%20in%20mechanical%20loading%20yield%20proportional%20changes%20in%20bone%20density,%20bone%20architecture,%20and%20muscle%20mass&author=R.%20Ellman&author=J.%20Spatz&author=A.%20Cloutier&author=R.%20Palme&author=B.%20A.%20Christiansen&volume=28&publication_year=2013&pages=875-885&pmid=23165526&doi=10.1002/jbmr.1814&)]
* 38.Henneicke H., Herrmann M., Kalak R., Brennan-Speranza T. C., Heinevetter U., Bertollo N., et al. (2011) Corticosterone selectively targets endo-cortical surfaces by an osteoblast-dependent mechanism. *Bone*
  49, 733–742. doi: 10.1016/j.bone.2011.06.013
   [[DOI](https://doi.org/10.1016/j.bone.2011.06.013)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21722764/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bone&title=Corticosterone%20selectively%20targets%20endo-cortical%20surfaces%20by%20an%20osteoblast-dependent%20mechanism&author=H.%20Henneicke&author=M.%20Herrmann&author=R.%20Kalak&author=T.%20C.%20Brennan-Speranza&author=U.%20Heinevetter&volume=49&publication_year=2011&pages=733-742&pmid=21722764&doi=10.1016/j.bone.2011.06.013&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

S1 File. Nanostring supple.

(XLSX)

[Click here for additional data file.](/articles/instance/8509868/bin/pone.0250715.s001.xlsx) (21.1KB, xlsx)

S2 File. RNAseq supple.

(CSV)

[Click here for additional data file.](/articles/instance/8509868/bin/pone.0250715.s002.csv) (7.1MB, csv)

### Data Availability Statement

The data underlying the results are provided as [Supporting information](#sec008) files, and the transcriptomic profile data has been deposited to Gene Expression Omnibus database (accession number GSE169292).