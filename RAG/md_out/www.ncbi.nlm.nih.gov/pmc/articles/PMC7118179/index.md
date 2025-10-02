Microbiol Resour Announc

. 2020 Apr 2;9(14):e00003-20. doi: [10.1128/MRA.00003-20](https://doi.org/10.1128/MRA.00003-20)

# Identification of Metagenome-Assembled Genomes Containing Antimicrobial Resistance Genes, Isolated from an Advanced Water Treatment Facility

[Blake W Stamps](https://pubmed.ncbi.nlm.nih.gov/?term=%22Stamps%20BW%22%5BAuthor%5D)

### Blake W Stamps

aDepartment of Civil and Environmental Engineering, Colorado School of Mines, Golden, Colorado, USA

Find articles by [Blake W Stamps](https://pubmed.ncbi.nlm.nih.gov/?term=%22Stamps%20BW%22%5BAuthor%5D)

a, [John R Spear](https://pubmed.ncbi.nlm.nih.gov/?term=%22Spear%20JR%22%5BAuthor%5D)

### John R Spear

aDepartment of Civil and Environmental Engineering, Colorado School of Mines, Golden, Colorado, USA

Find articles by [John R Spear](https://pubmed.ncbi.nlm.nih.gov/?term=%22Spear%20JR%22%5BAuthor%5D)

a,✉

Editor: Frank J Stewartb

* Author information
* Article notes
* Copyright and License information

aDepartment of Civil and Environmental Engineering, Colorado School of Mines, Golden, Colorado, USA

bGeorgia Institute of Technology

✉

Address correspondence to John R. Spear, jspear@mines.edu.

**Citation** Stamps BW, Spear JR. 2020. Identification of metagenome-assembled genomes containing antimicrobial resistance genes, isolated from an advanced water treatment facility. Microbiol Resour Announc 9:e00003-20. <https://doi.org/10.1128/MRA.00003-20>.

✉

Corresponding author.

#### Roles

**Frank J Stewart**: Editor

Received 2020 Jan 3; Accepted 2020 Mar 9; Collection date 2020 Apr.

Copyright © 2020 Stamps and Spear.

This is an open-access article distributed under the terms of the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).

[PMC Copyright notice](/about/copyright/)

PMCID: PMC7118179  PMID: [32241853](https://pubmed.ncbi.nlm.nih.gov/32241853/)

---

Here, we present 95 metagenome-assembled genomes (MAGs) that harbor antimicrobial resistance genes, isolated from samples obtained in a large advanced wastewater reclamation facility prior to microfiltration. The MAGs were not in abundance after filtration at the facility and represent a useful resource to the water treatment community at large.

## ABSTRACT

Here, we present 95 metagenome-assembled genomes (MAGs) that harbor antimicrobial resistance genes, isolated from samples obtained in a large advanced wastewater reclamation facility prior to microfiltration. The MAGs were not in abundance after filtration at the facility and represent a useful resource to the water treatment community at large.

## ANNOUNCEMENT

Human society faces an acceleration of water scarcity due to increasing population, pollution, and land use. Such water scarcity also brings a decrease in water quality, as demonstrated by increased eutrophication, among other concerns ([1](#B1)). Treatment and reuse of water are critical tools in combating water stress globally. Reuse of wastewater carries the potential risk of transmission of small-molecule metabolites and antibiotic resistance genes (ARGs) ([2](#B2)), while its use relieves stress on natural sources of water. Previously, biofilms were sampled from the Orange County Water District (OCWD) Advanced Water Purification Facility (AWPF) in Southern California, which showed differences in the microbial communities in both influent and biofilms on microfiltration and reverse osmosis membranes ([3](#B3)). In a recent study that more fully characterized both biofilms and large volumes of water throughout the treatment process, we described both microbial diversity and load decreasing across this well-engineered system ([4](#B4)). Here, we have expanded and enhanced this previous work ([4](#B4)) by identifying metagenome-assembled genomes (MAGs) that contain ARGs to expand our knowledge of all microbial lineages harboring ARGs that are present within an ultrapurified water facility.

Water and biofilm were sampled at the OCWD AWPF as previously described ([4](#B4)). Briefly, all water samples were filtered using a large-volume concentrator (LVC) dialysis filter cartridge system (Innova Prep LLC, Drexel, MO). Approximately 60 to 100 liters of water were filtered per sample, prior to concentration onto replicate 25-mm (diameter), 0.22-μm (pore size) nitrocellulose filters. Filters were placed in BashingBead lysis tubes (Zymo, Inc., Irvine, CA) containing 750 μl of DNA/RNA Shield (Zymo, Inc.) to preserve samples onsite. Biofilm samples were similarly placed in lysis tubes with DNA/RNA Shield. DNA was extracted using the Zymo Microbiomics DNA/RNA coextraction kit (Zymo, Inc.). Libraries were prepared as previously described in full ([4](#B4)) using the Nextera XT library prep kit (Illumina, San Diego, CA), modified to use 13 cycles of PCR. All samples were sequenced on an Illumina HiSeq 3000 instrument using PE150 chemistry. Two biofilm samples from filtration units at the AWPF obtained from Leddy et al. ([3](#B3)) were processed as described previously and sequenced using SE100 chemistry. Sequence reads were error corrected using BayesHammer v3.12.0 ([5](#B5)) and assembled using MEGAHIT v1.1.3 ([6](#B6)) to produce a single coassembly. Reads were mapped to the assembly with Bowtie 2 v2.3.4.1 ([7](#B7)) and binned into MAGs using Anvi’o v v5 and CONCOCT ([8](#B8), [9](#B9)). MAG completion and redundancy estimates were also computed within Anvi’o. MAGs were queried for ARGs using DeepARG ([10](#B10)) and identified phylogenetically by GTDB-Tk v0.3.0 ([11](#B11)). Default parameters were used for all software unless otherwise noted.

A total of 95 MAGs were selected after manual curation within Anvi’o and by DeepARG that contained 185 open reading frames putatively identified as antimicrobial resistance genes. Of note, two MAGs were identified by GTDB-Tk as belonging to the “*Candidatus* Gracilibacteria” and “*Candidatus* Patescibacteria” lineages ([12](#B12)). Others identified included an unclassified *Dongiaceae* MAG that was previously associated with a wastewater treatment facility ([13](#B13)). A more detailed list of assembly statistics and taxonomy of all MAGs can be found in [Table 1](#tab1). As reported previously, no metagenomic sequence and therefore no MAGs were identified after barrier filtration within the system due to a lack of sufficient extractable or amplifiable DNA ([4](#B4)). Future work will further describe the ARGs and will identify non-ARG-containing MAGs and determine how they impact the operation of the OCWD AWPF.

### TABLE 1.

Detailed taxonomy, accession information, and assembly statistics of MAGs

| Bin name | Taxonomy[*a*](#ngtab1.1) | GenBank assembly accession no. | Total length (bp) | *N*50 (bp) | GC content (%) | Completeness (%) | Redundancy (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bin\_1\_1 | *Mycobacterium* sp. AWPF1 | [SSGB00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGB00000000) | 2,707,225 | 10,968 | 68.44 | 38.85 | 0.72 |
| Bin\_1\_3 | *Mycobacterium* sp. AWPF2 | [SSGA00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGA00000000) | 4,217,119 | 13,813 | 68.81 | 60.43 | 3.6 |
| Bin\_1\_5 | Unclassified *Actinobacteria* family [UBA10799](https://www.ncbi.nlm.nih.gov/protein/UBA10799) bacterium AWPF1 | [SSET00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSET00000000) | 3,552,223 | 35,771 | 69.31 | 84.17 | 8.63 |
| Bin\_1\_8 | Unclassified *Actinobacteria* family [UBA10799](https://www.ncbi.nlm.nih.gov/protein/UBA10799) bacterium AWPF2 | [SSES00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSES00000000) | 1,125,909 | 10,906 | 67.03 | 22.3 | 9.35 |
| Bin\_10\_1 | *Polynucleobacter* sp. | [SSFP00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFP00000000) | 1,928,064 | 15,906 | 42.88 | 78.42 | 7.19 |
| Bin\_11\_1 | *Tolumonas* sp. | [SSEX00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEX00000000) | 1,832,732 | 10,968 | 47.81 | 53.24 | 2.88 |
| Bin\_11\_4 | Unclassified *Cyclobacteriaceae* bacterium | [SSEN00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEN00000000) | 2,496,402 | 8,305 | 45.51 | 36.69 | 9.35 |
| Bin\_11\_5 | *Cyclobacteriaceae* ELB16-189 sp. | [VIGN00000000](https://www.ncbi.nlm.nih.gov/nuccore/VIGN00000000) | 1,066,491 | 8,282 | 43.86 | 36.69 | 12.23 |
| Bin\_12\_3 | Unclassified *Hyphomicrobiaceae* bacterium | [SSEH00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEH00000000) | 2,999,406 | 8,617 | 55.82 | 7.19 | 12.23 |
| Bin\_14\_1 | *Novosphingobium* sp. | [SSFU00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFU00000000) | 1,517,683 | 8,392 | 64.2 | 29.5 | 0.72 |
| Bin\_14\_3 | Unclassified *Gammaproteobacteria* bacterium AWPF1 | [SSEJ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEJ00000000) | 2,472,121 | 8,119 | 63.57 | 51.08 | 14.39 |
| Bin\_14\_4 | *Pseudoxanthomonas* sp. | [SSFJ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFJ00000000) | 1,848,156 | 8,064 | 67.96 | 34.53 | 0 |
| Bin\_14\_5 | Unclassified *Gammaproteobacteria* bacterium AWPF2 | [SSEI00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEI00000000) | 1,859,286 | 10,791 | 62.7 | 43.17 | 41.73 |
| Bin\_15\_1 | *Nitrosomonas* sp. AWPF2 | [SSFW00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFW00000000) | 2,557,120 | 18,443 | 43.85 | 83.45 | 1.44 |
| Bin\_15\_2 | *Burkholderiaceae* UBA7693 sp. | [SSGW00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGW00000000) | 2,650,165 | 9,223 | 49.03 | 22.3 | 0.72 |
| Bin\_15\_3 | *Moranbacterales* UBA1568 sp. | [SSGE00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGE00000000) | 580,840 | 8,401 | 50.03 | 48.2 | 2.88 |
| Bin\_15\_5 | Unclassified *Moranbacterales* UBA1568 sp. AWPF1 | [SSEE00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEE00000000) | 880,789 | 8,806 | 45.6 | 66.91 | 19.42 |
| Bin\_15\_6 | Unclassified *Moranbacterales* UBA1568 sp. AWPF2 | [SSED00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSED00000000) | 1,461,468 | 7,107 | 48.36 | 52.52 | 15.83 |
| Bin\_17\_3 | Unclassified *Rhodocyclaceae* bacterium AWPF3 | [SSDZ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDZ00000000) | 3,614,409 | 8,707 | 60.2 | 60.43 | 10.79 |
| Bin\_19\_1 | *Ottowia* sp. AWPF1 | [SSFT00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFT00000000) | 2,464,482 | 7,364 | 68.69 | 17.27 | 2.16 |
| Bin\_19\_2 | *Ottowia* sp. AWPF2 | [SSFS00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFS00000000) | 2,330,319 | 8,499 | 69.66 | 42.45 | 6.47 |
| Bin\_19\_5 | *Thermomonas* sp. | [SSFC00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFC00000000) | 1,187,954 | 11,860 | 67.14 | 38.13 | 0.72 |
| Bin\_2\_1 | Unclassified *Thermomicrobiales* family UBA6265 bacterium | [SSDT00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDT00000000) | 2,680,321 | 10,114 | 60.7 | 49.64 | 7.91 |
| Bin\_20\_1 | *Niabella* sp. | [SSFZ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFZ00000000) | 1,214,478 | 6,588 | 38.77 | 33.81 | 7.91 |
| Bin\_21\_1 | *Zoogloea* sp. | [SSDR00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDR00000000) | 2,929,105 | 10,734 | 64.98 | 55.4 | 1.44 |
| Bin\_21\_3 | *Limnohabitans* sp. AWPF1 | [SSGJ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGJ00000000) | 1,670,846 | 9,983 | 63.22 | 19.42 | 0.72 |
| Bin\_23\_2 | *Flavobacterium* GCA\_002422095.1 | [SSGM00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGM00000000) | 1,906,623 | 10,479 | 32.59 | 66.19 | 9.35 |
| Bin\_23\_3 | *Flavobacterium* sp. | [SSGL00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGL00000000) | 2,075,117 | 12,249 | 32.14 | 33.09 | 2.88 |
| Bin\_24\_1 | *Rhodoferax* sp. | [SSFF00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFF00000000) | 3,654,053 | 136,395 | 62.3 | 99.28 | 7.19 |
| Bin\_24\_2 | *Limnohabitans* sp. AWPF2 | [SSGI00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGI00000000) | 2,967,058 | 22,882 | 63.25 | 73.38 | 5.04 |
| Bin\_24\_4 | *Pseudorhodobacter* sp. | [SSFK00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFK00000000) | 3,302,298 | 8,369 | 63.29 | 49.64 | 10.79 |
| Bin\_25\_1 | Unclassified *Rhodocyclaceae* bacterium AWPF1 | [SSDY00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDY00000000) | 2,178,082 | 10,805 | 64.25 | 62.59 | 2.16 |
| Bin\_25\_2 | *Flavobacteriales* PHOS-HE28 sp. | [SSGN00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGN00000000) | 4,081,487 | 21,145 | 62.07 | 76.98 | 7.91 |
| Bin\_25\_4 | *Dechloromonas* sp. | [SSGP00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGP00000000) | 3,029,215 | 19,114 | 62.22 | 58.99 | 5.76 |
| Bin\_26\_1 | Unclassified *Sphingomonadales* bacterium | [SSDV00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDV00000000) | 3,053,326 | 60,967 | 64.22 | 99.28 | 0.72 |
| Bin\_26\_2 | *Mycobacterium mageritense* | [SSGC00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGC00000000) | 7,650,754 | 60,194 | 66.88 | 79.14 | 5.76 |
| Bin\_26\_3 | Unclassified *Dongiaceae* bacterium | [SSEL00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEL00000000) | 5,719,975 | 142,361 | 61.3 | 99.28 | 5.04 |
| Bin\_27\_1 | *Thauera aminoaromatica* | [SSFD00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFD00000000) | 5,236,562 | 14,873 | 67.89 | 73.38 | 8.63 |
| Bin\_27\_2 | Unclassified *Burkholderiaceae* bacterium | [SSER00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSER00000000) | 3,032,333 | 8,502 | 67.32 | 22.3 | 0.72 |
| Bin\_29\_1 | Unclassified *Mycobacterium* bacterium | [SSEC00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEC00000000) | 6,629,733 | 18,228 | 66.91 | 85.61 | 7.91 |
| Bin\_29\_2 | *Mycobacterium arupense* | [SSGD00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGD00000000) | 5,009,268 | 45,297 | 66.94 | 99.28 | 7.19 |
| Bin\_3\_3 | *Chryseobacterium cucumeris* | [SSGV00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGV00000000) | 2,503,246 | 11,245 | 36.61 | 22.3 | 0 |
| Bin\_3\_4 | Unclassified *Chitinophagaceae* bacterium | [SSEO00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEO00000000) | 1,501,328 | 17,275 | 33.51 | 50.36 | 0.72 |
| Bin\_3\_8 | Unclassified *Bacteroidia* bacterium | [SSEU00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEU00000000) | 2,309,706 | 6,910 | 35.54 | 57.55 | 19.42 |
| Bin\_30 | Unclassified *Burkholderiaceae* bacterium AWPF1 | [SSEQ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEQ00000000) | 6,171,595 | 8,294 | 70.29 | 47.48 | 4.32 |
| Bin\_31\_2 | *Aeromicrobium* sp. | [SSHC00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSHC00000000) | 1,861,791 | 18,902 | 58.23 | 82.73 | 1.44 |
| Bin\_34 | Unclassified *Desulfurella* bacterium | [SSEM00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEM00000000) | 6,288,683 | 10,284 | 58.83 | 3.6 | 5.04 |
| Bin\_35\_1 | *Pseudomonas monteilii* | [SSFN00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFN00000000) | 5,048,709 | 26,274 | 63.26 | 51.8 | 2.16 |
| Bin\_35\_2 | *Thiobacillus* GCA\_002343685.1 | [SSFB00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFB00000000) | 3,564,805 | 105,954 | 62.36 | 86.33 | 5.76 |
| Bin\_35\_3 | Unclassified *Nevskiaceae* bacterium AWPF1 | [SSEB00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEB00000000) | 3,246,569 | 241,139 | 65.99 | 86.33 | 2.16 |
| Bin\_36\_2 | *Crocinitomicaceae* UBA5422 sp. AWPF1 | [SSGS00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGS00000000) | 1,134,521 | 8,082 | 36.56 | 17.27 | 0 |
| Bin\_38\_1 | *Nitrosomonas* sp. AWPF1 | [SSFV00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFV00000000) | 2,613,687 | 22,274 | 44.56 | 57.55 | 0 |
| Bin\_39\_1 | *Pelomonas* sp. | [SSFQ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFQ00000000) | 3,131,775 | 9,407 | 69.9 | 30.22 | 2.16 |
| Bin\_4\_1 | *Cupriavidus* sp. | [SSGQ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGQ00000000) | 3,464,703 | 7,277 | 64.08 | 16.55 | 2.88 |
| Bin\_4\_3 | *Rhizobium* sp. AWPF1 | [SSFH00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFH00000000) | 4,147,977 | 10,631 | 61.05 | 18.71 | 1.44 |
| Bin\_42\_2 | *Methylophilus methylotrophus* | [SSGG00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGG00000000) | 1,188,656 | 14,601 | 49.11 | 28.06 | 2.88 |
| Bin\_43\_1 | *Chryseobacterium* sp. | [SSGU00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGU00000000) | 2,092,908 | 10,855 | 38.01 | 44.6 | 7.91 |
| Bin\_43\_5 | *Crocinitomicaceae* UBA5422 sp. AWPF2 | [SSGR00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGR00000000) | 641,979 | 9,434 | 42.11 | 35.25 | 17.27 |
| Bin\_44\_1 | *Betaproteobacteriales* [UBA11063](https://www.ncbi.nlm.nih.gov/protein/UBA11063) sp. AWPF1 | [SSGY00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGY00000000) | 2,803,113 | 14,546 | 36.96 | 86.33 | 2.16 |
| Bin\_45\_1 | *Betaproteobacteriales* [UBA11063](https://www.ncbi.nlm.nih.gov/protein/UBA11063) sp. AWPF2 | [SSGX00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGX00000000) | 2,467,391 | 70,519 | 35.22 | 79.14 | 1.44 |
| Bin\_45\_4 | “*Candidatus* Gracilibacteria” UBA5532 sp. | [SSGK00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGK00000000) | 668,037 | 10,255 | 37.87 | 58.27 | 0.72 |
| Bin\_48\_1 | *Afipia* sp. | [SSHB00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSHB00000000) | 3,379,245 | 12,763 | 61.87 | 54.68 | 2.88 |
| Bin\_48\_2 | *Rhizobium* sp. AWPF2 | [SSFG00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFG00000000) | 2,353,640 | 12,778 | 60.82 | 38.13 | 0.72 |
| Bin\_5\_1 | *Lysobacter* sp. | [SSGH00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGH00000000) | 4,387,597 | 162,300 | 65.61 | 94.24 | 5.76 |
| Bin\_5\_5 | Unclassified *Xanthomonadaceae* bacterium | [SSEV00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEV00000000) | 3,535,438 | 16,226 | 63.31 | 47.48 | 0.72 |
| Bin\_5\_7 | Unclassified *Rhodocyclaceae* bacterium AWPF2 | [SSDX00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDX00000000) | 1,708,980 | 12,103 | 65.16 | 33.09 | 0.72 |
| Bin\_51\_4 | Unclassified *Saccharimonadales* UBA4665 | [SSDW00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDW00000000) | 818,540 | 13,215 | 50.23 | 61.87 | 8.63 |
| Bin\_52\_1 | *Pseudomonas alcaligenes* | [SSFO00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFO00000000) | 3,682,067 | 12,539 | 64.72 | 71.22 | 3.6 |
| Bin\_52\_2 | *Pseudomonas* sp. AWPF1 | [SSFM00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFM00000000) | 1,540,019 | 11,651 | 61.81 | 17.27 | 4.32 |
| Bin\_54\_1 | *Nitrosomonas oligotropha* | [SSFX00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFX00000000) | 2,754,397 | 36,184 | 49.22 | 67.63 | 0.72 |
| Bin\_54\_3 | *Nitrosomonas* GCA\_002083595.1 | [SSFY00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFY00000000) | 2,292,023 | 8,445 | 48.32 | 29.5 | 6.47 |
| Bin\_55\_1 | 46-32 GCA 001898405.1 | [SSHF00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSHF00000000) | 5,043,020 | 214,644 | 44.27 | 94.96 | 0 |
| Bin\_55\_2 | *Methylophilus* sp. | [SSGF00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGF00000000) | 2,747,675 | 94,685 | 50.49 | 66.91 | 2.16 |
| Bin\_56\_1 | *Thiothrix* sp. | [SSFA00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFA00000000) | 4,155,808 | 145,664 | 44.77 | 69.78 | 3.6 |
| Bin\_56\_2 | *Pedobacter* sp. | [SSFR00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFR00000000) | 2,341,987 | 206,071 | 38.94 | 98.56 | 0.72 |
| Bin\_57\_1 | *Rheinheimera* sp. | [SSFI00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFI00000000) | 3,863,184 | 45,966 | 52.26 | 63.31 | 2.88 |
| Bin\_57\_2 | UBA7239 sp. | [SSEW00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEW00000000) | 1,251,491 | 7,537 | 52.91 | 38.13 | 9.35 |
| Bin\_59\_2 | Unclassified *Nevskiaceae* bacterium AWPF2 | [SSEA00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEA00000000) | 2,177,696 | 27,134 | 59.28 | 27.34 | 5.04 |
| Bin\_63\_2 | Unclassified WS6 bacterium | [SSDS00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDS00000000) | 1,242,531 | 11,680 | 44.02 | 34.53 | 9.35 |
| Bin\_64\_3 | *Romboutsia* sp. | [SSFE00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFE00000000) | 381,413 | 7,806 | 27.61 | 45.32 | 0 |
| Bin\_65 | *Crocinitomicaceae* 40-80 sp. | [SSGT00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGT00000000) | 2,395,197 | 12,217 | 40.24 | 70.5 | 2.16 |
| Bin\_67 | Unclassified *Spirochaetes* class [UBA12135](https://www.ncbi.nlm.nih.gov/protein/UBA12135) bacterium | [SSDU00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSDU00000000) | 1,932,890 | 10,511 | 31.46 | 5.04 | 0 |
| Bin\_68\_2 | Unclassified *Moranbacterales* class UBA1568 bacterium | [SSEF00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEF00000000) | 1,023,203 | 34,589 | 53.99 | 79.14 | 5.76 |
| Bin\_7\_2 | Unclassified *Burkholderiaceae* bacterium AWPF2 | [SSEP00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEP00000000) | 2,384,147 | 7,064 | 63.49 | 12.95 | 0.72 |
| Bin\_7\_3 | *Alicycliphilus* sp. | [SSHA00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSHA00000000) | 3,015,590 | 10,496 | 66.2 | 43.17 | 5.76 |
| Bin\_7\_4 | *Aquabacterium* sp. AWPF1 | [SSGZ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGZ00000000) | 1,352,035 | 7,819 | 65.11 | 21.58 | 0 |
| Bin\_7\_5 | *Pseudomonas* sp. AWPF2 | [SSFL00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSFL00000000) | 1,978,447 | 9,650 | 63.83 | 51.08 | 10.79 |
| Bin\_7\_6 | *Aquabacterium* sp. AWPF2 | [VKOJ00000000](https://www.ncbi.nlm.nih.gov/nuccore/VKOJ00000000) | 2,228,505 | 10,843 | 63.58 | 33.81 | 2.16 |
| Bin\_71 | Unclassified *Leptospira* bacterium | [SSEG00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEG00000000) | 1,795,065 | 38,625 | 54.29 | 6.17 | 0 |
| Bin\_8\_1 | *Acinetobacter* sp. AWPF1 | [SSHE00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSHE00000000) | 2,045,996 | 23,569 | 41.75 | 75.54 | 2.16 |
| Bin\_8\_2 | *Thiothrix* sp. AWPF1 | [SSEZ00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEZ00000000) | 1,300,697 | 7,394 | 44.99 | 30.22 | 1.44 |
| Bin\_8\_3 | *Thiothrix* sp. AWPF2 | [SSEY00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEY00000000) | 2,137,450 | 7,937 | 45.31 | 47.48 | 16.55 |
| Bin\_8\_5 | *Acinetobacter* sp. AWPF2 | [SSHD00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSHD00000000) | 1,422,583 | 9,315 | 42.74 | 74.1 | 7.19 |
| Bin\_9\_3 | Unclassified *Elusimicrobia* order F11 bacterium | [SSEK00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSEK00000000) | 2,256,510 | 6,750 | 63.91 | 51.8 | 10.79 |
| Bin\_9\_4 | *Dokdonella* sp. | [SSGO00000000](https://www.ncbi.nlm.nih.gov/nuccore/SSGO00000000) | 1,632,646 | 10,049 | 62.2 | 31.65 | 2.16 |

[Open in a new tab](table/tab1/)

a

Taxonomy given was identified using GTDB-tk and is the taxonomy reported within the NCBI accession record.

### Data availability.

Raw sequence reads are available under BioProject accession number [PRJNA428383](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA428383). Whole-genome sequences are available under the sequential BioSample accession numbers [SAMN10026417](https://www.ncbi.nlm.nih.gov/biosample/SAMN10026417) to [SAMN10026511](https://www.ncbi.nlm.nih.gov/biosample/SAMN10026511), which include annotations produced with the Prokaryotic Gene Annotation Pipeline (PGAP). [Table 1](#tab1) contains individual Web links to each bin assembly and annotation.

## ACKNOWLEDGMENTS

Research reported in this publication was supported by a grant to J.R.S. from the Bureau of Reclamation. We thank the Alfred P. Sloan Foundation for a postdoctoral fellowship to B.W.S.

We acknowledge the sequencing services provided by Cosmos ID, Inc., and Nur A. Hasan, and we thank the Orange County Water District, Megan H. Plumlee (OCWD), and Menu B. Leddy for their previous critical support of the project.

## REFERENCES

* 1.Moss B.
  2011.
  Allied attack: climate change and eutrophication. Inland Waters
  1:101–105. doi: 10.5268/IW-1.2.359. [[DOI](https://doi.org/10.5268/IW-1.2.359)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inland%20Waters&title=Allied%20attack:%20climate%20change%20and%20eutrophication&author=B%20Moss&volume=1&publication_year=2011&pages=101-105&doi=10.5268/IW-1.2.359&)]
* 2.Garner E, Chen C, Xia K, Bowers J, Engelthaler DM, McLain J, Edwards MA, Pruden A.
  2018.
  Metagenomic characterization of antibiotic resistance genes in full-scale reclaimed water distribution systems and corresponding potable systems. Environ Sci Technol
  52:6113–6125. doi: 10.1021/acs.est.7b05419. [[DOI](https://doi.org/10.1021/acs.est.7b05419)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29741366/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Environ%20Sci%20Technol&title=Metagenomic%20characterization%20of%20antibiotic%20resistance%20genes%20in%20full-scale%20reclaimed%20water%20distribution%20systems%20and%20corresponding%20potable%20systems&author=E%20Garner&author=C%20Chen&author=K%20Xia&author=J%20Bowers&author=DM%20Engelthaler&volume=52&publication_year=2018&pages=6113-6125&pmid=29741366&doi=10.1021/acs.est.7b05419&)]
* 3.Leddy MB, Hasan NA, Subramanian P, Heberling C, Cotruvo J, Colwell RR.
  2017.
  Characterization of microbial signatures from advanced treated wastewater biofilms. J Am Water Works Assoc
  109:E503–E512. doi: 10.5942/jawwa.2017.109.0116. [[DOI](https://doi.org/10.5942/jawwa.2017.109.0116)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Am%20Water%20Works%20Assoc&title=Characterization%20of%20microbial%20signatures%20from%20advanced%20treated%20wastewater%20biofilms&author=MB%20Leddy&author=NA%20Hasan&author=P%20Subramanian&author=C%20Heberling&author=J%20Cotruvo&volume=109&publication_year=2017&pages=E503-E512&doi=10.5942/jawwa.2017.109.0116&)]
* 4.Stamps BW, Leddy MB, Plumlee MH, Hasan NA, Colwell RR, Spear JR.
  2018.
  Characterization of the microbiome at the world’s largest potable water reuse facility. Front Microbiol
  9:2435. doi: 10.3389/fmicb.2018.02435. [[DOI](https://doi.org/10.3389/fmicb.2018.02435)] [[PMC free article](/articles/PMC6212505/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30416489/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front%20Microbiol&title=Characterization%20of%20the%20microbiome%20at%20the%20world%E2%80%99s%20largest%20potable%20water%20reuse%20facility&author=BW%20Stamps&author=MB%20Leddy&author=MH%20Plumlee&author=NA%20Hasan&author=RR%20Colwell&volume=9&publication_year=2018&pages=2435&pmid=30416489&doi=10.3389/fmicb.2018.02435&)]
* 5.Bankevich A, Nurk S, Antipov D, Gurevich AA, Dvorkin M, Kulikov AS, Lesin VM, Nikolenko SI, Pham S, Prjibelski AD, Pyshkin AV, Sirotkin AV, Vyahhi N, Tesler G, Alekseyev MA, Pevzner PA.
  2012.
  SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing. J Comput Biol
  19:455–477. doi: 10.1089/cmb.2012.0021. [[DOI](https://doi.org/10.1089/cmb.2012.0021)] [[PMC free article](/articles/PMC3342519/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22506599/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J%20Comput%20Biol&title=SPAdes:%20a%20new%20genome%20assembly%20algorithm%20and%20its%20applications%20to%20single-cell%20sequencing&author=A%20Bankevich&author=S%20Nurk&author=D%20Antipov&author=AA%20Gurevich&author=M%20Dvorkin&volume=19&publication_year=2012&pages=455-477&pmid=22506599&doi=10.1089/cmb.2012.0021&)]
* 6.Li D, Liu CM, Luo R, Sadakane K, Lam TW.
  2015.
  MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph. Bioinformatics
  31:1674–1676. doi: 10.1093/bioinformatics/btv033. [[DOI](https://doi.org/10.1093/bioinformatics/btv033)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25609793/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=MEGAHIT:%20an%20ultra-fast%20single-node%20solution%20for%20large%20and%20complex%20metagenomics%20assembly%20via%20succinct%20de%20Bruijn%20graph&author=D%20Li&author=CM%20Liu&author=R%20Luo&author=K%20Sadakane&author=TW%20Lam&volume=31&publication_year=2015&pages=1674-1676&pmid=25609793&doi=10.1093/bioinformatics/btv033&)]
* 7.Langmead B, Salzberg SL.
  2012.
  Fast gapped-read alignment with Bowtie 2. Nat Methods
  9:357–359. doi: 10.1038/nmeth.1923. [[DOI](https://doi.org/10.1038/nmeth.1923)] [[PMC free article](/articles/PMC3322381/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22388286/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat%20Methods&title=Fast%20gapped-read%20alignment%20with%20Bowtie%202&author=B%20Langmead&author=SL%20Salzberg&volume=9&publication_year=2012&pages=357-359&pmid=22388286&doi=10.1038/nmeth.1923&)]
* 8.Alneberg J, Bjarnason BS, de Bruijn I, Schirmer M, Quick J, Ijaz UZ, Lahti L, Loman NJ, Andersson AF, Quince C.
  2014.
  Binning metagenomic contigs by coverage and composition. Nat Methods
  11:1144–1146. doi: 10.1038/nmeth.3103. [[DOI](https://doi.org/10.1038/nmeth.3103)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25218180/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat%20Methods&title=Binning%20metagenomic%20contigs%20by%20coverage%20and%20composition&author=J%20Alneberg&author=BS%20Bjarnason&author=I%20de%20Bruijn&author=M%20Schirmer&author=J%20Quick&volume=11&publication_year=2014&pages=1144-1146&pmid=25218180&doi=10.1038/nmeth.3103&)]
* 9.Eren AM, Esen ÖC, Quince C, Vineis JH, Morrison HG, Sogin ML, Delmont TO.
  2015.
  Anvi’o: an advanced analysis and visualization platform for ‘omics data. PeerJ
  3:e1319. doi: 10.7717/peerj.1319. [[DOI](https://doi.org/10.7717/peerj.1319)] [[PMC free article](/articles/PMC4614810/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26500826/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PeerJ&title=Anvi%E2%80%99o:%20an%20advanced%20analysis%20and%20visualization%20platform%20for%20%E2%80%98omics%20data&author=AM%20Eren&author=%C3%96C%20Esen&author=C%20Quince&author=JH%20Vineis&author=HG%20Morrison&volume=3&publication_year=2015&pages=e1319&pmid=26500826&doi=10.7717/peerj.1319&)]
* 10.Arango-Argoty G, Garner E, Pruden A, Heath LS, Vikesland P, Zhang L.
  2018.
  DeepARG: a deep learning approach for predicting antibiotic resistance genes from metagenomic data. Microbiome
  6:23. doi: 10.1186/s40168-018-0401-z. [[DOI](https://doi.org/10.1186/s40168-018-0401-z)] [[PMC free article](/articles/PMC5796597/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29391044/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microbiome&title=DeepARG:%20a%20deep%20learning%20approach%20for%20predicting%20antibiotic%20resistance%20genes%20from%20metagenomic%20data&author=G%20Arango-Argoty&author=E%20Garner&author=A%20Pruden&author=LS%20Heath&author=P%20Vikesland&volume=6&publication_year=2018&pages=23&pmid=29391044&doi=10.1186/s40168-018-0401-z&)]
* 11.Parks DH, Chuvochina M, Waite DW, Rinke C, Skarshewski A, Chaumeil P-A, Hugenholtz P.
  2018.
  A standardized bacterial taxonomy based on genome phylogeny substantially revises the tree of life. Nat Biotechnol
  36:996–1004. doi: 10.1038/nbt.4229. [[DOI](https://doi.org/10.1038/nbt.4229)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30148503/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat%20Biotechnol&title=A%20standardized%20bacterial%20taxonomy%20based%20on%20genome%20phylogeny%20substantially%20revises%20the%20tree%20of%20life&author=DH%20Parks&author=M%20Chuvochina&author=DW%20Waite&author=C%20Rinke&author=A%20Skarshewski&volume=36&publication_year=2018&pages=996-1004&pmid=30148503&doi=10.1038/nbt.4229&)]
* 12.Rinke C, Schwientek P, Sczyrba A, Ivanova NN, Anderson IJ, Cheng J-F, Darling A, Malfatti S, Swan BK, Gies EA, Dodsworth JA, Hedlund BP, Tsiamis G, Sievert SM, Liu W-T, Eisen JA, Hallam SJ, Kyrpides NC, Stepanauskas R, Rubin EM, Hugenholtz P, Woyke T.
  2013.
  Insights into the phylogeny and coding potential of microbial dark matter. Nature
  499:431–437. doi: 10.1038/nature12352. [[DOI](https://doi.org/10.1038/nature12352)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23851394/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature&title=Insights%20into%20the%20phylogeny%20and%20coding%20potential%20of%20microbial%20dark%20matter&author=C%20Rinke&author=P%20Schwientek&author=A%20Sczyrba&author=NN%20Ivanova&author=IJ%20Anderson&volume=499&publication_year=2013&pages=431-437&pmid=23851394&doi=10.1038/nature12352&)]
* 13.Liu Y, Jin JH, Liu YH, Zhou YG, Liu ZP.
  2010.
  *Dongia mobilis* gen. nov., sp. nov., a new member of the family *Rhodospirillaceae* isolated from a sequencing batch reactor for treatment of malachite green effluent. Int J Syst Evol Microbiol
  60:2780–2785. doi: 10.1099/ijs.0.020347-0. [[DOI](https://doi.org/10.1099/ijs.0.020347-0)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20061488/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int%20J%20Syst%20Evol%20Microbiol&title=Dongia%20mobilis%20gen.%20nov.,%20sp.%20nov.,%20a%20new%20member%20of%20the%20family%20Rhodospirillaceae%20isolated%20from%20a%20sequencing%20batch%20reactor%20for%20treatment%20of%20malachite%20green%20effluent&author=Y%20Liu&author=JH%20Jin&author=YH%20Liu&author=YG%20Zhou&author=ZP%20Liu&volume=60&publication_year=2010&pages=2780-2785&pmid=20061488&doi=10.1099/ijs.0.020347-0&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Data Availability Statement

Raw sequence reads are available under BioProject accession number [PRJNA428383](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA428383). Whole-genome sequences are available under the sequential BioSample accession numbers [SAMN10026417](https://www.ncbi.nlm.nih.gov/biosample/SAMN10026417) to [SAMN10026511](https://www.ncbi.nlm.nih.gov/biosample/SAMN10026511), which include annotations produced with the Prokaryotic Gene Annotation Pipeline (PGAP). [Table 1](#tab1) contains individual Web links to each bin assembly and annotation.