Genes (Basel)

. 2021 Feb 25;12(3):337. doi: [10.3390/genes12030337](https://doi.org/10.3390/genes12030337)

# Network Analysis of Gene Transcriptions of *Arabidopsis thaliana* in Spaceflight Microgravity

[Vidya Manian](https://pubmed.ncbi.nlm.nih.gov/?term=%22Manian%20V%22%5BAuthor%5D)

### Vidya Manian

1Department of Electrical and Computer Engineering, University of Puerto Rico, Mayaguez, PR 00681-9000, USA; Jairo.orozco@upr.edu

2Department of Bioengineering, University of Puerto Rico, Mayaguez, PR 00681-9000, USA; harshini.gangapuram@upr.edu

Find articles by [Vidya Manian](https://pubmed.ncbi.nlm.nih.gov/?term=%22Manian%20V%22%5BAuthor%5D)

1,2,\*, [Jairo Orozco](https://pubmed.ncbi.nlm.nih.gov/?term=%22Orozco%20J%22%5BAuthor%5D)

### Jairo Orozco

1Department of Electrical and Computer Engineering, University of Puerto Rico, Mayaguez, PR 00681-9000, USA; Jairo.orozco@upr.edu

Find articles by [Jairo Orozco](https://pubmed.ncbi.nlm.nih.gov/?term=%22Orozco%20J%22%5BAuthor%5D)

1, [Harshini Gangapuram](https://pubmed.ncbi.nlm.nih.gov/?term=%22Gangapuram%20H%22%5BAuthor%5D)

### Harshini Gangapuram

2Department of Bioengineering, University of Puerto Rico, Mayaguez, PR 00681-9000, USA; harshini.gangapuram@upr.edu

Find articles by [Harshini Gangapuram](https://pubmed.ncbi.nlm.nih.gov/?term=%22Gangapuram%20H%22%5BAuthor%5D)

2, [Heeralal Janwa](https://pubmed.ncbi.nlm.nih.gov/?term=%22Janwa%20H%22%5BAuthor%5D)

### Heeralal Janwa

3Department of Mathematics, University of Puerto Rico, Rio Piedras, PR 00925-2537, USA; heeralal.janwa@upr.edu (H.J.); carlos.agrinsoni@upr.edu (C.A.)

Find articles by [Heeralal Janwa](https://pubmed.ncbi.nlm.nih.gov/?term=%22Janwa%20H%22%5BAuthor%5D)

3, [Carlos Agrinsoni](https://pubmed.ncbi.nlm.nih.gov/?term=%22Agrinsoni%20C%22%5BAuthor%5D)

### Carlos Agrinsoni

3Department of Mathematics, University of Puerto Rico, Rio Piedras, PR 00925-2537, USA; heeralal.janwa@upr.edu (H.J.); carlos.agrinsoni@upr.edu (C.A.)

Find articles by [Carlos Agrinsoni](https://pubmed.ncbi.nlm.nih.gov/?term=%22Agrinsoni%20C%22%5BAuthor%5D)

3

* Author information
* Article notes
* Copyright and License information

1Department of Electrical and Computer Engineering, University of Puerto Rico, Mayaguez, PR 00681-9000, USA; Jairo.orozco@upr.edu

2Department of Bioengineering, University of Puerto Rico, Mayaguez, PR 00681-9000, USA; harshini.gangapuram@upr.edu

3Department of Mathematics, University of Puerto Rico, Rio Piedras, PR 00925-2537, USA; heeralal.janwa@upr.edu (H.J.); carlos.agrinsoni@upr.edu (C.A.)

\*

Correspondence: vidya.manian@upr.edu; Tel.: +787-832-4040 (ext. 3094)

Received 2020 Dec 26; Accepted 2021 Feb 23; Collection date 2021 Mar.

© 2021 by the authors.

Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ([http://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

[PMC Copyright notice](/about/copyright/)

PMCID: PMC7996555  PMID: [33668919](https://pubmed.ncbi.nlm.nih.gov/33668919/)

## Abstract

The transcriptomic datasets of the plant model organism *Arabidopsis thaliana* grown in the International Space Station provided by GeneLab have been mined to isolate the impact of spaceflight microgravity on gene expressions related to root growth. A set of computational tools is used to identify the hub genes that respond differently in spaceflight with controlled lighting compared to on the ground. These computational tools based on graph-theoretic approaches are used to infer gene regulatory networks from the transcriptomic datasets. The three main algorithms used for network analyses are Least Absolute Shrinkage and Selection Operator (LASSO), Pearson correlation, and the Hyperlink-Induced Topic Search (HITS) algorithm. Graph-based spectral analyses reveal distinct properties of the spaceflight microgravity networks for the Wassilewskija (WS), Columbia (Col)-0, and mutant phytochromeD (*phyD*) ecotypes. The set of hub genes that are significantly altered in spaceflight microgravity are mainly involved in cell wall synthesis, protein transport, response to auxin, stress responses, and catabolic processes. Network analysis highlights five important root growth-regulating hub genes that have the highest outdegree distribution in spaceflight microgravity networks. These concerned genes coding for proteins are identified from the Gene Regulatory Networks (GRNs) corresponding to spaceflight total light environment. Furthermore, network analysis uncovers genes that encode nucleotide-diphospho-sugar interconversion enzymes that have higher transcriptional regulation in spaceflight microgravity and are involved in cell wall biosynthesis.

**Keywords:** gene expression, graphs, network analysis, root growth, cell wall biosynthesis, spaceflight microgravity, *Arabidopsis thaliana*

## 1. Introduction

Gravity plays a key role in plant growth [[1](#B1-genes-12-00337)]. *Arabidopsis thaliana* (*Arabidopsis*) is a flowering plant that has been chosen by biologists as a model plant organism to study the effects of gravity and other environmental stressors, since it has a short life cycle and because of the existence of a multitude of mutants and transgenic plants. The current visibility of *Arabidopsis* research reflects the growing realization among biologists that this simple angiosperm can serve as a convenient model not only for plant biology but also for addressing fundamental questions of biological structure and function common to all Eukaryotes [[2](#B2-genes-12-00337)]. To achieve the goal of providing long term life support for deep space missions a fundamental knowledge on plant growth in spaceflight has to be gained. The International Space Station (ISS) is currently equipped with all capabilities to collect data needed to address fundamental questions of plant physiology and development in spaceflight microgravity [[3](#B3-genes-12-00337)].

In this article, we are interested in identifying the genes that show transcriptional abundance under the influence of spaceflight microgravity, and the genes primarily influencing root growth and cell wall biosynthesis in spaceflight. The transcriptomic profile of *Arabidopsis* has been studied in simulated microgravity [[4](#B4-genes-12-00337)]. The effect of gravity and mechanical stimulation on the growth of the root apex of *Arabidopsis* has resulted in transient changes in gene expressions [[5](#B5-genes-12-00337)]. The effect of spaceflight microgravity on *Arabidopsis* root growth is presented in [[6](#B6-genes-12-00337)]. Cell wall modeling in the roots, shoots, and hypocotyls of plants is an important metabolic adaptation brought about by genes and proteins. Metabolic phenotyping of *Arabidopsis* has been carried out on the ground [[7](#B7-genes-12-00337)]. Metabolic fingerprinting is important for improving the quality of crops grown in spaceflight. Several of the cell wall proteome changes have been corroborated with transcriptomic changes in spaceflight [[8](#B8-genes-12-00337)]. As plants are important for the bioregenerative life support in spaceflight, the cell wall perturbations may affect the yield of crops grown in the altered spaceflight environment [[9](#B9-genes-12-00337)]. Of the 33 XTH Arabidopsis root growth genes, XTH17 to XTH20 are the main contributors [[10](#B10-genes-12-00337)]. Nucleotide sugar interconversions in plants are discussed in [[11](#B11-genes-12-00337),[12](#B12-genes-12-00337)]. From terrestrial studies, nucleotide-diphsopho-(NPD) sugar interconversion enzymes (NSE) of the small dehydrogenase/reductase superfamily are given in [[13](#B13-genes-12-00337)]. Plant Cell Wall (PCW) genes were identified using gene co-expression analysis in [[14](#B14-genes-12-00337)], and it was shown how these genes are transcriptionally co-regulated [[15](#B15-genes-12-00337)]. These sugars require subtle quantitative control during plant root growth and development. Hence, it is important to identify the genes that encode these enzymes involved in regulating growth of adventitious roots, and their waving and skewing in spaceflight microgravity.

Researchers have used various ecotypes and mutants of *Arabidopsis* to isolate genes with transcriptional variation in spaceflight environment compared to on the ground. Since we are not doing the experiment and performing the data collection, we rely on datasets available from GeneLab for plants grown in spaceflight microgravity. GeneLab provides transcriptomic datasets for various ecotypes of *Arabidopsis* from spaceflight. The *Arabidopsis* ecotypes Col-0, Ws-2, Ler-0, and Cvi-0 showed differential gene expression due to oxidative stress in spaceflight [[16](#B16-genes-12-00337)]. Differential gene expression analysis of *Arabidopsis* exposed over six days to blue light at different levels of gravity in comparison to unit gravity control has been presented in [[17](#B17-genes-12-00337)], and it was found that blue-light phototropism may be enough to reduce stress due to lower levels of gravity in spaceflight. It was found that plants in spaceflight microgravity grow slower than plants in unit gravity on the ground. Two ecotypes of *Arabidopsis* (WS and Col-0) were grown in spaceflight under directional light, and it was found that skewing and waving of roots were independent of gravity, the roots were negatively phototropic, and both ecotypes skewed differently in the presence of light, due to a lack of gravity [[18](#B18-genes-12-00337)]. Major organ-specific and cellular remodeling of *Arabidopsis* has been identified from its growth in ISS and physiological adaptation to spaceflight [[3](#B3-genes-12-00337),[19](#B19-genes-12-00337)]. Previous literature, cited above, characterized unique transcriptions in WS, Col-0, and PhyD mutant of *Arabidopsis* using heat maps and fold change analysis methods. For all the genome analysis done, no phenotypic measurements have been presented or discussed. However, the gradient-light experiments conducted in the ISS resulted in the plant root growth in a skewing pattern. These were dramatic observations of phenotype changes concerning root growth and cell wall response in microgravity. Hence, we have chosen the GLDS-7 [[3](#B3-genes-12-00337)] and GLDS-120 [[20](#B20-genes-12-00337)] datasets collected under different lighting settings for applying our network analysis methods.

The biochemical interactions within a cell of a biological system are formulated as gene regulatory networks for modeling biological processes. GRNs are used to represent regulatory and transcriptional functions that underlie cellular, molecular, and biological phenomena. GRNs have become an indispensable tool that facilitates interpretation of biological processes, molecular functions, protein interactions, genome to phenome analysis, cellular differentiation, identification of genes as biomarkers, and the response of an organism to external stimuli. A Bayesian network generation method for GRN constructed for *Arabidopsis* has been presented [[21](#B21-genes-12-00337)]. Several machine learning algorithms have been implemented for the generation of these networks [[22](#B22-genes-12-00337)]. In [[23](#B23-genes-12-00337)], several statistical and machine learning methods have been reviewed for the prediction of GRNs from transcriptome datasets. In [[24](#B24-genes-12-00337)], many algorithms for GRN inferencing from single-cell transcriptomic data are benchmarked using simulated data. Several GRNs have been generated to study root development in *Arabidopsis* [[25](#B25-genes-12-00337)]. Vascular root development has been represented using GRNs in [[26](#B26-genes-12-00337)]. Furthermore, *Arabidopsis* secondary cell wall synthesis has been studied using a protein-DNA regulatory network and genes involved in secondary cell wall modeling, which form the cell shape and the bulk of the plant biomass [[27](#B27-genes-12-00337)]. Other GRNs for *Arabidopsis* growth and development are presented in [[28](#B28-genes-12-00337)]. Gene Ontology is the process of classifying an annotated gene to a particular function. Gene set enrichment analysis is used to determine changes of expression in groups of a priori defined gene sets. Additional web-tools and databases are available for *Arabidopsis* gene expression analysis [[29](#B29-genes-12-00337)]. These GRN studies do not identify hub genes and the target (authority) genes they regulate in spaceflight microgravity compared to on the ground for important biological processes that are affected in spaceflight, nor perform rigorous graph theoretic network analysis and derive biological interpretations.

We have used three basic graph-based network approaches in this paper (1) the LASSO, (2) Pearson correlation, and (3) HITS methods. LASSO and Pearson correlation methods are applied to construct GRNs of transcriptional regulations in spaceflight microgravity as well as ground control. [Section 2](#sec2-genes-12-00337) presents the materials and methods used for GRN inferencing and analysis. In [Section 3](#sec3-genes-12-00337), we present the results of the GRN analysis of the significant hub genes (identified from Pearson and HITS method) with the highest transcriptional abundance in spaceflight microgravity. Results from network analysis of the *Arabidopsis* ecotypes and genotype are discussed in this section. The root growth and cell wall genes affected in spaceflight microgravity are isolated and their molecular functions are discussed. [Section 4](#sec4-genes-12-00337) presents the conclusions.

## 2. Materials and Methods

### 2.1. GeneLab Arabidopsis Datasets

We have mined GeneLab GLDS-7 and GLDS -120 datasets for identifying hub genes that are affected by spaceflight. The GLDS-7 dataset contains microarray gene expression data for the *Arabidopsis* WS and Col-0 ecotypes for different tissues (roots, leaves, and hypocotyls) for the plants grown in ground control and spaceflight in white light. GLDS-120 contains the transcriptomics data of the *Arabidopsis* Wassilewskija (WS) and Columbia (Col-0) ecotypes, and the gene *Phytochrome D* (*phyD*) mutant of ecotype Col-0. The different stressors imposed on the plants are 4–6 umoles m-2 s-1 of total light and dark in spaceflight and on the ground. The design of the experiment was to investigate the effect of light on *Arabidopsis* root growth when the gravity stimuli were nullified. The *phyD* mutant was used, since it is a known light-related mutant in Col-0 background. RNAseq is used for transcription profiling. Gene expression data are available for pairs of combinations of genotypes and ecotypes.

### 2.2. Graph-Based GRN Inferencing

We define a graph-based representation for the gene expressions. Formally, a graph is a pair of sets G = (V, E) where V is the vertices (molecules, genes, proteins, nodes, points) and E is an ordered pair of vertices (u, v) that are called the edges (arcs), respectively [[30](#B30-genes-12-00337)]. One important advantage of the representation of networks by graphs is that they have an intuitive graphical representation. In a directed graph G = (V, E, o, t), e = (u, v) are the edges, the origin of e is denoted by o(e), and the terminal v is denoted by t(v). A graph is weighted if each edge e is assigned a positive real-valued weight w(e). Principal Component Analysis (PCA) method is applied to de-correlate the gene expression values. PCA is done to reduce the dimensions to three main components corresponding to the largest eigenvalues of the covariance matrix computed from the graph representation of the gene expression data. PCA projects the data on to an orthogonal space, such that the variance of the projected data is maximized. This space is lower in dimension with minimum projection cost. PCA is applied to the gene expression datasets before performing both LASSO regression and Pearson correlation GRN construction.

#### 2.2.1. LASSO Regression

Lasso is a linear regression algorithm that shrinks the data towards a central point. Lasso regression mostly leads to sparse models. Lasso uses the *l1* regularization, which means it adds a penalty that is equal to the sum of the absolute value of the coefficients. Lasso regression is computationally feasible and can fit any kind of statistical data [[31](#B31-genes-12-00337)]. *l1* regularization is applied to eliminate the relationship between the genes with the least importance. The Lasso regression is constructed according to the description in [[31](#B31-genes-12-00337)]. We have used the SILGGM package in R for the Lasso Regression [[32](#B32-genes-12-00337)]. In this algorithm, every gene present in the data is considered as a transcription factor, as well as a target gene, and the correlation between each gene with the other is calculated using the scaled Lasso algorithm. The results from the regression are used to construct GRNs in Cytoscape for the sub-modules of the genes of *Arabidopsis* spaceflight and ground datasets. The method has been applied to the GeneLab GLDS-120 dataset.

#### 2.2.2. Pearson Correlation

Pearson’s correlation coefficient between two genes (variables, nodes) is defined as the covariance of the two variables divided by the product of their standard deviations:

|  |  |
| --- | --- |
| ρX,Y=cov(X,Y)σXσY | (1) |

Pearson’s correlation coefficient is a test that measures the statistical relationship between two random variables. If the association between the elements is not linear, then the coefficient is not specifically identified. In this study, we use the Pearson correlation to construct the co-expressed gene network to identify genes with correlated expression patterns. This method is based on an adjusted threshold *p*-value to accommodate multiple hypotheses; the correlation between expression patterns is calculated for every pair of genes. The Pearson correlation coefficient is used as the measure of correlation (between −1 to 1) and gene pairs are considered to be co-expressed if their *p*-value is less than or equal to the corrected threshold *p*-value. The *t*-test is used to establish if the correlation coefficient is significantly different from zero, and hence, that there is evidence of an association between the two variables. The genes are treated as nodes and the relation between them is an edge. Therefore, the nodes with the highest degree are related to a higher number of target or authority genes. Those genes that have the highest degree or intra-module (within graph) connectivity are treated as hub genes to construct the gene regulatory networks. [Figure 1](#genes-12-00337-f001) shows the steps involved in generating the GRN from the microarray gene expression dataset using this method.

##### Figure 1.

[![Figure 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/2124785dda4f/genes-12-00337-g001.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g001.jpg)

[Open in a new tab](figure/genes-12-00337-f001/)

Flow chart of the procedure for gene regulatory network inferencing using the graph-based Pearson correlation method.

#### 2.2.3. Sparse Networks and the Weighted HITS Algorithm

We show that the GRN generated for the GeneLab *Arabidopsis* datasets are sparse networks or graphs. We define sparsity precisely so that we utilize quantitatively time and speedups in HITS and other algorithms. Briefly, we recall the following definitions obtained from [[30](#B30-genes-12-00337)] and [[33](#B33-genes-12-00337)].

Directed graph: The graph (V, E, o, t) is said to be directed if directed edges are allowed, i.e., not all edges have reverse edges as members of E. In a directed graph, G = (V, E, o, t), the edges e = (u, v), the origin of e is denoted by o, and the terminal v is denoted by t(v).

Bipartite graph: The graph is called *bipartite* if V=V1⊎ V2 such that edges connect node V1 to V2. The expanding constant or isoperimetric constant (or Cheeger constant) of X is defined as:

|  |  |
| --- | --- |
| hX= min∅≠F⊂V∂FminF, V\F | (2) |

where F⊂V and the boundary ∂F is the set of edges connecting F to V∖F. The isoperimetric constant is difficult to compute, but we can bound its value using the spectral gap. The Spectral Gap is defined as the difference between the two highest eigenvalues of the adjacency matrix of the graph.

Sparse graphs: We say that a graph (or the corresponding network) is sparse if hX is large. One of the major results of Cheeger for Riemannian manifolds and its equivalent for graphs is that a large spectral gap implies large hX. Computing hX is an NP-Complete problem, while the computing spectral gap is at most cubic and many times linear; we work with the spectral gap here.

Spectral gap: For a graph X, the Laplacian eigenvalues can be ordered as |λ1| ≥ |λ2| ≥ · · · ≥ |λn| (X may be directed or undirected, weighted or unweighted, simple or not). The spectral gap is defined as: δλ = |λ1| − |λ2|. By normalizing the Laplacian matrix of X, the eigenvalues are 1 = λ1 ≥ λ2 ≥ · · · ≥ λn > 0, and the Lapacian spectral gap will be: δλ =1 − |λ2|. The spectral gap is also known as a random walk, in terms of this concept λ2 is the most important eigenvalue. Note that if the spectral gap is 0, λ2 = 1 (Γ is not (strongly) connected or Γ is bipartite), and a typical random walk will not converge to a unique distribution or dominant eigenvector. As long as the spectral gap is greater than 0, which means |λ2| < 1, then the random walk converges to a unique dominant eigenvector, and the spectral gap measures the rate of convergence; the larger the spectral gap (the smaller |λ2|), the better the network flow (large hX, diffusion, mixing, random walk, expansion, sparsity, and other highly desirable properties of the network X).

Girth: The girth of X is the smallest positive integer r such that TraceAr>0. Let d=dX be the smallest integer (if it exists), so that for every pair of vertices u,v, there is a walk of length at most d from u to v. Then, dX is called the diameter or maximum eccentricity of the graph X.

Clustering coefficient: The clustering coefficient models the degree of clustering of a subset of nodes. A node is selected, and we see how connected the node is with other nodes that are also connected to it. The clustering coefficient is defined by:

|  |  |
| --- | --- |
| Ci=LiKiKi−1/2 | (3) |

where *Li* is the number of connections between Ki, which are the immediate neighbors of node *i*. The clustering coefficient is used to characterize network modularity, which is a strength of measure of a network division into modules or groups.

Degree distribution: The degree distribution is the number of neighbors connected to a node; in other words, it is the number of edges incident on a node. The degree distribution can give information about the structure of a network. The networks can be directed or undirected. In the undirected case, the degree of a node *i* is the number of connections it has, and it can be represented as an adjacency matrix:

|  |  |
| --- | --- |
| Ki=∑jaij | (4) |

where the sum is over all the nodes. For directed graphs, there are two types of degree distributions: in-degree, which is the number of connections entering the node, and out-degree, which is the number of outgoing connections. For this case, the sum of the *i*th rows and *i*th columns of the adjacency matrix are:

|  |  |
| --- | --- |
| Kitotal=∑jaij+ ∑jaji | (5) |

The degree distribution for a directed graph is the fraction of vertices of degree *kin* and *kout.*

Biomolecular networks such as GRNs follow preferential attachment models, which are scale-free with a degree distribution that follows an exponential law. Unlike the random graph model, these networks have nodes with large degrees, called hubs. Classically, with 0–1 (nonconnection-connection) networks, just the degree distribution is used in the identification of such hubs. A much more sophisticated algorithm is proposed by Kleinberg [[34](#B34-genes-12-00337)], called the HITS algorithm. Originally, it was meant for networks such as the Internet; however, now, it is used to study a variety of biomolecular networks, such as GRNs and Protein–Protein Interaction (PPI) networks [[35](#B35-genes-12-00337),[36](#B36-genes-12-00337)]. Most of these applications use PageRank to reveal localized information about the graph based on some form of external data. We apply this algorithm in our setting for the weighted and directed networks for the transcription factors-target gene networks and for co-expression networks.

In the weighted GRN setting, the traditional simplistic method of detecting hub genes would not yield meaningful information. Our approach uses iteratively the weighted HITS algorithm in a novel way as follows. The weighted HITS algorithm computes the hub h→k (resp. authority a→k) nodes iteratively as: h→k= ψkϕk−1AATh→k−2 and a→k= ϕkψk−1ATAa→k−2. These iterations converge to the dominant eigenvector of the real symmetric matrices AAT (ATA). These give us asymptotically hub and authority weights. A version of this algorithm is implemented and applied to the networks in the software SAGE. Our algorithm gives weighted-hub genes and weighted-authority (target) genes. In complex networks, the HITS algorithm has very high complexity, and cannot be applied successfully. The spectral gap analysis shows that the graphs are sparse but highly connected, helping us carry out HITS with a high degree of iterations. The weighted HITS algorithm has yielded important information about biomolecular networks [[37](#B37-genes-12-00337),[38](#B38-genes-12-00337),[39](#B39-genes-12-00337),[40](#B40-genes-12-00337),[41](#B41-genes-12-00337),[42](#B42-genes-12-00337),[43](#B43-genes-12-00337),[44](#B44-genes-12-00337),[45](#B45-genes-12-00337)]. For network topology, we refer to [[46](#B46-genes-12-00337)], and for the latest on the origin of biomolecular networks, topological, combinatorial, and spectral methods, we refer to [[47](#B47-genes-12-00337)].

## 3. Results and Discussion

The Pearson correlation method is used to generate weighted directed graphs. Two columns of 20,000 samples of gene expression values of Arabidopsis ecotypes WS and Col-0 root growth in spaceflight from GLDS-7 and GLDS-120 datasets are plotted in [Figure 2](#genes-12-00337-f002) (A) and (B), respectively. *X*-axis is the first column of the gene expression values and *y*-axis is the second column of the gene expression values. The plot shows that the values are highly correlated. Hence, PCA is first applied to reduce the dimensionality of the gene expression data to three dimensions. The three PCA components are then used for computing Pearson correlation and generating the network, as explained in [Section 2.2.2](#sec2dot2dot2-genes-12-00337). All the gene expression values from GLDS-7 and GLDS-120 spaceflight and ground data for Arabidopsis WS ecotype root growth are used for generating the networks. In [Table 1](#genes-12-00337-t001), sample correlation values between 13 genes, their t-statistics, and their *p*-values are given. Correlation values range from −1 to 1. *P*-values can also be used to construct GRNs by thresholding them between, for example, 0.01, and 0.0001, which will give the same network as a correlation threshold of 0.05. The threshold can be adjusted depending on the required level of complexity of the inferenced GRN. [Figure 3](#genes-12-00337-f003) and [Figure 4](#genes-12-00337-f004) show sub-graphs extracted from GLDS-7 root growth spaceflight and ground gene expression data, respectively, with a correlation threshold of 0.05. This threshold selects 11.3% of genes from the GLDS-7 dataset and 28.7% genes from the GLDS-120 dataset. These are weighted and directed sub-graphs extracted from the GLDS-7 spaceflight and ground GRNs, respectively. The weights are the correlation values (positive and negative) between the hub gene and the target gene, shown in [Figure 3](#genes-12-00337-f003) and [Figure 4](#genes-12-00337-f004). Negative interactions are important because they show an activation–inhibition two-way expression pattern. While positive correlations indicate shifting, scaling, or geometric pattern in gene expression data, negative correlations indicate opposite and complementary expression patterns, and self-negative regulation of transcription factors (TFs). Hence, we have extracted both maximal positive and negative correlations for constructing the GRNs. These gene interactions have not been validated by follow up experiments; however, they have been constructed from gene expression data obtained originally from experiments conducted in the ISS.

### Figure 2.

[![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/b50293e6ced6/genes-12-00337-g002.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g002.jpg)

[Open in a new tab](figure/genes-12-00337-f002/)

(**A**) Plot of gene expression values for *Arabidopsis thaliana* WS root growth in spaceflight microgravity from GLDS-7 dataset. The plot shows high correlation between the first column (*x*-axis) and second column (*y*-axis) of gene expression values for 20,000 genes. (**B**) Plot of gene expression values for *Arabidopsis thaliana* Col-0 root growth in spaceflight microgravity from GLDS-120 dataset. The plot shows high correlation between the first column (*x*-axis) and second column (*y*-axis) of gene expression values for 20,000 genes.

### Table 1.

Hub genes and target authority genes for 13 hub genes with their correlation value, t-statistics, and *p*-value.

| Interactor Gene A | Interactor Gene B | Correlation | t-Statistics | *p*-Value |
| --- | --- | --- | --- | --- |
| AT1G03430 | AT1G11185 | −0.95787 | −4.716511 | 0.04213 |
| AT1G03430 | AT1G12390 | 0.984801 | 8.018483 | 0.0152 |
| AT1G03430 | AT1G17170 | −0.98068 | −7.090435 | 0.01932 |
| AT1G03430 | AT1G17180 | 0.937057 | 3.795227 | 0.06294 |
| AT1G03430 | AT1G21140 | 0.454929 | 0.722456 | 0.54507 |
| AT1G03430 | AT1G24240 | 0.993113 | 11.98728 | 0.00689 |
| AT1G03430 | AT1G26470 | 0.98765 | 8.914699 | 0.01235 |
| AT1G03430 | AT1G27130 AT1G27140 | 0.998482 | 25.63509 | 0.00152 |
| AT1G03430 | AT1G27570 | −0.95498 | −4.552277 | 0.04502 |
| AT1G03430 | AT1G30360 | 0.9732 | 5.985038 | 0.0268 |
| AT1G03430 | AT1G32460 | 0.4588 | 0.730233 | 0.5412 |
| AT1G03430 | AT1G34180 | −0.99271 | −11.64964 | 0.00729 |
| AT1G03430 | AT1G34844 | 0.947816 | 4.204318 | 0.05218 |

[Open in a new tab](table/genes-12-00337-t001/)

### Figure 3.

[![Figure 3](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/9d9dd5c3f185/genes-12-00337-g003.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g003.jpg)

[Open in a new tab](figure/genes-12-00337-f003/)

Gene regulatory sub-graph for *Arabidopsis thaliana* root growth in spaceflight microgravity. The hub genes are the red circles representing the strong interactions with differentially expressed genes. The target (authority) genes are shown without circles. The weights on the arrows are the correlation values between the hub gene and the target gene.

### Figure 4.

[![Figure 4](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/4f1bff2cda93/genes-12-00337-g004.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g004.jpg)

[Open in a new tab](figure/genes-12-00337-f004/)

Gene regulatory sub-graph for *Arabidopsis thaliana* root growth in the ground control. The hub genes are the red circles representing the strong interactions with differentially expressed genes. The target (authority) genes are shown without circles. The weights on the arrows are the correlation values between the hub gene and the target gene.

[Figure 5](#genes-12-00337-f005)A shows the number of shared genes for Arabidopsis WS and Col-0 ecotypes between GRNs for spaceflight and ground data for both light and dark environments, respectively. [Figure 5](#genes-12-00337-f005)B shows the number of shared genes for the Arabidopsis Col-0 ecotype and Col-0 mutant *phyD* between GRNs for spaceflight and ground data for both light and dark environments, respectively. This helps us to make a secondary comparison between Col-0 ecotype with its mutant *phyD* and shows which hub genes are significantly represented in either case. Among the Arabidopsis ecotypes grown in spaceflight light environments, the GRN of Col-0 mutant *phyD* has 20 hub genes that are not shared with GRN of Col-0 ecotype grown in the same environment. The hub genes of Col-0 mutant *phyD* GRN overlap lesser with those of Col-0 than the overlap of the hub genes between WS and Col-0 GRNs in the light environment. The GRN of Col-0 mutant *phyD* in spaceflight light environment has the lowest number of shared hub genes. The *phyD* gene has a role in Red/Far-Red Light Sensing [[48](#B48-genes-12-00337)]. From our network analysis, we see that manipulation of a gene in an Arabidopsis ecotype can result in significantly different transcriptomic response that makes the biological organism to better adapt to the spaceflight environment [[20](#B20-genes-12-00337)].

### Figure 5.

[![Figure 5](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/7ff50cd6be78/genes-12-00337-g005.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g005.jpg)

[Open in a new tab](figure/genes-12-00337-f005/)

Venn diagrams showing the number of shared hub genes from the gene regulatory networks for *Arabidopsis thaliana*. (**A**) Between the WS and Col-0 ecotypes in spaceflight and ground control for both total light and dark environments. (**B**) Between Col-0 ecotype and Col-0 mutant *phyD* in spaceflight and ground control for both total light and dark environments.

[Figure 6](#genes-12-00337-f006) shows the Pearson correlation gene regulatory sub-graphs extracted from GRNs of the GLDS-120 dataset for the catabolic process for the Arabidopsis WS ecotype root growth in spaceflight light environment. The number of hub genes in the GRN representation can be controlled by suitably adjusting the threshold value. The lower the threshold, larger number of hub genes can be detected and vice versa. In all our networks, we have used a nominal correlation threshold value of 0.05. The original networks have more than 600 genes involved in regulatory pathways. The GSEA of these hub genes present in spaceflight microgravity and ground control GRNs for WS, Col-0, and Col mutant *phyD* ecotypes grown in different light environments are presented below.

### Figure 6.

[![Figure 6](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/e0026e6facb4/genes-12-00337-g006.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g006.jpg)

[Open in a new tab](figure/genes-12-00337-f006/)

Gene regulatory sub-graph for the catabolic process in *Arabidopsis thaliana* Col-0 mutant *phyD* in spaceflight total light environment. The hub genes are the red circles representing the strong interactions with differentially expressed genes. The target (authority) genes are white circles.

### 3.1. Gene Set Enrichment Analysis (GSEA)

The hub genes, shared genes for spaceflight and ground environments, and their gene ontology from the GeneLab GLDS-7 root growth datasets are given in [Table 2](#genes-12-00337-t002). The ShinyGO tool (<http://bioinformatics.sdstate.edu/go/>, accessed on 5 February 2021) is used to perform GSEA of the hub genes for the GeneLab GLDS-7 root growth GRN. The hub genes for spaceflight microgravity and ground overlap considerably and are involved in molecular functions, biological processes, and oxidation-reduction process. They enable NADH dehydrogenase activity, and are involved in NAD and quinone binding. Contrary to GLDS-7 GRN functions, the GRNs constructed for the *Arabidopsis* WS, Col-0, and Col mutant *phyD* show significantly different regulations in spaceflight in total light. These GRNs do share genes with ground control GRNs, but have other genes that show significant transcriptions in spaceflight microgravity, and these genes are not shared by the ground GRNs. Hence, these genes can be considered to be affected by spaceflight microgravity alone. These genes are related to biological processes such as DNA integration, the RNA-dependent DNA biosynthetic process, and the DNA metabolic process. We performed a GSEA analysis comparing hub genes for the WS wild ecotype and Col-0 ecotype. The hub genes for the WS ecotype are associated with biological processes such as the catabolic process, response to abiotic stimulus, localization, multicellular organismal process, developmental process, and anatomical structure development. The hub genes for the Col-0 ecotype perform similar functions to WS ecotype such as the catabolic process, regulation of metabolic process, positive regulation of biological process, cellular response to stimulus, signaling, multicellular organismal process, developmental process, and anatomical structure development. The shared hub genes between the Col-0 ecotype and Col-0 mutant *phyD* perform functions such as regulation of metabolic process, multicellular organismal process, developmental process, positive regulation of biological process, anatomical structure development, and catabolic process. The non-shared hub genes of *phyD* in spaceflight microgravity perform significant functions such as the cellular component organization of biogenesis, response to abiotic stress, and response to external stimulus.

#### Table 2.

Hub genes from the Pearson Correlation GRN and HITS method and shared hub genes for GLDS 7 for *Arabidopsis thaliana* root growth in spaceflight and ground control with their gene ontology.

| *Arabidopsis* Root | ATG Number | Enriched Sene Set (Biological Process) |
| --- | --- | --- |
| Root growth spaceflight hub genes | ATMG00880 ATMG00840 ATMG00660 | Part of mitochondrion; Enables molecular function; Involved in biological process |
| Root growth ground control hub genes | ATMG00720 ATMG01040 ATMG01020 ATMG00580 | Part of mitochondrion Enables molecular function; Involved in biological process; ATP synthesis coupled electron transport; Involved in oxidation-reduction process |
| Shared hub genes for root growth in spaceflight and ground control | ATMG00860 ATMG00510 ATMG00750 ATMG00740 ATMG00720 ATMG00600 ATMG00680 ATMG00820 | Part of mitochondrion Enables molecular function; Involved in biological process; Enables NADH dehydrogenase activity; Part of mitochondrial respiratory chain complex 1; Involved in oxidation-reduction process; Enables NAD binding; quinone binding |

[Open in a new tab](table/genes-12-00337-t002/)

#### 3.1.1. GSEA for Common Hub Genes

Eight common hub genes between the spaceflight and ground environments have been identified, as shown in [Table 2](#genes-12-00337-t002). Using g:Profiler, we found that these genes, including the gene ATMG00600 (ORF 106C), are uncharacterized mitochondrial protein and their function is DNA integration. AT1G04080 is a shared gene between the Col-0 and WS ecotypes, which encodes a U1 small nuclear ribonucleoprotein (snRNP) factor involved in alternative splicing. AT1G02930 and AT1G04980 are the shared genes between the Col-0 and Col-0 mutant *phyD*, which are involved in the defense response to bacterium, glutathione metabolic process, response to cadmium ion, response to oxidative stress, water deprivation, heat, response to unfolded protein, and ubiquitin pathway. The Pearson and LASSO methods have led to the identification of signature sub-networks that show the interaction across several important metabolic and signaling processes, and Transcription Factors (TFs) for *Arabidopsis* growth in spaceflight microgravity. Both methods were able to identify the transcription factors AT1G06040, AT1G01720, and AT1G04850. AT1G06040 encodes salt tolerance protein and AT1G01720 is involved in the cellular response to hypoxia and has a DNA binding TF activity. The TF AT1G04850 is a ubiquitin-associated (UBA)/TS-N domain-containing protein, and its function is zinc ion binding. From the GRNs, we can identify genes with the maximum degree (hub genes) that regulate a larger number of authority (target) genes.

#### 3.1.2. Gene Ontology of Transcription Factors (Genes) in Spaceflight

Thirty-eight hub genes with transcriptional abundance in spaceflight have been identified from the total light environment gene expression datasets of GLDS-120. Their ATG number, gene name, and gene ontology are presented in [Supplementary Table S1](#app1-genes-12-00337). These are hub genes, as their transcriptional responses are abundant only in spaceflight microgravity network and are not found to be hub genes in the corresponding terrestrial GRNs. Hence, these genes are functioning only in spaceflight microgravity conditions. From their ontology, it is evident that they are responsible for important functions necessary for the plant’s growth in an altered environmental setup compared to the terrestrial environment. The plant can sense the changes in abiotic stressors such as gravity, oxygen, and radiation and can step up transcriptional regulation to adapt to the new environment successfully. The transcription functions of these genes are chiefly cell wall biosynthesis, protein transport, stress responses, catabolic processes, auxin, and protein regulation. It is also significant that these genes were identifiable only from the GLDS-120 dataset, which had a different lighting environment in spaceflight. Through novel graph theoretic methods applied to GRNs of *Arabidopsis*, we can explain phenomenological traits that have been observed in spaceflight vis-à-vis on the ground.

### 3.2. Topological and Spectral Analyses of Gene Regulatory Networks

Topological and algebraic analyses of the GRNs are given in [Table 3](#genes-12-00337-t003). The WS ecotype in total light spaceflight environment has the largest spectral gap, which indicates that this network has the highest performance with stable synchronization, rapid convergence, mixing, expansion, and diffusion [[47](#B47-genes-12-00337)]. Random walks propagate more easily in networks with a large spectral gap. The large spectral gap has also made several algorithms we use tractable for such massively large GRN and indicates that in technical terms, these GRNs are highly sparse. This corroborates with results from other studies that have shown that the WS genotype increases the transcriptional cost of spaceflight adaptation [[20](#B20-genes-12-00337)]. The diameter of this network is 6, indicating that it has longer gene signaling pathways, and the hub genes of this network regulate about 1000 target genes. The WS and Col-0 ecotypes in the ground light environment show topological similarities with the same shortest path length, and the two networks show regulation of about 45 target genes.

#### Table 3.

Topological and spectral analysis for *Arabidopsis* (AT) spaceflight and ground gene regulatory networks.

| Dataset | Spectral Gap | Average Clustering Coefficient | Average Shortest Path Length (Distance) | Diameter (Maximum Eccentricity) | Authority Genes (Outdegree) |
| --- | --- | --- | --- | --- | --- |
| AT root spaceflight | 39.228 | 0.00897 | 1.452 | 3 | 95 |
| AT root ground | 59.96 | 0.00315 | 1.2017 | 3 | 166 |
| AT WS spaceflight light | 72.9 | 0.01272 | 1.89 | 6 | 1237.04 |
| AT WS ground light | 0.45 | 0.01788 | 1.11 | 2 | 45.63 |
| AT WS spaceflight dark | 3.99 | 0.01996 | 1.069 | 2 | 50.41 |
| AT WS ground dark | 2.32 | 0.02011 | 1.069 | 3 | 43.36 |
| AT *phyD* spaceflight light | 0.79 | 0.01000 | 1.036 | 2 | 35 |
| AT *phyD* ground light | 0.22 | 0.01996 | 1.069 | 2 | 50.41 |
| AT *phyD* spaceflight dark | 0.001 | 0.01219 | 1.146 | 2 | 38.24 |
| AT *phyD* ground dark | 3.15 | 0.0219 | 1.125 | 2 | 53.29 |
| AT Col-0 spaceflight light | 0.13 | 0.0212 | 1.107 | 2 | 40.26 |
| AT Col-0 ground light | 4.00 | 0.0146 | 1.113 | 2 | 44.28 |
| AT Col-0 spaceflight dark | 0.20 | 0.0224 | 1.066 | 1 | 29.09 |
| AT Col-0 ground dark | 2.67 | 0.0187 | 1.076 | 1 | 33.42 |

[Open in a new tab](table/genes-12-00337-t003/)

We show, with our spectral analysis methods, through the spectral estimates on the Cheeger constant that our networks are sparse, that the HITS algorithm works much faster, and we have been able to identify hubs and authority nodes (genes) in the networks. Rather than just the degree distribution, hubs and authority nodes are computed iteratively with newer algorithms considering weights using its implementation in the software SAGEMATH. Improved algorithms exist, e.g., [[35](#B35-genes-12-00337)], and some of Kleinberg’s works.

### 3.3. Arabidopsis Root Growth and Cell Wall Biosynthesis in Spaceflight Microgravity

Out of the 33 root-growth related genes of *Arabidopsis*, we have identified five significant hub genes listed in [Table 4](#genes-12-00337-t004) to have higher regulations in spaceflight. [Figure 7](#genes-12-00337-f007) shows the subgraph that is extracted from the original Pearson correlation GRN by thresholding the genes with higher correlation values and involved in the cell wall biosynthesis metabolic process that relates the co-expression of these genes in spaceflight microgravity for the *Arabidopsis* Col mutant *phyD* ecotype. These five hub genes have higher regulations only in the spaceflight subgraph for the cell wall response process and not in the ground subgraph. These genes are over-represented in the spaceflight responsive transcriptome because they regulate plant growth in spaceflight microgravity and enable adaptation of the plant to the altered environment. Similarly, comparing the GRNs generated by the LASSO method for *Arabidopsis* WS ecotype in spaceflight and ground environments, the hub genes that are involved only in spaceflight for cell wall biosynthesis have been identified and listed in [Supplementary Table S2](#app1-genes-12-00337). [Figure 8](#genes-12-00337-f008) shows the subgraph for the cell wall biosynthesis process for *Arabidopsis* WS ecotype in spaceflight microgravity, which is also extracted similarly by thresholding the correlation values. These genes encode NSEs and have higher transcriptional regulation in spaceflight, as they were not found to be hubs in the GRNs for the terrestrial datasets. These enzymes catalyze a series of biochemical reactions and are involved in building cell wall polysaccharides. The origin and divergence of these enzymes is not known, and it is interesting to note that they are significantly transcribed indicative of higher sugar diversity in spaceflight microgravity. The higher regulations of these genes may be the reason for the phenotypic skewing or waving effect found in the roots, as well as other parts of the plant in spaceflight. The differential transcriptions of NSEs indicate that they regulate developmental, metabolic, and stress-related responses in the spaceflight microgravity environment.

#### Table 4.

Root growth hub genes with transcriptional abundance in spaceflight microgravity and their most prominent gene ontology.

| ATG Number | Hub Gene Name/Description | Enriched Gene Set (Biological Process) |
| --- | --- | --- |
| AT2G36870 | *XTH32* | Involved in cellular glucan metabolic process |
| AT2G18800 | *XTH21* | Involved in cell wall organization |
| AT3G44990 | *XTH31* | Involved in glucanase activity |
| AT3G23730 | *XTH16* | Involved in the metabolic process |
| AT2G14620 | *XTH10* | Involved in cellular glucan metabolic process |

[Open in a new tab](table/genes-12-00337-t004/)

#### Figure 7.

[![Figure 7](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/49d27f6c7457/genes-12-00337-g007.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g007.jpg)

[Open in a new tab](figure/genes-12-00337-f007/)

Gene regulatory sub-graph involving root growth genes in *Arabidopsis thaliana* Col-0 mutant *phyD* in spaceflight total light environment. The hub genes are the red circles representing the strong interactions with differentially expressed genes. The target (authority) genes are white circles. The hub genes that have a higher degree distribution are larger in size.

#### Figure 8.

[![Figure 8](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/cba7/7996555/f611c39a089a/genes-12-00337-g008.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=7996555_genes-12-00337-g008.jpg)

[Open in a new tab](figure/genes-12-00337-f008/)

Gene regulatory sub-graph for the process of cell wall biosynthesis in *Arabidopsis thaliana* WS ecotype in spaceflight total light environment.

## 4. Conclusions

Graph-based network analysis methods and results have been presented for transcriptomic regulatory GeneLab *Arabidopsis* datasets. Previous studies were at the transcriptomic level. In this article, we have built gene regulatory networks for different ecotypes (via Pearson Correlation and LASSO methods), carried out both topological and algebraic network studies (the novel HITS algorithm for weighted and directed graphs to identify hubs and authority nodes), computed the spectral gap for the whole GRN, leading us to potential conclusions about phenomena such as diffusion and expansion of the GRN, and studied global and local topological parameters, such as clustering, average path length, eccentricity, and degree distribution. Therefore, our research is more complementary to prior studies and is more rigorous. Our novel graph-theoretic approach isolated hub genes regulated significantly different in spaceflight microgravity from terrestrial gene expressions. The GRN for the WS ecotype in spaceflight has the highest spectral gap, indicating that it has the highest transcriptional cost in spaceflight. GRN analysis showed that there are 38 genes with higher transcriptions in spaceflight microgravity and are involved in vital molecular and biological functions for the survival and growth of the plant in spaceflight.

While previous research has identified altered spaceflight transcriptions for cell wall remodeling, we have identified hub genes with higher transcriptional activity and that are involved in the cell wall response process only in spaceflight GRN; these hub genes are essentially metabolic phenotypes. The network analysis has detected xyloglucan endo-trans glycosylase/hydrolases (*XTHs*) that are cell wall modifying enzymes mediating vital elongation growth of *Arabidopsis* in spaceflight. The *XTHs* act on the cell wall, making it more extensible, resulting in cellular expansion and the skewing phenomenon of the roots in spaceflight microgravity.

Through advanced network analysis, we can shorten the gap between genotype to phenotype analysis by identifying primary metabolites or metabolic phenotypes involved in the growth of plants in spaceflight for bioregenerative life support. In the absence of mass spectroscopy, hyperspectral imaging methods in the ISS, and lack of plant physiological measurements, genome to phenome network analysis offers an alternative for identifying primary metabolic phenotypes. The spaceflight response of these metabolites can be further correlated with phenotypic data extracted from images and metabolomics datasets acquired from experiments conducted in the ISS or from similar experiments on the ground. Phenotypic data will enable novel trait correlations employing genome to phenome network analysis.

## Acknowledgments

The material contained in this document is based upon work supported by the National Aeronautics and Space Administration (NASA) grant 80NSSC19M0167. Carlos A. Agrinsoni’s work is supported by the NASA Training Grant No. NNX15AI11H. Opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of NASA.

## Supplementary Materials

The following are available online at <https://www.mdpi.com/2073-4425/12/3/337/s1>, The genelab datasets are available at <http://www.genelab.nasa.gov/>. Table S1: Hub genes differentially and significantly expressed only in spaceflight microgravity networks for each of the ecotypes, with their gene name and most prominent gene ontology; Table S2: Hub genes related to cell wall biosynthesis processes with transcriptional abundance in spaceflight microgravity, gene name and their most prominent gene ontology.

[Click here for additional data file.](/articles/instance/7996555/bin/genes-12-00337-s001.pdf) (112.9KB, pdf)

## Author Contributions

Conceptualization, V.M. and H.J.; methodology, V.M., J.O., H.G., and C.A.; software, J.O., H.G., and C.A.; validation, J.O., H.G., and C.A.; formal analysis, V.M. and J.O.; investigation, V.M., H.J.; resources, V.M., J.O., H.J., H.G., C.A.; data curation, J.O.; writing—original draft preparation, V.M.; writing—review and editing, V.M. and H.J.; visualization, V.M. and J.O.; supervision, V.M. and H.J.; project administration, V.M.; funding acquisition, V.M. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by NASA, grant number 80NSSC19M0167.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

<https://www.genelab.nasa.gov/>.

## Conflicts of Interest

The authors declare no conflict of interest.

## Footnotes

**Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## References

* 1.Hoson T. Plant growth and morphogenesis under different gravity conditions: Relevance to plant life in space. Life. 2014;4:205–216. doi: 10.3390/life4020205. [[DOI](https://doi.org/10.3390/life4020205)] [[PMC free article](/articles/PMC4187158/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25370193/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Life&title=Plant%20growth%20and%20morphogenesis%20under%20different%20gravity%20conditions:%20Relevance%20to%20plant%20life%20in%20space&author=T.%20Hoson&volume=4&publication_year=2014&pages=205-216&pmid=25370193&doi=10.3390/life4020205&)]
* 2.Koornneef M., Meinke D. The development of Arabidopsis as a model plant. Plant J. 2010;61:909–921. doi: 10.1111/j.1365-313X.2009.04086.x. [[DOI](https://doi.org/10.1111/j.1365-313X.2009.04086.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20409266/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20J.&title=The%20development%20of%20Arabidopsis%20as%20a%20model%20plant&author=M.%20Koornneef&author=D.%20Meinke&volume=61&publication_year=2010&pages=909-921&pmid=20409266&doi=10.1111/j.1365-313X.2009.04086.x&)]
* 3.Paul A.L., Zupanska A.K., Schultz E.R., Ferl R.J. Organ-specific remodeling of the Arabidopsis transcriptome in response to spaceflight. BMC Plant Biol. 2013;13:112. doi: 10.1186/1471-2229-13-112. [[DOI](https://doi.org/10.1186/1471-2229-13-112)] [[PMC free article](/articles/PMC3750915/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23919896/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=Organ-specific%20remodeling%20of%20the%20Arabidopsis%20transcriptome%20in%20response%20to%20spaceflight&author=A.L.%20Paul&author=A.K.%20Zupanska&author=E.R.%20Schultz&author=R.J.%20Ferl&volume=13&publication_year=2013&pages=112&pmid=23919896&doi=10.1186/1471-2229-13-112&)]
* 4.Kamal K.Y., van Loon J.J.W.A., Medina F.J., Herranz R. Differential transcriptional profile through cell cycle progression in Arabidopsis cultures under simulated microgravity. Genomics. 2019;111:1956–1965. doi: 10.1016/j.ygeno.2019.01.007. [[DOI](https://doi.org/10.1016/j.ygeno.2019.01.007)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30641127/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genomics&title=Differential%20transcriptional%20profile%20through%20cell%20cycle%20progression%20in%20Arabidopsis%20cultures%20under%20simulated%20microgravity&author=K.Y.%20Kamal&author=J.J.W.A.%20van%20Loon&author=F.J.%20Medina&author=R.%20Herranz&volume=111&publication_year=2019&pages=1956-1965&pmid=30641127&doi=10.1016/j.ygeno.2019.01.007&)]
* 5.Kimbrough J.M. The fast and transient transcriptional network of gravity and mechanical stimulation in the Arabidopsis root Apex. Plant Physiol. 2004;136:1–16. doi: 10.1104/pp.104.044594. [[DOI](https://doi.org/10.1104/pp.104.044594)] [[PMC free article](/articles/PMC523342/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15347791/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Physiol.&title=The%20fast%20and%20transient%20transcriptional%20network%20of%20gravity%20and%20mechanical%20stimulation%20in%20the%20Arabidopsis%20root%20Apex&author=J.M.%20Kimbrough&volume=136&publication_year=2004&pages=1-16&pmid=15347791&doi=10.1104/pp.104.044594&)]
* 6.Kiss J.Z., Wolverton C., Wyatt S.E., Hasenstein K.H., Van Loon J.J.W.A. Comparison of Microgravity Analogs to Spaceflight in Studies of Plant Growth and Development. Front. Plant Sci. 2019 doi: 10.3389/fpls.2019.01577. [[DOI](https://doi.org/10.3389/fpls.2019.01577)] [[PMC free article](/articles/PMC6908503/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31867033/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=Comparison%20of%20Microgravity%20Analogs%20to%20Spaceflight%20in%20Studies%20of%20Plant%20Growth%20and%20Development&author=J.Z.%20Kiss&author=C.%20Wolverton&author=S.E.%20Wyatt&author=K.H.%20Hasenstein&author=J.J.W.A.%20Van%20Loon&publication_year=2019&pmid=31867033&doi=10.3389/fpls.2019.01577&)]
* 7.Meyer R.C., Steinfath M., Lisec J., Becher M., Witucka-Wall H., Torjek O., Fiehn O., Eckardt A., Willmitzer L., Selbig J., et al. The metabolic signature related to high plant growth rate in Arabidopsis thaliana. Proc. Natl. Acad. Sci. USA. 2007;104:4759–4764. doi: 10.1073/pnas.0609709104. [[DOI](https://doi.org/10.1073/pnas.0609709104)] [[PMC free article](/articles/PMC1810331/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17360597/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proc.%20Natl.%20Acad.%20Sci.%20USA&title=The%20metabolic%20signature%20related%20to%20high%20plant%20growth%20rate%20in%20Arabidopsis%20thaliana&author=R.C.%20Meyer&author=M.%20Steinfath&author=J.%20Lisec&author=M.%20Becher&author=H.%20Witucka-Wall&volume=104&publication_year=2007&pages=4759-4764&pmid=17360597&doi=10.1073/pnas.0609709104&)]
* 8.Ferl R.J., Koh J., Denison F., Paul A.L. Spaceflight induces specific alterations in the proteomes of Arabidopsis. Astrobiology. 2015;15:32–56. doi: 10.1089/ast.2014.1210. [[DOI](https://doi.org/10.1089/ast.2014.1210)] [[PMC free article](/articles/PMC4290804/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25517942/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Astrobiology&title=Spaceflight%20induces%20specific%20alterations%20in%20the%20proteomes%20of%20Arabidopsis&author=R.J.%20Ferl&author=J.%20Koh&author=F.%20Denison&author=A.L.%20Paul&volume=15&publication_year=2015&pages=32-56&pmid=25517942&doi=10.1089/ast.2014.1210&)]
* 9.Johnson C.M., Subramanian A., Pattathil S., Correll M.J., Kiss J.Z. Comparative transcriptomics indicate changes in cell wall organization and stress response in seedlings during spaceflight. Am. J. Bot. 2017;104:1219–1231. doi: 10.3732/ajb.1700079. [[DOI](https://doi.org/10.3732/ajb.1700079)] [[PMC free article](/articles/PMC5821596/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28827451/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Bot.&title=Comparative%20transcriptomics%20indicate%20changes%20in%20cell%20wall%20organization%20and%20stress%20response%20in%20seedlings%20during%20spaceflight&author=C.M.%20Johnson&author=A.%20Subramanian&author=S.%20Pattathil&author=M.J.%20Correll&author=J.Z.%20Kiss&volume=104&publication_year=2017&pages=1219-1231&pmid=28827451&doi=10.3732/ajb.1700079&)]
* 10.Somssich M., Khan G.A., Staffan S.P. Cell wall heterogeneity in root development of Arabidopsis. Front. Plant Sci. 2016;7:1–11. doi: 10.3389/fpls.2016.01242. [[DOI](https://doi.org/10.3389/fpls.2016.01242)] [[PMC free article](/articles/PMC4987334/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27582757/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=Cell%20wall%20heterogeneity%20in%20root%20development%20of%20Arabidopsis&author=M.%20Somssich&author=G.A.%20Khan&author=S.P.%20Staffan&volume=7&publication_year=2016&pages=1-11&pmid=27582757&doi=10.3389/fpls.2016.01242&)]
* 11.Yin Y., Huang J., Gu X., Bar-Peled M., Xu Y. Evolution of plant nucleotide-sugar interconversion enzymes. PLoS ONE. 2011;6:e27995. doi: 10.1371/journal.pone.0027995. [[DOI](https://doi.org/10.1371/journal.pone.0027995)] [[PMC free article](/articles/PMC3220709/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22125650/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20ONE&title=Evolution%20of%20plant%20nucleotide-sugar%20interconversion%20enzymes&author=Y.%20Yin&author=J.%20Huang&author=X.%20Gu&author=M.%20Bar-Peled&author=Y.%20Xu&volume=6&publication_year=2011&pages=e27995&pmid=22125650&doi=10.1371/journal.pone.0027995&)]
* 12.Reiter W., Vanzin G.F. Molecular genetics of nucleotide sugar interconversion pathways in plants. Plant Mol. Biol. 2001;47:95–113. doi: 10.1023/A:1010671129803. [[DOI](https://doi.org/10.1023/A%3A1010671129803)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11554483/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Mol.%20Biol.&title=Molecular%20genetics%20of%20nucleotide%20sugar%20interconversion%20pathways%20in%20plants&author=W.%20Reiter&author=G.F.%20Vanzin&volume=47&publication_year=2001&pages=95-113&pmid=11554483&doi=10.1023/A:1010671129803&)]
* 13.Seifert G.J. Nucleotide sugar interconversions and cell wall biosynthesis: How to bring the inside to the outside. Curr. Opin. Plant Biol. 2004;7:277–284. doi: 10.1016/j.pbi.2004.03.004. [[DOI](https://doi.org/10.1016/j.pbi.2004.03.004)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15134748/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Opin.%20Plant%20Biol.&title=Nucleotide%20sugar%20interconversions%20and%20cell%20wall%20biosynthesis:%20How%20to%20bring%20the%20inside%20to%20the%20outside&author=G.J.%20Seifert&volume=7&publication_year=2004&pages=277-284&pmid=15134748&doi=10.1016/j.pbi.2004.03.004&)]
* 14.Cai B., Li C.H., Huang J. Systematic identification of cell-wall related genes in populus based on analysis of functional modules in co-expression network. PLoS ONE. 2014;9:e95176. doi: 10.1371/journal.pone.0095176. [[DOI](https://doi.org/10.1371/journal.pone.0095176)] [[PMC free article](/articles/PMC3988181/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24736620/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20ONE&title=Systematic%20identification%20of%20cell-wall%20related%20genes%20in%20populus%20based%20on%20analysis%20of%20functional%20modules%20in%20co-expression%20network&author=B.%20Cai&author=C.H.%20Li&author=J.%20Huang&volume=9&publication_year=2014&pages=e95176&pmid=24736620&doi=10.1371/journal.pone.0095176&)]
* 15.Wang S., Yin Y., Ma Q., Tang X., Hao D., Xu Y. Genome-scale identification of cell-wall related genes in Arabidopsis based on co-expression network analysis. BMC Plant Biol. 2012;12:1. doi: 10.1186/1471-2229-12-138. [[DOI](https://doi.org/10.1186/1471-2229-12-138)] [[PMC free article](/articles/PMC3463447/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22877077/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=Genome-scale%20identification%20of%20cell-wall%20related%20genes%20in%20Arabidopsis%20based%20on%20co-expression%20network%20analysis&author=S.%20Wang&author=Y.%20Yin&author=Q.%20Ma&author=X.%20Tang&author=D.%20Hao&volume=12&publication_year=2012&pages=1&pmid=22877077&doi=10.1186/1471-2229-12-138&)]
* 16.Choi W.G., Barker R.J., Kim S.H., Swanson S.J., Gilroy S. Variation in the transcriptome of different ecotypes of Arabidopsis thaliana reveals signatures of oxidative stress in plant responses to spaceflight. Am. J. Bot. 2019;106:123–136. doi: 10.1002/ajb2.1223. [[DOI](https://doi.org/10.1002/ajb2.1223)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30644539/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Am.%20J.%20Bot.&title=Variation%20in%20the%20transcriptome%20of%20different%20ecotypes%20of%20Arabidopsis%20thaliana%20reveals%20signatures%20of%20oxidative%20stress%20in%20plant%20responses%20to%20spaceflight&author=W.G.%20Choi&author=R.J.%20Barker&author=S.H.%20Kim&author=S.J.%20Swanson&author=S.%20Gilroy&volume=106&publication_year=2019&pages=123-136&pmid=30644539&doi=10.1002/ajb2.1223&)]
* 17.Herranz R., Vanderbrink J.P., Villacampa A., Manzano A., Poehlman W.L., Feltus F.A., Kiss J.Z., Medina F.J. RNAseq analysis of the response of Arabidopsis thaliana to fractional gravity under blue-light stimulation during spaceflight. Front. Plant Sci. 2019;10:1–11. doi: 10.3389/fpls.2019.01529. [[DOI](https://doi.org/10.3389/fpls.2019.01529)] [[PMC free article](/articles/PMC6889863/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31850027/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=RNAseq%20analysis%20of%20the%20response%20of%20Arabidopsis%20thaliana%20to%20fractional%20gravity%20under%20blue-light%20stimulation%20during%20spaceflight&author=R.%20Herranz&author=J.P.%20Vanderbrink&author=A.%20Villacampa&author=A.%20Manzano&author=W.L.%20Poehlman&volume=10&publication_year=2019&pages=1-11&pmid=31850027&doi=10.3389/fpls.2019.01529&)]
* 18.Paul A.L., Zupanska A.K., Ostrow D.T., Zhang Y., Sun Y., Li J.L., Shanker S., Farmerie W.G., Amalfitano C.E., Ferl R.J. Spaceflight transcriptomes: Unique responses to a novel environment. Astrobiology. 2012;12:40–56. doi: 10.1089/ast.2011.0696. [[DOI](https://doi.org/10.1089/ast.2011.0696)] [[PMC free article](/articles/PMC3264962/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22221117/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Astrobiology&title=Spaceflight%20transcriptomes:%20Unique%20responses%20to%20a%20novel%20environment&author=A.L.%20Paul&author=A.K.%20Zupanska&author=D.T.%20Ostrow&author=Y.%20Zhang&author=Y.%20Sun&volume=12&publication_year=2012&pages=40-56&pmid=22221117&doi=10.1089/ast.2011.0696&)]
* 19.Paul A.L., Zhou M., Callaham J., Reyes M., Stasiak M., Riva A., Zupanska A.K., Dixon M., Ferl R. Patterns of Arabidopsis gene expression in the face of hypobaric stress. AoB Plants. 2017;9:1–19. doi: 10.1093/aobpla/plx030. [[DOI](https://doi.org/10.1093/aobpla/plx030)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=AoB%20Plants&title=Patterns%20of%20Arabidopsis%20gene%20expression%20in%20the%20face%20of%20hypobaric%20stress&author=A.L.%20Paul&author=M.%20Zhou&author=J.%20Callaham&author=M.%20Reyes&author=M.%20Stasiak&volume=9&publication_year=2017&pages=1-19&doi=10.1093/aobpla/plx030&)]
* 20.Paul A.L., Sng N.J., Zupanska A.K., Krishnamurthy A., Schultz E.R., Ferl R.J. Genetic dissection of the Arabidopsis spaceflight transcriptome: Are some responses dispensable for the physiological adaptation of plants to spaceflight? PLoS ONE. 2017;12:1–24. doi: 10.1371/journal.pone.0180186. [[DOI](https://doi.org/10.1371/journal.pone.0180186)] [[PMC free article](/articles/PMC5491145/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28662188/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20ONE&title=Genetic%20dissection%20of%20the%20Arabidopsis%20spaceflight%20transcriptome:%20Are%20some%20responses%20dispensable%20for%20the%20physiological%20adaptation%20of%20plants%20to%20spaceflight?&author=A.L.%20Paul&author=N.J.%20Sng&author=A.K.%20Zupanska&author=A.%20Krishnamurthy&author=E.R.%20Schultz&volume=12&publication_year=2017&pages=1-24&pmid=28662188&doi=10.1371/journal.pone.0180186&)]
* 21.Dayanne D. Multi-study inference of regulatory networks for more accurate models of gene regulation. PLoS Comput. Biol. 2019;15:1–22. doi: 10.1101/279224. [[DOI](https://doi.org/10.1101/279224)] [[PMC free article](/articles/PMC6363223/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30677040/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20Comput.%20Biol.&title=Multi-study%20inference%20of%20regulatory%20networks%20for%20more%20accurate%20models%20of%20gene%20regulation&author=D.%20Dayanne&volume=15&publication_year=2019&pages=1-22&pmid=30677040&doi=10.1101/279224&)]
* 22.Needham C.J., Manfield I.W., Bulpitt A.J., Gilmartin P.M., Westhead D.R. From gene expression to gene regulatory networks in Arabidopsis thaliana. BMC Syst. Biol. 2009;3:85. doi: 10.1186/1752-0509-3-85. [[DOI](https://doi.org/10.1186/1752-0509-3-85)] [[PMC free article](/articles/PMC2760521/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19728870/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Syst.%20Biol.&title=From%20gene%20expression%20to%20gene%20regulatory%20networks%20in%20Arabidopsis%20thaliana&author=C.J.%20Needham&author=I.W.%20Manfield&author=A.J.%20Bulpitt&author=P.M.%20Gilmartin&author=D.R.%20Westhead&volume=3&publication_year=2009&pages=85&pmid=19728870&doi=10.1186/1752-0509-3-85&)]
* 23.Mochida K., Koda S., Inoue K., Nishii R. Statistical and machine learning approaches to predict gene regulatory networks from transcriptome datasets. Front. Plant Sci. 2018;871:1–7. doi: 10.3389/fpls.2018.01770. [[DOI](https://doi.org/10.3389/fpls.2018.01770)] [[PMC free article](/articles/PMC6281826/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30555503/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Plant%20Sci.&title=Statistical%20and%20machine%20learning%20approaches%20to%20predict%20gene%20regulatory%20networks%20from%20transcriptome%20datasets&author=K.%20Mochida&author=S.%20Koda&author=K.%20Inoue&author=R.%20Nishii&volume=871&publication_year=2018&pages=1-7&pmid=30555503&doi=10.3389/fpls.2018.01770&)]
* 24.Pratapa A., Jalihal A.P., Law J.N., Bharadwaj A., Murali T.M. Benchmarking algorithms for gene regulatory network inference from single-cell transcriptomic data. Nat. Methods. 2019;17:147–154. doi: 10.1038/s41592-019-0690-6. [[DOI](https://doi.org/10.1038/s41592-019-0690-6)] [[PMC free article](/articles/PMC7098173/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31907445/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Methods&title=Benchmarking%20algorithms%20for%20gene%20regulatory%20network%20inference%20from%20single-cell%20transcriptomic%20data&author=A.%20Pratapa&author=A.P.%20Jalihal&author=J.N.%20Law&author=A.%20Bharadwaj&author=T.M.%20Murali&volume=17&publication_year=2019&pages=147-154&pmid=31907445&doi=10.1038/s41592-019-0690-6&)]
* 25.De Lucas M., Brady S.M. Gene regulatory networks in the Arabidopsis root. Curr. Opin. Plant Biol. 2013;16:50–55. doi: 10.1016/j.pbi.2012.10.007. [[DOI](https://doi.org/10.1016/j.pbi.2012.10.007)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23196272/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Opin.%20Plant%20Biol.&title=Gene%20regulatory%20networks%20in%20the%20Arabidopsis%20root&author=M.%20De%20Lucas&author=S.M.%20Brady&volume=16&publication_year=2013&pages=50-55&pmid=23196272&doi=10.1016/j.pbi.2012.10.007&)]
* 26.El-Showk S., Taylor-Teeples M., Helariutta Y., Brady S.M. Gene regulatory networks during Arabidopsis root vascular development. Int. J. Plant Sci. 2013;174:1090–1097. doi: 10.1086/671449. [[DOI](https://doi.org/10.1086/671449)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Int.%20J.%20Plant%20Sci.&title=Gene%20regulatory%20networks%20during%20Arabidopsis%20root%20vascular%20development&author=S.%20El-Showk&author=M.%20Taylor-Teeples&author=Y.%20Helariutta&author=S.M.%20Brady&volume=174&publication_year=2013&pages=1090-1097&doi=10.1086/671449&)]
* 27.Taylor-Teeples M., Lin L., de Lucas M., Turco G., Toal T.W., Gaudinier A., Young N.F., Trabucco G.M., Veling M.T., Lamothe R., et al. An Arabidopsis gene regulatory network for secondary cell wall synthesis. Nature. 2015;517:571–575. doi: 10.1038/nature14099. [[DOI](https://doi.org/10.1038/nature14099)] [[PMC free article](/articles/PMC4333722/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25533953/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature&title=An%20Arabidopsis%20gene%20regulatory%20network%20for%20secondary%20cell%20wall%20synthesis&author=M.%20Taylor-Teeples&author=L.%20Lin&author=M.%20de%20Lucas&author=G.%20Turco&author=T.W.%20Toal&volume=517&publication_year=2015&pages=571-575&pmid=25533953&doi=10.1038/nature14099&)]
* 28.Doroshkov A.V., Konstantinov D.K., Afonnikov D.A., Gunbin K.V. The evolution of gene regulatory networks controlling Arabidopsis thaliana L. trichome development. BMC Plant Biol. 2019;19:53. doi: 10.1186/s12870-019-1640-2. [[DOI](https://doi.org/10.1186/s12870-019-1640-2)] [[PMC free article](/articles/PMC6393967/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30813891/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Plant%20Biol.&title=The%20evolution%20of%20gene%20regulatory%20networks%20controlling%20Arabidopsis%20thaliana%20L.%20trichome%20development&author=A.V.%20Doroshkov&author=D.K.%20Konstantinov&author=D.A.%20Afonnikov&author=K.V.%20Gunbin&volume=19&publication_year=2019&pages=53&pmid=30813891&doi=10.1186/s12870-019-1640-2&)]
* 29.Hehl R., Bulow L. AthaMap Web Tools for the Analysis of Transcriptional and Posttranscriptional Regulation of Gene Expression in Arabidopsis thaliana. Plant Circadian Networks. Volume 1158. Humana Press; New York, NY, USA: 2014. Methods in Molecular Biology. [[DOI](https://doi.org/10.1007/978-1-4939-0700-7_9)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24792049/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=AthaMap%20Web%20Tools%20for%20the%20Analysis%20of%20Transcriptional%20and%20Posttranscriptional%20Regulation%20of%20Gene%20Expression%20in%20Arabidopsis%20thaliana.%20Plant%20Circadian%20Networks&author=R.%20Hehl&author=L.%20Bulow&publication_year=2014&)]
* 30.Biggs N. Algebraic Graph Theory. 2nd ed. Cambridge University Press; Cambridge, UK: 1993.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Algebraic%20Graph%20Theory&author=N.%20Biggs&publication_year=1993&)]
* 31.Du Q., Campbell M., Yu H., Liu K., Walia H., Zhang Q., Zhang C. Network-based feature selection reveals substructures of gene modules responding to salt stress in rice. Plant Direct. 2019;3:e00154. doi: 10.1002/pld3.154. [[DOI](https://doi.org/10.1002/pld3.154)] [[PMC free article](/articles/PMC6689793/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31417977/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Direct&title=Network-based%20feature%20selection%20reveals%20substructures%20of%20gene%20modules%20responding%20to%20salt%20stress%20in%20rice&author=Q.%20Du&author=M.%20Campbell&author=H.%20Yu&author=K.%20Liu&author=H.%20Walia&volume=3&publication_year=2019&pages=e00154&pmid=31417977&doi=10.1002/pld3.154&)]
* 32.Zhang R., Ren Z., Chen W. SILGGM: An extensive R package for efficient statistical inference in large-scale gene networks. PLoS Comput. Biol. 2018;14:e1006369. doi: 10.1371/journal.pcbi.1006369. [[DOI](https://doi.org/10.1371/journal.pcbi.1006369)] [[PMC free article](/articles/PMC6107288/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30102702/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20Comput.%20Biol.&title=SILGGM:%20An%20extensive%20R%20package%20for%20efficient%20statistical%20inference%20in%20large-scale%20gene%20networks&author=R.%20Zhang&author=Z.%20Ren&author=W.%20Chen&volume=14&publication_year=2018&pages=e1006369&pmid=30102702&doi=10.1371/journal.pcbi.1006369&)]
* 33.Serre J.-P. Trees. Springer-Verlag; Berlin/Heidelberg, Germany: 1980.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Trees&author=J.-P.%20Serre&publication_year=1980&)]
* 34.Kleinberg J.M. Authoritative sources in a hyperlinked environment. J. ACM. 1999;46:604–632. doi: 10.1145/324133.324140. [[DOI](https://doi.org/10.1145/324133.324140)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20ACM&title=Authoritative%20sources%20in%20a%20hyperlinked%20environment&author=J.M.%20Kleinberg&volume=46&publication_year=1999&pages=604-632&doi=10.1145/324133.324140&)]
* 35.Lei X., Wang S., Wu F.X. Identification of essential proteins based on improved HITS algorithm. Genes. 2019;10:177. doi: 10.3390/genes10020177. [[DOI](https://doi.org/10.3390/genes10020177)] [[PMC free article](/articles/PMC6409685/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30823614/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genes&title=Identification%20of%20essential%20proteins%20based%20on%20improved%20HITS%20algorithm&author=X.%20Lei&author=S.%20Wang&author=F.X.%20Wu&volume=10&publication_year=2019&pages=177&pmid=30823614&doi=10.3390/genes10020177&)]
* 36.Easley D., Kleinberg J. Networks, Crowds, and Markets. Cambridge University Press; Cambridge, UK: 2010.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Networks,%20Crowds,%20and%20Markets&author=D.%20Easley&author=J.%20Kleinberg&publication_year=2010&)]
* 37.Miller J.C., Rae G., Schaefer F., Ward L.A., LoFaro T., Farahat A. Modifications of Kleinberg’s HITS algorithm using matrix exponentiation and web log records; Proceedings of the 24th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval; New Orleans, LA, USA. 9–13 September 2001; pp. 444–445. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%2024th%20Annual%20International%20ACM%20SIGIR%20Conference%20on%20Research%20and%20Development%20in%20Information%20Retrieval&title=Modifications%20of%20Kleinberg%E2%80%99s%20HITS%20algorithm%20using%20matrix%20exponentiation%20and%20web%20log%20records&author=J.C.%20Miller&author=G.%20Rae&author=F.%20Schaefer&author=L.A.%20Ward&author=T.%20LoFaro&pages=444-445&)]
* 38.Langville A.N., Meyer C.D. A survey of eigenvector methods for web information retrieval. SIAM Rev. 2005;47:135–161. doi: 10.1137/S0036144503424786. [[DOI](https://doi.org/10.1137/S0036144503424786)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=SIAM%20Rev.&title=A%20survey%20of%20eigenvector%20methods%20for%20web%20information%20retrieval&author=A.N.%20Langville&author=C.D.%20Meyer&volume=47&publication_year=2005&pages=135-161&doi=10.1137/S0036144503424786&)]
* 39.Emms D.M., Kelly S. OrthoFinder: Solving fundamental biases in whole genome comparisons dramatically improves orthogroup inference accuracy. Genome Biol. 2015;16:157. doi: 10.1186/s13059-015-0721-2. [[DOI](https://doi.org/10.1186/s13059-015-0721-2)] [[PMC free article](/articles/PMC4531804/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26243257/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Genome%20Biol.&title=OrthoFinder:%20Solving%20fundamental%20biases%20in%20whole%20genome%20comparisons%20dramatically%20improves%20orthogroup%20inference%20accuracy&author=D.M.%20Emms&author=S.%20Kelly&volume=16&publication_year=2015&pages=157&pmid=26243257&doi=10.1186/s13059-015-0721-2&)]
* 40.Bian T., Hu J., Deng Y. Identifying influential nodes in complex networks based on AHP. Phys. A Stat. Mech. Appl. 2017;479:422–436. doi: 10.1016/j.physa.2017.02.085. [[DOI](https://doi.org/10.1016/j.physa.2017.02.085)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Phys.%20A%20Stat.%20Mech.%20Appl.&title=Identifying%20influential%20nodes%20in%20complex%20networks%20based%20on%20AHP&author=T.%20Bian&author=J.%20Hu&author=Y.%20Deng&volume=479&publication_year=2017&pages=422-436&doi=10.1016/j.physa.2017.02.085&)]
* 41.Urbinati A., Galimberti E., Ruffo G. Hubs and authorities of the scientific migration network. arXiv. 20191907.07175 [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=arXiv&title=Hubs%20and%20authorities%20of%20the%20scientific%20migration%20network&author=A.%20Urbinati&author=E.%20Galimberti&author=G.%20Ruffo&publication_year=2019&)]
* 42.Eldén L. Matrix Methods in Data Mining and Pattern Recognition. 2th ed. SIAM; Philadelphia, PA, USA: 2019.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Matrix%20Methods%20in%20Data%20Mining%20and%20Pattern%20Recognition&author=L.%20Eld%C3%A9n&publication_year=2019&)]
* 43.Cowen L., Ideker T., Raphael B.J., Sharan R. Network propagation: A universal amplifier of genetic associations. Nat. Rev. Genet. 2017;18:551. doi: 10.1038/nrg.2017.38. [[DOI](https://doi.org/10.1038/nrg.2017.38)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28607512/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nat.%20Rev.%20Genet.&title=Network%20propagation:%20A%20universal%20amplifier%20of%20genetic%20associations&author=L.%20Cowen&author=T.%20Ideker&author=B.J.%20Raphael&author=R.%20Sharan&volume=18&publication_year=2017&pages=551&pmid=28607512&doi=10.1038/nrg.2017.38&)]
* 44.Opsahl T., Agneessens F., Skvoretz J. Node centrality in weighted networks: Generalizing degree and shortest paths. Soc. Netw. 2010;32:245–251. doi: 10.1016/j.socnet.2010.03.006. [[DOI](https://doi.org/10.1016/j.socnet.2010.03.006)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Soc.%20Netw.&title=Node%20centrality%20in%20weighted%20networks:%20Generalizing%20degree%20and%20shortest%20paths&author=T.%20Opsahl&author=F.%20Agneessens&author=J.%20Skvoretz&volume=32&publication_year=2010&pages=245-251&doi=10.1016/j.socnet.2010.03.006&)]
* 45.Gazestani V.H., Lewis N.E. From genotype to phenotype: Augmenting deep learning with networks and systems biology. Curr. Opin. Syst. Biol. 2019;15:68–73. doi: 10.1016/j.coisb.2019.04.001. [[DOI](https://doi.org/10.1016/j.coisb.2019.04.001)] [[PMC free article](/articles/PMC6880750/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31777764/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Curr.%20Opin.%20Syst.%20Biol.&title=From%20genotype%20to%20phenotype:%20Augmenting%20deep%20learning%20with%20networks%20and%20systems%20biology&author=V.H.%20Gazestani&author=N.E.%20Lewis&volume=15&publication_year=2019&pages=68-73&pmid=31777764&doi=10.1016/j.coisb.2019.04.001&)]
* 46.Loscalzo J., Barabási A.-L. Network Science. 1st ed. Cambridge University Press; Cambridge, UK: 2016.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Network%20Science&author=J.%20Loscalzo&author=A.-L.%20Barab%C3%A1si&publication_year=2016&)]
* 47.Janwa H., Massey S.E., Velev J., Mishra B. On the origin of biomolecular networks. Front. Genet. 2019;10:240–257. doi: 10.3389/fgene.2019.00240. [[DOI](https://doi.org/10.3389/fgene.2019.00240)] [[PMC free article](/articles/PMC6467946/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31024611/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Genet.&title=On%20the%20origin%20of%20biomolecular%20networks&author=H.%20Janwa&author=S.E.%20Massey&author=J.%20Velev&author=B.%20Mishra&volume=10&publication_year=2019&pages=240-257&pmid=31024611&doi=10.3389/fgene.2019.00240&)]
* 48.Aukerman M.J., Hirschfeld M., Wester L., Weaver M., Clack T., Amasino R.M., Sharrock R.A. A deletion in the PHYD gene of the Arabidopsis wassilewskija ecotype defines a role for phytochrome D in red/far-red light sensing. Plant Cell. 1997;9:1317–1326. doi: 10.1105/tpc.9.8.1317. [[DOI](https://doi.org/10.1105/tpc.9.8.1317)] [[PMC free article](/articles/PMC157000/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/9286109/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Plant%20Cell&title=A%20deletion%20in%20the%20PHYD%20gene%20of%20the%20Arabidopsis%20wassilewskija%20ecotype%20defines%20a%20role%20for%20phytochrome%20D%20in%20red/far-red%20light%20sensing&author=M.J.%20Aukerman&author=M.%20Hirschfeld&author=L.%20Wester&author=M.%20Weaver&author=T.%20Clack&volume=9&publication_year=1997&pages=1317-1326&pmid=9286109&doi=10.1105/tpc.9.8.1317&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

[Click here for additional data file.](/articles/instance/7996555/bin/genes-12-00337-s001.pdf) (112.9KB, pdf)

### Data Availability Statement

<https://www.genelab.nasa.gov/>.