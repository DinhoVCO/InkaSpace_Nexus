Nucleic Acids Res

. 2024 Nov 18;53(D1):D1697–D1710. doi: [10.1093/nar/gkae1116](https://doi.org/10.1093/nar/gkae1116)

# NASA open science data repository: open science for life in space

[Samrawit G Gebre](https://pubmed.ncbi.nlm.nih.gov/?term=%22Gebre%20SG%22%5BAuthor%5D)

### Samrawit G Gebre

1
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Samrawit G Gebre](https://pubmed.ncbi.nlm.nih.gov/?term=%22Gebre%20SG%22%5BAuthor%5D)

1,2, [Ryan T Scott](https://pubmed.ncbi.nlm.nih.gov/?term=%22Scott%20RT%22%5BAuthor%5D)

### Ryan T Scott

2
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Ryan T Scott](https://pubmed.ncbi.nlm.nih.gov/?term=%22Scott%20RT%22%5BAuthor%5D)

2,2, [Amanda M Saravia-Butler](https://pubmed.ncbi.nlm.nih.gov/?term=%22Saravia-Butler%20AM%22%5BAuthor%5D)

### Amanda M Saravia-Butler

3
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Amanda M Saravia-Butler](https://pubmed.ncbi.nlm.nih.gov/?term=%22Saravia-Butler%20AM%22%5BAuthor%5D)

3, [Danielle K Lopez](https://pubmed.ncbi.nlm.nih.gov/?term=%22Lopez%20DK%22%5BAuthor%5D)

### Danielle K Lopez

4
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Danielle K Lopez](https://pubmed.ncbi.nlm.nih.gov/?term=%22Lopez%20DK%22%5BAuthor%5D)

4, [Lauren M Sanders](https://pubmed.ncbi.nlm.nih.gov/?term=%22Sanders%20LM%22%5BAuthor%5D)

### Lauren M Sanders

5
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Lauren M Sanders](https://pubmed.ncbi.nlm.nih.gov/?term=%22Sanders%20LM%22%5BAuthor%5D)

5, [Sylvain V Costes](https://pubmed.ncbi.nlm.nih.gov/?term=%22Costes%20SV%22%5BAuthor%5D)

### Sylvain V Costes

6
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Sylvain V Costes](https://pubmed.ncbi.nlm.nih.gov/?term=%22Costes%20SV%22%5BAuthor%5D)

6,✉

* Author information
* Article notes
* Copyright and License information

1
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

2
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

3
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

4
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

5
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

6
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA

✉

To whom correspondence should be addressed. Tel: +1 650 526 2491; Email: sylvain.v.costes@nasa.gov

2

The first two authors should be regarded as Co-First Authors.

Accepted 2024 Oct 28; Revised 2024 Oct 11; Received 2024 Sep 6; Collection date 2025 Jan 6.

Published by Oxford University Press on behalf of Nucleic Acids Research 2024.

This work is written by (a) US Government employee(s) and is in the public domain in the US.

[PMC Copyright notice](/about/copyright/)

PMCID: PMC11701653  PMID: [39558178](https://pubmed.ncbi.nlm.nih.gov/39558178/)

## Abstract

Space biology and health data are critical for the success of deep space missions and sustainable human presence off-world. At the core of effectively managing biomedical risks is the commitment to open science principles, which ensure that data are findable, accessible, interoperable, reusable, reproducible and maximally open. The 2021 integration of the Ames Life Sciences Data Archive with GeneLab to establish the NASA Open Science Data Repository significantly enhanced access to a wide range of life sciences, biomedical-clinical and mission telemetry data alongside existing ‘omics data from GeneLab. This paper describes the new database, its architecture and new data streams supporting diverse data types and enhancing data submission, retrieval and analysis. Features include the biological data management environment for improved data submission, a new user interface, controlled data access, an enhanced API and comprehensive public visualization tools for environmental telemetry, radiation dosimetry data and ‘omics analyses. By fostering global collaboration through its analysis working groups and training programs, the open science data repository promotes widespread engagement in space biology, ensuring transparency and inclusivity in research. It supports the global scientific community in advancing our understanding of spaceflight's impact on biological systems, ensuring humans will thrive in future deep space missions.

## Graphical Abstract

### Graphical Abstract.

[![Graphical Abstract](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/a7f68ba28bfe/gkae1116figgra1.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116figgra1.jpg)

[Open in a new tab](figure/ga1/)

## Introduction

The fields of space biology and space health are rapidly expanding and becoming more essential as humanity embarks on missions to the Moon, Mars, and other deep space missions beyond low Earth orbit. The heightened biomedical risks and new challenges associated with deep space missions ([1](#B1)) necessitate the discovery of new knowledge, the development of new health countermeasures and the creation of novel ecosystems ([2](#B2),[3](#B3)), life support systems, crop production methods, *in situ* biomedical research and biomedical support capabilities ([4](#B4)). Supporting distant and long-duration missions is our new paradigm that requires biological and health-related data to be findable, accessible, interoperable and reusable (FAIR) ([5](#B5),[6](#B6)). Optimal data governance for public dissemination encompasses a spectrum from closed to mediated, embargoed and fully open access. Scientific reproducibility, knowledge discovery and data reuse is maximized when data are both FAIR and open ([7](#B7)).

For the past decade, NASA GeneLab ‘omics database has played the leading role in collecting, curating, processing and organizing space biology data ([8](#B8)), catalyzing numerous biological discoveries. Noteworthy publications that have utilized GeneLab include studies on mitochondrial dysfunction across species ([9](#B9)), short duration spaceflight on human health ([10](#B10)), kidney dysfunction ([11](#B11)), endocrinology ([12](#B12)), carbon dioxide impact ([13](#B13)), skin health ([14](#B14)), liver lipid dysregulation ([15](#B15)) and changes in the gut microbiome ([16](#B16)). Such pioneering work highlighted the need for all space biomedical data beyond molecular ‘omics to also be maximally open access and FAIR. Consequently in 2021, the integration ([17](#B17)) of the NASA Ames Life Sciences Data Archive (ALSDA) with the GeneLab database culminated in the creation of the NASA Open Science Data Repository (OSDR; <https://www.nasa.gov/osdr/>). Today, OSDR combines ‘omics with non-omics life sciences space-related data that span physiological, phenotypic, bioimaging, behavioral, clinical, environmental telemetry, hardware data and more. This integration involved ALSDA transforming to standardize, curate and make all its collected data more FAIR and open ([7](#B7),[17](#B17)).

This paper describes the new OSDR database architecture and features that enable the submission, hosting, retrieval and analysis of diverse data types, including both ‘omics and non-omics, from spaceflight to analog missions. We review the new biological data management environment (BDME), which supports the submission of both ‘omics and non-omics data in a standardized format. We introduce the new OSDR database layout, which includes access to additional experimental, payload and mission-specific information and telemetry data associated with each study. We also describe the new controlled data access feature that mediates the sharing of sensitive commercial astronaut data, making data as open as possible and as close as necessary. The generation of novel spaceflight data by the GeneLab Sample Processing Laboratory (SPL) is described, along with the expansion of GeneLab's standardized data processing pipelines and available processed data products. Access to all metadata and data hosted on OSDR is provided by the expanded Application Programming Interface (API) and Registry of Open Data on Amazon Web Services (AWS). We also review the rich set of visualization tools available to easily analyze and interpret OSDR data, further democratizing these data. We also present user roadmap examples for the public to engage in spaceflight biomedical sciences leveraging OSDR. Lastly, we introduce the OSDR Analysis Working Groups (AWGs) and training initiatives that enhance engagement with space-relevant data and support a robust and active space biology and space health research community.

## Expanded database architecture and new features

### Database content and use

OSDR champions data stewardship to enable all humanity to participate in discovery and exploration by making data more equitable and accessible to all ([18](#B18)). As of October 2024, OSDR houses over 500 studies, including close to 1000 spaceflight or space-analog datasets, with data from over 80 different assays, encompassing both ‘omics and physiological/phenotypic assays (Figure [1](#F1)). OSDR is species-agnostic, offering access to a diverse range of studies from rodents to plants, microbes and humans—including data from commercial astronauts connected to the Inspiration 4 SpaceX mission ([10](#B10)). The data hosted on OSDR are linked to 105 original peer-reviewed scientific publications and have enabled 92 publications, representing an 88% return on investment (ROI), measured by the number of enabled publications versus primary publications (Figure [1](#F1)). This indicates that the ROI grows faster than the number of primary publications because the data in OSDR have led to a significantly higher number of new publications, suggesting that each dataset submitted to OSDR has the potential to generate multiple follow-up studies and accelerate research output. The repository is also currently curating data from other space agencies and companies such as the European Space Agency (ESA), providing studies on human head-down bed rest, human dry immersion, model organisms exposed to simulated space radiation and other model organisms flown on the International Space Station (ISS). The demand for OSDR to ingest commercial human data has been surging, highlighting its unique role in the space biology ecosystem. Not only does OSDR promote greater FAIR/Open access to data, but it also enables comparisons across hundreds of datasets, spanning different species and various missions/experiments. This capability greatly enhances the scientific value of space exploration by enriching the biomedical insights gained from shared data.

#### Figure 1.

[![Figure 1.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/a2d367e061ec/gkae1116fig1.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig1.jpg)

[Open in a new tab](figure/F1/)

OSDR metrics. Overview of studies hosted on OSDR as of October 2024, including the total number of international studies, percent of total datasets for each ‘omics and each phenotypic-physiological measurement type, percent of total studies for each organism and the ROI measured by the number of enabled publications versus primary publications that use OSDR datasets.

### Data management workflow

To increase the reusability and accessibility of biological data from space-relevant experiments and data types and to improve data submission planning, the original GeneLab submission portal was expanded into the BDME. Key features such as Digital Object Identifiers (DOIs) and the ISA framework (Investigation, Study, Assay) ([19](#B19),[20](#B20)) remain integral to the BDME. The submission portal now has the capability to collect all types of data-metadata, encompassing not just ‘omics but all life science and biomedical assays. The enhanced BDME tools are designed to ease the submission process, enabling self-curation with established metadata and data standards through a new user-friendly interface and a streamlined workflow.

The BDME’s latest updates support ongoing data and metadata submission throughout research, avoiding end-of-grant rushes that compromise data quality, while preserving data privacy. BDME introduces a collaborative workspace, enabling users to privately share, organize and store files during their experiments. The collaborative workspace provides users a new solution for transferring large data files quickly and securely, with the File Application for Seamless Transfer to/from the Workspace (FASTWork). FASTWork ensures the integrity of data transfers by automatically resuming the process if interrupted due to connectivity issues or computer downtime. This functionality is accessible through both a command-line interface and a downloadable application, making it versatile for various user preferences and technical environments. Users can also add collaborators and specify permissions and roles such as editors, supervisors and submitters, enhancing the collaborative and efficient management of research data. Additionally, a private link feature lets researchers securely share dataset previews with peer reviewers and editors.

The Research Data Submission Agreement (RDSA), now a requirement under the NASA Biological and Physical Sciences (BPS) Division's Scientific Data Management Policy (<https://science.nasa.gov/biological-physical/data/>), guides NASA investigators in outlining data products, assays, tissues and submission timelines. The information captured in the RDSA generates a unique Experiment page, automatically populating the data to reduce further input from principal investigators (PIs), thus significantly lowering the burden of data entry and ensuring metadata richness—a key FAIR requirement. Importantly, aside from RDSA-directed NASA BPS policy timelines, there is no set timeframe for data release from submission to public availability on OSDR, providing submitters control over their data's accessibility. Since there is no required timeframe for public release after data submission, submitters are encouraged to begin the submission process as early as possible. Starting early helps researchers meticulously collect and standardize their metadata throughout their experiments and prevents a heavy data submission workload at the end of their grant. This ensures ample time to gather complete metadata, resulting in higher quality and more comprehensive curation records, ultimately streamlining the submission process.

### New data collections

Integrating ALSDA data into OSDR required developing new data schemas to manage diverse records such as experiments, biospecimens, hardware, payload and mission data. To achieve this, OSDR expanded on GeneLab's existing database to create a schema linking studies with their corresponding reference data collections.

To support the legacy ALSDA data structure used for the past 40 + years and meet new requirements, OSDR introduces a workflow based on a new data and metadata hierarchy (Figures [2](#F2) and [3](#F3)). This new system offers two distinct routes for data submission, one for NASA-funded data (Figure [2](#F2)), and one for non-NASA funded data (Figure [3](#F3)). For NASA-funded PIs, the process begins with the RDSA, which is the initial step and *first tier* of submission. RDSAs capture comprehensive grant-level information, organism metadata and anticipated datasets for submission (Figure [2](#F2)). The *second tier* in OSDR’s data management workflow describes all Experiments performed with grant funds, and establishes connections between individual investigations, linking them to related study collection, and reference data collections (Figure [2](#F2)). The *third-tier* guides submitters through the data submission process, offering options for either a structured, guided submission or independent data and metadata entry for each dataset within a study (Figure [2](#F2)). This tier is the point of entry for non-NASA PIs who do not need to have a NASA investigation identifier (Figure [3](#F3)).

#### Figure 2.

[![Figure 2.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/a3ccb1209c6a/gkae1116fig2.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig2.jpg)

[Open in a new tab](figure/F2/)

NASA funded PI data and metadata hierarchy. The RDSA is for NASA-funded PIs and describes the experiment(s) conducted with the associated grant funds. Each experiment receives a unique identifier (e.g. OS-636) and is linked to respective Reference data and studies. Reference data records associated with each experiment include payload (e.g. BRIC-16), mission (e.g. STS-131), hardware (e.g. BRIC-PDFU) and subject (e.g. Cress, mouse ear). Each study associated with an experiment has a unique identifier (e.g. OSD-44 and OSD-121). Most studies are categorized based on organism and tissue type, although plant studies are distinguished based solely on organism as shown here. Each study is further categorized between ‘omics and phenotypic-physiological datasets. GLDS includes all ‘omics data and LSDS contains all phenotypic-physiological data derived from the respective study.

#### Figure 3.

[![Figure 3.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/24d21ae87540/gkae1116fig3.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig3.jpg)

[Open in a new tab](figure/F3/)

Non-NASA funded PI data and metadata hierarchy. The point of entry for non-NASA PIs begins at the study level. Most studies are categorized based on organism and tissue type, although plant studies are distinguished based solely on organism. Each study can maintain links to respective reference data when applicable. Reference data records associated with each study can include payload (e.g. Inspiration4 Crew), mission (e.g. SpaceX Inspiration4), subject (e.g. Human) and/or hardware (not included in this study). Each study has a unique identifier (e.g. OSD-630, OSD-569, OSD-656). Each study is further categorized between ‘omics and phenotypic-physiological datasets. GLDS includes all ‘omics data and LSDS contains all phenotypic-physiological data derived from the respective study.

As illustrated in Figure [2](#F2), OSDR utilizes persistent identifiers throughout the hierarchy of its data schema. Specifically, NASA investigators are assigned a unique identifier for each RDSA (e.g. RDSA-563) and experiment (e.g. OS-636; OS = Open Science experiment), while all data submitters receive a unique study identifier (e.g. OSD-44; OSD = Open Science Dataset). Within this framework, an experiment can encompass multiple studies. The majority of studies are categorized by organism and tissue type, whereas plant studies are categorized solely by organism, often encompassing multiple tissue types within a single study. Each study, in turn, may include up to two types of datasets: ‘omics assays (e.g. GLDS-44; GLDS = GeneLab Dataset) and/or physiological/phenotypic assays (e.g. LSDS-56; LSDS = Life Science Dataset) and all assays of the same type are grouped under a single unique dataset identifier. This hierarchical arrangement promotes thorough organization and enhances the ease of data management and retrieval, supporting detailed scientific research, analysis, and the understanding of study design based on the original data.

These new collections are seamlessly integrated into the new OSDR repository webpage, making them findable using the OSDR repository search features, and they are also linked within each OSD study page, directly connecting studies to corresponding experiment, mission and payload pages (Figure [4](#F4)). In addition to these reference data record links, each study page consists of descriptive and rich metadata, links to definitions of ontology terms and detailed sample and assay metadata that follow community standards. Users can also access all available data files structured by data level, publication information and author contact details from a study page (Figure [4](#F4)). Additionally, the interface supports easy citation of datasets with a DOI, ensuring proper credit and discoverability.

#### Figure 4.

[![Figure 4.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/af6f1a513cda/gkae1116fig4.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig4.jpg)

[Open in a new tab](figure/F4/)

An OSD study page. Screenshot of study OSD-595 showing the links to the respective experiments (OS-808), mission (SpaceX-14) and payload (MVP-Fly-01) details, sample metadata, GLDS and LSDS assay metadata and primary publications (left) and study citation (inset).

The OSDR reference data collection is a new collection which reflects the integration of more than 2000 + records that span over 40 years of life sciences research migrated from the former ALSDA legacy relational database. In addition, if submitters lack the necessary reference data, OSDR’s curation team is available to assist in adding these to the repository and refining the collection. This flexibility ensures that non-NASA PIs can fully engage with the OSDR ecosystem without being hindered by NASA-specific administrative details.

### Controlled data access

Although almost all data available in OSDR are openly accessible, sensitive human-derived data are secured through a controlled access system based on the NIH Database of Genotypes and Phenotypes ([21](#B21)). This system allows storage and sharing of data in accordance with stringent agreements and policies established by the Institutional Review Board (IRB) of the data submitter. By adhering to these principles, OSDR facilitates the secure and responsible reuse of valuable research data, thereby advancing scientific discovery while maintaining the trust, ethics and rights of data contributors ([22](#B22),[23](#B23)).

Researchers can explore all OSDR data via the OSDR search functions, identifying studies and their access control levels. Restricted files are indicated by a lock icon and a ‘Request Access to Restricted Files’ button (Figure [5](#F5)). To access restricted data, investigators must submit a controlled access data access request form, including IRB documentation, and agree to the data user agreement. The request is then verified by the OSDR Curation Team and reviewed by a Data Access Committee led by the original data submitter. Approved requests grant data access under specified terms, and investigators must sign and comply with these terms and provide progress updates. Upon project completion, all downloaded data must be deleted, and proper citations and acknowledgments are required.

#### Figure 5.

[![Figure 5.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/d57b962cb809/gkae1116fig5.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig5.jpg)

[Open in a new tab](figure/F5/)

Data access request (DAR) process for OSDR controlled data. The process begins by clicking the ‘Request Access to Restricted Files’ button on datasets requiring controlled access (e.g. human sequence data). Requesters must submit a data request package with IRB documentation and agree to the Data User Agreement, which is reviewed by the Data Access Committee. Upon approval, data access is granted under the specified terms. Users are required to delete downloaded data upon project completion.

For example, users can request controlled data from the recent civilian astronaut mission Inspiration 4 ([10](#B10),[24](#B24)). With this process, one can request raw data generated from whole blood and urine samples, and skin biopsies from the crew, collected at different time points before, during, and after spaceflight (i.e. OSD-569, OSD-570, OSD-571, OSD-574, OSD-575, OSD-656, OSD-687). This process facilitates secure data sharing, more diverse and inclusive access to spaceflight research, and a unique opportunity for the scientific community to unlock profound insights into the consequences of space travel on the human body without revealing sensitive data.

## Enhancing usability and access

### Data generation

The opportunities for biological experimentation in space are constrained by high costs, limited crew time, and limited availability of space aboard spacecraft and habitats, which restricts the number of spaceflight studies and their sample sizes. Therefore, to maximize scientific discoveries from spaceflight missions, NASA GeneLab established the SPL, which processes preserved leftover samples to generate new data or augment existing studies on OSDR. Tissue samples provided by the NASA Biological Institutional Scientific Collection (NBISC) and the Biospecimen Sharing Program from experiments conducted on the ISS or from legacy missions (e.g. Space Shuttle-era) are processed by SPL. The resulting data, complete with detailed metadata including a description of the origin mission, are promptly made available on OSDR for public scientific analysis, enhancing data accessibility and interpretability.

The SPL shares publicly accessible standard operating procedures (SOP) for various processes including tissue storage, cutting, homogenization, nucleotide extraction, library preparation, and sequencing (<https://www.nasa.gov/osdr-sequencing-and-sample-processing-standard-operating-procedures/>), developed in collaboration with the International Standards for Space Omics Processing consortium (<https://issop.astrobotany.com/>) ([25](#B25)). The use of consistent SOPs for data generation across distinct laboratories ensures harmonized DNA and RNA sequencing data from a wide range of biological samples, such as mammalian and plant tissues, cells and microbes.

Currently, OSDR hosts over 75 OSD studies produced by GeneLab's SPL, including more than 100 ‘omics datasets from experiments involving rodent, plant, and bacterial samples. These datasets have been instrumental in 31 peer-reviewed scientific publications, thereby significantly enriching our understanding of spaceflight's impacts on terrestrial biology ([15](#B15),[26–29](#B26)). Additionally, GeneLab provides SPL services to NASA-funded PIs, allowing them to benefit from GeneLab's expertise in processing space-flown tissues (<https://osdr.nasa.gov/bio/forms/genelab-sequencing-services.html>). This simplifies data submission to OSDR, and the resulting data harmonization enables more accurate comparisons between studies.

### Metadata and community consensus standards enables interoperability and reusability

Within OSDR, NASA GeneLab provides assay metadata standards and templates for PIs to follow when submitting through BDME for over 40 ‘omics assays (Table [1](#tbl1)). The metadata for these assays follows the investigation, sample, assay (ISA)-tab format, a slightly altered version to meet the needs of OSDR ([19](#B19),[20](#B20)) and uses standardized, controlled ontologies to ensure data is maximally FAIR. In 2022, ALSDA began curating non-omics datasets (e.g. physiological and phenotypic) using a similar approach.

#### Table 1.

OSDR assay metadata configurations1

| ‘Omics assay types | Phenotypic-physiological assay types |
| --- | --- |
| AmpliconSequencing (ITS, 18S, 16S) ([31](#B31)) | ATPase activity via Spectrophotometry ([32](#B32)) |
| Whole Genome Bisulfite Sequencing | Rodent Gait ([33](#B33)) |
| Reduced Representation Bisulfite Sequencing | Open Field ([34](#B34)) |
| Whole Transcriptome Bisulfite Sequencing | Object in Place ([35](#B35)) |
| Enzymatic Methylation Sequencing | Radial Arm Water Maze ([36](#B36)) |
| Whole Genome Sequencing ([37](#B37),[38](#B38)), MINISEQE Guidelines <https://www.fged.org/projects/minseqe/>) | Unconstrained Cognitive Flexibility ([39](#B39)) |
| Targeted DNA Sequencing | Novel Object Recognition ([40](#B40)) |
| Whole Genome Shotgun Metagenomics Sequencing ([41](#B41)) | Elevated Plus Maze ([42](#B42),[43](#B43)) |
| Metatranscriptomics Sequencing | Attentional Set Shifting ([44](#B44),[45](#B45)) |
| NucleotideMicroarray(DNA, RNA, miRNA, SNP) ([46](#B46)) | Barnes Maze ([47](#B47)) |
| Protein Microarray ([46](#B46)) | 3-Chamber Social Isolation ([48](#B48)) |
| Bulk RNA Sequencing ([49](#B49)), MINISEQE Guidelines <https://www.fged.org/projects/minseqe/> ([49](#B49)) | Drosophila Climbing Locomotion ([50](#B50)) |
| Targeted RNA Sequencing | Drosophila in-Flight Behavior ([51](#B51)) |
| Single Cell/Nuclei RNA Sequencing ([52](#B52)) | Operant Response ([53](#B53)) |
| microRNA Sequencing | Novel Object Location ([54](#B54)) |
| Single Cell/Nuclei ATAC Sequencing | Balance Beam ([55](#B55)) |
| Spatial Transcriptomics | Deacon Score ([56](#B56)) |
| Nanopore DNA Sequencing | 3pt/4pt/Torsion Mechanical Tests ([57](#B57)) |
| Nanopore Targeted DNA Sequencing | Micro-computed Tomography ([58](#B58)) |
| Nanopore Direct RNA Sequencing | Dual-Energy X-Ray Absorptiometry ([59](#B59)) |
| Targeted Circular Consensus DNA Sequencing | Peripheral Quantitative Computed Tomography ([60](#B60)) |
| Proteomic Mass Spectrometry ([61](#B61)) | Calcium Uptake via Spectrofluorometry ([62](#B62)) |
| Metabolomic Mass Spectrometry | Echocardiogram Ultrasound ([63](#B63)) |
| Metabolite NMR Spectroscopy | Estrous Cycle Cytology ([64](#B64)) |
| Chromatin Immunoprecipitation Sequencing | Flow Cytometry ([65](#B65)) |
| Chromatin Immunocleavage Sequencing | Genome Wide Association Study ([66](#B66)) |
| Methylated DNA Immunoprecipitation Sequencing | Histomorphometry ([67](#B67)) |
| Enzyme-Linked ImmunoSorbent Assay (ELISA) | Histology |
|  | Light Microscopy |
|  | Immunohistochemistry |
|  | Immunostaining |
|  | Fluorescence Microscopy |
|  | Confocal Microscopy |
|  | Transmission Electron Microscopy ([68](#B68)) |
|  | Scanning Electron Microscopy ([69](#B69)) |
|  | Morphometric Photography |
|  | Muscle Contractility ([70](#B70)) |
|  | Muscle Force via Force Plate ([71](#B71)) |
|  | Muscle Force via Force Transducer ([72](#B72)) |
|  | Ophthalmological Ultrasound ([73](#B73)) |
|  | Optical Coherence Tomography ([74](#B74)) |
|  | Western Blot ([75](#B75)) |
|  | Magnetic Resonance Imaging ([76](#B76),[77](#B77)) |

[Open in a new tab](table/tbl1/)

1List of standardized ‘omics and physiological-phenotypic assay types available through OSDR’s BDME. Assay standards were determined using established standards in the literature and through feedback and consensus discussions from AWG SMEs.

As of October 2024, 61 ALSDA assay metadata configurations have been created and implemented on OSDR. As more data types or new data types are submitted to OSDR, more are continuously being developed. These were established through virtual meetings with ∼150 subject matter experts (SMEs) and asynchronous documentation feedback within the ALSDA AWG. Each assay metadata standard was reviewed and discussed by at least three SMEs, with some of the more common assays reviewed by up to 10 experts. All OSDR assay metadata configurations with references are openly available for public review and used as metadata templates for OSDR submission (<https://github.com/nasa/OSDR_Data_Curation>). Table [1](#tbl1) shows the majority of the newly standardized phenotypic-physiological assay types available in OSDR, as well as the ‘omics assays. The curation and maximally open accessibility of these phenotypic-physiological spaceflight data have already resulted in two publications stemming from users’ data mining and reusing the data ([28](#B28),[30](#B30)).

### Data repository search

OSDR is equipped with expanded search features (Figure [6](#F6)) that enable users to sort through studies using keyword searches and study search filters, including project type (e.g. spaceflight, ground, or high altitude), assay type (e.g. RNA sequencing, bisulfite sequencing, histomorphometry, mass spectrometry, ultrasonography, etc.), organism (e.g. rodent, human, plant, bacteria, etc.), tissue (e.g. leaf, seedlings, cells, feces, liver, retina, blood, etc.) and factors (e.g. spaceflight, ionizing radiation, age, sex, ecotype, etc.). Users can also filter searches based on data type, including study, experiment, subject, biospecimen, payload, mission, hardware and vehicle. They can specify their OSDR search to include ‘omics (GeneLab), non-omics (ALSDA) or both using the data source search filter. In addition to searching within OSDR, the data source search filter now includes federated search capabilities, allowing users to search other repositories, such as NIH GEO (<https://www.ncbi.nlm.nih.gov/gds>), EBI PRIDE (<https://www.ebi.ac.uk/pride/>), ANL MG-RAST (<https://www.mg-rast.org/>) and soon JGI (<https://data.jgi.doe.gov/>) and NMDC (<https://data.microbiomedata.org/>). These expanded search features enhance findability by helping users identify relevant datasets across different databases.

#### Figure 6.

[![Figure 6.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/ea97d631e5a9/gkae1116fig6.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig6.jpg)

[Open in a new tab](figure/F6/)

OSDR search features. The OSDR repository landing page is equipped with a search bar to search based on keywords or phrases (top middle). Users can refine their search based on search filters including data source (e.g. GeneLab, ALSDA or federated search in NIH GEO), data type (e.g. study, experiment and subject), project type (e.g. ground, spaceflight), assay type (e.g. bisulfite sequencing, behavior-gait, RNA-seq), organism (e.g. rodent, human and plant), tissue (e.g. liver, root and cells) and factor (e.g. spaceflight, ionizing radiation) (left). Search results are displayed and can be sorted by relevance, release date, accession or title (top right).

### Expanded API and direct cloud access

The OSDR API has been enhanced to include new data types, enabling users to query the database for experiment, mission, hardware, vehicle, subject and biospecimen data (<https://www.nasa.gov/reference/osdr-public-api/>). In addition, users can utilize the API to complete full-text searches, data file retrieval and metadata retrieval associated with both ‘omics and physiological-phenotypic data. The API empowers users to programmatically access data across multiple missions, experiments and datasets, facilitating meta-analysis and easing access to download large data files.

As part of the NASA Science Mission Directorate (SMD) Open-Source Science Initiative, AWS and NASA have established a Space Act Agreement to explore optimal practices for discovering, accessing and utilizing high-value NASA science datasets. All public data in OSDR are now available on the Registry of Open Data on AWS (<https://registry.opendata.aws/nasa-osdr/>), enabling users to directly query and execute scripts across extensive datasets using AWS S3 command-line tools. The scientific community gains significantly from this initiative, which removes the time required to download large datasets and allows for analysis using AWS’s computational resources directly.

## Increasing engagement

### Analysis working groups

As space-related biological, biomedical, and other life science data/metadata are precious national and global resources, OSDR serves not just as a data repository, but as a central community hub for global space life sciences/biomedical data, with scientific results helping enable life to thrive in space.

Beyond making space biology and space health data FAIR and maximally open, OSDR (and its precursor GeneLab) was designed to maximally engage scientific community members to ensure OSDR is in line and up to date with scientific best practices, enable networking within and beyond the space biology community, and to build trust with users. This was accomplished by the development and expansion of the OSDR AWGs, which have grown into an enormous community around OSDR (<https://awg.osdr.space/>). There are ∼800 volunteer OSDR AWG members, who provide feedback on scientific standards for reuse (subject and assay metadata; data processing pipelines; dataset formats and uniform structures for machine-readability) and collaborate to mine and reuse OSDR data to conduct scientific analyses. OSDR has enabled 92 publications as of October 2024, many directly from AWG collaborations and most notably in ‘The Biology of Spaceflight’ Cell Press package in 2020 (<https://www.cell.com/c/the-biology-of-spaceflight>) and the ‘Space Omics and Medical Atlas (SOMA) across orbits’ Nature Portfolio package in 2024 (<https://www.nature.com/immersive/d42859-024-00009-8/index.html>).

The OSDR AWGs are open to anyone in the world to join and currently consist of members from ∼40 different countries. Participants range in career level from high school students to undergraduate and graduate students to postdocs to PIs and established scientists in a variety of different sectors including citizen scientists, academia, government, non-profits, NGOs and commercial industry.

### Greater access, inclusion and quality with standardized data processing

‘Omics data in their raw form are largely inaccessible to non-bioinformaticians; therefore, GeneLab collaborates with the scientific community via the AWG to develop standard processing pipelines to generate and publish processed data on OSDR. Unlike raw data, processed data have greater immediate value to diverse users with varying technical backgrounds and computational capabilities. Furthermore, standardizing processing workflows is essential to match the pace of raw data generation, ensure reproducibility and enable standardized processed data for comparison across datasets.

At the second AWG annual workshop in 2019, GeneLab and the AWGs achieved a milestone by establishing and publishing the first RNAseq consensus pipeline ([78](#B78)). Building on this achievement, GeneLab has since developed standard processing pipelines for a variety of ‘omics assays across different genomic, transcriptomic and epigenetic technologies. All these pipelines undergo a rigorous review process by the AWGs, incorporating feedback before their publication and implementation. These pipelines are publicly available on GitHub for broader access and use by the scientific community (<https://github.com/nasa/GeneLab_Data_Processing>). GeneLab pipelines are wrapped into Nextflow workflows ([79](#B79)) to automate and accelerate processing of these ‘omics data types. In addition to core data processing, workflows also include raw data staging and a robust verification and validation program to identify errors in real-time, halt additional downstream computation and preserve computational resources.

To enhance reproducibility of GeneLab-generated data and expand access to GeneLab workflows for users without sufficient computing resources or the knowledge to install and run software, GeneLab partnered with the Department of Energy through a memorandum of understanding to create the NASA EDGE Bioinformatics platform (<https://nasa.edgebioinformatics.org/home>). NASA EDGE (Empowering the Development of Genomics Expertise; [([80](#B80))]) Bioinformatics is an open-access web-based platform that utilizes shared compute resources to run the GeneLab standardized bioinformatics workflows, which eliminates the need for researchers to have their own high-performance computing cluster. The web-based platform makes complicated biological analyses incredibly easy to perform, thus expanding the reach of these analyses to bioinformatics novices, students and even citizen scientists enabling them to contribute to scientific discoveries and progress.

### Visualization tools enable knowledge discovery

Standardized processing pipelines in OSDR convert large volumes of raw data into tabular data that are easily interpretable, even for those without bioinformatics expertise, assuming the availability of suitable tools for data visualization. GeneLab recognized this need years ago by initiating the Visualization Platform, enabling users to delve into individual transcriptomic datasets. Building on this foundation, OSDR has introduced the Multi-Study Visualization Platform, enhancing functionality by allowing users to simultaneously compare data across multiple studies (<https://visualization.genelab.nasa.gov/data/>). Today, OSDR offers a comprehensive suite of visualization tools tailored for diverse research needs and designed to help users understand how environmental factors may affect OSDR biological data (Figure [7](#F7)).

#### Figure 7.

[![Figure 7.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/995c2d62e314/gkae1116fig7.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig7.jpg)

[Open in a new tab](figure/F7/)

OSDR Visualization Tools. Top left: Multi-study data visualization dashboard showing interactive processed transcriptomic data search filters, principal component analysis plot, differential gene expression table and normalized enrichment score plot. Top right: RadLab dashboard showing interactive radiation detection instrument selection, time-series plots and detector comparison plots. Bottom: EDA dashboard showing interactive temperature, humidity and CO2 plots, mission milestones and multiple mission comparison plots.

The Multi-Study Visualization Platform enables the visualization of multiple RNA sequencing datasets simultaneously. Users can navigate through OSDR’s comprehensive dataset repository, applying filters such as experimental factors, assay technology types, organisms and tissue types to pinpoint specific studies. Once users select samples from one or more RNA sequencing datasets to combine, they have the flexibility to normalize the combined data using the DESeq2 Median of Ratios method, followed by performing differential expression analysis. Additional selections can be made after examining both normalized and unnormalized PCA plots. The visualization interface includes interactive tools like pair plots, volcano plots, ideograms, gene set enrichment analysis and differential gene expression charts, all designed to enhance the user's ability to explore and analyze the data effectively.

Accessing environmental telemetry data of spacecraft relevant to the biological payloads available in OSDR has always been challenging due to data fragmentation and unclear data governance across space agencies and databases. To address this issue, OSDR introduced the Environmental Data Application (EDA; <https://visualization.osdr.nasa.gov/eda>), which transforms data streams from spacecraft into a time series format and reduces confounding factors among independent variables. As of October 2024, EDA focuses on telemetry and radiation data from Rodent Research missions aboard the ISS, encompassing temperature, relative humidity, CO2 levels and radiation dose. The application enables users to analyze data from individual missions, compare two missions and download both summary and detailed data tables. Plans to expand EDA’s capabilities to include additional biological payloads (human, plant, etc.) are contingent on receiving detailed data streams of information from the specific hardware and payloads involved.

In response to difficulties in accessing radiation data, OSDR supported the creation of RadLab, a database integrating radiation dosimetry from multiple space agencies including NASA, ESA, the German and Italian Space Agencies and the Bulgarian Academy of Sciences. RadLab features a visualization portal (<https://visualization.osdr.nasa.gov/radlab>) and an API (<https://visualization.osdr.nasa.gov/radlab/api>) that facilitates data queries by craft, sensor type, time range and radiation type (e.g. galactic cosmic rays, solar particle events, the contribution of the South Atlantic Anomaly), enhancing the accessibility and usability of these data. The API provides programmatic access for use in computational pipelines and GUIs for data visualization and exploration, making these data FAIR. OSDR is actively enhancing its integration with RadLab to provide average absorbed radiation doses for any payload, by incorporating these metadata directly into the repository. Additionally, radiation dose time series data are being directly fed into EDA to streamline access and analysis.

### Training the next generation of space biologists and bioinformaticians

To sensitize the scientific community to space biology and increase the number of scientists who understand and utilize OSDR data and resources in 2021, OSDR introduced the GL4U training program (GeneLab for Colleges and Universities). GL4U leverages the consensus ‘omics processing pipelines, developed by GeneLab and the AWGs, to teach students about space biology and bioinformatics via a series of lectures and hands-on training through Jupyter notebooks. The program offers annual 1–2-week long bootcamps for both students and educators (<https://www.nasa.gov/reference/osdr-educator-resources/>). During the bootcamps, participants complete the GL4U Introduction module set, which includes an introduction to NASA SMD, the NASA Space Biology program, OSDR and GeneLab, and hands-on training in basic coding in Unix and R. Participants then complete a GL4U ‘omics-specific module set, which includes lectures and hands-on training in experimental design and data processing using the GeneLab standard pipeline. As of October, 2024, GL4U ‘omics-specific module sets have been developed for RNA Sequencing and Amplicon Sequencing. To date, 14 educators and 76 students from 7 minority serving institutions have successfully completed a GL4U bootcamp. Pre- versus post-bootcamp surveys revealed a 115% increase, on average, in both participant understanding of ‘omics data processing and in familiarity with NASA Space Biology resources, showing the overwhelming success of these bootcamps. GeneLab is expanding GL4U into a series of open-access on-demand training modules.

NASA’s SMD initiated the Transform to Open Science (TOPS) program in response to the 2022 White House mandate for open science for federal research, launching its operations in 2023, the Year of Open Science ([18](#B18)). The goal of TOPS is to rapidly transform agencies, organizations, and communities to an inclusive culture of open science in part by providing open-source training centered around open science. As part of this initiative, scientists from OSDR and the AWG were awarded a TOPS-T ScienceCore grant to create a training course titled: ‘Training in Artificial Intelligence and Machine Learning for Space Biological Sciences Using NASA Cloud-Based Data’. This course, available on the Canvas platform (enroll here: <https://canvas.instructure.com/enroll/8JYKD7>), offers artificial intelligence and machine learning (AI/ML) training that uses space biology/health data, including OSDR datasets, to teach participants about space biology, model building, data handling and advanced modeling techniques. Students are shown how to interpret results through hands-on practice with real-world use cases from OSDR, using two large AI benchmark datasets released by OSDR for BPS on the Registry of Open Data on AWS (i.e. <https://registry.opendata.aws/bps_microscopy/> and <https://registry.opendata.aws/bps_rnaseq/>). Originally offered synchronously through a live virtual course, the training is now also available asynchronously, allowing participants to engage with a rich array of data types such as phenotypic-physiological, biomedical, imaging and ‘omics data, all hosted on OSDR with extensive, standardized metadata and processed data files. This curriculum paves the way for new scientific discoveries by leveraging AI/ML to mine the comprehensive data resources available through OSDR.

## User roadmap for open science involvement

All data, metadata, resources and trainings available in the OSDR ecosystem are designed to help lower the bar for entry for users worldwide to engage and contribute scientifically to space exploration. Here, we outline three potential journeys of users to leverage different aspects of the OSDR ecosystem (Figure [8](#F8)).

### Figure 8.

[![Figure 8.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35b0/11701653/3b520053ab40/gkae1116fig8.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=11701653_gkae1116fig8.jpg)

[Open in a new tab](figure/F8/)

User roadmap. Part 1: Student journey through OSDR training resources and visualization platforms. Part 2: PI journey through NBISC tissue request. Part 3: Student journey through TOPS-T AI/ML training resources and AWG collaboration.

In the first journey, a student may leverage the training and visualization aspects of the OSDR ecosystem by completing GL4U RNAseq bootcamp, gaining hands-on experience in space biology 'omics data and bioinformatics. Equipped with this knowledge, the student now has the tools to download and analyze data from OSDR and identifies OSD-104 and OSD-105 as studies with muscle multi-omics data from Rodent Research-1 (RR-1). The student uses the Multi-Study Data Visualization portal to combine both datasets, generating a PCA plot and a volcano plot from the RNAseq data and examining the differentially expressed genes between flight and ground control samples. The student notes that the PCA plot shows a strong bias toward tissue difference dominating the impact of spaceflight versus ground control. The student uses the EDA to visualize environmental variables during the RR-1 mission to investigate whether there are any environmental impacts contributing to the 'omics signals. To expand on this analysis, the student joins an AWG and collaborates with other researchers to explore the epigenomics and proteomics data available in these studies. This collaboration leads to the generation of new data that culminates in a scientific publication.

In the second journey, a PI with an established lab requests RR-1 and RR-9 muscle tissues from NBISC and performs functional analysis in the lab. While publishing the findings, the PI submits data to OSDR using the data submission tutorial (<https://osdr-tutorials.readthedocs.io/en/latest/>) and submits the data into OSDR. One of the functional data types does not yet have an assay metadata configuration nor data format standard in OSDR, so the PI joins the AWG and helps create a new assay standard as part of a consensus with other AWG SME members with expertise on that assay. An example of such a workflow is Braun et al., 2021 ([81](#B81)), who requested NBISC samples, then analyzed muscle calcium uptake, helped create the OSDR assay configuration for such measurement and submitted the data to OSDR (OSD-488).

Finally, in the third journey, a student interested in using AI/ML approaches for space biology research enrolls in the asynchronous TOPS-T AI/ML for space biology training course. Enriched with new skills, the student proposes a project to the AWG to develop a predictive model using both RR-1 and RR-9 omics and functional data available on OSDR, leveraging the power of AI/ML for heterogeneous data types. The team re-analyzes the OSDR datasets and publishes their updated results, contributing valuable insights to the field. An example of a similar study is Li et al., 2023 ([28](#B28)), who analyzed 'omics and functional-physiological muscle data from OSDR using a ML workflow.

Images within this figure are adapted from: Braun J. et al. Characterizing SERCA function in murine skeletal muscles after 35–37 days of spaceflight. International Journal of Molecular Sciences, 2021, licensed under CC BY 4.0; Li K. et al. Explainable ML identifies multi-omics signatures of muscle response to spaceflight in mice. NPJ Microgravity, 2023, licensed under CC BY 4.0.

## Discussion and future directions

The successful expansion of human life into deep space hinges on profound advancements in our understanding of space biology and the critical biomedical responses and health systems developed for long-duration and long-distance spaceflight missions. Centralizing and standardizing data, alongside the strategic reuse of tissues, are pivotal for maximizing the value extracted from every piece of available data and tissue. However, a meta-analysis of the field of space medicine and space life sciences by Bellomo et al. reviewed 1215 open-access articles and found that only a third shared their data. Analysis code was almost never shared, and practically no researchers used registered assay methodology standards ([82](#B82)). Especially as humanity nears returning to the Moon, this finding underscores the urgent need for a paradigm shift towards open science in space biology and aerospace medicine, an essential shift required to develop health countermeasures and conduct space biological research.

Responding to this need and leveraging the pioneering work of GeneLab ([8](#B8)), OSDR has rapidly expanded as a public resource to foster extensive engagement in spaceflight science, discovery, research, and development. This expansion has attracted tens of thousands of participants globally, especially via the AWG, and makes all relevant life sciences data from space experiments maximally open access and of high quality. Furthermore, ESA has recently adopted OSDR as its default portal for all life sciences ‘omics data, marking a significant international endorsement of OSDR standards. This collaboration is poised to augment OSDR with hundreds of terabytes of ‘omics data soon, enhancing the repository's utility and scope.

Commercial astronauts are also actively participating in the space biology ecosystem by securely sharing their sensitive data through the OSDR DAR portal ([10](#B10),[18](#B18)). Such practices not only show a shared commitment to centralizing valuable datasets between the scientific community and commercial space sectors but also enhance our ability to compare human, animal, microbial, plant and other data to deepen our understanding of space biology.

Acknowledging the limitations of traditional statistical methods ([83](#B83)), OSDR is also broadening its analytical range to include AI/ML technologies ([4](#B4),[84](#B84)). In partnership with researchers from UC San Francisco, OSDR is integrating a knowledge graph analysis tool known as 'SPOKE' (Scalable Precision Medicine Open Knowledge Engine) into its visualization-analysis portal. This integration aims to enable users to identify symptoms, diseases, and potential therapeutic targets by mining and comparing datasets, enhancing the utility of OSDR for advanced data-driven discoveries ([85–87](#B85)).

OSDR is continuously refining its systems to provide better access and improved tools. The OSDR API will continue evolving to better serve users, with plans to develop more visualization tools for data analytics, including single-cell sequencing, metagenomics and physio-phenotypic-bioimaging data. AI/ML enhancements will streamline data submission, and an OSDR chatbot is being developed to help users discover and interpret datasets more easily.

To conclude, as humanity has entered the ‘Second Space Age’ ([88](#B88)), a central goal for the future of OSDR has evolved from FAIR data and metadata to the FAIREST principles, standing for more Engagement, more Social connections, and more Trust in its quality and stewardship ([89](#B89)). As the commercial spaceflight industry expands, OSDR is poised to facilitate broader public access to life science and biomedical data. As a leading force in open science, OSDR empowers the global community to actively engage in space exploration and discovery, aligning directly with NASA’s ambitious goals for the ‘Moon to Mars’ ([90](#B90)) and Artemis campaigns.

## Acknowledgements

We wish to thank the scientific community including data submitters, users and advisors for their longstanding support of OSDR. We thank all OSDR AWG members for their years of feedback, support, and acts of scientific discovery in support of spaceflight life sciences. Numbering over 800 people, the robustness and successes of OSDR reflect this community of scientists, students and citizen scientists. Much of the activity and excitement around spaceflight life sciences and health would not be possible without the hard work of this community. Special thanks to the commercial crew, commercial researchers and international space agencies who collaborate and leverage OSDR for their datasets. We would like to thank all members of the OSDR team for their dedication, support and passion.

## Contributor Information

Samrawit G Gebre,
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA.

Ryan T Scott,
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA.

Amanda M Saravia-Butler,
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA.

Danielle K Lopez,
KBR, Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA.

Lauren M Sanders,
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA.

Sylvain V Costes,
Space Biosciences Division, NASA Ames Research Center, Moffett Field, CA 94035, USA.

## Data availability

All data are available on the NASA Open Science Data Repository: <https://www.nasa.gov/osdr/>.

## Funding

NASA Space Biology Program, part of the NASA Biological and Physical Sciences Division within the NASA Science Mission Directorate; NASA Human Research Program. Funding for open access: NASA.

*Conflict of interest statement*. None declared.

## References

* 1.
  Afshinnekoo E., Scott R.T., MacKay M.J., Pariset E., Cekanaviciute E., Barker R., Gilroy S., Hassane D., Smith S.M., Zwart S.R.et al..
  Fundamental biological features of spaceflight: advancing the field to enable deep-space exploration. Cell. 2020; 183:1162–1184.
   [[DOI](https://doi.org/10.1016/j.cell.2020.10.050)] [[PMC free article](/articles/PMC8441988/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33242416/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell&title=Fundamental%20biological%20features%20of%20spaceflight:%20advancing%20the%20field%20to%20enable%20deep-space%20exploration&volume=183&publication_year=2020&pages=1162-1184&pmid=33242416&doi=10.1016/j.cell.2020.10.050&)]
* 2.
  Blaber E., Boothby T., Carr C.E., Craig Everroad R., Foster J., Galazka J., Lee J.A., Lera M., Ricco A., Sanders L.et al..
  Space biology beyond LEO instrumentation & science series science working group 2022 annual report. NASA Techn. Rep. Server. 2023; 20230008417. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NASA%20Techn.%20Rep.%20Server&title=Space%20biology%20beyond%20LEO%20instrumentation%20&%20science%20series%20science%20working%20group%202022%20annual%20report&publication_year=2023&pages=20230008417&)]
* 3.
  National Academies of Sciences, Engineering, and Medicine; Division on Engineering and Physical Sciences; Aeronautics and Space Engineering Board; Space Studies Board; Committee on Biological and Physical Sciences Research in Space 2023–2032
  Thriving in Space: Ensuring the Future of Biological and Physical Sciences Research: A Decadal Survey for 2023-2032. 2023; Washington (DC).National Academies Press(US). [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38289988/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Thriving%20in%20Space:%20Ensuring%20the%20Future%20of%20Biological%20and%20Physical%20Sciences%20Research:%20A%20Decadal%20Survey%20for%202023-2032&publication_year=2023&)]
* 4.
  Scott R.T., Sanders L.M., Antonsen E.L., Hastings J.J.A., Park S.-M., Mackintosh G., Reynolds R.J., Hoarfrost A.L., Sawyer A., Greene C.S.et al..
  Biomonitoring and precision health in deep space supported by artificial intelligence. Nat. Mach. Intell. 2023; 5:196–207. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Mach.%20Intell.&title=Biomonitoring%20and%20precision%20health%20in%20deep%20space%20supported%20by%20artificial%20intelligence&volume=5&publication_year=2023&pages=196-207&)]
* 5.
  Wilkinson M.D., Dumontier M., Aalbersberg I.J.J., Appleton G., Axton M., Baak A., Blomberg N., Boiten J.-W., da Silva Santos L.B., Bourne P.E.et al..
  The FAIR Guiding Principles for scientific data management and stewardship. Sci. Data. 2016; 3:160018.
   [[DOI](https://doi.org/10.1038/sdata.2016.18)] [[PMC free article](/articles/PMC4792175/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26978244/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Data&title=The%20FAIR%20Guiding%20Principles%20for%20scientific%20data%20management%20and%20stewardship&volume=3&publication_year=2016&pages=160018&pmid=26978244&doi=10.1038/sdata.2016.18&)]
* 6.
  Stall S., Yarmey L., Cutcher-Gershenfeld J., Hanson B., Lehnert K., Nosek B., Parsons M., Robinson E., Wyborn L..
  Make scientific data FAIR. Nature. 2019; 570:27–29.
   [[DOI](https://doi.org/10.1038/d41586-019-01720-7)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31164768/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature&title=Make%20scientific%20data%20FAIR&volume=570&publication_year=2019&pages=27-29&pmid=31164768&doi=10.1038/d41586-019-01720-7&)]
* 7.
  Higman R., Bangert D., Jones S..
  Three camps, one destination: the intersections of research data management, FAIR and Open. Insights Imaging. 2019; 32:1–9. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Insights%20Imaging&title=Three%20camps,%20one%20destination:%20the%20intersections%20of%20research%20data%20management,%20FAIR%20and%20Open&volume=32&publication_year=2019&pages=1-9&)]
* 8.
  Berrios D.C., Galazka J., Grigorev K., Gebre S., Costes S.V..
  NASA GeneLab: interfaces for the exploration of space omics data. Nucleic Acids Res. 2021; 49:D1515–D1522.
   [[DOI](https://doi.org/10.1093/nar/gkaa887)] [[PMC free article](/articles/PMC7778922/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33080015/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=NASA%20GeneLab:%20interfaces%20for%20the%20exploration%20of%20space%20omics%20data&volume=49&publication_year=2021&pages=D1515-D1522&pmid=33080015&doi=10.1093/nar/gkaa887&)]
* 9.
  da Silveira W.A., Fazelinia H., Rosenthal S.B., Laiakis E.C., Kim M.S., Meydan C., Kidane Y., Rathi K.S., Smith S.M., Stear B.et al..
  Comprehensive multi-omics analysis reveals mitochondrial stress as a central biological hub for spaceflight impact. Cell. 2020; 183:1185–1201.
   [[DOI](https://doi.org/10.1016/j.cell.2020.11.002)] [[PMC free article](/articles/PMC7870178/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33242417/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell&title=Comprehensive%20multi-omics%20analysis%20reveals%20mitochondrial%20stress%20as%20a%20central%20biological%20hub%20for%20spaceflight%20impact&volume=183&publication_year=2020&pages=1185-1201&pmid=33242417&doi=10.1016/j.cell.2020.11.002&)]
* 10.
  Sanders L.M., Grigorev K.A., Scott R.T., Saravia-Butler A.M., Polo S.-H.L., Gilbert R., Overbey E.G., Kim J., Mason C.E., Costes S.V..
  Inspiration4 data access through the NASA Open Science Data Repository. NPJ Microgravity. 2024; 10:56.
   [[DOI](https://doi.org/10.1038/s41526-024-00393-5)] [[PMC free article](/articles/PMC11094041/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38744887/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=Inspiration4%20data%20access%20through%20the%20NASA%20Open%20Science%20Data%20Repository&volume=10&publication_year=2024&pages=56&pmid=38744887&doi=10.1038/s41526-024-00393-5&)]
* 11.
  Siew K., Nestler K.A., Nelson C., D’Ambrosio V., Zhong C., Li Z., Grillo A., Wan E.R., Patel V., Overbey E.et al..
  Cosmic kidney disease: an integrated pan-omic, physiological and morphological study into spaceflight-induced renal dysfunction. Nat. Commun. 2024; 15:4923.
   [[DOI](https://doi.org/10.1038/s41467-024-49212-1)] [[PMC free article](/articles/PMC11167060/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862484/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Commun.&title=Cosmic%20kidney%20disease:%20an%20integrated%20pan-omic,%20physiological%20and%20morphological%20study%20into%20spaceflight-induced%20renal%20dysfunction&volume=15&publication_year=2024&pages=4923&pmid=38862484&doi=10.1038/s41467-024-49212-1&)]
* 12.
  Mathyk B.A., Tabetah M., Karim R., Zaksas V., Kim J., Anu R.I., Muratani M., Tasoula A., Singh R.S., Chen Y.-K.et al..
  Spaceflight induces changes in gene expression profiles linked to insulin and estrogen. Commun. Biol. 2024; 7:692.
   [[DOI](https://doi.org/10.1038/s42003-023-05213-2)] [[PMC free article](/articles/PMC11166981/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862620/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Commun.%20Biol.&title=Spaceflight%20induces%20changes%20in%20gene%20expression%20profiles%20linked%20to%20insulin%20and%20estrogen&volume=7&publication_year=2024&pages=692&pmid=38862620&doi=10.1038/s42003-023-05213-2&)]
* 13.
  Beheshti A., Cekanaviciute E., Smith D.J., Costes S.V..
  Global transcriptomic analysis suggests carbon dioxide as an environmental stressor in spaceflight: a systems biology GeneLab case study. Sci. Rep. 2018; 8:4191.
   [[DOI](https://doi.org/10.1038/s41598-018-22613-1)] [[PMC free article](/articles/PMC5843582/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29520055/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Global%20transcriptomic%20analysis%20suggests%20carbon%20dioxide%20as%20an%20environmental%20stressor%20in%20spaceflight:%20a%20systems%20biology%20GeneLab%20case%20study&volume=8&publication_year=2018&pages=4191&pmid=29520055&doi=10.1038/s41598-018-22613-1&)]
* 14.
  Cope H., Elsborg J., Demharter S., McDonald J.T., Wernecke C., Parthasarathy H., Unadkat H., Chatrathi M., Claudio J., Reinsch S.et al..
  Transcriptomics analysis reveals molecular alterations underpinning spaceflight dermatology. Commun. Med. 2024; 4:106.
   [[DOI](https://doi.org/10.1038/s43856-024-00532-9)] [[PMC free article](/articles/PMC11166967/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862781/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Commun.%20Med.&title=Transcriptomics%20analysis%20reveals%20molecular%20alterations%20underpinning%20spaceflight%20dermatology&volume=4&publication_year=2024&pages=106&pmid=38862781&doi=10.1038/s43856-024-00532-9&)]
* 15.
  Beheshti A., Chakravarty K., Fogle H., Fazelinia H., Silveira W.A.d., Boyko V., Polo S.-H.L., Saravia-Butler A.M., Hardiman G., Taylor D.et al..
  Multi-omics analysis of multiple missions to space reveal a theme of lipid dysregulation in mouse liver. Sci. Rep. 2019; 9:19195.
   [[DOI](https://doi.org/10.1038/s41598-019-55869-2)] [[PMC free article](/articles/PMC6915713/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31844325/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Multi-omics%20analysis%20of%20multiple%20missions%20to%20space%20reveal%20a%20theme%20of%20lipid%20dysregulation%20in%20mouse%20liver&volume=9&publication_year=2019&pages=19195&pmid=31844325&doi=10.1038/s41598-019-55869-2&)]
* 16.
  Jiang P., Green S.J., Chlipala G.E., Turek F.W., Vitaterna M.H..
  Reproducible changes in the gut microbiome suggest a shift in microbial and host metabolism during spaceflight. Microbiome. 2019; 7:113.
   [[DOI](https://doi.org/10.1186/s40168-019-0724-4)] [[PMC free article](/articles/PMC6689164/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31399081/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microbiome&title=Reproducible%20changes%20in%20the%20gut%20microbiome%20suggest%20a%20shift%20in%20microbial%20and%20host%20metabolism%20during%20spaceflight&volume=7&publication_year=2019&pages=113&pmid=31399081&doi=10.1186/s40168-019-0724-4&)]
* 17.
  Scott R.T., Grigorev K., Mackintosh G., Gebre S.G., Mason C.E., Del Alto M.E., Costes S.V..
  Advancing the Integration of Biosciences Data Sharing to Further Enable Space Exploration. Cell Rep. 2020; 33:108441.
   [[DOI](https://doi.org/10.1016/j.celrep.2020.108441)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33242404/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Rep.&title=Advancing%20the%20Integration%20of%20Biosciences%20Data%20Sharing%20to%20Further%20Enable%20Space%20Exploration&volume=33&publication_year=2020&pages=108441&pmid=33242404&doi=10.1016/j.celrep.2020.108441&)]
* 18.
  Costes S., Gentemann C., Platts S.H., Carnell L.A..
  Biological horizons: pioneering open science in the cosmos. Nat. Commun. 2024; 15:4780.
   [[DOI](https://doi.org/10.1038/s41467-024-48633-2)] [[PMC free article](/articles/PMC11167097/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862512/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Commun.&title=Biological%20horizons:%20pioneering%20open%20science%20in%20the%20cosmos&volume=15&publication_year=2024&pages=4780&pmid=38862512&doi=10.1038/s41467-024-48633-2&)]
* 19.
  Sansone S.-A., Rocca-Serra P., Brandizi M., Brazma A., Field D., Fostel J., Garrow A.G., Gilbert J., Goodsaid F., Hardy N.et al..
  The first RSBI (ISA-TAB) Workshop: ‘Can a Simple Format Work for Complex Studies?’. OMICS. 2008; 12:143–149.
   [[DOI](https://doi.org/10.1089/omi.2008.0019)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18447634/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=OMICS&title=The%20first%20RSBI%20(ISA-TAB)%20Workshop:%20%E2%80%98Can%20a%20Simple%20Format%20Work%20for%20Complex%20Studies?%E2%80%99&volume=12&publication_year=2008&pages=143-149&pmid=18447634&doi=10.1089/omi.2008.0019&)]
* 20.
  González-Beltrán A., Maguire E., Sansone S.-A., Rocca-Serra P..
  linkedISA: semantic representation of ISA-Tab experimental metadata. BMC Bioinf. 2014; 15:1–15. [[DOI](https://doi.org/10.1186/1471-2105-15-S14-S4)] [[PMC free article](/articles/PMC4255742/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25472428/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Bioinf.&title=linkedISA:%20semantic%20representation%20of%20ISA-Tab%20experimental%20metadata&volume=15&publication_year=2014&pages=1-15&pmid=25472428&doi=10.1186/1471-2105-15-S14-S4&)]
* 21.
  Tryka K.A., Hao L., Sturcke A., Jin Y., Wang Z.Y., Ziyabari L., Lee M., Popova N., Sharopova N., Kimura M.et al..
  NCBI’s database of genotypes and phenotypes: dbGaP. Nucleic Acids Res. 2014; 42:D975–D979.
   [[DOI](https://doi.org/10.1093/nar/gkt1211)] [[PMC free article](/articles/PMC3965052/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24297256/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=NCBI%E2%80%99s%20database%20of%20genotypes%20and%20phenotypes:%20dbGaP&volume=42&publication_year=2014&pages=D975-D979&pmid=24297256&doi=10.1093/nar/gkt1211&)]
* 22.
  Rahimzadeh V., Fogarty J., Caulfield T., Auñón-Chancellor S., Borry P., Candia J., Cohen I.G., Covington M., Lynch H.F., Greely H.T.et al..
  Ethically cleared to launch?. Science. 2023; 381:1408–1411.
   [[DOI](https://doi.org/10.1126/science.adh9028)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/37769066/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Science&title=Ethically%20cleared%20to%20launch?&volume=381&publication_year=2023&pages=1408-1411&pmid=37769066&doi=10.1126/science.adh9028&)]
* 23.
  Seylani A., Galsinh A.S., Tasoula A., I A.R., Camera A., Calleja-Agius J., Borg J., Goel C., Kim J., Clark K.B.et al..
  Ethical considerations for the age of non-governmental space exploration. Nat. Commun. 2024; 15:4774.
   [[DOI](https://doi.org/10.1038/s41467-023-44357-x)] [[PMC free article](/articles/PMC11166968/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862473/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Commun.&title=Ethical%20considerations%20for%20the%20age%20of%20non-governmental%20space%20exploration&volume=15&publication_year=2024&pages=4774&pmid=38862473&doi=10.1038/s41467-023-44357-x&)]
* 24.
  Jones C.W., Overbey E.G., Lacombe J., Ecker A.J., Meydan C., Ryon K., Tierney B., Damle N., MacKay M., Afshin E.E.et al..
  Molecular and physiological changes in the SpaceX Inspiration4 civilian crew. Nature. 2024; 632:1155–1164.
   [[DOI](https://doi.org/10.1038/s41586-024-07648-x)] [[PMC free article](/articles/PMC11357997/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862026/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature&title=Molecular%20and%20physiological%20changes%20in%20the%20SpaceX%20Inspiration4%20civilian%20crew&volume=632&publication_year=2024&pages=1155-1164&pmid=38862026&doi=10.1038/s41586-024-07648-x&)]
* 25.
  Rutter L., Barker R., Bezdan D., Cope H., Costes S.V., Degoricija L., Fisch K.M., Gabitto M.I., Gebre S., Giacomello S.et al..
  A new era for space life science: international standards for space omics processing. Patterns (N Y). 2020; 1:100148.
   [[DOI](https://doi.org/10.1016/j.patter.2020.100148)] [[PMC free article](/articles/PMC7733874/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33336201/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Patterns%20(N%20Y)&title=A%20new%20era%20for%20space%20life%20science:%20international%20standards%20for%20space%20omics%20processing&volume=1&publication_year=2020&pages=100148&pmid=33336201&doi=10.1016/j.patter.2020.100148&)]
* 26.
  Camera A., Tabetah M., Castañeda V., Kim J., Galsinh A.S., Haro-Vinueza A., Salinas I., Seylani A., Arif S., Das S.et al..
  Aging and putative frailty biomarkers are altered by spaceflight. Sci. Rep. 2024; 14:13098.
   [[DOI](https://doi.org/10.1038/s41598-024-57948-5)] [[PMC free article](/articles/PMC11166946/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862573/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Aging%20and%20putative%20frailty%20biomarkers%20are%20altered%20by%20spaceflight&volume=14&publication_year=2024&pages=13098&pmid=38862573&doi=10.1038/s41598-024-57948-5&)]
* 27.
  Vitry G., Finch R., Mcstay G., Behesti A., Déjean S., Larose T., Wotring V., da Silveira W.A..
  Muscle atrophy phenotype gene expression during spaceflight is linked to a metabolic crosstalk in both the liver and the muscle in mice. iScience. 2022; 25:105213.
   [[DOI](https://doi.org/10.1016/j.isci.2022.105213)] [[PMC free article](/articles/PMC9576569/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36267920/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=iScience&title=Muscle%20atrophy%20phenotype%20gene%20expression%20during%20spaceflight%20is%20linked%20to%20a%20metabolic%20crosstalk%20in%20both%20the%20liver%20and%20the%20muscle%20in%20mice&volume=25&publication_year=2022&pages=105213&pmid=36267920&doi=10.1016/j.isci.2022.105213&)]
* 28.
  Li K., Desai R., Scott R.T., Steele J.R., Machado M., Demharter S., Hoarfrost A., Braun J.L., Fajardo V.A., Sanders L.M.et al..
  Explainable machine learning identifies multi-omics signatures of muscle response to spaceflight in mice. NPJ Microgravity. 2023; 9:90.
   [[DOI](https://doi.org/10.1038/s41526-023-00337-5)] [[PMC free article](/articles/PMC10719374/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38092777/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NPJ%20Microgravity&title=Explainable%20machine%20learning%20identifies%20multi-omics%20signatures%20of%20muscle%20response%20to%20spaceflight%20in%20mice&volume=9&publication_year=2023&pages=90&pmid=38092777&doi=10.1038/s41526-023-00337-5&)]
* 29.
  Sanders L.M., Chok H., Samson F., Acuna A.U., Polo S.-H.L., Boyko V., Chen Y.-C., Dinh M., Gebre S., Galazka J.M.et al..
  Batch effect correction methods for NASA GeneLab transcriptomic datasets. Front. Astron. Space Sci. 2023; 10:1200132. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Astron.%20Space%20Sci.&title=Batch%20effect%20correction%20methods%20for%20NASA%20GeneLab%20transcriptomic%20datasets&volume=10&publication_year=2023&pages=1200132&)]
* 30.
  Reynolds R.J., Scott R.T., Turner R.T., Iwaniec U.T., Bouxsein M.L., Sanders L.M., Antonsen E.L..
  Validating causal diagrams of human health risks for spaceflight: An example using bone data from rodents. Biomedicines. 2022; 10:2187.
   [[DOI](https://doi.org/10.3390/biomedicines10092187)] [[PMC free article](/articles/PMC9496259/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36140288/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Biomedicines&title=Validating%20causal%20diagrams%20of%20human%20health%20risks%20for%20spaceflight:%20An%20example%20using%20bone%20data%20from%20rodents&volume=10&publication_year=2022&pages=2187&pmid=36140288&doi=10.3390/biomedicines10092187&)]
* 31.
  Keenum I., Player R., Kralj J., Servetas S., Sussman M.D., Russell J.A., Stone J., Chandrapati S., Sozhamannan S..
  Amplicon sequencing minimal information (ASqMI): quality and reporting guidelines for actionable calls in biodefense applications. J. AOAC Int. 2023; 106:1424–1430.
   [[DOI](https://doi.org/10.1093/jaoacint/qsad047)] [[PMC free article](/articles/PMC10472743/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/37067472/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20AOAC%20Int.&title=Amplicon%20sequencing%20minimal%20information%20(ASqMI):%20quality%20and%20reporting%20guidelines%20for%20actionable%20calls%20in%20biodefense%20applications&volume=106&publication_year=2023&pages=1424-1430&pmid=37067472&doi=10.1093/jaoacint/qsad047&)]
* 32.
  Rule C.S., Patrick M., Sandkvist M..
  Measuring in vitro ATPase activity for enzymatic characterization. J. Vis. Exp. 2016; 114:e54305. [[DOI](https://doi.org/10.3791/54305)] [[PMC free article](/articles/PMC5091952/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27584824/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Measuring%20in%20vitro%20ATPase%20activity%20for%20enzymatic%20characterization&volume=114&publication_year=2016&pages=e54305&pmid=27584824&doi=10.3791/54305&)]
* 33.
  Dorman C.W., Krug H.E., Frizelle S.P., Funkenbusch S., Mahowald M.L..
  A comparison of DigiGaitTM and TreadScanTM imaging systems: assessment of pain using gait analysis in murine monoarthritis. J. Pain Res. 2014; 7:25–35.
   [[DOI](https://doi.org/10.2147/JPR.S52195)] [[PMC free article](/articles/PMC3883276/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24516338/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Pain%20Res.&title=A%20comparison%20of%20DigiGaitTM%20and%20TreadScanTM%20imaging%20systems:%20assessment%20of%20pain%20using%20gait%20analysis%20in%20murine%20monoarthritis&volume=7&publication_year=2014&pages=25-35&pmid=24516338&doi=10.2147/JPR.S52195&)]
* 34.
  Seibenhener M.L., Wooten M.C..
  Use of the Open Field Maze to measure locomotor and anxiety-like behavior in mice. J. Vis. Exp. 2015; 96:e52434. [[DOI](https://doi.org/10.3791/52434)] [[PMC free article](/articles/PMC4354627/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25742564/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Use%20of%20the%20Open%20Field%20Maze%20to%20measure%20locomotor%20and%20anxiety-like%20behavior%20in%20mice&volume=96&publication_year=2015&pages=e52434&pmid=25742564&doi=10.3791/52434&)]
* 35.
  Huang H., Jiang N., Zhang Y.W., Lv J.W., Wang H.X., Lu C., Liu X.M., Lu G.H..
  Gastrodia elata blume ameliorates circadian rhythm disorder-induced mice memory impairment. Life Sci. Space Res. 2021; 31:51–58. [[DOI](https://doi.org/10.1016/j.lssr.2021.07.004)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34689950/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Life%20Sci.%20Space%20Res.&title=Gastrodia%20elata%20blume%20ameliorates%20circadian%20rhythm%20disorder-induced%20mice%20memory%20impairment&volume=31&publication_year=2021&pages=51-58&pmid=34689950&doi=10.1016/j.lssr.2021.07.004&)]
* 36.
  Penley S.C., Gaudet C.M., Threlkeld S.W..
  Use of an eight-arm radial water maze to assess working and reference memory following neonatal brain injury. J. Vis. Exp. 2013; 82:e50940. [[DOI](https://doi.org/10.3791/50940)] [[PMC free article](/articles/PMC4030456/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24335781/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Use%20of%20an%20eight-arm%20radial%20water%20maze%20to%20assess%20working%20and%20reference%20memory%20following%20neonatal%20brain%20injury&volume=82&publication_year=2013&pages=e50940&pmid=24335781&doi=10.3791/50940&)]
* 37.
  Field D., Garrity G., Gray T., Morrison N., Selengut J., Sterk P., Tatusova T., Thomson N., Allen M.J., Angiuoli S.V.et al..
  The minimum information about a genome sequence (MIGS) specification. Nat. Biotechnol. 2008; 26:541–547.
   [[DOI](https://doi.org/10.1038/nbt1360)] [[PMC free article](/articles/PMC2409278/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18464787/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=The%20minimum%20information%20about%20a%20genome%20sequence%20(MIGS)%20specification&volume=26&publication_year=2008&pages=541-547&pmid=18464787&doi=10.1038/nbt1360&)]
* 38.
  Yilmaz P., Kottmann R., Field D., Knight R., Cole J.R., Amaral-Zettler L., Gilbert J.A., Karsch-Mizrachi I., Johnston A., Cochrane G.et al..
  Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications. Nat. Biotechnol. 2011; 29:415–420.
   [[DOI](https://doi.org/10.1038/nbt.1823)] [[PMC free article](/articles/PMC3367316/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21552244/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=Minimum%20information%20about%20a%20marker%20gene%20sequence%20(MIMARKS)%20and%20minimum%20information%20about%20any%20(x)%20sequence%20(MIxS)%20specifications&volume=29&publication_year=2011&pages=415-420&pmid=21552244&doi=10.1038/nbt.1823&)]
* 39.
  Britten R.A., Duncan V.D., Fesshaye A., Rudobeck E., Nelson G.A., Vlkolinsky R..
  Altered cognitive flexibility and synaptic plasticity in the rat prefrontal cortex after exposure to low (≤15 cGy) doses of 28Si radiation. Radiat. Res. 2020; 193:223–235.
   [[DOI](https://doi.org/10.1667/RR15458.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32011211/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Altered%20cognitive%20flexibility%20and%20synaptic%20plasticity%20in%20the%20rat%20prefrontal%20cortex%20after%20exposure%20to%20low%20(%E2%89%A415%20cGy)%20doses%20of%2028Si%20radiation&volume=193&publication_year=2020&pages=223-235&pmid=32011211&doi=10.1667/RR15458.1&)]
* 40.
  Lueptow L.M.
  Novel object recognition test for the investigation of learning and memory in mice. J. Vis. Exp. 2017; 126:e55718. [[DOI](https://doi.org/10.3791/55718)] [[PMC free article](/articles/PMC5614391/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28892027/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Novel%20object%20recognition%20test%20for%20the%20investigation%20of%20learning%20and%20memory%20in%20mice&volume=126&publication_year=2017&pages=e55718&pmid=28892027&doi=10.3791/55718&)]
* 41.
  Bowers R.M., Kyrpides N.C., Stepanauskas R., Harmon-Smith M., Doud D., Reddy T.B.K., Schulz F., Jarett J., Rivers A.R., Eloe-Fadrosh E.A.et al..
  Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea. Nat. Biotechnol. 2017; 35:725–731.
   [[DOI](https://doi.org/10.1038/nbt.3893)] [[PMC free article](/articles/PMC6436528/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28787424/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=Minimum%20information%20about%20a%20single%20amplified%20genome%20(MISAG)%20and%20a%20metagenome-assembled%20genome%20(MIMAG)%20of%20bacteria%20and%20archaea&volume=35&publication_year=2017&pages=725-731&pmid=28787424&doi=10.1038/nbt.3893&)]
* 42.
  Komada M., Takao K., Miyakawa T..
  Elevated plus maze for mice. J. Vis. Exp. 2008; 22:e1088. [[DOI](https://doi.org/10.3791/1088)] [[PMC free article](/articles/PMC2762911/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19229173/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Elevated%20plus%20maze%20for%20mice&volume=22&publication_year=2008&pages=e1088&pmid=19229173&doi=10.3791/1088&)]
* 43.
  Walf A.A., Frye C.A..
  The use of the elevated plus maze as an assay of anxiety-related behavior in rodents. Nat. Protoc. 2007; 2:322–328.
   [[DOI](https://doi.org/10.1038/nprot.2007.44)] [[PMC free article](/articles/PMC3623971/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17406592/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Protoc.&title=The%20use%20of%20the%20elevated%20plus%20maze%20as%20an%20assay%20of%20anxiety-related%20behavior%20in%20rodents&volume=2&publication_year=2007&pages=322-328&pmid=17406592&doi=10.1038/nprot.2007.44&)]
* 44.
  Tait D.S., Bowman E.M., Neuwirth L.S., Brown V.J..
  Assessment of intradimensional/extradimensional attentional set-shifting in rats. Neurosci. Biobehav. Rev. 2018; 89:72–84.
   [[DOI](https://doi.org/10.1016/j.neubiorev.2018.02.013)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29474818/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Neurosci.%20Biobehav.%20Rev.&title=Assessment%20of%20intradimensional/extradimensional%20attentional%20set-shifting%20in%20rats&volume=89&publication_year=2018&pages=72-84&pmid=29474818&doi=10.1016/j.neubiorev.2018.02.013&)]
* 45.
  Jewell J.S., Duncan V.D., Fesshaye A., Tondin A., Macadat E., Britten R.A..
  Exposure to ≤15 cGy of 600 MeV/n 56Fe particles impairs rule acquisition but not long-term memory in the attentional set-shifting assay. Radiat. Res. 2018; 190:565–575.
   [[DOI](https://doi.org/10.1667/RR15085.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30407900/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Exposure%20to%20%E2%89%A415%20cGy%20of%20600%20MeV/n%2056Fe%20particles%20impairs%20rule%20acquisition%20but%20not%20long-term%20memory%20in%20the%20attentional%20set-shifting%20assay&volume=190&publication_year=2018&pages=565-575&pmid=30407900&doi=10.1667/RR15085.1&)]
* 46.
  Brazma A., Hingamp P., Quackenbush J., Sherlock G., Spellman P., Stoeckert C., Aach J., Ansorge W., Ball C.A., Causton H.C.et al..
  Minimum information about a microarray experiment (MIAME)-toward standards for microarray data. Nat. Genet. 2001; 29:365–371.
   [[DOI](https://doi.org/10.1038/ng1201-365)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11726920/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Genet.&title=Minimum%20information%20about%20a%20microarray%20experiment%20(MIAME)-toward%20standards%20for%20microarray%20data&volume=29&publication_year=2001&pages=365-371&pmid=11726920&doi=10.1038/ng1201-365&)]
* 47.
  Barnes C.A., Jung M.W., McNaughton B.L., Korol D.L., Andreasson K., Worley P.F..
  LTP saturation and spatial learning disruption: effects of task variables and saturation levels. J. Neurosci. 1994; 14:5793–5806.
   [[DOI](https://doi.org/10.1523/JNEUROSCI.14-10-05793.1994)] [[PMC free article](/articles/PMC6576980/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/7931545/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Neurosci.&title=LTP%20saturation%20and%20spatial%20learning%20disruption:%20effects%20of%20task%20variables%20and%20saturation%20levels&volume=14&publication_year=1994&pages=5793-5806&pmid=7931545&doi=10.1523/JNEUROSCI.14-10-05793.1994&)]
* 48.
  Kaidanovich-Beilin O., Lipina T., Vukobradovic I., Roder J., Woodgett J.R..
  Assessment of social interaction behaviors. J. Vis. Exp. 2011; 48:e2473. [[DOI](https://doi.org/10.3791/2473)] [[PMC free article](/articles/PMC3197404/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21403628/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Assessment%20of%20social%20interaction%20behaviors&volume=48&publication_year=2011&pages=e2473&pmid=21403628&doi=10.3791/2473&)]
* 49.
  Kolesnikov N., Hastings E., Keays M., Melnichuk O., Tang Y.A., Williams E., Dylag M., Kurbatova N., Brandizi M., Burdett T.et al..
  ArrayExpress update–simplifying data submissions. Nucleic Acids Res. 2015; 43:D1113–D1116.
   [[DOI](https://doi.org/10.1093/nar/gku1057)] [[PMC free article](/articles/PMC4383899/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25361974/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=ArrayExpress%20update%E2%80%93simplifying%20data%20submissions&volume=43&publication_year=2015&pages=D1113-D1116&pmid=25361974&doi=10.1093/nar/gku1057&)]
* 50.
  Le Bourg E., Lints F.A..
  Hypergravity and aging in Drosophila melanogaster. 4. Climbing activity. Gerontology. 1992; 38:59–64.
   [[DOI](https://doi.org/10.1159/000213307)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/1612462/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Gerontology&title=Hypergravity%20and%20aging%20in%20Drosophila%20melanogaster.%204.%20Climbing%20activity&volume=38&publication_year=1992&pages=59-64&pmid=1612462&doi=10.1159/000213307&)]
* 51.
  Mhatre S.D., Iyer J., Petereit J., Dolling-Boreham R.M., Tyryshkina A., Paul A.M., Gilbert R., Jensen M., Woolsey R.J., Anand S.et al..
  Artificial gravity partially protects space-induced neurological deficits in Drosophila melanogaster. Cell Rep. 2022; 40:111279.
   [[DOI](https://doi.org/10.1016/j.celrep.2022.111279)] [[PMC free article](/articles/PMC10503492/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36070701/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell%20Rep.&title=Artificial%20gravity%20partially%20protects%20space-induced%20neurological%20deficits%20in%20Drosophila%20melanogaster&volume=40&publication_year=2022&pages=111279&pmid=36070701&doi=10.1016/j.celrep.2022.111279&)]
* 52.
  Füllgrabe A., George N., Green M., Nejad P., Aronow B., Fexova S.K., Fischer C., Freeberg M.A., Huerta L., Morrison N.et al..
  Guidelines for reporting single-cell RNA-seq experiments. Nat. Biotechnol. 2020; 38:1384–1386.
   [[DOI](https://doi.org/10.1038/s41587-020-00744-z)] [[PMC free article](/articles/PMC9302581/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33188371/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=Guidelines%20for%20reporting%20single-cell%20RNA-seq%20experiments&volume=38&publication_year=2020&pages=1384-1386&pmid=33188371&doi=10.1038/s41587-020-00744-z&)]
* 53.
  Rabin B.M., Miller M.G., Larsen A., Spadafora C., Zolnerowich N.N., Dell’Acqua L.A., Shukitt-Hale B..
  Effects of exposure to 12C and 4He particles on cognitive performance of intact and ovariectomized female rats. Life Sci. Space Res. 2019; 22:47–54. [[DOI](https://doi.org/10.1016/j.lssr.2019.07.005)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31421848/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Life%20Sci.%20Space%20Res.&title=Effects%20of%20exposure%20to%2012C%20and%204He%20particles%20on%20cognitive%20performance%20of%20intact%20and%20ovariectomized%20female%20rats&volume=22&publication_year=2019&pages=47-54&pmid=31421848&doi=10.1016/j.lssr.2019.07.005&)]
* 54.
  Denninger J.K., Smith B.M., Kirby E.D..
  Novel object recognition and object location behavioral testing in mice on a budget. J. Vis. Exp. 2018; 141:e58593. [[DOI](https://doi.org/10.3791/58593)] [[PMC free article](/articles/PMC6800058/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30531711/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Novel%20object%20recognition%20and%20object%20location%20behavioral%20testing%20in%20mice%20on%20a%20budget&volume=141&publication_year=2018&pages=e58593&pmid=30531711&doi=10.3791/58593&)]
* 55.
  Feng Q., Ma Y., Mu S., Wu J., Chen S., Ouyang L., Lei W..
  Specific reactions of different striatal neuron types in morphology induced by quinolinic acid in rats. PLoS One. 2014; 9:e91512.
   [[DOI](https://doi.org/10.1371/journal.pone.0091512)] [[PMC free article](/articles/PMC3954627/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24632560/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Specific%20reactions%20of%20different%20striatal%20neuron%20types%20in%20morphology%20induced%20by%20quinolinic%20acid%20in%20rats&volume=9&publication_year=2014&pages=e91512&pmid=24632560&doi=10.1371/journal.pone.0091512&)]
* 56.
  Deacon R.M.J.
  Assessing nest building in mice. Nat. Protoc. 2006; 1:1117–1119.
   [[DOI](https://doi.org/10.1038/nprot.2006.170)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17406392/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Protoc.&title=Assessing%20nest%20building%20in%20mice&volume=1&publication_year=2006&pages=1117-1119&pmid=17406392&doi=10.1038/nprot.2006.170&)]
* 57.
  Jepsen K.J., Silva M.J., Vashishth D., Guo X.E., van der Meulen M.C.H..
  Establishing biomechanical mechanisms in mouse models: practical guidelines for systematically evaluating phenotypic changes in the diaphyses of long bones. J. Bone Miner. Res. 2015; 30:951–966.
   [[DOI](https://doi.org/10.1002/jbmr.2539)] [[PMC free article](/articles/PMC4794979/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25917136/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Bone%20Miner.%20Res.&title=Establishing%20biomechanical%20mechanisms%20in%20mouse%20models:%20practical%20guidelines%20for%20systematically%20evaluating%20phenotypic%20changes%20in%20the%20diaphyses%20of%20long%20bones&volume=30&publication_year=2015&pages=951-966&pmid=25917136&doi=10.1002/jbmr.2539&)]
* 58.
  Bouxsein M.L., Boyd S.K., Christiansen B.A., Guldberg R.E., Jepsen K.J., Müller R..
  Guidelines for assessment of bone microstructure in rodents using micro-computed tomography. J. Bone Miner. Res. 2010; 25:1468–1486.
   [[DOI](https://doi.org/10.1002/jbmr.141)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20533309/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Bone%20Miner.%20Res.&title=Guidelines%20for%20assessment%20of%20bone%20microstructure%20in%20rodents%20using%20micro-computed%20tomography&volume=25&publication_year=2010&pages=1468-1486&pmid=20533309&doi=10.1002/jbmr.141&)]
* 59.
  Nagy T.R., Clair A.L..
  Precision and accuracy of dual-energy X-ray absorptiometry for determining in vivo body composition of mice. Obes. Res. 2000; 8:392–398.
   [[DOI](https://doi.org/10.1038/oby.2000.47)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/10968731/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Obes.%20Res.&title=Precision%20and%20accuracy%20of%20dual-energy%20X-ray%20absorptiometry%20for%20determining%20in%20vivo%20body%20composition%20of%20mice&volume=8&publication_year=2000&pages=392-398&pmid=10968731&doi=10.1038/oby.2000.47&)]
* 60.
  Whittier D.E., Boyd S.K., Burghardt A.J., Paccou J., Ghasem-Zadeh A., Chapurlat R., Engelke K., Bouxsein M.L..
  Guidelines for the assessment of bone density and microarchitecture in vivo using high-resolution peripheral quantitative computed tomography. Osteoporos. Int. 2020; 31:1607–1627.
   [[DOI](https://doi.org/10.1007/s00198-020-05438-5)] [[PMC free article](/articles/PMC7429313/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32458029/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Osteoporos.%20Int.&title=Guidelines%20for%20the%20assessment%20of%20bone%20density%20and%20microarchitecture%20in%20vivo%20using%20high-resolution%20peripheral%20quantitative%20computed%20tomography&volume=31&publication_year=2020&pages=1607-1627&pmid=32458029&doi=10.1007/s00198-020-05438-5&)]
* 61.
  Taylor C.F., Paton N.W., Lilley K.S., Binz P.-A., Julian R.K. Jr, Jones A.R., Zhu W., Apweiler R., Aebersold R., Deutsch E.W.et al..
  The minimum information about a proteomics experiment (MIAPE). Nat. Biotechnol. 2007; 25:887–893.
   [[DOI](https://doi.org/10.1038/nbt1329)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17687369/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=The%20minimum%20information%20about%20a%20proteomics%20experiment%20(MIAPE)&volume=25&publication_year=2007&pages=887-893&pmid=17687369&doi=10.1038/nbt1329&)]
* 62.
  Tupling R., Green H..
  Silver ions induce Ca2+ release from the SR in vitro by acting on the Ca2+ release channel and the Ca2+ pump. J. Appl. Physiol. 2002; 92:1603–1610.
   [[DOI](https://doi.org/10.1152/japplphysiol.00756.2001)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11896027/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Appl.%20Physiol.&title=Silver%20ions%20induce%20Ca2+%20release%20from%20the%20SR%20in%20vitro%20by%20acting%20on%20the%20Ca2+%20release%20channel%20and%20the%20Ca2+%20pump&volume=92&publication_year=2002&pages=1603-1610&pmid=11896027&doi=10.1152/japplphysiol.00756.2001&)]
* 63.
  Wu J., Bu L., Gong H., Jiang G., Li L., Ma H., Zhou N., Lin L., Chen Z., Ye Y.et al..
  Effects of heart rate and anesthetic timing on high-resolution echocardiographic assessment under isoflurane anesthesia in mice. J. Ultrasound Med. 2010; 29:1771–1778.
   [[DOI](https://doi.org/10.7863/jum.2010.29.12.1771)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21098849/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Ultrasound%20Med.&title=Effects%20of%20heart%20rate%20and%20anesthetic%20timing%20on%20high-resolution%20echocardiographic%20assessment%20under%20isoflurane%20anesthesia%20in%20mice&volume=29&publication_year=2010&pages=1771-1778&pmid=21098849&doi=10.7863/jum.2010.29.12.1771&)]
* 64.
  McLean A.C., Valenzuela N., Fai S., Bennett S.A.L..
  Performing vaginal lavage, crystal violet staining, and vaginal cytological evaluation for mouse estrous cycle staging identification. J. Vis. Exp. 2012; 67:e4389. [[DOI](https://doi.org/10.3791/4389)] [[PMC free article](/articles/PMC3490233/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23007862/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp.&title=Performing%20vaginal%20lavage,%20crystal%20violet%20staining,%20and%20vaginal%20cytological%20evaluation%20for%20mouse%20estrous%20cycle%20staging%20identification&volume=67&publication_year=2012&pages=e4389&pmid=23007862&doi=10.3791/4389&)]
* 65.
  McKinnon K.M.
  Flow cytometry: an overview. Curr. Protoc. Immunol. 2018; 120:1–16. [[DOI](https://doi.org/10.1002/cpim.40)] [[PMC free article](/articles/PMC5939936/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29512141/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Protoc.%20Immunol.&title=Flow%20cytometry:%20an%20overview&volume=120&publication_year=2018&pages=1-16&pmid=29512141&doi=10.1002/cpim.40&)]
* 66.
  Robinson J.R., Denny J.C., Roden D.M., Van Driest S.L..
  Genome-wide and phenome-wide approaches to understand variable drug actions in electronic health records. Clin. Transl. Sci. 2018; 11:112–122.
   [[DOI](https://doi.org/10.1111/cts.12522)] [[PMC free article](/articles/PMC5866959/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29148204/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Clin.%20Transl.%20Sci.&title=Genome-wide%20and%20phenome-wide%20approaches%20to%20understand%20variable%20drug%20actions%20in%20electronic%20health%20records&volume=11&publication_year=2018&pages=112-122&pmid=29148204&doi=10.1111/cts.12522&)]
* 67.
  Dempster D.W., Compston J.E., Drezner M.K., Glorieux F.H., Kanis J.A., Malluche H., Meunier P.J., Ott S.M., Recker R.R., Parfitt A.M..
  Standardized nomenclature, symbols, and units for bone histomorphometry: a 2012 update of the report of the ASBMR Histomorphometry Nomenclature Committee. J. Bone Miner. Res. 2013; 28:2–17.
   [[DOI](https://doi.org/10.1002/jbmr.1805)] [[PMC free article](/articles/PMC3672237/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23197339/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Bone%20Miner.%20Res.&title=Standardized%20nomenclature,%20symbols,%20and%20units%20for%20bone%20histomorphometry:%20a%202012%20update%20of%20the%20report%20of%20the%20ASBMR%20Histomorphometry%20Nomenclature%20Committee&volume=28&publication_year=2013&pages=2-17&pmid=23197339&doi=10.1002/jbmr.1805&)]
* 68.
  Taheri M.L., Stach E.A., Arslan I., Crozier P.A., Kabius B.C., LaGrange T., Minor A.M., Takeda S., Tanase M., Wagner J.B.et al..
  Current status and future directions for in situ transmission electron microscopy. Ultramicroscopy. 2016; 170:86–95.
   [[DOI](https://doi.org/10.1016/j.ultramic.2016.08.007)] [[PMC free article](/articles/PMC5100813/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27566048/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ultramicroscopy&title=Current%20status%20and%20future%20directions%20for%20in%20situ%20transmission%20electron%20microscopy&volume=170&publication_year=2016&pages=86-95&pmid=27566048&doi=10.1016/j.ultramic.2016.08.007&)]
* 69.
  Golding C.G., Lamboo L.L., Beniac D.R., Booth T.F..
  The scanning electron microscope in microbiology and diagnosis of infectious disease. Sci. Rep. 2016; 6:26516.
   [[DOI](https://doi.org/10.1038/srep26516)] [[PMC free article](/articles/PMC4876401/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27212232/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=The%20scanning%20electron%20microscope%20in%20microbiology%20and%20diagnosis%20of%20infectious%20disease&volume=6&publication_year=2016&pages=26516&pmid=27212232&doi=10.1038/srep26516&)]
* 70.
  Gittings W., Bunda J., Stull J.T., Vandenboom R..
  Interaction of posttetanic potentiation and the catchlike property in mouse skeletal muscle. Muscle Nerve. 2016; 54:308–316.
   [[DOI](https://doi.org/10.1002/mus.25053)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26802366/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Muscle%20Nerve&title=Interaction%20of%20posttetanic%20potentiation%20and%20the%20catchlike%20property%20in%20mouse%20skeletal%20muscle&volume=54&publication_year=2016&pages=308-316&pmid=26802366&doi=10.1002/mus.25053&)]
* 71.
  Sobotka S., Mu L..
  Characteristics of tetanic force produced by the sternomastoid muscle of the rat. J. Biomed. Biotechnol. 2010; 2010:194984.
   [[DOI](https://doi.org/10.1155/2010/194984)] [[PMC free article](/articles/PMC2875700/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20508813/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Biomed.%20Biotechnol.&title=Characteristics%20of%20tetanic%20force%20produced%20by%20the%20sternomastoid%20muscle%20of%20the%20rat&volume=2010&publication_year=2010&pages=194984&pmid=20508813&doi=10.1155/2010/194984&)]
* 72.
  Takeshita H., Yamamoto K., Nozato S., Inagaki T., Tsuchimochi H., Shirai M., Yamamoto R., Imaizumi Y., Hongyo K., Yokoyama S.et al..
  Modified forelimb grip strength test detects aging-associated physiological decline in skeletal muscle function in male mice. Sci. Rep. 2017; 7:42323.
   [[DOI](https://doi.org/10.1038/srep42323)] [[PMC free article](/articles/PMC5296723/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28176863/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Modified%20forelimb%20grip%20strength%20test%20detects%20aging-associated%20physiological%20decline%20in%20skeletal%20muscle%20function%20in%20male%20mice&volume=7&publication_year=2017&pages=42323&pmid=28176863&doi=10.1038/srep42323&)]
* 73.
  Rose L.T., Moshegov C.N..
  Comparison of the Zeiss IOLMaster and applanation A-scan ultrasound: biometry for intraocular lens calculation. Clin. Exp. Ophthalmol. 2003; 31:121–124.
   [[DOI](https://doi.org/10.1046/j.1442-9071.2003.00617.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/12648044/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Clin.%20Exp.%20Ophthalmol.&title=Comparison%20of%20the%20Zeiss%20IOLMaster%20and%20applanation%20A-scan%20ultrasound:%20biometry%20for%20intraocular%20lens%20calculation&volume=31&publication_year=2003&pages=121-124&pmid=12648044&doi=10.1046/j.1442-9071.2003.00617.x&)]
* 74.
  Rahman W., Chen F.K., Yeoh J., Patel P., Tufail A., Da Cruz L..
  Repeatability of manual subfoveal choroidal thickness measurements in healthy subjects using the technique of enhanced depth imaging optical coherence tomography. Invest. Ophthalmol. Vis. Sci. 2011; 52:2267–2271.
   [[DOI](https://doi.org/10.1167/iovs.10-6024)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21087970/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Invest.%20Ophthalmol.%20Vis.%20Sci.&title=Repeatability%20of%20manual%20subfoveal%20choroidal%20thickness%20measurements%20in%20healthy%20subjects%20using%20the%20technique%20of%20enhanced%20depth%20imaging%20optical%20coherence%20tomography&volume=52&publication_year=2011&pages=2267-2271&pmid=21087970&doi=10.1167/iovs.10-6024&)]
* 75.
  Mahmood T., Yang P.-C..
  Western blot: technique, theory, and trouble shooting. N. Am. J. Med. Sci. 2012; 4:429–434.
   [[DOI](https://doi.org/10.4103/1947-2714.100998)] [[PMC free article](/articles/PMC3456489/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23050259/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=N.%20Am.%20J.%20Med.%20Sci.&title=Western%20blot:%20technique,%20theory,%20and%20trouble%20shooting&volume=4&publication_year=2012&pages=429-434&pmid=23050259&doi=10.4103/1947-2714.100998&)]
* 76.
  Grover V.P.B., Tognarelli J.M., Crossey M.M.E., Cox I.J., Taylor-Robinson S.D., McPhail M.J.W..
  Magnetic Resonance Imaging: Principles and Techniques: Lessons for Clinicians. J. Clin. Exp. Hepatol. 2015; 5:246–255.
   [[DOI](https://doi.org/10.1016/j.jceh.2015.08.001)] [[PMC free article](/articles/PMC4632105/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26628842/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Clin.%20Exp.%20Hepatol.&title=Magnetic%20Resonance%20Imaging:%20Principles%20and%20Techniques:%20Lessons%20for%20Clinicians&volume=5&publication_year=2015&pages=246-255&pmid=26628842&doi=10.1016/j.jceh.2015.08.001&)]
* 77.
  Pautler R.G.
  Mouse MRI: concepts and applications in physiology. Physiology. 2004; 19:168–175.
   [[DOI](https://doi.org/10.1152/physiol.00016.2004)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15304630/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Physiology&title=Mouse%20MRI:%20concepts%20and%20applications%20in%20physiology&volume=19&publication_year=2004&pages=168-175&pmid=15304630&doi=10.1152/physiol.00016.2004&)]
* 78.
  Overbey E.G., Saravia-Butler A.M., Zhang Z., Rathi K.S., Fogle H., da Silveira W.A., Barker R.J., Bass J.J., Beheshti A., Berrios D.C.et al..
  NASA GeneLab RNA-seq consensus pipeline: standardized processing of short-read RNA-seq data. iScience. 2021; 24:102361.
   [[DOI](https://doi.org/10.1016/j.isci.2021.102361)] [[PMC free article](/articles/PMC8044432/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33870146/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=iScience&title=NASA%20GeneLab%20RNA-seq%20consensus%20pipeline:%20standardized%20processing%20of%20short-read%20RNA-seq%20data&volume=24&publication_year=2021&pages=102361&pmid=33870146&doi=10.1016/j.isci.2021.102361&)]
* 79.
  Di Tommaso P., Chatzou M., Floden E.W., Barja P.P., Palumbo E., Notredame C..
  Nextflow enables reproducible computational workflows. Nat. Biotechnol. 2017; 35:316–319.
   [[DOI](https://doi.org/10.1038/nbt.3820)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28398311/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Biotechnol.&title=Nextflow%20enables%20reproducible%20computational%20workflows&volume=35&publication_year=2017&pages=316-319&pmid=28398311&doi=10.1038/nbt.3820&)]
* 80.
  Li P.-E., Lo C.-C., Anderson J.J., Davenport K.W., Bishop-Lilly K.A., Xu Y., Ahmed S., Feng S., Mokashi V.P., Chain P.S.G..
  Enabling the democratization of the genomics revolution with a fully integrated web-based bioinformatics platform. Nucleic Acids Res. 2017; 45:67–80.
   [[DOI](https://doi.org/10.1093/nar/gkw1027)] [[PMC free article](/articles/PMC5224473/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27899609/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=Enabling%20the%20democratization%20of%20the%20genomics%20revolution%20with%20a%20fully%20integrated%20web-based%20bioinformatics%20platform&volume=45&publication_year=2017&pages=67-80&pmid=27899609&doi=10.1093/nar/gkw1027&)]
* 81.
  Braun J.L., Geromella M.S., Hamstra S.I., Messner H.N., Fajardo V.A..
  Characterizing SERCA function in Murine skeletal muscles after 35-37 days of spaceflight. Int. J. Mol. Sci. 2021; 22:11764.
   [[DOI](https://doi.org/10.3390/ijms222111764)] [[PMC free article](/articles/PMC8584217/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/34769190/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci.&title=Characterizing%20SERCA%20function%20in%20Murine%20skeletal%20muscles%20after%2035-37%20days%20of%20spaceflight&volume=22&publication_year=2021&pages=11764&pmid=34769190&doi=10.3390/ijms222111764&)]
* 82.
  Bellomo R.K., Zavalis E.A., Ioannidis J.P.A..
  Assessment of transparency indicators in space medicine. PLoS One. 2024; 19:e0300701.
   [[DOI](https://doi.org/10.1371/journal.pone.0300701)] [[PMC free article](/articles/PMC10986997/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38564591/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Assessment%20of%20transparency%20indicators%20in%20space%20medicine&volume=19&publication_year=2024&pages=e0300701&pmid=38564591&doi=10.1371/journal.pone.0300701&)]
* 83.
  Reynolds R.J., Shelhamer M..
  Reynolds R.J.
  Research methods for the next 60 years of space exploration, BeyondLEO-Human Health Issues for Deep Space Exploration. Beyond LEO. 2020; London: IntechOpen; 1–7. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Beyond%20LEO&publication_year=2020&)]
* 84.
  Sanders L.M., Scott R.T., Yang J.H., Qutub A.A., Garcia Martin H., Berrios D.C., Hastings J.J.A., Rask J., Mackintosh G., Hoarfrost A.L.et al..
  Biological research and self-driving labs in deep space supported by artificial intelligence. Nat. Mach. Intell. 2023; 5:208–219. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Mach.%20Intell.&title=Biological%20research%20and%20self-driving%20labs%20in%20deep%20space%20supported%20by%20artificial%20intelligence&volume=5&publication_year=2023&pages=208-219&)]
* 85.
  Nelson C.A., Butte A.J., Baranzini S.E..
  Integrating biomedical research and electronic health records to create knowledge-based biologically meaningful machine-readable embeddings. Nat. Commun. 2019; 10:3045.
   [[DOI](https://doi.org/10.1038/s41467-019-11069-0)] [[PMC free article](/articles/PMC6620318/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31292438/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Commun.&title=Integrating%20biomedical%20research%20and%20electronic%20health%20records%20to%20create%20knowledge-based%20biologically%20meaningful%20machine-readable%20embeddings&volume=10&publication_year=2019&pages=3045&pmid=31292438&doi=10.1038/s41467-019-11069-0&)]
* 86.
  Morris J.H., Soman K., Akbas R.E., Zhou X., Smith B., Meng E.C., Huang C.C., Cerono G., Schenk G., Rizk-Jackson A.et al..
  The scalable precision medicine open knowledge engine (SPOKE): a massive knowledge graph of biomedical information. Bioinformatics. 2023; 39:btad080.
   [[DOI](https://doi.org/10.1093/bioinformatics/btad080)] [[PMC free article](/articles/PMC9940622/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/36759942/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=The%20scalable%20precision%20medicine%20open%20knowledge%20engine%20(SPOKE):%20a%20massive%20knowledge%20graph%20of%20biomedical%20information&volume=39&publication_year=2023&pages=btad080&pmid=36759942&doi=10.1093/bioinformatics/btad080&)]
* 87.
  Nelson C.A., Acuna A.U., Paul A.M., Scott R.T., Butte A.J., Cekanaviciute E., Baranzini S.E., Costes S.V..
  Knowledge network embedding of transcriptomic data from spaceflown mice uncovers signs and symptoms associated with terrestrial diseases. Life. 2021; 11:42.
   [[DOI](https://doi.org/10.3390/life11010042)] [[PMC free article](/articles/PMC7828077/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33445483/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Life&title=Knowledge%20network%20embedding%20of%20transcriptomic%20data%20from%20spaceflown%20mice%20uncovers%20signs%20and%20symptoms%20associated%20with%20terrestrial%20diseases&volume=11&publication_year=2021&pages=42&pmid=33445483&doi=10.3390/life11010042&)]
* 88.
  Mason C.E., Green J., Adamopoulos K.I., Afshin E.E., Baechle J.J., Basner M., Bailey S.M., Bielski L., Borg J., Borg J.et al..
  A second space age spanning omics, platforms, and medicine across orbits. Nature. 2024; 632:995–1008.
   [[DOI](https://doi.org/10.1038/s41586-024-07586-8)] [[PMC free article](/articles/PMC12366838/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/38862027/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature&title=A%20second%20space%20age%20spanning%20omics,%20platforms,%20and%20medicine%20across%20orbits&volume=632&publication_year=2024&pages=995-1008&pmid=38862027&doi=10.1038/s41586-024-07586-8&)]
* 89.
  d’Aquin M., Kirstein F., Oliveira D., Schimmler S., Urbanek S..
  FAIREST: a framework for assessing research repositories. Data Intell. 2023; 5:202–241. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Data%20Intell&title=FAIREST:%20a%20framework%20for%20assessing%20research%20repositories&volume=5&publication_year=2023&pages=202-241&)]
* 90.
  Goodliff K.E., Merancy N.F., Bhakta S.S., Rucker M.A., Chai P.R.P., Ashurst T.E., Troutman P.A., Stromgren C..
  Exploration Systems Development Mission Directorate (ESDMD) moon-to-mars architecture definition document. NASA Techn. Rep. Server. 2023; 20230002706. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=NASA%20Techn.%20Rep.%20Server&title=Exploration%20Systems%20Development%20Mission%20Directorate%20(ESDMD)%20moon-to-mars%20architecture%20definition%20document&publication_year=2023&pages=20230002706&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Data Availability Statement

All data are available on the NASA Open Science Data Repository: <https://www.nasa.gov/osdr/>.