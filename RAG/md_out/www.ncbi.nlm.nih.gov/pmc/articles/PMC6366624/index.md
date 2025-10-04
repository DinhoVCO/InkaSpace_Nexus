FASEB Bioadv

. Author manuscript; available in PMC: 2020 Jan 1.

*Published in final edited form as:* FASEB Bioadv. 2018 Aug 30;1(1):6–17.

# A comparison of unamplified and massively multiplexed PCR amplification for murine antibody repertoire sequencing

[Trisha A Rettig](https://pubmed.ncbi.nlm.nih.gov/?term=%22Rettig%20TA%22%5BAuthor%5D)

### Trisha A Rettig

\*Division of Biology, Kansas State University, Manhattan, KS, USA

Find articles by [Trisha A Rettig](https://pubmed.ncbi.nlm.nih.gov/?term=%22Rettig%20TA%22%5BAuthor%5D)

\*, [Michael J Pecaut](https://pubmed.ncbi.nlm.nih.gov/?term=%22Pecaut%20MJ%22%5BAuthor%5D)

### Michael J Pecaut

†Division of Radiation Research, Loma Linda University, Loma Linda, CA, USA

Find articles by [Michael J Pecaut](https://pubmed.ncbi.nlm.nih.gov/?term=%22Pecaut%20MJ%22%5BAuthor%5D)

†, [Stephen K Chapes](https://pubmed.ncbi.nlm.nih.gov/?term=%22Chapes%20SK%22%5BAuthor%5D)

### Stephen K Chapes

\*Division of Biology, Kansas State University, Manhattan, KS, USA

Find articles by [Stephen K Chapes](https://pubmed.ncbi.nlm.nih.gov/?term=%22Chapes%20SK%22%5BAuthor%5D)

\*,1

* Author information
* Article notes
* Copyright and License information

\*Division of Biology, Kansas State University, Manhattan, KS, USA

†Division of Radiation Research, Loma Linda University, Loma Linda, CA, USA

1

Corresponding Author: Stephen Keith Chapes, Ph.D., M.P.H., 1717 Claflin Rd., Kansas State University, Manhattan, KS 66506-4901, voice: 785-532-6705; fax: 785-532-6653, skcbiol@ksu.edu

Authorship

T. Rettig and S. K. Chapes contributed to experimental design, data analysis, manuscript preparation and editing. M. J. Pecaut contributed to experimental design and manuscript editing.

Issue date 2019 Jan.

[PMC Copyright notice](/about/copyright/)

PMCID: PMC6366624  NIHMSID: NIHMS987236  PMID: [30740592](https://pubmed.ncbi.nlm.nih.gov/30740592/)

The publisher's version of this article is available at [FASEB Bioadv](https://onlinelibrary.wiley.com/doi/full/10.1096/fba.1017)

## Abstract

Sequencing antibody repertoires has steadily become cheaper and easier. Sequencing methods usually rely on some form of amplification, often a massively multiplexed PCR prior to sequencing. To eliminate potential biases and create a data set that could be used for other studies, our lab compared unamplified sequencing results from the splenic heavy-chain repertoire in the mouse to those processed through two commercial applications. We also compared the use of mRNA vs total RNA, reverse transcriptase, and primer usage for cDNA synthesis and submission. The use of mRNA for cDNA synthesis resulted in higher read counts but reverse transcriptase and primer usage had no statistical effects on read count. Although most of the amplified data sets contained more antibody reads than the unamplified data set, we detected more unique V-gene segments in the unamplified data set. Although unique CDR3 detection was much lower in the unamplified data set, RNASeq detected 98% of the high frequency CDR3s. We have shown that unamplified profiling of the antibody repertoire is possible, detects more V-gene segments, and detects high frequency clones in the repertoire.

**Keywords:** High throughput sequencing, Immunoglobulin genes, Mouse, Heavy Chain, RepSEQ

## Introduction

Antibodies are B cell proteins that play a vital role in adaptive immunity. These complex molecules, and their diverse specificities are defined at several levels. At the protein level, these molecules are heterodimers joined with disulfide bonds between heavy and light chains. At the genetic level, the antibody specificity is influenced by semi-randomly recombining a variable (V), diversity (D), and joining (J) gene segments that are encoded in the genome. This V-D-J, or in the case of the light chain, V-J rearrangement, also influences antibody specificity by random and semi-random base insertions or deletions during the recombination process. In the end, the collection of antibodies produced, the antibody repertoire, is a fingerprint of what antigens an organism has been exposed to and a measure of immunocompetence. Sequencing has become easier, cheaper, and faster in recent years. Antibody repertoires have been sequenced in numerous species, in response to vaccinations ([1](#R1)–[3](#R3)) and infections ([4](#R4)–[6](#R6)), and have been employed in cancer detection; providing valuable feedback regarding the immune system’s response to challenges and for early cancer detection in patients ([7](#R7), [8](#R8)).

In an effort to supplement unamplified MiSeq data sets used in our laboratory ([9](#R9)), we explored the use of commercial processes that use technologies to amplify sequences to increase the depth of coverage of specifically targeted immunoglobulin gene transcripts. These data sets are created using massively multiplexed PCR reactions that are subsequently sequenced on the Illumina platform. Multiplex amplification strategies have been used to explore the T cell ([10](#R10), [11](#R11)) and B cell repertoires ([12](#R12)–[15](#R15)) and biases, omissions ([10](#R10), [11](#R11), [16](#R16)–[18](#R18)).and PCR artifacts have been detected in the data sets ([10](#R10)).

We started this project with the hypothesis that our unamplified data set would provide comparable results to those seen in the commercially amplified data sets. However, we are unaware of any immunoglobulin repertoire studies that have been done to compare data obtained using amplification techniques compared to the repertoire in a total RNASeq library. Concurrent with performing these analyses, we discovered that the required sample preparation for commercial sequencing also varied. Therefore, we found it necessary to examine the impact of sample preparation as part of our effort. This manuscript describes our results comparing a data set generated using unamplified total RNA (TRNA) to commercially amplified data sets. We examined the role of commercial amplification and cDNA generation methods as well as the impact of the starting material on sequence output.

## Materials and Methods

### KSU RNA Preparation

RNA was prepared as outlined in Rettig et al 2017 ([9](#R9)). Briefly, RNA was extracted from the spleens of four nine-week old female C57Bl/6J mice. TRNA was submitted to the Kansas State University Integrated Genomics Facility for sequencing and cDNA was prepared using standard Illumina protocols. cDNA made from the TRNA using random hexamer primers and oligo-dT selection, was size selected to 275-800bp length and sequenced on the Illumina MiSeq at 2×300bp using Illumina’s protocol. No additional amplification beyond that required by Illumina preparation was used and consider these samples non-specifically amplified, or “unamplified”.

### Commercial Sample preparations

mRNA was extracted from the TRNA isolated from the sample used for the KSU data set using the PolyATtract mRNA isolation system (Promega, Fitchburg, WI) following manufacturer’s instructions. RT-PCR for samples amplified with Avian Myeloblastosis Virus (AMV) reverse transcriptase based sample preparation was performed using the Access RT-PCR System (Promega, Fitchburg, WI) following the manufacturer’s instructions. RT-PCR for Moloney Murine Leukemia Virus (MMLV) reverse transcriptase based sample preparation was performed using the SuperScript III First-Strand Synthesis System (Invitrogen, Carlsbrad, CA) following manufacturer’s instructions. Starting material for RT-PCR was either TRNA from the KSU data set or the purified mRNA. RT-PCR products were submitted to Adaptive Biotechnologies (Seattle, WA) **(Com1)** on dry ice following company protocols. TRNA and mRNA (unamplified) were submitted to iRepertoire, Inc. (Huntsville, AL) **(Com2)** on dry ice following company protocols.

### Bioinformatic Analysis

KSU sequencing results were analyzed as described previously ([9](#R9)). Briefly, sequencing results were quality controlled. Antibody-specific sequences were isolated and submitted to ImMunoGeneTics (IMGT) ([19](#R19)) for analysis. Individual sequences were assigned a unique ID by the sequencing machinery during Illumina sequencing and were used to identify unique sequences. The sequence containing the most high quality information was retained for further analysis as outlined in Rettig *et al* ([9](#R9)). No further filtering of reads was performed. Both commercial sequencers provided their own bioinformatic analyses of the sequencing results. The raw sequencing results from Com1 and Com2 were also submitted to IMGT for analysis and subjected to the standard KSU bioinformatics pipeline. IMGT’s nomenclature and classifications were used throughout this paper. We assessed all functional V-gene segments as identified by IMGT. We also include three putative functional genes (V5S21, V1S100, and V3S7) which were detected in rearranged transcripts (containing a CDR3 C-xx-W motif or class switched) in our previous analysis of the normal C57BL/6 repertoire ([20](#R20)). IMGT’s High-V Quest occasionally assigned multiple potential V-gene segments to a single sequence, likely due to incomplete capture of the entire V-gene sequence or high homology between gene segments.

In all IMGT processed data, sequences that contained two possible V-gene segment possibilities were assigned a weighted value of 0.5 per sequence, as opposed to one for full matches. Sequences with V-gene segments that were assigned more than two potential matches were excluded from analysis. Initial results were tabulated using the companys’ proprietary bioinformatic results. However, to determine the role of bioinformatic handling of the data, some of Com1 and Com2 data were subjected to the standard KSU bioinformatic workflow analysis and CDR3 analyses ([9](#R9)).

### Statistical Tests

All statistical analyses were carried out using GraphPad Prism (Version 6.0). Paired T-tests were performed using the raw read counts. Coefficient of determinations (R2) were performed by comparing the percent of repertoire between animals. Percent of repertoire is determined by dividing the read count for a specific V-gene segment by the total number of reads detected and multiplying by 100.

## Results

Most studies examining immunoglobulin repertoires use amplification to increase the depth of sequencing, but amplification comes with some drawbacks. We wanted to assess the comparability of amplified and non-amplified data from identical samples. In preparation to do this comparison, we found that different commercial amplification methodologies required different types of sample preparation. For example, sample submission for the Com1 data sets required a cDNA sample. The Com1 process amplified the resulting cDNA using proprietary primers and sequencing on the Illumina platform. After an initial submission showed a low correlation between the Com1 sequencing and the KSU data set (data not shown), we hypothesized that cDNA preparation plays a role in determining the amplified repertoire. To test this hypothesis, we assessed the role of starting material (mRNA or TRNA), reverse transcriptase (AMV vs MMLV), and primer templates (oligo-dT or random hexamer) on the sequenced B cell immunoglobulin repertoire. Com2 submissions required the submission of TRNA, rather than cDNA.

### Assessment of Transcriptional Read Counts

Com1amplified data sets returned between 7,084 and 1,263,003 sequences, dependent on the preparation method. mRNA starting material yielded more total transcriptional reads than TRNA (P=0.013, 2 tailed matched T test; [Table 1](#T1)). Generally, the AMV reverse transcriptase and random hexamer primers tended to yield higher numbers of transcripts. The use of AMV and random hexamer primers resulted in more total productive reads in three out of four of the comparisons directly comparing primers, however, the overall differences were not statistically different (P>0.05, 2 tailed matched T test; [Table 1](#T1)). In the Com2 data set, we found a moderate number of reads, about one-half of those detected in the highest Com1 numbers. These compare to 11,200 sequence reads containing a CDR3 generated in the KSU data set using a total MiSeq approach.

#### Table 1:

Total number of productive reads per data set

|  | KSU[a](#TFN1) | Com 1[a](#TFN1) | | | | | | | | Com 2[a](#TFN1) | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mRNA[b](#TFN2) | | | | TRNA[b](#TFN2) | | | | mRNA[b](#TFN2) | TRNA[b](#TFN2) |
| AMV[c](#TFN3) | | MMLV[c](#TFN3) | | AMV[c](#TFN3) | | MMLV[c](#TFN3) | |
| dT[d](#TFN4) | Hex[d](#TFN4) | dT[d](#TFN4) | Hex[d](#TFN4) | dT[d](#TFN4) | Hex[d](#TFN4) | dT[d](#TFN4) | Hex[d](#TFN4) |
| Total Productive Reads | 11,200[e](#TFN5) | 553,521 | 1,263,003 | 883,532 | 1,035,461 | 7,975 | 6,867 | 208,979 | 220,772 | 637,214 | 766,075 |

[Open in a new tab](table/T1/)

a

– Sequencing technique (Com1 and Com2 are amplified data sets)

b

– starting material (mRNA – Messenger RNA, TRNA – Total RNA)

c

– reverse transcriptase (AMV - Avian Myeloblastosis Virus, MMLV - Moloney Murine Leukemia Virus)

d

– primer (dt – Oligo dT, Hex – Random hexamer)

e

– an additional 27,896 reads were used for V-gene segment usage assessment. These sequences were not long enough for CDR3 detection.

### Determination of Sequencing Reproducibility

To assess the repeatability of the amplified Com1 and Com2 data sets, we examined the correlation of V-gene segment usage. In the C57BL/6 mouse, the V-gene segment is the most varied in the heavy chain (IgH locus) comprising a total of 109 functional V-gene segments, three putative function V-gene segments, and alleles compared to 19 for the D-gene segment and four for the J-gene ([21](#R21), [22](#R22)). The nucleotide sequences in the V-gene segments are also highly varied and require a complex multiplex PCR to amplify. Correlations were assessed using the data provided by the commercial vendor’s proprietary bioinformatics.

Non-strain specific V-gene segment assignments accounted for between 0.84% and 1.46% of the sequencing results from Com 1 and 1.74% and 1.41% for Com2 ([Table 2](#T2)). Although there were differences in the immunoglobulin gene transcripts detected, there was a high correlation in the V-gene sequences detected among the different technical replicates in the Com1 data (R2 range from 0.6986 to 0.9933, all p<0.0001) ([Figure 1](#F1)). The R2 between technical replicates in Com2 was 0.9621 (p<0.0001). We also examined the reproducibility of two technical replicates of KSU sequencing used for a different analysis and obtained an R2 of 0.9996 for Mouse 32, and 0.9995 for Mouse 39 (p<0.001) showing high levels of reproducibility between KSU sequencing runs. Therefore, although total transcripts generated varied with sample preparation, the V-gene segments that were detected were consistently detected using two different commercial approaches.

#### Table 2:

Percent of non-C57BL/6 V-gene segments detected per data set

|  | Com 1[a](#TFN6) | | | | | | | | Com 2[a](#TFN6) | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mRNA[b](#TFN7) | | | | TRNA[b](#TFN7) | | | | mRNA[b](#TFN7) | TRNA[b](#TFN7) |
| AMV[c](#TFN8) | | MMLV[c](#TFN8) | | AMV[c](#TFN8) | | MMLV[c](#TFN8) | |
| dT[d](#TFN9) | Hex[d](#TFN9) | dT[d](#TFN9) | Hex[d](#TFN9) | dT[d](#TFN9) | Hex[d](#TFN9) | dT[d](#TFN9) | Hex[d](#TFN9) |
| % Non-B6 V-Gene segments | 0.92 | 0.88 | 0.84 | 1.17 | 1.30 | 1.46 | 1.02 | 1.14 | 1.74 | 1.41 |

[Open in a new tab](table/T2/)

a

– Sequencing technique (Com1 and Com2 are amplified data sets)

b

– starting material (mRNA – Messenger RNA, TRNA – Total RNA)

c

– reverse transcriptase (AMV - Avian Myeloblastosis Virus, MMLV - Moloney Murine Leukemia Virus)

d

– primer (dt – Oligo dT, Hex – Random hexamer)

#### Figure 1.

![Figure 1.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83bb/6366624/4d78f2ff66da/nihms-987236-f0001.jpg)

[Open in a new tab](figure/F1/)

R2 values of sequencing technical replicates. The percent of repertoire for each V-gene segment detected was compared between technical replicates. The highest R2 are dark read, the lowest R2 are blue.

### Impact of Amplification on V-gene Segment Detection

The unamplified KSU approach produced a data set where a total of 112 V-gene segments were detected while the Com1 data sets contained between 85 and 100 V-gene segments. The Com2 mRNA data set contained 99 detectable V-gene segments and the TRNA contained 100. Comparisons of V-gene segments in the Com1 data set to the KSU data set showed moderate R2 values; 0.4457 to 0.5841 (all p<0.0001) ([Table 3](#T3)). The Com2 data sets also showed moderate R2 of 0.6695 for mRNA and 0.6607 for TRNA (all p<0.0001). To determine why there were differences in V-gene detection, we compared the results from the most commonly detected V-gene segments in the KSU data sets to their frequencies in the Com1 and Com2 data sets. The protocol for Illumina sequencing uses mRNA selection, SuperScriptIII reverse transcriptase, and random hexamer primers. To best compare results, we used the Com1 mRNA-MMLV-Hex data set and the Com2 mRNA data set using the top 34 V-gene segments in the KSU data set. These V-gene segments comprise over one percent of the detected repertoire and are considered highly expressed. In the Com1 data set, of these 36 highly expressed V-gene segments, five (V1-26, V1-18, V1-50, V4-1, and V2-6) were detected at two-fold lower frequency than in the KSU data set ([Figure 2](#F2)). These five V-gene segments were either absent or were near zero percent of the repertoire ([Figure 2](#F2)). Of these same top 34 V-gene segments in the Com1 data set, two (V6-3 and V2-6-8) were detected at two-fold greater than the KSU data set ([Figure 2](#F2)). The R2 for these top 36 V-gene segments to the KSU data set was 0.1783 (P=0.0128).

#### Table 3:

Correlations of data sets to unamplified KSU data set and read counts

|  | Com 1[a](#TFN10) | | | | | | | | Com 2[a](#TFN10) | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mRNA[b](#TFN11) | | | | TRNA[b](#TFN11) | | | | mRNA[b](#TFN11) | TRNA[b](#TFN11) |
| AMV[c](#TFN12) | | MMLV[c](#TFN12) | | AMV[c](#TFN12) | | MMLV[c](#TFN12) | |
| dT[d](#TFN13) | Hex[d](#TFN13) | dT[d](#TFN13) | Hex[d](#TFN13) | dT[d](#TFN13) | Hex[d](#TFN13) | dT[d](#TFN13) | Hex[d](#TFN13) |
| R2 to KSU Dataset | 0.5677 | 0.5773 | 0.4496 | 0.5517 | 0.4457 | 0.5606 | 0.5554 | 0.5841 | 0.6695 | 0.6607 |
| Assessed V-Gene Segments | 506,503 | 151,104 | 1,749,618 | 1,245,999 | 267,946 | 5,666 | 267,946 | 302,057 | 626,093 | 755,280 |

[Open in a new tab](table/T3/)

a

– Sequencing technique (Com1 and Com2 are amplified data sets)

b

– starting material (mRNA – Messenger RNA, TRNA – Total RNA)

c

– reverse transcriptase (AMV - Avian Myeloblastosis Virus, MMLV - Moloney Murine Leukemia Virus)

d

– primer (dt – Oligo dT, Hex – Random hexamer)

#### Figure 2.

![Figure 2.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83bb/6366624/1de6df894d56/nihms-987236-f0002.jpg)

[Open in a new tab](figure/F2/)

Percent of repertoire for high frequency V-gene segments among data sets. Percent of repertoire for the KSU, Com1 (mRNA-MMLV-hex), Com2 (mRNA), and Prod (productive only sequences from the KSU data set) are displayed. The highest value percent of repertoire is dark read while the lowest are white. Black boxes represent no detected reads (true zero). Rounded zeros are represented as 0.0.

We also compared the Com2 mRNA data set to the same 34 V-gene segments from the unamplified KSU data. Nine of the 34 V-gene sequences (V9-3, V4-1, V2-6, V1-81, V5-17, V2-2, V8-8, V11-2, V14-2) were detected at a twofold or lower level than in the KSU data set ([Figure 2](#F2)). Five other V-gene segments (V1-53, V3-6, V1-64, V10-1, and V1-69) were detected at twofold higher levels than those found in the KSU data set ([Figure 2](#F2)). The correlation of these top 34 V-gene segments was better than the Com1 R2 at 0.4098 (P=<0.0001).

Our normal workflow methods include the use of functionally productive and unknown transcripts for analysis ([9](#R9)). This inclusion helps balance the lower read numbers obtained with unamplified sequences. We performed the same analysis as above between our productive + unknown dataset used above, with our productive only dataset. We detected a tota1 of 104 V-gene segments. Those not detected in the productive only list (V3S7, V6-7, V6-4, V1-62-1, V5-12-4, V1-17-1, and V6-5) comprised less than 0.7% of the repertoire. The correlation coefficient was high at 0.9596(P<0.0001), and there were no changes at great than 2-fold of the productive + unknown data set ([Figure 2](#F2)). These analyses reveal that the addition of unknown functionality V-gene segments does not significantly alter the repertoire.

### Direct Comparisons of Amplified and Unamplified Data Sets

The comparisons in V-gene use were made using the bioinformatics provided by the commercial ventures. To standardize the data handling to remove bioinformatic reasons for the differences in data, we processed the sequencing results from the Com1 mRNA-MMLV-Hex and Com2 mRNA data sets using the KSU bioinformatics work flow ([9](#R9)).

The KSU bioinformatic treatment of the Com1 data set correlated moderately with the commercially provided bioinformatics (R2=0.4795, p<0.0001). After processing the Com1 data with the KSU bioinformatics pipeline, the R2 to the KSU data set increased slightly from 0.5517 ([Table 3](#T3)) with the original bioinformatics to 0.5649 (p<0.0001) with the adjusted bioinformatics. However, nine V-gene segments were detected in the Com1 data set using the KSU bioinformatics workflow that were not originally detected using the commercially provided bioinformatics ([Sup Fig 1](#SD1)). When we processed the Com2 data using the KSU bioinformatic pipeline, the Com2 data set was highly correlated with the original commercially provided bioinformatics treatment (R2=0.9860, p<0.0001). When we compared Com2 data set processed with the KSU bioinformatics pipeline to the KSU RNASeq data set, the data still only had an R2=0.6791 (p<0.0001). The KSU bioinformatics workflow detected an additional four V-gene segments that were not detected by the commercial bioinformatics ([Sup Fig 1](#SD1)).

When we reanalyzed the bioinformatics data from Com1 and Com2 using the KSU pipeline, we detected gene segments that were not detected in the original commercially provided bioinformatics. However, the inclusion of these gene segments, did not greatly improve the R2 between the amplified data sets and the KSU RNASeq data. In the Com1 data set, some gene segments (V1-26, V1-18, V1-50, V2-9-1) were not detected or only detected at low levels in the original bioinformatics but were detected at high levels (>1%) in the KSU/IMGT processed data ([Sup Fig 1](#SD1)). The three additional V-gene segments detected in the Com2 data set (V2-5, V1-62-2, and V1-62-3 were found in less than <0.3% of the repertoire ([Sup Fig 1](#SD1)). These changes were not sufficient to significantly improve R2 values.

### Impact of Amplification on the Reproducibility of CDR3 Detection

The absence of some V-gene segments in the Com1 and Com2 data compared to the KSU data was a concern. It precludes a complete picture of the V-gene repertoire. Nevertheless, amplified sequencing of the antibody repertoire is thought to provide an advantage in that the depth of coverage is increased over unamplified data sets due to the number of reads generated. To determine how extensive the discrepancy is between amplified and unamplified data, we assessed the read depth (number of reads generated) and resampling efficiency of CDR3 (number of unique CDR3s resampled between replicates) using technical replicates of samples sequenced with the various sequencing techniques. As anticipated, amplified data sets had both higher total read numbers and unique CDR3 numbers ([Table 4](#T4)).

#### Table 4:

|  | KSU | mRNA-MMLV-Hex (Com1) | mRNA (Com2) |
| --- | --- | --- | --- |
|  | --- | | |
| Read Count | 11,200 | 1,035,461 | 637,214 |
| Unique CDR3 Sequences | 6668 | 180,266 | 146,231 |

[Open in a new tab](table/T4/)

Resampling/reproducibility has been assumed to improve with the depth of coverage. We had the unique opportunity to compare sequencing data from the same biological material subjected to multiple sequencing methodologies. We have also had the opportunity to do technical replicates on multiple samples subjected to RNASeq or amplification procedures. This allowed us the ability to look at CDR3 sampling reproducibility and to determine if amplification provided any advantage in CDR3 reproducibility. For the KSU unamplified data set, two C57BL/6J mouse spleen RNA samples (#32 and #39) were sequenced independently two times each and the CDR3s sampled were compared. In the KSU data set, 32-1 shared 28% of its total unique reads with 32-2. ([Figure 3](#F3)). 32-2 shared 24% of its reads with 32-1 ([Figure 3](#F3)). KSU data set, 39, showed 25% overlap of their total unique reads between each sampling ([Figure 3](#F3)). For the Com2 data, since there was such a strong correlation between the sequence output between mRNA and TRNA samples of C57BL/6J spleen samples (R2 = 0.9644), we considered these technical replicates. The mRNA data set shared 24% of its sequences with the TRNA data set while the TRNA data set shared 30% of its sequences with the mRNA data set. We also examined the resampling efficiency in the Com1 data set using the spleen mRNA-MMLV data sets that were reversed transcribed with two different primers, random hexamer and oligo-dT. Although this was not a perfect technical replicate, there was an R2 of almost 0.94 in V-gene segments detected ([Figure 1](#F1)). Therefore, we felt these served as “incipient” technical replicates. The random hexamer data set shared 20% of the detected CDR3s and the oligo dT data set shared 32% of its CDR3 sequences. Therefore, regardless of data set, there was an average of 26-27% sampling overlap regardless of whether amplification was performed or not.

#### Figure 3.

![Figure 3.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83bb/6366624/5c0987937083/nihms-987236-f0003.jpg)

[Open in a new tab](figure/F3/)

Overlap of CDR3 sequence detection between technical replicates. CDR3 amino acid sequences were compared between technical replicates. Sequences unique to one data set are displayed in the outer circles. Sequences shared between data sets are in the overlap. Percent of shared CDR3 sequences is displayed in parentheses in the outer circles. (A) KSU data sets 32-1 and 32-2. (B) KSU data sets 39-1 and 39-2. (C) Com1 data sets mRNA-MMLV-Hex and mRNA-MMLV-dT. (D) Com2 data sets mRNA and TRNA.

We also assessed the overlap in the detected CDR3s between the Com1 data set (mRNA-MMLV-Hex), Com2 data set (mRNA), and the KSU original data set to determine the extent of the overlap of CD3 detection using the different methods. From the 295,116 CDR3 unique sequences that were detected, 2662 of those sequences were shared among all three data sets ([Figure 4](#F4)). The amplified data sets from Com1 and Com2 shared the most CDR3 sequences between them with 34,141 sequences found in both data sets ([Figure 4](#F4)). The KSU data set shared 59% of its detected CDR3 sequences with the Com1 and Com2 data sets ([Figure 4](#F4)). These data are consistent with the lower depth of sequencing of the unamplified data set compared to the Com1 and Com2 data sets where 19-32% overlap occurred in detected CDR3 sequences.

#### Figure 4.

![Figure 4.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83bb/6366624/1b79c07fc0ef/nihms-987236-f0004.jpg)

[Open in a new tab](figure/F4/)

CDR3 sequence capture among Com1, Com2, and KSU data sets. CDR3 amino acid sequences were compared among the Com1 mRNA-MMLV-Hex, Com2 mRNA, and the KSU data sets. Percent of the repertoire shared with at least one other data set is listed in parentheses.

### Detection of High Frequency CDR3s

To gauge whether the highest frequency CDR3s can be detected by the different techniques, we assessed the 25 highest frequency CDR3s from each sequencing method. This resulted in a total of 48 unique CDR3s from the three different methods ([Figure 5](#F5)). The KSU data set detected all but one (CARGYFDVW) of these 48 sequences, the Com1 data set failed to detect four sequences (CARGTYW, CTWDEGNYW, CARGIYW, CARGSYW) and the Com2 data set detected all 48 sequences ([Figure 5](#F5)). The CDR3s that were not detected in the Com1 data set, did use V-gene segments that were detected in the data set. These data show that although the depth of sequencing of the KSU data set was about 10% of the amplified data sets, the data set still captured 98% of the highest frequency CDR3’s.

#### Figure 5.

![Figure 5.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83bb/6366624/8ceb9b2187c1/nihms-987236-f0005.jpg)

[Open in a new tab](figure/F5/)

High frequency CDR3s detected among the Com1, Com2, and KSU data sets. The top 25 CDR3s from each data set (48 total) were compiled and percent of repertoire compared. Black boxes represent no detected reads (true zero). Rounded zeros are represented as 0.0.

### CDR3 Frequency Assessment

While the high frequency CDR3s were shared among at least two sequencing runs, most of the CDR3 sequences detected were unique to each sequencing run ([Figure 4](#F4)). To determine the frequency of unique CDR3 sequences, we compared the most frequent, least frequent, and average percent of the measured CD3 repertoire ([Table 5](#T5)). The highest frequency CDR3 was detected at 4.16%, 0.22%, 2.26%, and of the repertoire for the KSU, Com1, and Com2 data sets, respectively ([Table 5](#T5)). The lowest frequency CDR3s, representing only a single detected read, were 0.0088%, 0.0004%, and 0.0002%, of the repertoire for the KSU, Com1, and Com2 data sets, respectively ([Table 5](#T5)). The average detection level for the KSU data set was 0.015%, 0.0006% for the Com1 data set, and 0.0007% for the Com 2data set ([Table 5](#T5)).

#### Table 5:

|  | Whole Repertoire | | | Unique Repertoire | | |
| --- | --- | --- | --- | --- | --- | --- |
| KSU | Com1 | Com2 | KSU | Com1 | Com2 |
| Minimum | 0.008758 | 0.000446 | 0.000221 | 0.008758 | 0.000446 | 0.000221 |
| Maximum | 4.1655 | 0.216969 | 2.259680 | 0.035032 | 0.005804 | 0.026044 |
| Average | 0.014997 | 0.000555 | 0.00684 | 0.008929 | 0.000478 | 0.00290 |

[Open in a new tab](table/T5/)

We also examined the frequency of CDR3s that were unique to each data set. Overall, the maximum and the average frequencies of the data sets were reduced compared to the whole repertoire ([Table 5](#T5)). This demonstrates that the unique reads in each data set were most likely transcripts from low frequency B cells. Moreover, these data suggest that even without amplification, the KSU data set was detecting the most prevalent CDR3s and many low-frequency sequences.

## Discussion

Illumina sequencing of total RNA from mouse spleen is able to capture a representative sample of the splenic B cell repertoire. This snapshot of the repertoire, while producing less reads than amplified data sets, detected more V-gene segments than data sets that used two different amplification strategies and captures 98% of the high frequency CDR3s found in the amplified data sets. While amplified data sets provide more CDR3 depth of coverage, the unamplified data sets produced from an RNASeq allow for further data mining, eliminate as much primer bias as possible and provides an accurate representation of the repertoire.

Sequencing requirements of the B cell receptor are more challenging than those of the T cell receptor. There are no consensus sequences to reference ([10](#R10)). Additionally, transcripts from the germline which are not successfully rearranged can be detected ([23](#R23)). Therefore, avoiding bias is one of the main priorities for antibody repertoire sequencing ([16](#R16)). PCR errors are accumulated through the amplification process which can falsely inflate the repertoire or they can add suspected mutations that do not exist ([10](#R10), [17](#R17), [24](#R24), [25](#R25)) and they may not be distinguishable from low level mutations that actually do exist in the repertoire ([24](#R24), [26](#R26)). PCR biases can be introduced because of primer binding properties, CG content, mispriming, non-specific binding, and errors during replication ([16](#R16), [27](#R27)–[29](#R29)). A specific issue in targeting antibody gene segments is primer annealing efficiencies since the gene segments that make up the murine IgH locus are similar, though not identical ([28](#R28)). The biases inherent in the multiplex PCR can lead to false repertoire skewing, gene frequency inaccuracies, and a less comprehensive view of the repertoire ([25](#R25), [30](#R30), [31](#R31)). The development of these multiplex primers, is highly challenging ([32](#R32)). Work by Bashford-Rogers ([33](#R33)) shows that there is little difference between RNA-capture, 5’RACE or PCR amplification in humans but others ([27](#R27)) have shown that PCR does create biases and 5’ RACE helps reduce these.

Our results demonstrate some of the issues of assessing B-cell repertoires using massively multiplexed PCR reactions. While reproducibility for technical replicates was moderate to high, there was a large range of total read numbers across methodologies. Given the increase in read results with mRNA samples compared to TRNA samples, the authors hypothesize that mRNA increases the availability of antibody specific transcripts, increasing the overall read counts. Additionally, the reverse transcriptase plays a role in sequence generation. AMV reverse transcriptase has an RNase H activity, where MMLV reverse transcriptase does not ([34](#R34)). This activity may cleave RNA transcripts prior to completion of amplification, resulting in shorter reads with inadequate length for amplification. The use of oligo-dT primers will begin reverse transcription from the most 3’ end of the transcript. The target of amplification is around 1.5 kilobases upstream of the poly-A tail ([35](#R35)), likely leading to shorter reads and failure to amplify the region of interest. Random hexamer primers maybe able to overcome this bias due to their random priming nature.

In addition to variations in read depth, the correlations of these data sets to the unamplified KSU data sets were low to moderate, even when the same bioinformatics processing was employed. Of significant concern is the Com1 and Com2 sets failed to detect 13 V-gene segments that were detected by the unamplified KSU RNASeq data set. The absence of these genes draws into question how one compares the various data sets with correlation coefficients that are below 0.7 when technical replicates of the same sequencing are greater than 0.99. Although Carlson *et al.* argues that amplification methodologies can capture the entire repertoire, there are concerns ([11](#R11)). Even when we only looked at the V-gene families detected at the highest frequency there were omissions. Of the 34 V-genes that we categorized as “high frequency” (>1% of the repertoire), Com1 found lower detection levels (defined as less than two-fold that found in the KSU data set) for five gene segments (V1-26, V1-18, V1-50, V4-1, and V2-6) and nine (V9-3, V4-1, V2-6, V1-, V5-17, V2-2, V8-8, V11-2, V14-2) for the Com2 data set. These results suggest that those methods are skewing the reported repertoire by missing or underreporting those high frequency V-gene segments. Interestingly, two V-gene segments (V4-1 and V2-6) were underrepresented in both data sets, but the other V-gene segments were unique.

The failure of primers to capture specific V-genes is not a new discovery, as primers failed to adequately sequence hybridomas previously ([18](#R18), [36](#R36)). “Universal” primers for the human antibody repertoire do exist, but some questions remain if they cover the entire repertoire ([37](#R37)). The difficulty in developing a “universal” or even highly comprehensive primer set for the mouse is likely due to their highly varied leader sequences, V-gene segments, and framework regions. Primer design would have to rely on massively multiplexed reactions and/or degenerate primers. Additionally, the most commercially viable amplification methods would need to amplify across multiple common strains adding additional levels of complexity. Indeed, in our attempts to design “universal” primers, we found a minimum of 11 primer sets would be needed to detect V-genes associated for each isotype. Even then, there were still issues with matching PCR conditions and efficiency. Methods to overcome the biases detected in amplification have been developed, such as the use of 5’ RACE ([26](#R26), [38](#R38), [39](#R39)) and using molecular barcodes or identifiers ([40](#R40), [41](#R41)). However, these methods are expensive and have their own draw backs. Replication of the entire repertoire using 5’RACE would still require the use of multiple constant region primers, leading to the same multiplexing issues. Barcoding can have errors and chimeric reads making repertoires difficult to reconstruct ([42](#R42)). This latter issue is not a problem with our RNASeq data.

While bias exists in the massively multiplexed amplification process, there may be some sequencing errors in the unamplified KSU data set as well. While not specifically amplified for antibody sequences, random hexamers and oligo-dT capture beads are used prior to sequencing to generate the library ([43](#R43)) and some biases have been observed in random hexamer binding ([44](#R44)). The use of oligo-dTs can result in enhancement of the 3’ end of transcripts ([45](#R45)). We do not think this is particularly problematic since Illumina sequence methodology aims to reduce bias in their library preparations by combining the random hexamer and oligo-dT capture. Additionally, while all libraries were sequenced on the Illumina platform, 3.19% of high-quality Illumina reads contain false base calls, which are impossible to differentiate using normal bioinformatics methods ([10](#R10)). Over representation of specific dineuclotides can also be detected in sequencing which are not related to primer usage ([46](#R46)). Therefore, although we hope to reduce bias and omission by doing RNASeq, we still have some technical issues that keep the data set from being a perfect reflection of the repertoire. Multiple technical replications help reduce the impact of this problem.

One analysis that was not pursued in this current investigation was the identification of clonally related sequences. We were specifically interested in the functional antibody repertoire present in the spleen and focused our analysis at the transcript level. We acknowledge that the overrepresentation of some sequences may be likely within our data sets since we don’t use barcoding or clonality analysis to collapse similar mRNA sequences. Nevertheless, the overrepresentation of a specific sequence by an overly productive cell is also representative of cellular activation of transcription, and likely, functional antibody protein in the body ([47](#R47), [48](#R48)).

The lack of amplification also results in varying sequence lengths in our data set. We selected 40nt as our minimum cutoff to provide us enough information to detect V-, D-, and J- gene segments. While some short sequences were included in the data analysis, our overall average sequence length was 287nt, with productive sequences averaging 331nt and unknown sequences averaging 270 nt (data not shown). Overall, less than 0.5% of the sequences analyzed where less than 100nt long (data not shown). Therefore, we do not think that sequence length is an issue in this study.

Although there are issues using massively multiplexed PCR reactions, there are advantages that may overshadow the disadvantages. For example, increased sequencing depth (*e.g.* 1,260,000 reads *vs*. 11,200 complete reads), better low frequency CDR3 detection (20-fold more unique CDR3 sequence than the unamplified KSU data set), and sequencing costs can be lower than an Illumina MiSeq run (by integrating multiplexing/barcoding).

Although amplification provides more detail in the CDR3 repertoire, if one is interested in the B cell clones that are most prevalent, then RNASeq does not appear to be at a disadvantage. CDR3 resampling was similar (20-32%) regardless of method. Additionally, when examining high frequency CDR3s, the unamplified data set only failed to detect a single unique CDR3 sequence, while the Com1 data set failed to detect four. Without using an amplification method with unique barcoding, such as that used in Shugay et al ([49](#R49)) it is impossible to tell which unique CDR3s are, in fact, correctly identified new sequences and which involve miscalls, leading to false diversity. As our current paper does not focus on the actual diversity of the repertoire, and instead focuses on the differences among sample preparations and sequencing methods, we do not attempt to identify false call unique CDR3s as doing so may falsely reduce diversity. Instead, the we used strict read quality cutoffs to prevent low quality base calls from being included in analysis, and we point to our highly overlapping V-gene segment usage (R2 = 0.9995 among multiple sequencing replicates to assure us that we minimized artifacts. Additionally, all sequencing was performed on the Illumina platform, so false base call rates should be similar across methodologies which we were focused on in this study.

When preparing for antibody repertoire sequencing, multiple factors must be considered within the framework of the specific biological questions being asked. This includes needed coverage, cost, and starting material ([39](#R39)). Additionally, it is important to consider that all repertoire sequencing is merely a snapshot of a constantly shifting image ([25](#R25)). We will also never be able to fully capture the full diversity of the B cell immunoglobulin repertoire, which is estimated to range from 106-107 possible unique rearrangements and mutations ([25](#R25), [39](#R39)) to as much as 1013 ([15](#R15)). The failure of the KSU data set to detect rare clones compared to the amplified data sets is likely due to this; but even the amplified data sets only sampled a fraction of the total repertoire. Therefore, one must decide how “deep” is adequate for the question being addressed.

During this investigation, we also had to address the issue that starting material may influence the quality of one’s sequencing. mRNA as a starting template increased reads up to two orders of magnitude. Furthermore, random hexamer primers and MMLV reverse transcriptase generally yielded higher read count results. Interestingly, the use of mRNA, with MMLV reverse transcriptase and hexanucleotide primers is most technically like that used in Illumina sequencing. However, additional data will be needed to confirm our observations since we did not pursue this aspect of the study in detail and the replicate number did not allow for robust statistical comparisons.

In conclusion, we have demonstrated that sequencing of unamplified splenic RNA provides a realistic snapshot of the total splenic B cell repertoire. We also have demonstrated that a good understanding of the bioinformatics work flow and reporting of the methodology is critical and cannot be understated. We understand that there are cellular biases and transcript stability differences with in B cell subpopulations ([50](#R50), [51](#R51)). However, for the purpose of assessing a whole tissue B cell repertoire, unamplified RNASeq can provide a glimpse of the most prevalent B cell clones. The unamplified approach could just as well be applied to specific cell populations when the application requires it. Moreover, an unamplified data set may detect V-gene segments that amplified data sets miss.

## Supplementary Material

Supp FigS1

[NIHMS987236-supplement-Supp\_FigS1.pdf](/articles/instance/6366624/bin/NIHMS987236-supplement-Supp_FigS1.pdf) (365.2KB, pdf)

## Acknowledgements

Our work is supported by NASA grants NNX13AN34G and NNX15AB45G, NIH grant GM103418, the Molecular Biology Core supported by the College of Veterinary Medicine at Kansas State University, and the Kansas State University Johnson Cancer Research Center. The authors declare no conflict of interest.

## Abbreviations:

V
:   Variable Gene Segment

D
:   Diversity Gene Segment

J
:   Joining Gene Segment

TRNA
:   Total RNA

AMV
:   Avian Myeloblastosis Virus

MMLV
:   Moloney Murine Leukemia Virus

IMGT
:   ImMunoGeneTics

## References

* 1.Ademokun A, Wu Y-C, Martin V, Mitra R, Sack U, Baxendale H, Kipling D, and Dunn Walters D (2011) Vaccination-induced changes in human B-cell repertoire and pneumococcal IgM and IgA antibody at different ages. Aging cell
  10, 922–930 [[DOI](https://doi.org/10.1111/j.1474-9726.2011.00732.x)] [[PMC free article](/articles/PMC3264704/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21726404/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Aging%20cell&title=Vaccination-induced%20changes%20in%20human%20B-cell%20repertoire%20and%20pneumococcal%20IgM%20and%20IgA%20antibody%20at%20different%20ages&author=A%20Ademokun&author=Y-C%20Wu&author=V%20Martin&author=R%20Mitra&author=U%20Sack&volume=10&publication_year=2011&pages=922-930&pmid=21726404&doi=10.1111/j.1474-9726.2011.00732.x&)]
* 2.Galson JD, Clutterbuck EA, Truck J, Ramasamy MN, Munz M, Fowler A, Cerundolo V, Pollard AJ, Lunter G, and Kelly DF (2015) BCR repertoire sequencing: different patterns of B-cell activation after two Meningococcal vaccines. Immunology and cell biology
  93, 885–895 [[DOI](https://doi.org/10.1038/icb.2015.57)] [[PMC free article](/articles/PMC4551417/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25976772/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Immunology%20and%20cell%20biology&title=BCR%20repertoire%20sequencing:%20different%20patterns%20of%20B-cell%20activation%20after%20two%20Meningococcal%20vaccines&author=JD%20Galson&author=EA%20Clutterbuck&author=J%20Truck&author=MN%20Ramasamy&author=M%20Munz&volume=93&publication_year=2015&pages=885-895&pmid=25976772&doi=10.1038/icb.2015.57&)]
* 3.Strauli NB, and Hernandez RD (2016) Statistical inference of a convergent antibody repertoire response to influenza vaccine. Genome medicine
  8, 60. [[DOI](https://doi.org/10.1186/s13073-016-0314-z)] [[PMC free article](/articles/PMC4891843/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27255379/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genome%20medicine&title=Statistical%20inference%20of%20a%20convergent%20antibody%20repertoire%20response%20to%20influenza%20vaccine&author=NB%20Strauli&author=RD%20Hernandez&volume=8&publication_year=2016&pages=60&pmid=27255379&doi=10.1186/s13073-016-0314-z&)]
* 4.Fan Q, Nelson CS, Bialas KM, Chiuppesi F, Amos J, Gurley TC, Marshall DJ, Eudailey J, Heimsath H, Himes J, Deshpande A, Walter MR, Wussow F, Diamond DJ, Barry PA, Moody MA, Kaur A, and Permar SR (2017) Plasmablast Response to Primary Rhesus Cytomegalovirus (CMV) Infection in a Monkey Model of Congenital CMV Transmission. Clinical and vaccine immunology: CVI
  24, e00510–00516 [[DOI](https://doi.org/10.1128/CVI.00510-16)] [[PMC free article](/articles/PMC5424243/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28298291/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Clinical%20and%20vaccine%20immunology:%20CVI&title=Plasmablast%20Response%20to%20Primary%20Rhesus%20Cytomegalovirus%20(CMV)%20Infection%20in%20a%20Monkey%20Model%20of%20Congenital%20CMV%20Transmission&author=Q%20Fan&author=CS%20Nelson&author=KM%20Bialas&author=F%20Chiuppesi&author=J%20Amos&volume=24&publication_year=2017&pages=e00510-00516&pmid=28298291&doi=10.1128/CVI.00510-16&)]
* 5.Nivarthi UK, Kose N, Sapparapu G, Widman D, Gallichotte E, Pfaff JM, Doranz BJ, Weiskopf D, Sette A, Durbin AP, Whitehead SS, Baric R, Crowe JE Jr., and de Silva AM (2017) Mapping the Human Memory B Cell and Serum Neutralizing Antibody Responses to Dengue Virus Serotype 4 Infection and Vaccination. Journal of virology
  91, e02041–02016 [[DOI](https://doi.org/10.1128/JVI.02041-16)] [[PMC free article](/articles/PMC5309932/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28031369/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20virology&title=Mapping%20the%20Human%20Memory%20B%20Cell%20and%20Serum%20Neutralizing%20Antibody%20Responses%20to%20Dengue%20Virus%20Serotype%204%20Infection%20and%20Vaccination&author=UK%20Nivarthi&author=N%20Kose&author=G%20Sapparapu&author=D%20Widman&author=E%20Gallichotte&volume=91&publication_year=2017&pages=e02041-02016&pmid=28031369&doi=10.1128/JVI.02041-16&)]
* 6.Racanelli V, Brunetti C, De Re V, Caggiari L, De Zorzi M, Leone P, Perosa F, Vacca A, and Dammacco F (2011) Antibody V(h) repertoire differences between resolving and chronically evolving hepatitis C virus infections. PloS one
  6, e25606. [[DOI](https://doi.org/10.1371/journal.pone.0025606)] [[PMC free article](/articles/PMC3182224/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21980500/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20one&title=Antibody%20V(h)%20repertoire%20differences%20between%20resolving%20and%20chronically%20evolving%20hepatitis%20C%20virus%20infections&author=V%20Racanelli&author=C%20Brunetti&author=V%20De%20Re&author=L%20Caggiari&author=M%20De%20Zorzi&volume=6&publication_year=2011&pages=e25606&pmid=21980500&doi=10.1371/journal.pone.0025606&)]
* 7.Faham M, Zheng J, Moorhead M, Carlton VE, Stow P, Coustan-Smith E, Pui CH, and Campana D (2012) Deep-sequencing approach for minimal residual disease detection in acute lymphoblastic leukemia. Blood
  120, 5173–5180 [[DOI](https://doi.org/10.1182/blood-2012-07-444042)] [[PMC free article](/articles/PMC3537310/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23074282/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Blood&title=Deep-sequencing%20approach%20for%20minimal%20residual%20disease%20detection%20in%20acute%20lymphoblastic%20leukemia&author=M%20Faham&author=J%20Zheng&author=M%20Moorhead&author=VE%20Carlton&author=P%20Stow&volume=120&publication_year=2012&pages=5173-5180&pmid=23074282&doi=10.1182/blood-2012-07-444042&)]
* 8.Gerasimov E, Zelikovsky A, Mandoiu I, and Ionov Y (2017) Identification of cancer-specific motifs in mimotope profiles of serum antibody repertoire. BMC bioinformatics
  18, 33–38 [[DOI](https://doi.org/10.1186/s12859-017-1661-5)] [[PMC free article](/articles/PMC5471937/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28617221/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20bioinformatics&title=Identification%20of%20cancer-specific%20motifs%20in%20mimotope%20profiles%20of%20serum%20antibody%20repertoire&author=E%20Gerasimov&author=A%20Zelikovsky&author=I%20Mandoiu&author=Y%20Ionov&volume=18&publication_year=2017&pages=33-38&pmid=28617221&doi=10.1186/s12859-017-1661-5&)]
* 9.Rettig TA, Ward C, Pecaut MJ, and Chapes SK (2017) Validation of Methods to Assess the Immunoglobulin Gene Repertoire in Tissues Obtained from Mice on the International Space Station. Gravitational and Space Research
  5, 2–23 [[PMC free article](/articles/PMC5736159/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29270444/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Gravitational%20and%20Space%20Research&title=Validation%20of%20Methods%20to%20Assess%20the%20Immunoglobulin%20Gene%20Repertoire%20in%20Tissues%20Obtained%20from%20Mice%20on%20the%20International%20Space%20Station&author=TA%20Rettig&author=C%20Ward&author=MJ%20Pecaut&author=SK%20Chapes&volume=5&publication_year=2017&pages=2-23&pmid=29270444&)]
* 10.Bolotin DA, Mamedov IZ, Britanova OV, Zvyagin IV, Shagin D, Ustyugova SV, Turchaninova MA, Lukyanov S, Lebedev YB, and Chudakov DM (2012) Next generation sequencing for TCR repertoire profiling: platform-specific features and correction algorithms. European journal of immunology
  42, 3073–3083 [[DOI](https://doi.org/10.1002/eji.201242517)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22806588/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=European%20journal%20of%20immunology&title=Next%20generation%20sequencing%20for%20TCR%20repertoire%20profiling:%20platform-specific%20features%20and%20correction%20algorithms&author=DA%20Bolotin&author=IZ%20Mamedov&author=OV%20Britanova&author=IV%20Zvyagin&author=D%20Shagin&volume=42&publication_year=2012&pages=3073-3083&pmid=22806588&doi=10.1002/eji.201242517&)]
* 11.Carlson CS, Emerson RO, Sherwood AM, Desmarais C, Chung MW, Parsons JM, Steen MS, LaMadrid-Herrmannsfeldt MA, Williamson DW, Livingston RJ, Wu D, Wood BL, Rieder MJ, and Robins H (2013) Using synthetic templates to design an unbiased multiplex PCR assay. Nature communications
  4, 2680. [[DOI](https://doi.org/10.1038/ncomms3680)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24157944/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20communications&title=Using%20synthetic%20templates%20to%20design%20an%20unbiased%20multiplex%20PCR%20assay&author=CS%20Carlson&author=RO%20Emerson&author=AM%20Sherwood&author=C%20Desmarais&author=MW%20Chung&volume=4&publication_year=2013&pages=2680&pmid=24157944&doi=10.1038/ncomms3680&)]
* 12.Arnaout R, Lee W, Cahill P, Honan T, Sparrow T, Weiand M, Nusbaum C, Rajewsky K, and Koralov S (2011) High-resolution description of antibody heavy-chain repertoires in humans. PloS one
  6, e22365. [[DOI](https://doi.org/10.1371/journal.pone.0022365)] [[PMC free article](/articles/PMC3150326/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21829618/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20one&title=High-resolution%20description%20of%20antibody%20heavy-chain%20repertoires%20in%20humans&author=R%20Arnaout&author=W%20Lee&author=P%20Cahill&author=T%20Honan&author=T%20Sparrow&volume=6&publication_year=2011&pages=e22365&pmid=21829618&doi=10.1371/journal.pone.0022365&)]
* 13.Bashford-Rogers RJM, Palser A, Huntly B, Rance R, Vassiliou G, Follows G, and Kellam P (2013) Network properties derived from deep sequencing of human B-cell receptor repertoires delineate B-cell populations. Genome research
  23, 1874–1884 [[DOI](https://doi.org/10.1101/gr.154815.113)] [[PMC free article](/articles/PMC3814887/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23742949/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genome%20research&title=Network%20properties%20derived%20from%20deep%20sequencing%20of%20human%20B-cell%20receptor%20repertoires%20delineate%20B-cell%20populations&author=RJM%20Bashford-Rogers&author=A%20Palser&author=B%20Huntly&author=R%20Rance&author=G%20Vassiliou&volume=23&publication_year=2013&pages=1874-1884&pmid=23742949&doi=10.1101/gr.154815.113&)]
* 14.Briney B, Le K, Zhu J, and Burton DR (2016) Clonify: unseeded antibody lineage assignment from next-generation sequencing data. Scientific reports
  6, 23901. [[DOI](https://doi.org/10.1038/srep23901)] [[PMC free article](/articles/PMC4840318/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27102563/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientific%20reports&title=Clonify:%20unseeded%20antibody%20lineage%20assignment%20from%20next-generation%20sequencing%20data&author=B%20Briney&author=K%20Le&author=J%20Zhu&author=DR%20Burton&volume=6&publication_year=2016&pages=23901&pmid=27102563&doi=10.1038/srep23901&)]
* 15.Greiff V, Menzel U, Miho E, Weber C, Riedel R, Cook S, Valai A, Lopes T, Radbruch A, Winkler TH, and Reddy ST (2017) Systems Analysis Reveals High Genetic and Antigen-Driven Predetermination of Antibody Repertoires throughout B Cell Development. Cell reports
  19, 1467–1478 [[DOI](https://doi.org/10.1016/j.celrep.2017.04.054)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28514665/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20reports&title=Systems%20Analysis%20Reveals%20High%20Genetic%20and%20Antigen-Driven%20Predetermination%20of%20Antibody%20Repertoires%20throughout%20B%20Cell%20Development&author=V%20Greiff&author=U%20Menzel&author=E%20Miho&author=C%20Weber&author=R%20Riedel&volume=19&publication_year=2017&pages=1467-1478&pmid=28514665&doi=10.1016/j.celrep.2017.04.054&)]
* 16.Best K, Oakes T, Heather JM, Shawe-Taylor J, and Chain B (2015) Computational analysis of stochastic heterogeneity in PCR amplification efficiency revealed by single molecule barcoding. Scientific reports
  5, 14629. [[DOI](https://doi.org/10.1038/srep14629)] [[PMC free article](/articles/PMC4602216/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26459131/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientific%20reports&title=Computational%20analysis%20of%20stochastic%20heterogeneity%20in%20PCR%20amplification%20efficiency%20revealed%20by%20single%20molecule%20barcoding&author=K%20Best&author=T%20Oakes&author=JM%20Heather&author=J%20Shawe-Taylor&author=B%20Chain&volume=5&publication_year=2015&pages=14629&pmid=26459131&doi=10.1038/srep14629&)]
* 17.van Dijk EL, Jaszczyszyn Y, and Thermes C (2014) Library preparation methods for next-generation sequencing: tone down the bias. Experimental cell research
  322, 12–20 [[DOI](https://doi.org/10.1016/j.yexcr.2014.01.008)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24440557/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Experimental%20cell%20research&title=Library%20preparation%20methods%20for%20next-generation%20sequencing:%20tone%20down%20the%20bias&author=EL%20van%20Dijk&author=Y%20Jaszczyszyn&author=C%20Thermes&volume=322&publication_year=2014&pages=12-20&pmid=24440557&doi=10.1016/j.yexcr.2014.01.008&)]
* 18.Wang Y, Chen W, Li X, and Cheng B (2006) Degenerated primer design to amplify the heavy chain variable region from immunoglobulin cDNA. BMC bioinformatics
  7
  Suppl 4, S9. [[DOI](https://doi.org/10.1186/1471-2105-7-S4-S9)] [[PMC free article](/articles/PMC1780117/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17217527/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20bioinformatics&title=Degenerated%20primer%20design%20to%20amplify%20the%20heavy%20chain%20variable%20region%20from%20immunoglobulin%20cDNA&author=Y%20Wang&author=W%20Chen&author=X%20Li&author=B%20Cheng&volume=7&issue=Suppl%204&publication_year=2006&pages=S9&pmid=17217527&doi=10.1186/1471-2105-7-S4-S9&)]
* 19.Alamyar E, Duroux P, Lefranc M-P, and Giudicelli V (2012) IMGT® Tools for the Nucleotide Analysis of Immunoglobulin (IG) and T Cell Receptor (TR) V-(D)-J Repertoires, Polymorphisms, and IG Mutations: IMGT/V-QUEST and IMGT/HighV-QUEST for NGS In Immunogenetics (Christiansen FT, and Tait BD, eds) Vol. 882 pp. 569–604, Humana Press;  [[DOI](https://doi.org/10.1007/978-1-61779-842-9_32)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22665256/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Immunogenetics&author=E%20Alamyar&author=P%20Duroux&author=M-P%20Lefranc&author=V%20Giudicelli&author=FT%20Christiansen&publication_year=2012&)]
* 20.Rettig TA, Ward C, Bye BA, Pecaut MJ, and Chapes SK (2018) Characterization of the naive murine antibody repertoire using unamplified high-throughput sequencing. PloS one
  13, e0190982. [[DOI](https://doi.org/10.1371/journal.pone.0190982)] [[PMC free article](/articles/PMC5761896/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29320559/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20one&title=Characterization%20of%20the%20naive%20murine%20antibody%20repertoire%20using%20unamplified%20high-throughput%20sequencing&author=TA%20Rettig&author=C%20Ward&author=BA%20Bye&author=MJ%20Pecaut&author=SK%20Chapes&volume=13&publication_year=2018&pages=e0190982&pmid=29320559&doi=10.1371/journal.pone.0190982&)]
* 21.(2017) IMGT Repertoire (IG and TR).
* 22.(2017) Igh immunoglobulin heavy chain complex [Mus musculus (house mouse)] - Gene - NCBI.
* 23.Angelin-Duclos C, and Calame K (1998) Evidence that immunoglobulin VH-DJ recombination does not require germ line transcription of the recombining variable gene segment. Molecular and cellular biology
  18, 6253–6264 [[DOI](https://doi.org/10.1128/mcb.18.11.6253)] [[PMC free article](/articles/PMC109212/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/9774642/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Molecular%20and%20cellular%20biology&title=Evidence%20that%20immunoglobulin%20VH-DJ%20recombination%20does%20not%20require%20germ%20line%20transcription%20of%20the%20recombining%20variable%20gene%20segment&author=C%20Angelin-Duclos&author=K%20Calame&volume=18&publication_year=1998&pages=6253-6264&pmid=9774642&doi=10.1128/mcb.18.11.6253&)]
* 24.Turchaninova MA, Davydov A, Britanova OV, Shugay M, Bikos V, Egorov ES, Kirgizova VI, Merzlyak EM, Staroverov DB, Bolotin DA, Mamedov IZ, Izraelson M, Logacheva MD, Kladova O, Plevova K, Pospisilova S, and Chudakov DM (2016) High-quality full-length immunoglobulin profiling with unique molecular barcoding. Nature protocols
  11, 1599–1616 [[DOI](https://doi.org/10.1038/nprot.2016.093)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27490633/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20protocols&title=High-quality%20full-length%20immunoglobulin%20profiling%20with%20unique%20molecular%20barcoding&author=MA%20Turchaninova&author=A%20Davydov&author=OV%20Britanova&author=M%20Shugay&author=V%20Bikos&volume=11&publication_year=2016&pages=1599-1616&pmid=27490633&doi=10.1038/nprot.2016.093&)]
* 25.Hou XL, Wang L, Ding YL, Xie Q, and Diao HY (2016) Current status and recent advances of next generation sequencing techniques in immunological repertoire. Genes and immunity
  17, 153–164 [[DOI](https://doi.org/10.1038/gene.2016.9)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26963138/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genes%20and%20immunity&title=Current%20status%20and%20recent%20advances%20of%20next%20generation%20sequencing%20techniques%20in%20immunological%20repertoire&author=XL%20Hou&author=L%20Wang&author=YL%20Ding&author=Q%20Xie&author=HY%20Diao&volume=17&publication_year=2016&pages=153-164&pmid=26963138&doi=10.1038/gene.2016.9&)]
* 26.Georgiou G, Ippolito GC, Beausang J, Busse CE, Wardemann H, and Quake SR (2014) The promise and challenge of high-throughput sequencing of the antibody repertoire. Nature biotechnology
  32, 158–168 [[DOI](https://doi.org/10.1038/nbt.2782)] [[PMC free article](/articles/PMC4113560/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24441474/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20biotechnology&title=The%20promise%20and%20challenge%20of%20high-throughput%20sequencing%20of%20the%20antibody%20repertoire&author=G%20Georgiou&author=GC%20Ippolito&author=J%20Beausang&author=CE%20Busse&author=H%20Wardemann&volume=32&publication_year=2014&pages=158-168&pmid=24441474&doi=10.1038/nbt.2782&)]
* 27.Benichou J, Ben Hamo R, Louzoun Y, and Efroni S (2012) Rep-Seq: uncovering the immunological repertoire through next-generation sequencing. Immunology
  135, 183–191 [[DOI](https://doi.org/10.1111/j.1365-2567.2011.03527.x)] [[PMC free article](/articles/PMC3311040/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22043864/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Immunology&title=Rep-Seq:%20uncovering%20the%20immunological%20repertoire%20through%20next-generation%20sequencing&author=J%20Benichou&author=R%20Ben%20Hamo&author=Y%20Louzoun&author=S%20Efroni&volume=135&publication_year=2012&pages=183-191&pmid=22043864&doi=10.1111/j.1365-2567.2011.03527.x&)]
* 28.Boyd SD, and Joshi SA (2014) High-Throughput DNA Sequencing Analysis of Antibody Repertoires. Microbiology spectrum
  2, AID-0017–2014 [[DOI](https://doi.org/10.1128/microbiolspec.AID-0017-2014)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26104353/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microbiology%20spectrum&title=High-Throughput%20DNA%20Sequencing%20Analysis%20of%20Antibody%20Repertoires&author=SD%20Boyd&author=SA%20Joshi&volume=2&publication_year=2014&pmid=26104353&doi=10.1128/microbiolspec.AID-0017-2014&)]
* 29.Robasky K, Lewis NE, and Church GM (2014) The role of replicates for error mitigation in next-generation sequencing. Nature reviews. Genetics
  15, 56–62 [[DOI](https://doi.org/10.1038/nrg3655)] [[PMC free article](/articles/PMC4103745/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24322726/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20reviews.%20Genetics&title=The%20role%20of%20replicates%20for%20error%20mitigation%20in%20next-generation%20sequencing&author=K%20Robasky&author=NE%20Lewis&author=GM%20Church&volume=15&publication_year=2014&pages=56-62&pmid=24322726&doi=10.1038/nrg3655&)]
* 30.Langerak AW, Bruggemann M, Davi F, Darzentas N, van Dongen JJM, Gonzalez D, Cazzaniga G, Giudicelli V, Lefranc MP, Giraud M, Macintyre EA, Hummel M, Pott C, Groenen P, and Stamatopoulos K (2017) High-Throughput Immunogenetics for Clinical and Research Applications in Immunohematology: Potential and Challenges. Journal of immunology (Baltimore, Md. : 1950)
  198, 3765–3774 [[DOI](https://doi.org/10.4049/jimmunol.1602050)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28416603/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20immunology%20(Baltimore,%20Md.%20:%201950)&title=High-Throughput%20Immunogenetics%20for%20Clinical%20and%20Research%20Applications%20in%20Immunohematology:%20Potential%20and%20Challenges&author=AW%20Langerak&author=M%20Bruggemann&author=F%20Davi&author=N%20Darzentas&author=JJM%20van%20Dongen&volume=198&publication_year=2017&pages=3765-3774&pmid=28416603&doi=10.4049/jimmunol.1602050&)]
* 31.Baum P, Venturi V, and Price D (2012) Wrestling with the repertoire: the promise and perils of next generation sequencing for antigen receptors. European journal of immunology
  42, 2834–2839 [[DOI](https://doi.org/10.1002/eji.201242999)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23108932/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=European%20journal%20of%20immunology&title=Wrestling%20with%20the%20repertoire:%20the%20promise%20and%20perils%20of%20next%20generation%20sequencing%20for%20antigen%20receptors&author=P%20Baum&author=V%20Venturi&author=D%20Price&volume=42&publication_year=2012&pages=2834-2839&pmid=23108932&doi=10.1002/eji.201242999&)]
* 32.Calis JJ, and Rosenberg BR (2014) Characterizing immune repertoires by high throughput sequencing: strategies and applications. Trends in immunology
  35, 581–590 [[DOI](https://doi.org/10.1016/j.it.2014.09.004)] [[PMC free article](/articles/PMC4390416/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25306219/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Trends%20in%20immunology&title=Characterizing%20immune%20repertoires%20by%20high%20throughput%20sequencing:%20strategies%20and%20applications&author=JJ%20Calis&author=BR%20Rosenberg&volume=35&publication_year=2014&pages=581-590&pmid=25306219&doi=10.1016/j.it.2014.09.004&)]
* 33.Bashford-Rogers RJ, Palser AL, Idris SF, Carter L, Epstein M, Callard RE, Douek DC, Vassiliou GS, Follows GA, Hubank M, and Kellam P (2014) Capturing needles in haystacks: a comparison of B-cell receptor sequencing methods. BMC immunology
  15, 29. [[DOI](https://doi.org/10.1186/s12865-014-0029-0)] [[PMC free article](/articles/PMC4243823/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25189176/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20immunology&title=Capturing%20needles%20in%20haystacks:%20a%20comparison%20of%20B-cell%20receptor%20sequencing%20methods&author=RJ%20Bashford-Rogers&author=AL%20Palser&author=SF%20Idris&author=L%20Carter&author=M%20Epstein&volume=15&publication_year=2014&pages=29&pmid=25189176&doi=10.1186/s12865-014-0029-0&)]
* 34.Kotewicz ML, Sampson CM, D’Alessio JM, and Gerard GF (1988) Isolation of cloned Moloney murine leukemia virus reverse transcriptase lacking ribonuclease H activity. Nucleic acids research
  16, 265–277 [[DOI](https://doi.org/10.1093/nar/16.1.265)] [[PMC free article](/articles/PMC334625/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/2448747/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20acids%20research&title=Isolation%20of%20cloned%20Moloney%20murine%20leukemia%20virus%20reverse%20transcriptase%20lacking%20ribonuclease%20H%20activity&author=ML%20Kotewicz&author=CM%20Sampson&author=JM%20D%E2%80%99Alessio&author=GF%20Gerard&volume=16&publication_year=1988&pages=265-277&pmid=2448747&doi=10.1093/nar/16.1.265&)]
* 35.(2018) Ighm immunoglobulin heavy constant mu [Mus musculus (house mouse)] - Gene - NCBI. Pubs
* 36.Berdoz J, Monath TP, and Kraehenbuhl JP (1995) Specific amplification by PCR of rearranged genomic variable regions of immunoglobulin genes from mouse hybridoma cells. PCR methods and applications
  4, 256–264 [[DOI](https://doi.org/10.1101/gr.4.5.256)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/7580911/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PCR%20methods%20and%20applications&title=Specific%20amplification%20by%20PCR%20of%20rearranged%20genomic%20variable%20regions%20of%20immunoglobulin%20genes%20from%20mouse%20hybridoma%20cells&author=J%20Berdoz&author=TP%20Monath&author=JP%20Kraehenbuhl&volume=4&publication_year=1995&pages=256-264&pmid=7580911&doi=10.1101/gr.4.5.256&)]
* 37.Sun Y, Liu HY, Mu L, and Luo EJ (2012) Degenerate primer design to clone the human repertoire of immunoglobulin heavy chain variable regions. World journal of microbiology & biotechnology
  28, 381–386 [[DOI](https://doi.org/10.1007/s11274-011-0830-3)] [[PMC free article](/articles/PMC7089251/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22806814/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=World%20journal%20of%20microbiology%20&%20biotechnology&title=Degenerate%20primer%20design%20to%20clone%20the%20human%20repertoire%20of%20immunoglobulin%20heavy%20chain%20variable%20regions&author=Y%20Sun&author=HY%20Liu&author=L%20Mu&author=EJ%20Luo&volume=28&publication_year=2012&pages=381-386&pmid=22806814&doi=10.1007/s11274-011-0830-3&)]
* 38.Lees WD, and Shepherd AJ (2017) Studying Antibody Repertoires with Next-Generation Sequencing. Methods in molecular biology (Clifton, N.J.)
  1526, 257–270 [[DOI](https://doi.org/10.1007/978-1-4939-6613-4_15)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27896747/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Methods%20in%20molecular%20biology%20(Clifton,%20N.J.)&title=Studying%20Antibody%20Repertoires%20with%20Next-Generation%20Sequencing&author=WD%20Lees&author=AJ%20Shepherd&volume=1526&publication_year=2017&pages=257-270&pmid=27896747&doi=10.1007/978-1-4939-6613-4_15&)]
* 39.Six A, Mariotti-Ferrandiz ME, Chaara W, Magadan S, Pham HP, Lefranc MP, Mora T, Thomas-Vaslin V, Walczak AM, and Boudinot P (2013) The past, present, and future of immune repertoire biology - the rise of next-generation repertoire analysis. Frontiers in immunology
  4, 413. [[DOI](https://doi.org/10.3389/fimmu.2013.00413)] [[PMC free article](/articles/PMC3841818/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24348479/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Frontiers%20in%20immunology&title=The%20past,%20present,%20and%20future%20of%20immune%20repertoire%20biology%20-%20the%20rise%20of%20next-generation%20repertoire%20analysis&author=A%20Six&author=ME%20Mariotti-Ferrandiz&author=W%20Chaara&author=S%20Magadan&author=HP%20Pham&volume=4&publication_year=2013&pages=413&pmid=24348479&doi=10.3389/fimmu.2013.00413&)]
* 40.Cole C, Volden R, Dharmadhikari S, Scelfo-Dalbey C, and Vollmers C (2016) Highly Accurate Sequencing of Full-Length Immune Repertoire Amplicons Using Tn5-Enabled and Molecular Identifier-Guided Amplicon Assembly. Journal of immunology (Baltimore, Md. : 1950)
  196, 2902–2907 [[DOI](https://doi.org/10.4049/jimmunol.1502563)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26856699/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20immunology%20(Baltimore,%20Md.%20:%201950)&title=Highly%20Accurate%20Sequencing%20of%20Full-Length%20Immune%20Repertoire%20Amplicons%20Using%20Tn5-Enabled%20and%20Molecular%20Identifier-Guided%20Amplicon%20Assembly&author=C%20Cole&author=R%20Volden&author=S%20Dharmadhikari&author=C%20Scelfo-Dalbey&author=C%20Vollmers&volume=196&publication_year=2016&pages=2902-2907&pmid=26856699&doi=10.4049/jimmunol.1502563&)]
* 41.Robinson WH (2015) Sequencing the functional antibody repertoire--diagnostic and therapeutic discovery. Nature reviews. Rheumatology
  11, 171–182 [[DOI](https://doi.org/10.1038/nrrheum.2014.220)] [[PMC free article](/articles/PMC4382308/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25536486/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20reviews.%20Rheumatology&title=Sequencing%20the%20functional%20antibody%20repertoire--diagnostic%20and%20therapeutic%20discovery&author=WH%20Robinson&volume=11&publication_year=2015&pages=171-182&pmid=25536486&doi=10.1038/nrrheum.2014.220&)]
* 42.Shlemov A, Bankevich S, Bzikadze A, Turchaninova MA, Safonova Y, and Pevzner PA (2017) Reconstructing Antibody Repertoires from Error-Prone Immunosequencing Reads. Journal of immunology (Baltimore, Md. : 1950)  [[DOI](https://doi.org/10.4049/jimmunol.1700485)] [[PMC free article](/articles/PMC5661950/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28978691/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20immunology%20(Baltimore,%20Md.%20:%201950)&title=Reconstructing%20Antibody%20Repertoires%20from%20Error-Prone%20Immunosequencing%20Reads&author=A%20Shlemov&author=S%20Bankevich&author=A%20Bzikadze&author=MA%20Turchaninova&author=Y%20Safonova&publication_year=2017&pmid=28978691&doi=10.4049/jimmunol.1700485&)]
* 43.Hansen KD, Brenner SE, and Dudoit S (2010) Biases in Illumina transcriptome sequencing caused by random hexamer priming. Nucleic acids research
  38, e131. [[DOI](https://doi.org/10.1093/nar/gkq224)] [[PMC free article](/articles/PMC2896536/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20395217/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20acids%20research&title=Biases%20in%20Illumina%20transcriptome%20sequencing%20caused%20by%20random%20hexamer%20priming&author=KD%20Hansen&author=SE%20Brenner&author=S%20Dudoit&volume=38&publication_year=2010&pages=e131&pmid=20395217&doi=10.1093/nar/gkq224&)]
* 44.van Gurp TP, McIntyre LM, and Verhoeven KJ (2013) Consistent errors in first strand cDNA due to random hexamer mispriming. PloS one
  8, e85583. [[DOI](https://doi.org/10.1371/journal.pone.0085583)] [[PMC free article](/articles/PMC3875578/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24386481/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PloS%20one&title=Consistent%20errors%20in%20first%20strand%20cDNA%20due%20to%20random%20hexamer%20mispriming&author=TP%20van%20Gurp&author=LM%20McIntyre&author=KJ%20Verhoeven&volume=8&publication_year=2013&pages=e85583&pmid=24386481&doi=10.1371/journal.pone.0085583&)]
* 45.Weber CF, and Kuske CR (2012) Comparative assessment of fungal cellobiohydrolase I richness and composition in cDNA generated using oligo(dT) primers or random hexamers. Journal of microbiological methods
  88, 224–228 [[DOI](https://doi.org/10.1016/j.mimet.2011.11.016)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22178429/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20microbiological%20methods&title=Comparative%20assessment%20of%20fungal%20cellobiohydrolase%20I%20richness%20and%20composition%20in%20cDNA%20generated%20using%20oligo(dT)%20primers%20or%20random%20hexamers&author=CF%20Weber&author=CR%20Kuske&volume=88&publication_year=2012&pages=224-228&pmid=22178429&doi=10.1016/j.mimet.2011.11.016&)]
* 46.Zheng W, Chung LM, and Zhao H (2011) Bias detection and correction in RNA-Sequencing data. BMC bioinformatics
  12, 290. [[DOI](https://doi.org/10.1186/1471-2105-12-290)] [[PMC free article](/articles/PMC3149584/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21771300/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20bioinformatics&title=Bias%20detection%20and%20correction%20in%20RNA-Sequencing%20data&author=W%20Zheng&author=LM%20Chung&author=H%20Zhao&volume=12&publication_year=2011&pages=290&pmid=21771300&doi=10.1186/1471-2105-12-290&)]
* 47.Lou Z, Casali P, and Xu Z (2015) Regulation of B Cell Differentiation by Intracellular Membrane-Associated Proteins and microRNAs: Role in the Antibody Response. Frontiers in immunology
  6 [[DOI](https://doi.org/10.3389/fimmu.2015.00537)] [[PMC free article](/articles/PMC4620719/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26579118/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Frontiers%20in%20immunology&title=Regulation%20of%20B%20Cell%20Differentiation%20by%20Intracellular%20Membrane-Associated%20Proteins%20and%20microRNAs:%20Role%20in%20the%20Antibody%20Response&author=Z%20Lou&author=P%20Casali&author=Z%20Xu&volume=6&publication_year=2015&pmid=26579118&doi=10.3389/fimmu.2015.00537&)]
* 48.Zhang Q, Bernatoniene J, Bagrade L, Paton JC, Mitchell TJ, Hammerschmidt S, Nunez DA, and Finn A (2006) Regulation of Production of Mucosal Antibody to Pneumococcal Protein Antigens by T-Cell-Derived Gamma Interferon and Interleukin-10 in Children. Infection and Immunity
  74, 4735–4743 [[DOI](https://doi.org/10.1128/IAI.00165-06)] [[PMC free article](/articles/PMC1539627/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16861661/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Infection%20and%20Immunity&title=Regulation%20of%20Production%20of%20Mucosal%20Antibody%20to%20Pneumococcal%20Protein%20Antigens%20by%20T-Cell-Derived%20Gamma%20Interferon%20and%20Interleukin-10%20in%20Children&author=Q%20Zhang&author=J%20Bernatoniene&author=L%20Bagrade&author=JC%20Paton&author=TJ%20Mitchell&volume=74&publication_year=2006&pages=4735-4743&pmid=16861661&doi=10.1128/IAI.00165-06&)]
* 49.Shugay M, Britanova OV, Merzlyak EM, Turchaninova MA, Mamedov IZ, Tuganbaev TR, Bolotin DA, Staroverov DB, Putintseva EV, Plevova K, Linnemann C, Shagin D, Pospisilova S, Lukyanov S, Schumacher TN, and Chudakov DM (2014) Towards error-free profiling of immune repertoires. Nature methods
  11, 653–655 [[DOI](https://doi.org/10.1038/nmeth.2960)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24793455/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20methods&title=Towards%20error-free%20profiling%20of%20immune%20repertoires&author=M%20Shugay&author=OV%20Britanova&author=EM%20Merzlyak&author=MA%20Turchaninova&author=IZ%20Mamedov&volume=11&publication_year=2014&pages=653-655&pmid=24793455&doi=10.1038/nmeth.2960&)]
* 50.Allman D, Lindsley RC, DeMuth W, Rudd K, Shinton SA, and Hardy RR (2001) Resolution of three nonproliferative immature splenic B cell subsets reveals multiple selection points during peripheral B cell maturation. Journal of immunology (Baltimore, Md. : 1950)
  167, 6834–6840 [[DOI](https://doi.org/10.4049/jimmunol.167.12.6834)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11739500/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20immunology%20(Baltimore,%20Md.%20:%201950)&title=Resolution%20of%20three%20nonproliferative%20immature%20splenic%20B%20cell%20subsets%20reveals%20multiple%20selection%20points%20during%20peripheral%20B%20cell%20maturation&author=D%20Allman&author=RC%20Lindsley&author=W%20DeMuth&author=K%20Rudd&author=SA%20Shinton&volume=167&publication_year=2001&pages=6834-6840&pmid=11739500&doi=10.4049/jimmunol.167.12.6834&)]
* 51.Allman DM, Ferguson SE, Lentz VM, and Cancro MP (1993) Peripheral B cell maturation. II. Heat-stable antigen(hi) splenic B cells are an immature developmental intermediate in the production of long-lived marrow-derived B cells. Journal of immunology (Baltimore, Md. : 1950)
  151, 4431–4444 [[PubMed](https://pubmed.ncbi.nlm.nih.gov/8409411/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20immunology%20(Baltimore,%20Md.%20:%201950)&title=Peripheral%20B%20cell%20maturation.%20II.%20Heat-stable%20antigen(hi)%20splenic%20B%20cells%20are%20an%20immature%20developmental%20intermediate%20in%20the%20production%20of%20long-lived%20marrow-derived%20B%20cells&author=DM%20Allman&author=SE%20Ferguson&author=VM%20Lentz&author=MP%20Cancro&volume=151&pages=4431-4444&pmid=8409411&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

Supp FigS1

[NIHMS987236-supplement-Supp\_FigS1.pdf](/articles/instance/6366624/bin/NIHMS987236-supplement-Supp_FigS1.pdf) (365.2KB, pdf)