Nucleic Acids Res

. 2020 Oct 20;49(D1):D1515–D1522. doi: [10.1093/nar/gkaa887](https://doi.org/10.1093/nar/gkaa887)

# NASA GeneLab: interfaces for the exploration of space omics data

[Daniel C Berrios](https://pubmed.ncbi.nlm.nih.gov/?term=%22Berrios%20DC%22%5BAuthor%5D)

### Daniel C Berrios

1
USRA/NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Daniel C Berrios](https://pubmed.ncbi.nlm.nih.gov/?term=%22Berrios%20DC%22%5BAuthor%5D)

1, [Jonathan Galazka](https://pubmed.ncbi.nlm.nih.gov/?term=%22Galazka%20J%22%5BAuthor%5D)

### Jonathan Galazka

2
NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Jonathan Galazka](https://pubmed.ncbi.nlm.nih.gov/?term=%22Galazka%20J%22%5BAuthor%5D)

2, [Kirill Grigorev](https://pubmed.ncbi.nlm.nih.gov/?term=%22Grigorev%20K%22%5BAuthor%5D)

### Kirill Grigorev

3
Weill Cornell Medicine, New York, NY 10065, USA

Find articles by [Kirill Grigorev](https://pubmed.ncbi.nlm.nih.gov/?term=%22Grigorev%20K%22%5BAuthor%5D)

3, [Samrawit Gebre](https://pubmed.ncbi.nlm.nih.gov/?term=%22Gebre%20S%22%5BAuthor%5D)

### Samrawit Gebre

4
KBR/NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Samrawit Gebre](https://pubmed.ncbi.nlm.nih.gov/?term=%22Gebre%20S%22%5BAuthor%5D)

4, [Sylvain V Costes](https://pubmed.ncbi.nlm.nih.gov/?term=%22Costes%20S%22%5BAuthor%5D)

### Sylvain V Costes

5
NASA Ames Research Center, Moffett Field, CA 94035, USA

Find articles by [Sylvain V Costes](https://pubmed.ncbi.nlm.nih.gov/?term=%22Costes%20S%22%5BAuthor%5D)

5,✉

* Author information
* Article notes
* Copyright and License information

1
USRA/NASA Ames Research Center, Moffett Field, CA 94035, USA

2
NASA Ames Research Center, Moffett Field, CA 94035, USA

3
Weill Cornell Medicine, New York, NY 10065, USA

4
KBR/NASA Ames Research Center, Moffett Field, CA 94035, USA

5
NASA Ames Research Center, Moffett Field, CA 94035, USA

✉

To whom correspondence should be addressed. Tel: +1 650 604 5343; Email: sylvain.v.costes@nasa.gov

Accepted 2020 Oct 6; Revised 2020 Sep 16; Received 2020 Aug 21; Collection date 2021 Jan 8.

© The Author(s) 2020. Published by Oxford University Press on behalf of Nucleic Acids Research.

This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (<http://creativecommons.org/licenses/by-nc/4.0/>), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact journals.permissions@oup.com

[PMC Copyright notice](/about/copyright/)

PMCID: PMC7778922  PMID: [33080015](https://pubmed.ncbi.nlm.nih.gov/33080015/)

## Abstract

The mission of NASA’s GeneLab database (<https://genelab.nasa.gov/>) is to collect, curate, and provide access to the genomic, transcriptomic, proteomic and metabolomic (so-called ‘omics’) data from biospecimens flown in space or exposed to simulated space stressors, maximizing their utilization. This large collection of data enables the exploration of molecular network responses to space environments using a systems biology approach. We review here the various components of the GeneLab platform, including the new data repository web interface, and the GeneLab Online Data Entry (GEODE) web portal, which will support the expansion of the database in the future to include companion non-omics assay data. We discuss our design for GEODE, particularly how it promotes investigators providing more accurate metadata, reducing the curation effort required of GeneLab staff. We also introduce here a new GeneLab Application Programming Interface (API) specifically designed to support tools for the visualization of processed omics data. We review the outreach efforts by GeneLab to utilize the spaceflight data in the repository to generate novel discoveries and develop new hypotheses, including spearheading data analysis working groups, and a high school student training program. All these efforts are aimed ultimately at supporting precision risk management for human space exploration.

## INTRODUCTION

Scientists are leveraging space-based platforms such as the International Space Station (ISS) and earth-based laboratories such as the NASA Space Radiation Laboratory to study the effects of space on biological organisms, generating nucleic acid, protein, and metabolite profiling data at an unprecedented rate. The 2011 National Research Council (NRC) Decadal Survey presaged this ‘wave of change’ almost a decade ago, and called for the development of more powerful informatics technologies to meet the growing needs of these researchers ([1](#B1)). The Survey also promulgated the use of a systems biology approach by space biosciences investigators, which led to the formation of the GeneLab project (<https://genelab.nasa.gov/>), a science initiative at NASA to maximize omics data collected from spaceflight and ground simulation experiments, and including the creation in 2014 of the NASA GeneLab data repository (<https://genelab-data.ndc.nasa.gov/> ) ([1](#B1)). The mission of GeneLab is to maximize the utilization of valuable biospecimens flown in space or exposed to simulated space stressors through the collection and curation of genomic, transcriptomic, proteomic and metabolomic (so-called ‘omics’) data, in order to enable the exploration of molecular network responses to space environments using a systems biology approach. Our designs for the data repository continue to be guided by the FAIR principles ([2](#B2),[3](#B3)). To foster open science in space biology research and to stimulate research opportunities based on an integrated multi-omics analysis approach, investigators who generate omics data are encouraged to contact GeneLab for the latest information concerning data submission requirements and procedures. All GeneLab repository data are open-access.

We review here the various components (Figure [1](#F1)) of the database, then describe its new data repository web interface and the GeneLab Online Data Entry (GEODE) web portal, which provides ‘self-service’ data curation, and will support the expansion of the database in the future to include companion non-omics assay data. We discuss our design strategies for GEODE, emphasizing how they promote investigators providing more accurate metadata using controlled vocabularies, reducing the curation effort required of GeneLab staff. We also introduce here a new GeneLab Application Programming Interface (API) specifically designed to support tools for the visualization of processed omics data. Such visualization tools are essential to fulfil an ‘Open Science’ mandate, democratizing the access to data and allowing the scientific community at large to gain new knowledge on how spaceflight affects life, from humans and mice, to plants and microbes.

### Figure 1.

[![Figure 1.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8c6e/7778922/b0f8bf71b266/gkaa887fig1.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7778922_gkaa887fig1.jpg)

[Open in a new tab](figure/F1/)

The GeneLab database and its connections to intramural and extramural systems. The database API is leveraged extensively by components of the GeneLab Data Systems: the database web browser interface (**A**), the GeneLab Online Data Entry tool (**B**), a workspace tool for private data sharing (**C**), and the GeneLab data visualization server (**D**). The database API is also being used to power various extramural data analytics and visualization tools (**E, F**). The GeneLab Public Analytics platform (**G**) and Data Processing systems (**H**) access the repository data files directly.

## GENELAB DATABASE HOLDINGS

As of August 2020, GeneLab houses data from 271 studies representing investigations of many kinds of spaceflight experimental factors: gravity level (microgravity, hypergravity), ionizing radiation, circadian disruption, and atmospheric pressure, together with information on confounding variables such as organism diet, age, and sample preservation methods, for a variety of biological organisms (Figure [2](#F2)). Approximately half the studies in the GeneLab repository are from experiments conducted in space, and the other half from ground-based (space analogue) environments ([4](#B4)). Mammalian (primarily rodent and human cell line) investigations account for a majority the studies. Other organisms studied include various flowering plants, (e.g. *Arabidopsis thaliana*), microbes, nematodes (primarily *Caenorhabditis elegans*), insects (*Drosophila melanogaster*), and bony fish. Although, the most prevalent study assay type is transcription profiling, the database also includes studies of protein expression, whole genome sequencing, metabolite profiling, metagenomics, epigenomics and epitranscriptomics. Investigators continue to submit data from new kinds of assays at an ever-increasing rate, particularly new kinds of RNA sequencing assays, such as spatial transcription profiling ([5](#B5)) data ([6](#B6)). Accommodating these new kinds of assays have not required GeneLab data systems software development, only minor changes to systems configuration files.

### Figure 2.

[![Figure 2.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8c6e/7778922/bd6dfeb314ab/gkaa887fig2.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7778922_gkaa887fig2.jpg)

[Open in a new tab](figure/F2/)

GeneLab database content by study experiment environment (**A**), study assay type by year of data publication (**B**), and organism studied by year of data publication (**C**).

## DATA PROCESSING STANDARDIZATION

Since its inception GeneLab has focused on adopting best practices regarding the use of community-derived standards for metadata and data processing. For submitted metadata, GeneLab curators encourage the use of domain ontologies, and meticulously, manually harmonize submitted metadata with those of existing studies ([1](#B1)). To support consistent interpretation of submitted data, GeneLab curators augment submitted metadata for spaceflight studies with spacecraft environmental metadata. For example, for experiments conducted on board the U.S. Space Transportation System (the ‘Space Shuttle’), on the ISS, and on board various other spacecraft, GeneLab has gathered, summarized, and attached radiation exposure metadata to the other experiment metadata submitted by investigators ([4](#B4)). Ambient CO2, temperature, and humidity data are also gathered, summarized, and associated with each sample for metadata submitted for ISS experiments.

GeneLab has also begun to process submitted transcriptomic data using consensus pipelines developed by representatives of the space biology community (<https://github.com/nasa/GeneLab_Data_Processing>). This yields gene expression analysis data that are then made available in the database together with the raw data, and all intermediate data processing files. At the time of this writing, 103 GeneLab transcription profiling studies in the database have processed data available.

## KEY DATABASE FEATURES

When originally designed, the GeneLab data systems sought merely to replicate features of existing, publicly-available life sciences data repositories that have long been recognized as valuable to end-users. These included the use of persistent, immutable accession numbers for submitted data, completely open access, and an API to allow for data file and metadata retrieval. Since this original design several years ago, GeneLab has sought to improve on this set of features, and implement new ones in line with advancing end-user needs and new, community-derived design principles for data repositories.

### User interface

The initial user interface for the data repository organized study metadata using a series of tabs, one each for administrative, protocol, sample, and assay metadata. However, this layout makes it difficult for users to see more than one active tab's content at the same time. We have since revised the layout to use navigable, movable, and collapsible sections for each kind of metadata (Figure [3](#F3)) so that users can create custom displays to organize and view the exact kind of metadata they want.

#### Figure 3.

[![Figure 3.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8c6e/7778922/cdb314dbd7f5/gkaa887fig3.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7778922_gkaa887fig3.jpg)

[Open in a new tab](figure/F3/)

Redesigned ‘individual study page’ of the GeneLab data repository. Users can click on the section links (**A**) to navigate to each panel of metadata, open/close (collapse) each panel of metadata using the arrow on the panel header (**B**), and/or drag panels to re-order metadata displays (**C**). For each study dataset, a DOI is generated (**D**), and every submitted version of the dataset can be displayed using a drop-down menu (**E**).

### Increased FAIRness

#### Digital object identifiers

From its inception, GeneLab has sought to implement community-derived (i.e. open) standards for the data and metadata it curates, and for the operation of the database (end-user interactions, curation by GeneLab, etc.). Largely concurrent with the design of the GeneLab Data Repository, the global scientific community converged on a set of optimal design features for data repositories, now termed the FAIR (Findability, Accessibility, Interoperability, and Reusability) principles. In the area of Findability, the data repository now provides Digital Object Identifiers (DOIs) for all submitted datasets. DOIs have guaranteed persistence, and resolution control mechanisms that are centralized (independent of the data source), and provide users of the GeneLab datasets with a way to cite them easily and uniformly. In addition, each version of a dataset (distinguished by changes in data files or in metadata) is tracked in the data repository, and users can opt to see previous versions through the web interface (Figure [3](#F3)). This ensures persistence of the specific version of data as cited by others. Finally, NASA is currently developing processes for the automated submission to other databases of data submitted first to GeneLab, with the twin goals of making the data more findable from extramural database systems, and reducing the burden to data providers of generating multiple data submissions.

#### Accessibility

All data in the GeneLab data repository continues to be accessible to all users without user authentications. To provide the greatest accessibility to its data analysis tools and collaborative workspace, the GeneLab analysis and collaboration platforms have integrated the widely-available Google credentialing system into its authentication systems. Users can opt to use their Google-managed credentials or, if they have them, use their NASA credentials to access these subsystems. It is our intention that this development leads to increased access to and usage of these tools for more investigators.

#### Linked data

One the biggest areas where many data repositories fall short using FAIR-based metrics is interoperability ([2](#B2)), which often presents a barrier to data reusability. In order to support systems interoperation and increase data reuse, the GeneLab repository data uses the widely known ISA experiment model ([7](#B7)) for tagging data files with metadata. The ISA model leverages community-developed concept vocabularies (ontologies), so that there is agreement among users on metadata meaning, and therefore data characterization. Furthermore these models support linkage of data values (‘linked data’) so that, for example, biological samples, personnel or resources reused across experiments need only be described once by the first experiment to refer to them. Subsequent investigations that also use these objects then can quickly search for and refer to them in their investigation descriptions.

In the specific domain of space biology, it is common to re-use samples across different investigations, given the high cost of generating biological sample data in space environments. In many other application areas, it is common to re-use parts of experimental protocols, and these too can be similar referred to by data submitters using the ISA model, rather than duplicated semantically in the data repository.

#### Web-browser data submissions

The most recent addition to the GeneLab Data Systems is GEODE, the GeneLab Environment for Online Data Entry. This interface supports the creation of complex metadata descriptions of datasets, and was built in collaboration with, and by extending an interface originally developed by, the Metabolights ([8](#B8)) database at EBI. This web browser interface (Figure [4](#F4)) allows users to develop ISA-tab sets of metadata through either a guided submission ‘wizard’, in which users create metadata step-by-step, or ‘Study Overview’ method, in which metadata can be arbitrarily edited. Data submitters and GeneLab curation staff can both create metadata using GEODE; submitters are limited to editing only their own submitted metadata, while GeneLab curation staff can access and edit all metadata. The web interface provides the capability for submitters (or curators) to look up metadata concepts in online ontologies dynamically, which reduces metadata normalization effort of the curation staff. Furthermore, GEODE provides continuously available data set editing for submitters (or curators), so that they can rapidly and efficiently update and correct their data; any data set owner (or curator) can change the status of their published data sets to ‘In Review’, make changes to the data/metadata, and re-submit it for release at any time.

##### Figure 4.

![Figure 4.](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8c6e/7778922/24be0242fc01/gkaa887fig4.jpg)

[Open in a new tab](figure/F4/)

The GEODE web browser interface used by both data submitters and GeneLab data curation staff. Below the data set ‘Status’ and desired release date fields (**A**) are the user-entered title, contact(s) and brief study description fields (**B**), the user-selected chosen taxon(s) studied (**C**), relevant publication objects (**D**) and subsections for users to specify further details of the study's description, protocols, samples, assays and study files (**E**), all validated against the ISA model.

#### Enhanced API

GeneLab has always provided an Application Programming Interface (API) for the retrieval of individual experiment data and metadata files. Improvements in this API now enables users to query the database for samples, potentially across multiple datasets and assays, by combinations of values of metadata fields, and then to retrieve sample-associated experiment data. Both the data and the accompanying annotations are returned in a tabular format suitable for downstream processing in a variety of languages and environments commonly used by data scientists. This, in turn, empowers researchers to conduct multi-dataset and multi-omics analyses, such as investigating the impact of single experiment factors on a variety of organisms during space flight. For example, the API can be leveraged to interrogate the entirety of the GeneLab database for RNA-Seq assay gene expression counts from all samples from *Mus musculus* that experienced a specified level of ionizing radiation; such a request returns gene counts from multiple datasets as well as all other metadata values associated with the samples (status of space flight, radiation dose, diet, age, etc.), immediately providing the end-user with data and annotations suitable to build a complex model that accounts for all main and confounding factors known to the database. The API also supports queries for multiple assay types, for example, all transcriptomic and epigenomic assays, facilitating multi-omics data analyses. This enhanced API layer is currently being leveraged within GeneLab to provide advanced data visualizations of GeneLab processed data ([9](#B9)). These include a data table browser for sample data and annotations, and common statistical data visualizations such as principal component analysis, in a web-browser interface. Finally, we should note that, as the data API leverages the versatile ISA-Tab format to bring annotations to data files, this API could be easily extended to numerous types of assay data, not just omics.

## COMMUNITY

### Scientific outreach

A key goal of the GeneLab project is to bring together a community of scientists to generate novel hypotheses and make valuable scientific discoveries using the data in the GeneLab database. GeneLab has sought to engage working groups of students, bioinformaticians, space biologists, researchers and citizen scientists by providing freely-available data analysis tools and support for their use. Users can access user guides and tutorial videos on how to use the various GeneLab applications, including how to analyze RNA-seq datasets using the GeneLab Analysis Platform (<https://genelab.nasa.gov/help/tutorials>). Furthermore, NASA has developed the GeneLab 4 High School (GL4HS) training program, in which fifteen high school students learn how to use the GeneLab tools over four weeks to analyze spaceflight microarray and RNA-seq data, how to generate follow-on hypotheses based on these analyses, how to design a ground-based experiment to test these hypotheses, and ultimately write research proposals for the experiments (<https://www.nasa.gov/ames/genelab-for-high-schools>). GeneLab is also launching an Education Working Group, a group of educators and scientists, who will develop educational content that promotes the use of the GeneLab database, and its visualization and analytical tools.

### Analysis working groups

In 2018 GeneLab formed four Analysis Working Groups (AWGs) comprised of over 100 scientists and students from multiple space agencies, academia, and industry, for the purpose of optimizing and standardizing the processing of raw omics data from the GeneLab repository. The AWGs work in four major areas: animal, plant, microbial, and multi-omics data processing. The consensus data processing pipelines developed in each group are then used by GeneLab to process the data in the repository (see **Data Processing Standardization** above). The AWGs have begun to utilize the processed data to publish insights in important areas of space biology ([10–14](#B10)).

### Data re-use

The number of GeneLab studies continue to grow rapidly, providing more opportunities for meta-analysis. Currently there are 18 publications of this type linked to repository datasets that together leveraged 78 repository datasets (see <https://genelab.nasa.gov/publications/derived>). In addition, an increasing number of extramural visualization tools are consuming the processed data in the repository through its API. For example, the Test of Arabidopsis Space Transcriptome (TOAST) tool has a graphical user interface through which users can quickly compare the data from plant spaceflight experiments using real-time, gene-specific queries, or explore gene networks of interest ([15](#B15)). Likewise, Project MANGO (<https://www.ebi.ac.uk/metagenomics/super-studies/3>) users can generate and visualize taxonomic analyses of GeneLab processed data to explore the microbiome of the ISS.

## FUTURE DIRECTIONS

### Astronaut data

In 2011 the National Research Council of the U.S. recognized the importance of collecting astronaut data, in addition to model organism data in the Decadal Survey ([16](#B16)): ‘because of the limited number of humans who undergo exposure to the space environment, maintaining an extensive and well-organized database and managing it as a resource to be shared with the scientific community has long been viewed as an essential step for scientific discovery’. However, anonymizing astronaut data presents a unique challenge as the cohort is indeed extremely small, and very few metadata (e.g. just gender and flight dates) may be used to identify individuals. Nevertheless, to achieve greater reuse of these data, they too should be made part of an Open Science framework using FAIR principles. They should be stored in non-proprietary formats based on open (community-derived) standards, with open access and with linkages to other data that provide important context ([17](#B17)). This goal was nicely summarized by Higman *et al.* ([17](#B17)), ‘data should be as open as possible, as closed as necessary’. More effort should be put into identifying what types of data can remain open, even if one can identify the individuals to which they belong. For example, gene expression levels do not present any sensitive information in the context of the response to stresses like microgravity and radiation. Such information should therefore be made available through open science frameworks as soon as these data are released for publication by investigators. Any information revealing sensitive and personal information, such as that which can be derived from DNA or RNA sequences, would remain access-controlled.

### Enabling precision space risk management

Although valuable knowledge has been gained from experiments conducted in space or from space simulations on the ground, little progress has been made in terms of modelling the impact of spaceflight on humans. Most risk models have been focusing on space radiation and cancer ([18–20](#B18)). The strong epidemiological data on cancer risk from ionizing radiation ([21](#B21)) and the existence of accelerators dedicated to simulating space radiation have been the main thrust behind these risk models. Ionizing radiation is an easy-to-use experimental factor, with good quantitative input and output, enabling mathematical models. Briefly, scientists control precisely the dose, the dose rate and the type of radiation delivered and they can measure precisely short-term endpoints such as DNA double strand breaks ([22](#B22),[23](#B23)). Interestingly, such responses have been shown to be modulated by the genetic background of an individual ([24–26](#B24)), eventually leading to DNA mutations and cancer ([27–29](#B27)). Because modelling requires quantitative data, omics data are very well suited to informing risk models and to tackling more challenging stressors such as microgravity. The growing amount of omics data generated by NASA principal investigators and the recent guidelines from NASA emphasizing the importance of submitting all omics data to GeneLab are therefore exciting developments for modellers. Indeed, the software architecture designed by GeneLab and its strategies around data and metadata harmonization will enable the development of the next generation of space risk models. By classifying experimental factors into digital objects and by transforming raw data into comparable quantitative endpoints using a workflow approved by the community, GeneLab lets users see how space factors affect a large array of biological processes ([13](#B13),[30–32](#B30)). By establishing mathematical laws describing the relationship between factors’ values and biological endpoints, one can start building more elaborate computer models. By integrating information from other NASA databases with more qualitative data (e.g. immunocytochemistry, behavioural data) using the same metadata schema and harmonization strategies, GeneLab can continue to evolve as a knowledge-based system, fully leveraging advances in machine learning, providing insights on enabling human life in space, and enabling individualized space risk models for precision space medicine.

GeneLab plans to utilize machine learning algorithms and artificial intelligence (AI) to maximize the usage of its data, especially in the context of modelling and extrapolation to human risks. Such effort may start by providing a portal proposing mechanistic models describing known health risks (cancer, muscle atrophy, bone loss, etc.). Such a tool would allow users to test how well GeneLab omics data and data from other databases support these models and test alternative models. Such approach will involve collaborating with the NASA Ames Life Sciences Data Archive (ALSDA), which archives biospecimens and non-omics data from mammalian and microbial NASA experiments.

## DATA AVAILABILITY

NASA GeneLab is an open-access data repository (<https://genelab.nasa.gov>).

## ACKNOWLEDGEMENTS

We would like to thank all members of the GeneLab team and the data systems team in particular: Ms Jamie Bales, Mr Peter O’Donnell, Ms Sonja Caldwell and Mr Matias Fernandez, for developing the database and web applications.

## Contributor Information

Daniel C Berrios,
USRA/NASA Ames Research Center, Moffett Field, CA 94035, USA.

Jonathan Galazka,
NASA Ames Research Center, Moffett Field, CA 94035, USA.

Kirill Grigorev,
Weill Cornell Medicine, New York, NY 10065, USA.

Samrawit Gebre,
KBR/NASA Ames Research Center, Moffett Field, CA 94035, USA.

Sylvain V Costes,
NASA Ames Research Center, Moffett Field, CA 94035, USA.

## FUNDING

Space Biology Program (Science Mission Directorate, Biological and Physical Sciences Division) of the National Aeronautics and Space Administration. Funding for open access charge: NASA.

*Conflict of interest statement*. None declared.

## REFERENCES

* 1.
  Ray S., Gebre S., Fogle H., Berrios D.C., Tran P.B., Galazka J.M., Costes S.V..
  GeneLab: Omics database for spaceflight experiments. Bioinformatics. 2019; 35:1753–1759. [[DOI](https://doi.org/10.1093/bioinformatics/bty884)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30329036/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bioinformatics&title=GeneLab:%20Omics%20database%20for%20spaceflight%20experiments&author=S.%20Ray&author=S.%20Gebre&author=H.%20Fogle&author=D.C.%20Berrios&author=P.B.%20Tran&volume=35&publication_year=2019&pages=1753-1759&pmid=30329036&doi=10.1093/bioinformatics/bty884&)]
* 2.
  Berrios D.C., Beheshti A., Costes S.V..
  FAIRness and usability for open-access omics data systems. Proceedings of the 2018 AMIA Annual Symposium. 2018; AMIA; 232–241. [[PMC free article](/articles/PMC6371294/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30815061/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Proceedings%20of%20the%202018%20AMIA%20Annual%20Symposium&author=D.C.%20Berrios&author=A.%20Beheshti&author=S.V.%20Costes&publication_year=2018&)]
* 3.
  Wilkinson M.D., Dumontier M., Aalbersberg I.J., Appleton G., Axton M., Baak A., Blomberg N., Boiten J.W., da Silva Santos L.B., Bourne P.E. et al..
  The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016; 3:160018. [[DOI](https://doi.org/10.1038/sdata.2016.18)] [[PMC free article](/articles/PMC4792175/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26978244/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci%20Data&title=The%20FAIR%20Guiding%20Principles%20for%20scientific%20data%20management%20and%20stewardship&author=M.D.%20Wilkinson&author=M.%20Dumontier&author=I.J.%20Aalbersberg&author=G.%20Appleton&author=M.%20Axton&volume=3&publication_year=2016&pages=160018&pmid=26978244&doi=10.1038/sdata.2016.18&)]
* 4.
  Beheshti A., Miller J., Kidane Y., Berrios D., Gebre S.G., Costes S.V..
  NASA GeneLab project: bridging space radiation omics with ground studies. Radiat. Res. 2018; 189:553–559. [[DOI](https://doi.org/10.1667/RR15062.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29652620/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=NASA%20GeneLab%20project:%20bridging%20space%20radiation%20omics%20with%20ground%20studies&author=A.%20Beheshti&author=J.%20Miller&author=Y.%20Kidane&author=D.%20Berrios&author=S.G.%20Gebre&volume=189&publication_year=2018&pages=553-559&pmid=29652620&doi=10.1667/RR15062.1&)]
* 5.
  Ståhl P.L., Salmén F., Vickovic S., Lundmark A., Navarro J.F., Magnusson J., Giacomello S., Asp M., Westholm J.O., Huss M. et al..
  Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science. 2016; 353:78–82. [[DOI](https://doi.org/10.1126/science.aaf2403)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27365449/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Science&title=Visualization%20and%20analysis%20of%20gene%20expression%20in%20tissue%20sections%20by%20spatial%20transcriptomics&author=P.L.%20St%C3%A5hl&author=F.%20Salm%C3%A9n&author=S.%20Vickovic&author=A.%20Lundmark&author=J.F.%20Navarro&volume=353&publication_year=2016&pages=78-82&pmid=27365449&doi=10.1126/science.aaf2403&)]
* 6.
  Galazka J., Giacomello S., Lai Polo S.-H., Andrusivova Z., Saravia-Butler A., Fogle H., Andrusivova Z., Giacomello S., Andrusivova Z., Boyko V. et al..
  Spatially resolved transcriptional analysis of hearts from mice flown on the RR-3 mission. GeneLab. 2020; 10.26030/09s2-9×11 version 2. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=GeneLab&title=Spatially%20resolved%20transcriptional%20analysis%20of%20hearts%20from%20mice%20flown%20on%20the%20RR-3%20mission&author=J.%20Galazka&author=S.%20Giacomello&author=S.-H.%20Lai%C2%A0Polo&author=Z.%20Andrusivova&author=A.%20Saravia-Butler&publication_year=2020&)]
* 7.
  González-Beltrán A., Maguire E., Sansone S.A., Rocca-Serra P..
  linkedISA: semantic representation of ISA-Tab experimental metadata. BMC Bioinformatics. 2014; 15:S4. [[DOI](https://doi.org/10.1186/1471-2105-15-S14-S4)] [[PMC free article](/articles/PMC4255742/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25472428/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Bioinformatics&title=linkedISA:%20semantic%20representation%20of%20ISA-Tab%20experimental%20metadata&author=A.%20Gonz%C3%A1lez-Beltr%C3%A1n&author=E.%20Maguire&author=S.A.%20Sansone&author=P.%20Rocca-Serra&volume=15&publication_year=2014&pages=S4&pmid=25472428&doi=10.1186/1471-2105-15-S14-S4&)]
* 8.
  Haug K., Cochrane K., Nainala V.C., Williams M., Chang J., Jayaseelan K.V., O’Donovan C..
  MetaboLights: a resource evolving in response to the needs of its scientific community. Nucleic Acids Res. 2020; 48:D440–D444. [[DOI](https://doi.org/10.1093/nar/gkz1019)] [[PMC free article](/articles/PMC7145518/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31691833/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nucleic%20Acids%20Res.&title=MetaboLights:%20a%20resource%20evolving%20in%20response%20to%20the%20needs%20of%20its%20scientific%20community&author=K.%20Haug&author=K.%20Cochrane&author=V.C.%20Nainala&author=M.%20Williams&author=J.%20Chang&volume=48&publication_year=2020&pages=D440-D444&pmid=31691833&doi=10.1093/nar/gkz1019&)]
* 9.
  Berrios D., Weitz E., Grigorev K., Costes S.V., Gebre S., Beheshti A..
  Ding Q., Eulenstein O., Al-Mubaid H..
  Proceedings of the 12th International Conference on Bioinformatics and Computational Biology. 2020; 70:EasyChair; 89–98. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Proceedings%20of%20the%2012th%20International%20Conference%20on%20Bioinformatics%20and%20Computational%20Biology&author=D.%20Berrios&author=E.%20Weitz&author=K.%20Grigorev&author=S.V.%20Costes&author=S.%20Gebre&publication_year=2020&)]
* 10.
  Bailey S., Mason C.E., Beheshti A., Hassane D., Costes S.V., Grabham P., Scott R., Keune J., Bristow T., Klotz R. et al..
  Hallmarks of space biology: the next stage of exploration. Cell. 2020; In press. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cell&title=Hallmarks%20of%20space%20biology:%20the%20next%20stage%20of%20exploration&author=S.%20Bailey&author=C.E.%20Mason&author=A.%20Beheshti&author=D.%20Hassane&author=S.V.%20Costes&publication_year=2020&)]
* 11.
  Beheshti A., Chakravarty K., Fogle H., Fazelinia H., Silveira W.A.D., Boyko V., Polo S.-H.L., Saravia-Butler A.M., Hardiman G., Taylor D. et al..
  Multi-omics analysis of multiple missions to space reveal a theme of lipid dysregulation in mouse liver. Sci. Rep. 2019; 9:19195. [[DOI](https://doi.org/10.1038/s41598-019-55869-2)] [[PMC free article](/articles/PMC6915713/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31844325/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Multi-omics%20analysis%20of%20multiple%20missions%20to%20space%20reveal%20a%20theme%20of%20lipid%20dysregulation%20in%20mouse%20liver&author=A.%20Beheshti&author=K.%20Chakravarty&author=H.%20Fogle&author=H.%20Fazelinia&author=W.A.D.%20Silveira&volume=9&publication_year=2019&pages=19195&pmid=31844325&doi=10.1038/s41598-019-55869-2&)]
* 12.
  Beheshti A., McDonald J.T., Miller J., Grabham P., Costes S.V..
  GeneLab database analyses suggest long-term impact of space radiation on the cardiovascular system by the activation of FYN through reactive oxygen species. Int. J. Mol. Sci. 2019; 20:661–683. [[DOI](https://doi.org/10.3390/ijms20030661)] [[PMC free article](/articles/PMC6387434/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30717456/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci.&title=GeneLab%20database%20analyses%20suggest%20long-term%20impact%20of%20space%20radiation%20on%20the%20cardiovascular%20system%20by%20the%20activation%20of%20FYN%20through%20reactive%20oxygen%20species&author=A.%20Beheshti&author=J.T.%20McDonald&author=J.%20Miller&author=P.%20Grabham&author=S.V.%20Costes&volume=20&publication_year=2019&pages=661-683&pmid=30717456&doi=10.3390/ijms20030661&)]
* 13.
  McDonald J.T., Stainforth R., Miller J., Cahill T., da Silveira W.A., Rathi K.S., Hardiman G., Taylor D., Costes S.V., Chauhan V. et al..
  NASA genelab platform utilized for biological response to space radiation in animal models. Cancers (Basel). 2020; 12:318–341. [[DOI](https://doi.org/10.3390/cancers12020381)] [[PMC free article](/articles/PMC7072278/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32045996/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Cancers%20(Basel)&title=NASA%20genelab%20platform%20utilized%20for%20biological%20response%20to%20space%20radiation%20in%20animal%20models&author=J.T.%20McDonald&author=R.%20Stainforth&author=J.%20Miller&author=T.%20Cahill&author=W.A.%20da%C2%A0Silveira&volume=12&publication_year=2020&pages=318-341&pmid=32045996&doi=10.3390/cancers12020381&)]
* 14.
  Overbey E.G., Paul A.M., da Silveira W.A., Tahimic C.G.T., Reinsch S.S., Szewczyk N., Stanbouly S., Wang C., Galazka J.M., Mao X.W..
  Mice exposed to combined chronic low-dose irradiation and modeled microgravity develop long-term neurological sequelae. Int. J. Mol. Sci. 2019; 20:4094–5010. [[DOI](https://doi.org/10.3390/ijms20174094)] [[PMC free article](/articles/PMC6747492/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31443374/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Mol.%20Sci.&title=Mice%20exposed%20to%20combined%20chronic%20low-dose%20irradiation%20and%20modeled%20microgravity%20develop%20long-term%20neurological%20sequelae&author=E.G.%20Overbey&author=A.M.%20Paul&author=W.A.%20da%C2%A0Silveira&author=C.G.T.%20Tahimic&author=S.S.%20Reinsch&volume=20&publication_year=2019&pages=4094-5010&pmid=31443374&doi=10.3390/ijms20174094&)]
* 15.
  Barker R., Lombardino J., Rasmussen K., Gilroy S..
  Test of arabidopsis space transcriptome: a discovery environment to explore multiple plant biology spaceflight experiments. Front. Plant Sci. 2020; 11:147–147. [[DOI](https://doi.org/10.3389/fpls.2020.00147)] [[PMC free article](/articles/PMC7076552/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32265943/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=Test%20of%20arabidopsis%20space%20transcriptome:%20a%20discovery%20environment%20to%20explore%20multiple%20plant%20biology%20spaceflight%20experiments&author=R.%20Barker&author=J.%20Lombardino&author=K.%20Rasmussen&author=S.%20Gilroy&volume=11&publication_year=2020&pages=147-147&pmid=32265943&doi=10.3389/fpls.2020.00147&)]
* 16.
  National Academies of Sciences Engineering and Medicine (U.S.). Committee on a Midterm Assessment of Implementation of the Decadal Survey on Life and Physical Sciences Research at NASA, National Academies of Sciences Engineering and Medicine (U.S.). Aeronautics and Space Engineering Board., National Academies of Sciences Engineering and Medicine (U.S.). Space Studies Board. and National Academies of Sciences Engineering and Medicine (U.S.). Division on Engineering and Physical Sciences
  A Midterm Assessment of Implementation of the Decadal Survey on Life and Physical Sciences Research at NASA. 2018; Washington, DC: The National Academies Press. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29924532/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A%20Midterm%20Assessment%20of%20Implementation%20of%20the%20Decadal%20Survey%20on%20Life%20and%20Physical%20Sciences%20Research%20at%20NASA&publication_year=2018&)]
* 17.
  Rosie H., Bangert D., Jones S..
  Three camps, one destination: the intersections of research data management, FAIR and open. Insights. 2019; 32:18–27. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Insights&title=Three%20camps,%20one%20destination:%20the%20intersections%20of%20research%20data%20management,%20FAIR%20and%20open&author=H.%20Rosie&author=D.%20Bangert&author=S.%20Jones&volume=32&publication_year=2019&pages=18-27&)]
* 18.
  Schimmerling W., Cucinotta F.A., Wilson J.W..
  Radiation risk and human space exploration. Adv. Space Res. 2003; 31:27–34. [[DOI](https://doi.org/10.1016/s0273-1177%2802%2900653-1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/12577903/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Adv.%20Space%20Res.&title=Radiation%20risk%20and%20human%20space%20exploration&author=W.%20Schimmerling&author=F.A.%20Cucinotta&author=J.W.%20Wilson&volume=31&publication_year=2003&pages=27-34&pmid=12577903&doi=10.1016/s0273-1177(02)00653-1&)]
* 19.
  Cucinotta F.A., Durante M..
  Cancer risk from exposure to galactic cosmic rays: implications for space exploration by human beings. Lancet Oncol. 2006; 7:431–435. [[DOI](https://doi.org/10.1016/S1470-2045%2806%2970695-7)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16648048/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Lancet%20Oncol.&title=Cancer%20risk%20from%20exposure%20to%20galactic%20cosmic%20rays:%20implications%20for%20space%20exploration%20by%20human%20beings&author=F.A.%20Cucinotta&author=M.%20Durante&volume=7&publication_year=2006&pages=431-435&pmid=16648048&doi=10.1016/S1470-2045(06)70695-7&)]
* 20.
  Heuskin A.C., Osseiran A.I., Tang J., Costes S.V..
  Simulating space radiation-Induced breast tumor incidence using automata. Radiat. Res. 2016; 186:27–38. [[DOI](https://doi.org/10.1667/RR14338.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27333083/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res&title=Simulating%20space%20radiation-Induced%20breast%20tumor%20incidence%20using%20automata&author=A.C.%20Heuskin&author=A.I.%20Osseiran&author=J.%20Tang&author=S.V.%20Costes&volume=186&publication_year=2016&pages=27-38&pmid=27333083&doi=10.1667/RR14338.1&)]
* 21.
  Preston D.L., Ron E., Tokuoka S., Funamoto S., Nishi N., Soda M., Mabuchi K., Kodama K..
  Solid cancer incidence in atomic bomb survivors: 1958–1998. Radiat. Res. 2007; 168:1–64. [[DOI](https://doi.org/10.1667/RR0763.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17722996/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Solid%20cancer%20incidence%20in%20atomic%20bomb%20survivors:%201958%E2%80%931998&author=D.L.%20Preston&author=E.%20Ron&author=S.%20Tokuoka&author=S.%20Funamoto&author=N.%20Nishi&volume=168&publication_year=2007&pages=1-64&pmid=17722996&doi=10.1667/RR0763.1&)]
* 22.
  Costes S.V., Boissiere A., Ravani S., Romano R., Parvin B., Barcellos-Hoff M.H..
  Imaging features that discriminate between foci induced by high- and low-LET radiation in human fibroblasts. Radiat. Res. 2006; 165:505–515. [[DOI](https://doi.org/10.1667/RR3538.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16669704/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Imaging%20features%20that%20discriminate%20between%20foci%20induced%20by%20high-%20and%20low-LET%20radiation%20in%20human%20fibroblasts&author=S.V.%20Costes&author=A.%20Boissiere&author=S.%20Ravani&author=R.%20Romano&author=B.%20Parvin&volume=165&publication_year=2006&pages=505-515&pmid=16669704&doi=10.1667/RR3538.1&)]
* 23.
  Georgescu W., Osseiran A., Rojec M., Liu Y., Bombrun M., Tang J., Costes S.V..
  Characterizing the DNA damage response by cell tracking algorithms and cell features classification using high-content time-lapse analysis. PLoS One. 2015; 10:e0129438. [[DOI](https://doi.org/10.1371/journal.pone.0129438)] [[PMC free article](/articles/PMC4479605/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26107175/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Characterizing%20the%20DNA%20damage%20response%20by%20cell%20tracking%20algorithms%20and%20cell%20features%20classification%20using%20high-content%20time-lapse%20analysis&author=W.%20Georgescu&author=A.%20Osseiran&author=M.%20Rojec&author=Y.%20Liu&author=M.%20Bombrun&volume=10&publication_year=2015&pages=e0129438&pmid=26107175&doi=10.1371/journal.pone.0129438&)]
* 24.
  Ochola D.O., Sharif R., Bedford J.S., Keefe T.J., Kato T.A., Fallgren C.M., Demant P., Costes S.V., Weil M.M..
  Persistence of gamma-H2AX foci in bronchial cells correlates with susceptibility to radiation associated lung cancer in mice. Radiat. Res. 2019; 191:67–75. [[DOI](https://doi.org/10.1667/RR14979.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30398394/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Persistence%20of%20gamma-H2AX%20foci%20in%20bronchial%20cells%20correlates%20with%20susceptibility%20to%20radiation%20associated%20lung%20cancer%20in%20mice&author=D.O.%20Ochola&author=R.%20Sharif&author=J.S.%20Bedford&author=T.J.%20Keefe&author=T.A.%20Kato&volume=191&publication_year=2019&pages=67-75&pmid=30398394&doi=10.1667/RR14979.1&)]
* 25.
  Penninckx S., Cekanaviciute E., Degorre C., Guiet E., Viger L., Lucas S., Costes S.V..
  Dose, LET and strain dependence of radiation-induced 53BP1 foci in 15 mouse strains ex vivo introducing novel DNA damage metrics. Radiat. Res. 2019; 192:1–12. [[DOI](https://doi.org/10.1667/RR15338.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31081741/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Dose,%20LET%20and%20strain%20dependence%20of%20radiation-induced%2053BP1%20foci%20in%2015%20mouse%20strains%20ex%20vivo%20introducing%20novel%20DNA%20damage%20metrics&author=S.%20Penninckx&author=E.%20Cekanaviciute&author=C.%20Degorre&author=E.%20Guiet&author=L.%20Viger&volume=192&publication_year=2019&pages=1-12&pmid=31081741&doi=10.1667/RR15338.1&)]
* 26.
  Pariset E., Penninckx S., Degorre C., Guiet E., Lopez Macha A., Cekanaviciute E., Snijders A.M., Mao J.H., Paris F., Costes S.V..
  53BP1 repair kinetics for prediction of in vivo radiation susceptibility in 15 mouse strains. Radiat. Res. 2020; doi:10.1667/RADE-20-00122.1. [[DOI](https://doi.org/10.1667/RADE-20-00122.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32991727/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=53BP1%20repair%20kinetics%20for%20prediction%20of%20in%20vivo%20radiation%20susceptibility%20in%2015%20mouse%20strains&author=E.%20Pariset&author=S.%20Penninckx&author=C.%20Degorre&author=E.%20Guiet&author=A.%20Lopez%C2%A0Macha&publication_year=2020&pmid=32991727&doi=10.1667/RADE-20-00122.1&)]
* 27.
  Costes S., Sachs R., Hlatky L., Vannais D., Waldren C., Fouladi B..
  Large-mutation spectra induced at hemizygous loci by low-LET radiation: evidence for intrachromosomal proximity effects. Radiat. Res. 2001; 156:545–557. [[DOI](https://doi.org/10.1667/0033-7587%282001%29156%5B0545%3Almsiah%5D2.0.co;2)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11604068/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Large-mutation%20spectra%20induced%20at%20hemizygous%20loci%20by%20low-LET%20radiation:%20evidence%20for%20intrachromosomal%20proximity%20effects&author=S.%20Costes&author=R.%20Sachs&author=L.%20Hlatky&author=D.%20Vannais&author=C.%20Waldren&volume=156&publication_year=2001&pages=545-557&pmid=11604068&doi=10.1667/0033-7587(2001)156%5B0545:lmsiah%5D2.0.co;2&)]
* 28.
  Tang j., Georgescu W., Deschamps T., Yannone S.M., Costes S.V..
  Genomic Instability and Cancer Metastasis. 2015; Springer Science & Business Media; 75–93. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Genomic%20Instability%20and%20Cancer%20Metastasis&author=j.%20Tang&author=W.%20Georgescu&author=T.%20Deschamps&author=S.M.%20Yannone&author=S.V.%20Costes&publication_year=2015&)]
* 29.
  Heuskin A.C., Osseiran A.I., Tang J., Costes S.V..
  Simulating space radiation-induced breast tumor incidence using automata. Radiat. Res. 2016; 186:27–38. [[DOI](https://doi.org/10.1667/RR14338.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27333083/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Radiat.%20Res.&title=Simulating%20space%20radiation-induced%20breast%20tumor%20incidence%20using%20automata&author=A.C.%20Heuskin&author=A.I.%20Osseiran&author=J.%20Tang&author=S.V.%20Costes&volume=186&publication_year=2016&pages=27-38&pmid=27333083&doi=10.1667/RR14338.1&)]
* 30.
  Beheshti A., Shirazi-Fard Y., Choi S., Berrios D., Gebre S.G., Galazka J.M., Costes S.V..
  Exploring the effects of spaceflight on mouse physiology using the open access NASA GeneLab platform. J. Vis. Exp. 2019; 143:e58447. [[DOI](https://doi.org/10.3791/58447)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30688299/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Vis.%20Exp&title=Exploring%20the%20effects%20of%20spaceflight%20on%20mouse%20physiology%20using%20the%20open%20access%20NASA%20GeneLab%20platform&author=A.%20Beheshti&author=Y.%20Shirazi-Fard&author=S.%20Choi&author=D.%20Berrios&author=S.G.%20Gebre&volume=143&publication_year=2019&pages=e58447&pmid=30688299&doi=10.3791/58447&)]
* 31.
  Beheshti A., Chakravarty K., Fogle H., Fazelinia H., Silveira W.A.D., Boyko V., Polo S.L., Saravia-Butler A.M., Hardiman G., Taylor D. et al..
  Multi-omics analysis of multiple missions to space reveal a theme of lipid dysregulation in mouse liver. Sci. Rep. 2019; 9:19195. [[DOI](https://doi.org/10.1038/s41598-019-55869-2)] [[PMC free article](/articles/PMC6915713/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31844325/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Multi-omics%20analysis%20of%20multiple%20missions%20to%20space%20reveal%20a%20theme%20of%20lipid%20dysregulation%20in%20mouse%20liver&author=A.%20Beheshti&author=K.%20Chakravarty&author=H.%20Fogle&author=H.%20Fazelinia&author=W.A.D.%20Silveira&volume=9&publication_year=2019&pages=19195&pmid=31844325&doi=10.1038/s41598-019-55869-2&)]
* 32.
  Beheshti A., Cekanaviciute E., Smith D.J., Costes S.V..
  Global transcriptomic analysis suggests carbon dioxide as an environmental stressor in spaceflight: a systems biology GeneLab case study. Sci. Rep. 2018; 8:4191. [[DOI](https://doi.org/10.1038/s41598-018-22613-1)] [[PMC free article](/articles/PMC5843582/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29520055/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Global%20transcriptomic%20analysis%20suggests%20carbon%20dioxide%20as%20an%20environmental%20stressor%20in%20spaceflight:%20a%20systems%20biology%20GeneLab%20case%20study&author=A.%20Beheshti&author=E.%20Cekanaviciute&author=D.J.%20Smith&author=S.V.%20Costes&volume=8&publication_year=2018&pages=4191&pmid=29520055&doi=10.1038/s41598-018-22613-1&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Data Availability Statement

NASA GeneLab is an open-access data repository (<https://genelab.nasa.gov>).