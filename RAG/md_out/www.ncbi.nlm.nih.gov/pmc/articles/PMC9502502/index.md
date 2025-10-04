Life (Basel)

. 2022 Sep 8;12(9):1399. doi: [10.3390/life12091399](https://doi.org/10.3390/life12091399)

# Simulated Micro-, Lunar, and Martian Gravities on Earth—Effects on *Escherichia coli* Growth, Phenotype, and Sensitivity to Antibiotics

[Lily A Allen](https://pubmed.ncbi.nlm.nih.gov/?term=%22Allen%20LA%22%5BAuthor%5D)

### Lily A Allen

1BioServe Space Technologies, University of Colorado Boulder, Boulder, CO 80309, USA

2Smead Aerospace Engineering Sciences Department, University of Colorado Boulder, Boulder, CO 80309, USA

Find articles by [Lily A Allen](https://pubmed.ncbi.nlm.nih.gov/?term=%22Allen%20LA%22%5BAuthor%5D)

1,2, [Amir H Kalani](https://pubmed.ncbi.nlm.nih.gov/?term=%22Kalani%20AH%22%5BAuthor%5D)

### Amir H Kalani

3Molecular, Cellular and Developmental Biology Department, University of Colorado Boulder, Boulder, CO 80309, USA

Find articles by [Amir H Kalani](https://pubmed.ncbi.nlm.nih.gov/?term=%22Kalani%20AH%22%5BAuthor%5D)

3, [Frederico Estante](https://pubmed.ncbi.nlm.nih.gov/?term=%22Estante%20F%22%5BAuthor%5D)

### Frederico Estante

2Smead Aerospace Engineering Sciences Department, University of Colorado Boulder, Boulder, CO 80309, USA

Find articles by [Frederico Estante](https://pubmed.ncbi.nlm.nih.gov/?term=%22Estante%20F%22%5BAuthor%5D)

2, [Aaron J Rosengren](https://pubmed.ncbi.nlm.nih.gov/?term=%22Rosengren%20AJ%22%5BAuthor%5D)

### Aaron J Rosengren

4Department of Mechanical and Aerospace Engineering, University of California San Diego, San Diego, CA 92093, USA

Find articles by [Aaron J Rosengren](https://pubmed.ncbi.nlm.nih.gov/?term=%22Rosengren%20AJ%22%5BAuthor%5D)

4, [Louis Stodieck](https://pubmed.ncbi.nlm.nih.gov/?term=%22Stodieck%20L%22%5BAuthor%5D)

### Louis Stodieck

1BioServe Space Technologies, University of Colorado Boulder, Boulder, CO 80309, USA

2Smead Aerospace Engineering Sciences Department, University of Colorado Boulder, Boulder, CO 80309, USA

Find articles by [Louis Stodieck](https://pubmed.ncbi.nlm.nih.gov/?term=%22Stodieck%20L%22%5BAuthor%5D)

1,2, [David Klaus](https://pubmed.ncbi.nlm.nih.gov/?term=%22Klaus%20D%22%5BAuthor%5D)

### David Klaus

2Smead Aerospace Engineering Sciences Department, University of Colorado Boulder, Boulder, CO 80309, USA

Find articles by [David Klaus](https://pubmed.ncbi.nlm.nih.gov/?term=%22Klaus%20D%22%5BAuthor%5D)

2, [Luis Zea](https://pubmed.ncbi.nlm.nih.gov/?term=%22Zea%20L%22%5BAuthor%5D)

### Luis Zea

1BioServe Space Technologies, University of Colorado Boulder, Boulder, CO 80309, USA

2Smead Aerospace Engineering Sciences Department, University of Colorado Boulder, Boulder, CO 80309, USA

Find articles by [Luis Zea](https://pubmed.ncbi.nlm.nih.gov/?term=%22Zea%20L%22%5BAuthor%5D)

1,2,\*

Editor: Dirk Schulze-Makuch

* Author information
* Article notes
* Copyright and License information

1BioServe Space Technologies, University of Colorado Boulder, Boulder, CO 80309, USA

2Smead Aerospace Engineering Sciences Department, University of Colorado Boulder, Boulder, CO 80309, USA

3Molecular, Cellular and Developmental Biology Department, University of Colorado Boulder, Boulder, CO 80309, USA

4Department of Mechanical and Aerospace Engineering, University of California San Diego, San Diego, CA 92093, USA

\*

Correspondence: luis.zea@colorado.edu

#### Roles

**Dirk Schulze-Makuch**: Academic Editor

Received 2022 Aug 12; Accepted 2022 Aug 29; Collection date 2022 Sep.

© 2022 by the authors.

Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (<https://creativecommons.org/licenses/by/4.0/>).

[PMC Copyright notice](/about/copyright/)

PMCID: PMC9502502  PMID: [36143436](https://pubmed.ncbi.nlm.nih.gov/36143436/)

## Abstract

Bacterial behavior has been studied under microgravity conditions, but very little is known about it under lunar and Martian gravitational regimes. An Earth-based approach was designed and implemented using inclined clinostats and an in-house-developed code to determine the optimal clinorotation angular speed for bacterial liquid cultures of 5 RPM. With this setup, growth dynamics, phenotypic changes, and sensitivity to antibiotics (minimum inhibitory concentration (MIC) of two different classes of antibiotics) for three *Escherichia coli* strains (including uropathogenic) were examined under simulated micro-, lunar, and Martian gravities. The results included increased growth under simulated micro- and lunar gravities for some strains, and higher concentrations of antibiotics needed under simulated lunar gravity with respect to simulated micro- and Martian gravities. Clinostat-produced results can be considered suggestive but not determinative of what might be expected in altered gravity, as there is still a need to systematically verify these simulation devices’ ability to accurately replicate phenomena observed in space. Nevertheless, this approach serves as a baseline to start interrogating key cellular and molecular aspects relevant to microbial processes on the lunar and Martian surfaces.

**Keywords:** clinostat, minimum inhibitory concentration, MIC, rpoS, cell size, aggregation, ciprofloxacin, gentamicin, urinary tract infection, UTI, spaceflight

## 1. Introduction

Humans carry roughly as many bacterial cells in and on our bodies as we have total mammalian cells [[1](#B1-life-12-01399)]. By the nature of this, we will ubiquitously share space habitats with bacteria. Hence, it is important to understand how an altered gravitational environment may affect bacterial behavior and, in the context of human health concerns, the efficacy of antibiotics. Although no overarching definitive conclusions have yet been reached [[2](#B2-life-12-01399),[3](#B3-life-12-01399)], many studies performed in space have shown altered bacterial behavior in microgravity with respect to 1 g on Earth [[4](#B4-life-12-01399)], including modified cell and biofilm phenotype [[5](#B5-life-12-01399),[6](#B6-life-12-01399),[7](#B7-life-12-01399),[8](#B8-life-12-01399)], increased virulence [[9](#B9-life-12-01399)], and reduced bacterial susceptibility to antibiotics [[7](#B7-life-12-01399),[10](#B10-life-12-01399),[11](#B11-life-12-01399),[12](#B12-life-12-01399),[13](#B13-life-12-01399),[14](#B14-life-12-01399),[15](#B15-life-12-01399),[16](#B16-life-12-01399),[17](#B17-life-12-01399),[18](#B18-life-12-01399),[19](#B19-life-12-01399),[20](#B20-life-12-01399),[21](#B21-life-12-01399),[22](#B22-life-12-01399)].

While these studies have interrogated bacterial behavior and its potential consequences for crew health in the microgravity environment of orbital flight, very little is known on these topics under lunar and Martian gravitational regimes, 1.62 m/s2 (~⅙ g) and 3.72 m/s2 (~⅜ g), respectively. Of particular interest are processes related to urinary tract infections (UTI) given that urosepsis (which can occur if a UTI is not treated properly) is the third most likely reason for emergent medical evacuation from the International Space Station (ISS) [[23](#B23-life-12-01399)]. *Escherichia coli* is the most commonly isolated UTI pathogen [[24](#B24-life-12-01399)], and is also typically used as a bacterial model organism for spaceflight research [[19](#B19-life-12-01399)]. As part of a NASA-funded study using ten microbes (results of other species to be published separately), this manuscript describes experiments focused on characterizing growth dynamics (lag phase duration, exponential growth rate, and final cell counts at stationary phase), phenotypic changes (cell diameter and length and aggregation), and the sensitivity to antibiotics (minimum inhibitory concentration (MIC) of two different classes of antibiotics) for three *E. coli* strains cultured under simulated micro-, lunar, and Martian gravities. Our methodology to simulate some aspects of these gravitational conditions—inclined clinostats and a code to determine an optimal clinorotation angular speed for bacterial liquid cultures—are also explained.

## 2. Background

Although some mechanistic observations have been made [[19](#B19-life-12-01399),[20](#B20-life-12-01399),[22](#B22-life-12-01399)], it is not yet clearly elucidated how biophysical and molecular genetic phenomena—such as the activation of antibiotic resistant pathways—change within gravitational regimes between microgravity and 1 g, or how these environments impact bacterial phenotype, physiology, or behavior. To further interrogate the effects of reduced gravities, lunar and Martian gravitational regimes were simulated on Earth to the extent possible, using BioServe’s in-house developed clinostats. While rotating wall vessels and clinostats allows for the simulation of some aspects of the microgravity environment (also called ‘low-shear modeled microgravity’), the replication of regimes between microgravity and 1 g requires an additional step. Clinostats continuously rotate a container fully loaded with a liquid culture at a constant speed with the goal of maintaining cells within a determined depletion zone [[25](#B25-life-12-01399),[26](#B26-life-12-01399)]. To ensure the rotation is not so fast that cells are centrifuged away from this zone, or too slow so that they would sediment out of suspension, a code was developed to determine the angular velocity to be used based on parameters such as cell length, diameter, mass, buoyancy-corrected mass, density, medium density and viscosity, and vessel diameter via a set of second order, linear, separable, non-homogeneous stiff differential equations [[27](#B27-life-12-01399)]. These ‘FPA Clinostats’ could be set horizontally (to simulate microgravity), vertically (for 1 g controls), or at an angle in between to replicate certain aspects of regimes between micro- and 1 g (see [Figure 1](#life-12-01399-f001) and [Figure 2](#life-12-01399-f002)) [[28](#B28-life-12-01399),[29](#B29-life-12-01399),[30](#B30-life-12-01399),[31](#B31-life-12-01399),[32](#B32-life-12-01399),[33](#B33-life-12-01399)]. It is acknowledged that, just as clinostat-produced environments are not the same as actual microgravity (they cannot remove Earth’s gravity and can introduce confounding factors), inclined clinostats are not the same as the actual lunar or Martian surface. Nevertheless, they serve as a reasonable baseline to start interrogating key cellular and molecular aspects relevant to microbial processes on the lunar and Martian surfaces.

### Figure 1.

[![Figure 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/e79bae2cfdd9/life-12-01399-g001.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g001.jpg)

[Open in a new tab](figure/life-12-01399-f001/)

**Left**: BioServe’s FPA Clinostat inclined at an angle theta. While the x component of the gravity vector on any given cell is randomized via clinorotation, the y component replicates reduced sedimentation and buoyancy as would occur at a gravitational level between microgravity and 1 g. **Right**: All four clinostats for each gravitational regime configured for experimentation inside BioServe’s environmental test chamber.

### Figure 2.

[![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/983cf0bfa2ed/life-12-01399-g002.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g002.jpg)

[Open in a new tab](figure/life-12-01399-f002/)

Differences in non-motile bacterial sedimentation rates can be observed between FPAs clinorotated at different angles at 24 h of growth; sµg, sLg, and sMg refer to simulated micro-, lunar, and Martian gravities, respectively. Shown here are cultures from a study reported separately using non-motile *Salmonella* are shown, as no images were taken of this particular study. Cellular sedimentation (indicated by cyan lines) can be observed being collinear to the axis of rotation, regardless of the angle of clinostat inclination.

The *E. coli* strains chosen for this study were (i) ATCC® 4157™, previously flown by our group on eight space shuttle flights aboard STS-37, -43, -50, -54, -57, -60, -62, and -95 [[28](#B28-life-12-01399),[34](#B34-life-12-01399)] and to the ISS [[19](#B19-life-12-01399)], (ii) AMG1, a uropathogenic clinical isolate from the Stanford Medical Center [[35](#B35-life-12-01399)], and (iii) an *rpoS* knockout mutant of AMG1 to study this regulator gene’s pathways (associated with resistance to multiple types of stresses and resistance to some antibiotics on Earth via its product, the σS sigma factor [[36](#B36-life-12-01399),[37](#B37-life-12-01399),[38](#B38-life-12-01399),[39](#B39-life-12-01399),[40](#B40-life-12-01399)]. The latter two strains were flown to space on NASA’s EcAMSat [[40](#B40-life-12-01399),[41](#B41-life-12-01399),[42](#B42-life-12-01399)]. The uropathogens were challenged with Ciprofloxacin, the most commonly prescribed drug for UTI [[43](#B43-life-12-01399)]. ATCC® 4157™ was challenged with Gentamicin sulfate as in [[19](#B19-life-12-01399)].

## 3. Materials and Methods

### 3.1. Setup

*E. coli* AMG1 and its mutant strain were cultured in modified artificial urine medium supplemented with glucose and a high concentration of phosphate (mAUMg hi-Pi) [[5](#B5-life-12-01399),[44](#B44-life-12-01399)] to replicate human urine. While glucose concentrations in human urine are usually 0 to 0.8 mM or lower [[45](#B45-life-12-01399)], our growth medium had a higher concentration, 2 mM, for comparison against our group’s other spaceflight studies (to be published separately) and to ensure bacterial growth would take place, enabling us to interrogate the role of simulated gravitational conditions. *E. coli* 4157 was cultured in LB lennox broth (Sigma Aldrich, St. Louis, MO, USA, L3022). All strains were grown at 37 °C. Cultures were housed in BioServe’s FPAs, enclosed by rubber septa, and then loaded into BioServe’s FPA clinostats ([Figure 1](#life-12-01399-f001)). Washing, sigmacoting®, and sterilization was performed on all hardware prior to experimentation, per Zea et al. [[20](#B20-life-12-01399)].

### 3.2. Bacterial Motility

To determine the motility of each strain, a needle dipped in bacterial culture was inserted into motility tubes (Thermo Scientific, Waltham, MA, USA, Cat. No. R061410) and was incubated at 37 °C for 24 h. A motile culture was indicated by a dispersion of pink color resulting from the bacterial reduction of Tetrazolium (TTC), a metabolite within the agar ([Figure 3](#life-12-01399-f003)). The motility tests showed that *E. coli* AMG1 was semi motile, *E. coli* AMG1 ∆*rpoS* was motile, and *E. coli* ATCC 4157 was non-motile.

#### Figure 3.

[![Figure 3](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/3b545ad029b1/life-12-01399-g003.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g003.jpg)

[Open in a new tab](figure/life-12-01399-f003/)

AMG1 was semi motile, AMG1 ∆*rpoS* was motile, and ATCC 4157 was non-motile.

### 3.3. Experimental Approach

A 24-h culture was diluted by 1:100 and loaded into the FPAs. The optical density (OD)595 at the start of the experiment was 0.002 on average. The FPA consisted of four independent chambers, each containing 1.3 mL of culture, segregated by rubber septa. One FPA was sacrificed at each timestamp for OD data acquisition (the last timestamp had eight replicates for improved statistics). Timestamps were determined by preliminary growth curve experiments conducted at 1 g, and in the case of the *E. coli* AMG1 and *E. coli* AMG1 ∆*rpoS* strains, were based on the timeline presented in Pagden et al. [[40](#B40-life-12-01399)]. Additional FPAs were loaded with 10 mL of culture each for supplemental analyses, including microscopy.

For the antibiotic sensitivity experiments, each FPA had two independent chambers, each containing 3 mL of culture, and enough FPAs were loaded so that there were four replicates for each tested antibiotic concentration, per each gravitational condition. The desired antibiotic concentration was prepared with the same media used in the bacterial culture as diluent and was filter sterilized. In each test, four concentrations were assessed. Drugs (Ciprofloxacin (Fisher Sci., Waltham, MA, USA, Cat. No. AC456880050) or Gentamicin Sulfate (Fisher Sci., Waltham, MA, USA, Cat. No. BP918-1)) were introduced in the bacterial culture when they reached exponential phase. At this time, two FPAs per gravitational regime were sacrificed for OD data acquisition to quantify cell concentration at the time of antibiotic introduction. Then, the four antibiotic concentrations were introduced to their respective FPAs by injecting 1 mL of antibiotic into each chamber. All FPAs were returned to their FPA Clinostat and environmental test chamber at 37 °C for 12 additional hours, following the MIC protocol described by Andrews [[46](#B46-life-12-01399)], adapted to be implementable in this spaceflight hardware. In this assay, bacterial cultures are challenged with increasing concentrations of antibiotics to find the minimum concentration of a given drug sufficient to inhibit bacterial growth under those conditions. Growth inhibition is determined by statistically comparing cell concentration after 12 h of drug challenge against the cell concentration at the time of antibiotic introduction.

### 3.4. Code to Determine Clinostat Rotational Speed

One of the unique attributes of microgravity at the cellular level in a liquid medium is an altered extracellular mass transport profile. On Earth, a cell in a liquid medium will be subject to gravity-driven forces and resultant flows, including sedimentation, buoyancy, and convection, which help transport molecules from one location to another. In microgravity, however, and for non-motile cells in particular, mass transport is limited to diffusion arising from Brownian motion, surface effects, and/or gradient-driven transport phenomena, translating into a quiescent, quasi-stable extracellular environment where incoming substrate is thought to become limited, and excreted metabolic byproducts accumulate around a cell [[20](#B20-life-12-01399),[33](#B33-life-12-01399)]. Some aspects of this quiescent environment can be replicated using a clinostat on Earth to continuously rotate a vessel filled with a liquid culture, with the caveat that the 1 g vector is never removed as it is operated on Earth. Thus, the suspended cells still experience their full weight. The angular speed (*ω*) at which this vessel is rotated is a function of cellular and medium properties, including but not limited to cell length and diameter (normalized into an equivalent Stoke’s radius (*a*), mass (*m*), buoyancy-corrected mass (*m*\*), particle density (ρp), medium density (ρf), viscosity (*ν*), and Stoke’s drag constant (*f*), as well as the vessel diameter (*d*). If the vessel is rotated too slowly, the cell will sediment away from the quiescent zone; if it is rotated too quickly, however, the cell will be centrifuged out of the quiescent zone. The position of a particle at a given time (*t*) can be modeled based on the aforementioned parameters via two second order, linear, separable, non-homogenous stiff differential equations [[25](#B25-life-12-01399),[27](#B27-life-12-01399),[47](#B47-life-12-01399)]:

|  |  |
| --- | --- |
| x¨+fmx˙−m\*mω2x=−m\*gmsinωt | (1) |

|  |  |
| --- | --- |
| y¨+fmy˙−m\*mω2y=−m\*gmcosωt | (2) |

where *x* and *y* refer to the axes of a coordinate system upon which the vessel’s circular cross section is centered at the (0,0) position.

We developed a MATLAB® code based on the ode15 s ordinary differential equation solver [[27](#B27-life-12-01399)], to determine the longest duration a cell would stay within the putative quiescent zone under these conditions as a function of angular speed (accessible here: <https://github.com/SpaceLuisZea/Clinostat>) (accessed on 9 August 2022). As inputs to the code, we used a bacterial Stoke’s diameter of 5.6×10−5 cm, cell mass of 4.0×10−13 g, growth medium viscosity of 0.0102 g/cm·s and density of 1.011 g/cm3 (for reference, water’s viscosity at 25 °C and density are 0.0091 g/cm·s and 1.000 g/cm3, respectively), and an arbitrary quiescent zone diameter of 10 µm. This information (as well as recommended rotational speed) has been shared with other groups who have used our clinostats and FPAs [[48](#B48-life-12-01399)].

### 3.5. Data Acquisition

Cultures were extracted and transferred into a 24-well plate for mixing, and from there aliquots were transferred to a 96-well plate. OD was measured at 595 nm for the growth curve and at 600 nm for MIC experiments. Cultures from the last timestamp of the growth curve for each regime were preserved by mixing 1 mL of 4% PFA (Fisher Scientific, Waltham, MA, USA, Cat. No. AAJ61899AK) and 1 mL of sample. For microscopy, samples were centrifuged for two to three minutes at 900 g’s and an aliquot was transferred to a slide. Microscopy was performed on an OLYMPUS.IX81 Inverted Widefield Microscope with a 100X 1.40NA SAPO objective lens and images were captured via a Hamamatsu Orca R2 CCD camera.

### 3.6. Statistical Analysis

At each timestamp and for each gravitational regime, four replicates were sacrificed to acquire OD data. For each replicate, four aliquots were assessed, hence the OD for each regime at each timestamp was the mean of the averages of four aliquots per each of the four replicates. To determine if there were statistical differences between the gravitational regimes at 24 h, an Analysis of Variance (ANOVA) for parametric datasets or Dunn test for nonparametric data sets was performed. Slopes between the beginning and end of the exponential phase were found using Microsoft Excel’s “slope” function. These slopes were compared to the 1 g control (slopegravitational regime/slope1 g). R2 values were found by using Excel’s RSQ function. This same process was used to calculate the “death rate” via the slope between the stationary phase and the last timepoint in the experiment. The average length and width were calculated for 50 measurements of each condition, preserved at the last timestamp. For MIC tests, a Tukey, Kruskal, or Dunn test was performed between OD at the time of antibiotic introduction and after 12 h of being challenged with antibiotics. The lowest concentration for which there was no significance with respect to the OD at time of drug introduction was the MIC.

## 4. Results

### 4.1. Calculated Time to Depart a Putative 10 µm Depletion Zone

We used our MATLAB® code to simulate and subsequently determine how long it would take a non-motile bacterial cell to leave a depletion zone of 10 µm in diameter as a function of rotational speed and vessel diameter. [Figure 4](#life-12-01399-f004) shows the code output in this regard, indicating that for an FPA-like vessel (1 cm in diameter) and 5 RPM rotational speed, a non-motile bacterial cell could be expected to remain within this depletion zone (i.e., it would not sediment or be centrifuged away from it) for ~220 h, or just over nine days. Given that this was longer than our expected two-day long test, this RPM was chosen.

#### Figure 4.

[![Figure 4](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/1ba410bde84f/life-12-01399-g004.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g004.jpg)

[Open in a new tab](figure/life-12-01399-f004/)

Estimated time needed for a non-motile cell to depart an arbitrary 10 µm depletion zone as a function of clinostat angular velocity (5–60 rpm) and vessel diameter (1–8 cm), per our MATLAB® code.

### 4.2. AMG1 and ∆rpoS Results

#### 4.2.1. Growth Dynamics

[Figure 5](#life-12-01399-f005) shows the growth dynamics of *E. coli* AMG1 and *E. coli* AMG1 ∆*rpoS* under various simulated gravities. Limited by the times of data collection, the OD data indicate that the lag phase lasted to at least 1.25 h and 1 h for *E. coli* AMG1 and AMG1 ∆*rpoS*, respectively. The beginning and end of the exponential growth phase were 1.25 and 4.5 h for *E. coli* AMG1, and 3 and 5 h for AMG1 ∆*rpoS*, respectively. Slopes between these points are summarized in [Table 1](#life-12-01399-t001).

##### Figure 5.

[![Figure 5](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/dfa9605fc22c/life-12-01399-g005.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g005.jpg)

[Open in a new tab](figure/life-12-01399-f005/)

*E. coli* AMG1 and *E. coli* AMG1 ∆*rpoS* growth in mAUMg-high Pi in various simulated gravities. Circles indicate *E. coli* AMG1, and triangles indicate the mutant strain. Error bars are standard error with a 95% confidence interval for this figure and all other data figures (*n* = 4 for all data points except the last timestamp, which has *n* = 8). Timestamps 6 and 24 h of the *E. coli* AMG1 ∆*rpoS* dataset were moved to the right for clarity.

##### Table 1.

Slopes of each gravitational regime between the first and last points of the exponential phase for each strain. R2 > 0.90 and >0.94 for all slopes of AMG1 and AMG1 ∆rpoS, respectively; wrt = with respect to.

| Gravitational Regime | *E. coli* AMG1 | | *E. coli* AMG1 ∆*rpoS* | |
| --- | --- | --- | --- | --- |
| Slope | Slope wrt 1 g | Slope | Slope wrt 1 g |
| Simulated microgravity | 0.048 | 117% | 0.079 | 123% |
| Simulated lunar | 0.045 | 111% | 0.078 | 120% |
| Simulated Martian | 0.048 | 117% | 0.071 | 111% |
| 1 g | 0.041 | N/A | 0.065 | N/A |

[Open in a new tab](table/life-12-01399-t001/)

For *E. coli* AMG1, the stationary phase was reached at 6 h for all regimes. At the 6 h timepoint, significance was only observed between simulated microgravity and the 1 g control (13% increase under simulated microgravity with respect to 1 g, *p* = 0.036). To maintain consistency between the strains, statistical analysis was performed at the 12 h timepoint as well. No significant differences were observed between any regimes for *E. coli* AMG1.

For *E. coli* AMG1 ∆rpoS, cultures grown under simulated lunar gravity and at 1 g reached the stationary phase at 6 h. Under simulated micro and Martian gravities, growth continued until at least 11.25 h. Statistical analysis was performed on data from 11.25 h and significant increases in OD were observed in simulated microgravity with respect to the other three gravitational conditions: simulated lunar (8% increase, *p* = 0.0099), simulated Martian gravity (15% increase, *p* < 0.001), and 1 g (35% increase, *p* < 0.001). When compared to the 1 g control, simulated lunar gravity exhibited significant differences (25% increase, *p* < 0.001), but not when compared to simulated Martian gravity. Finally, simulated Martian gravity exhibited significant differences when compared to the 1 g control (17% increase, *p* < 0.001). Comparison of OD between the strains under each gravitational condition shows significance only for the simulated microgravity regime (34% increase of AMG1 ∆*rpoS* with respect to AMG1, *p* = 0.003) (orange line in [Figure 6](#life-12-01399-f006)).

##### Figure 6.

[![Figure 6](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/0ba83f623fe5/life-12-01399-g006.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g006.jpg)

[Open in a new tab](figure/life-12-01399-f006/)

*E. coli* AMG1 and *E. coli* AMG1 ∆*rpoS* ODs at 12 h and 11.25 h (respectively) for each gravitational regime. Bars with the symbol ‘∆’ are data for the mutant strain. The blue dotted lines indicate significance between regimes for *E. coli* AMG1 ∆*rpoS*, and the orange line indicates significance between strains for a given gravitational regime (no significance was observed for *E. coli* AMG1 between regimes). \*\*: 0.001 < *p* ≤ 0.01; \*\*\*: *p* ≤ 0.001.

The death phase of *E. coli* AMG1 and AMG1 ∆*rpoS* occurred somewhere between 12 and 24 h, and between 11.25 and 24 h, respectively, and is limited by the times of OD data collection of the experiment. Death rate slopes were calculated between these last two timepoints for each strain. This information is summarized in [Table 2](#life-12-01399-t002).

##### Table 2.

Death rate slopes (between the last two timepoints) of each gravitational regime; wrt = with respect to.

| Gravitational Regime | *E. coli* AMG1 | | *E. coli* AMG1 ∆*rpoS* | |
| --- | --- | --- | --- | --- |
| Slope | Slope wrt 1 g | Slope | Slope wrt 1 g |
| Simulated microgravity | −0.0009 | 26% | −0.0036 | 112% |
| Simulated lunar | −0.0031 | 91% | −0.0023 | 72% |
| Simulated Martian | −0.0039 | 115% | −0.0025 | 78% |
| 1 g | −0.0034 | N/A | −0.0032 | N/A |

[Open in a new tab](table/life-12-01399-t002/)

At the 24 h timestamp, for the wild-type strain, a significant increase in OD was observed under simulated microgravity with respect to the 1 g control (48% increase, *p* < 0.001). Similarly, simulated lunar and Martian gravity showed significant increases when compared to the 1 g control (36% increase, *p* = 0.0037; 33% increase, *p* = 0.0132, respectively). No significance was observed when comparing simulated lunar to simulated Martian gravity. For the mutant strain, while no significant differences in OD were observed between the three reduced gravitational conditions at 24 h, each of them did show statistical differences with respect to the 1 g control. Simulated microgravity had a 44% increase (*p* < 0.001), simulated lunar gravity also had a 44% increase (*p* < 0.001), and simulated Martian gravity had a 31% increase (*p* < 0.001). Comparison between strains under each gravitational condition showed significantly higher ODs for the mutant with respect to AMG1 under simulated lunar (23% increase, *p* = 0.003) and under simulated Martian gravities (12% increase, *p* = 0.045) (orange lines in [Figure 7](#life-12-01399-f007)).

##### Figure 7.

[![Figure 7](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/ed64da425427/life-12-01399-g007.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g007.jpg)

[Open in a new tab](figure/life-12-01399-f007/)

*E. coli* AMG1 and *E. coli* AMG1 ∆*rpoS* optical densities at 24 h for each gravitational regime. Bars with the symbol ‘∆’ are data for the mutant strain. The black lines indicate significance between regimes for *E. coli* AMG1, the blue dotted lines indicate significance between regimes for *E. coli* AMG1 ∆*rpoS*, and the orange lines indicate significance between strains for a given gravitational regime \*: 0.01 < *p* ≤ 0.05; \*\*: 0.001 < *p* ≤ 0.01; \*\*\*: *p* ≤ 0.001.

#### 4.2.2. Cell Size and Aggregation

Length and width were measured for both strains at the last timestamp, 24 h. [Table 3](#life-12-01399-t003) indicates average cell length and width for each gravitational regime and strain, and how each compares to the 1 g controls. The simulated microgravity regime for the wild-type had the biggest size difference for both length (17% greater) and width (11% greater) compared to the 1 g control. The Dunn test was used to identify statistically significant differences in cell length and width as a function of gravitational regime and strain.

##### Table 3.

Average cell sizes per gravitational condition for each strain (*n* = 50). Length and diameter values in µm. \*: 0.01 < *p* ≤ 0.05; \*\*\*: *p* ≤ 0.001; wrt = with respect to; sµm, sLg, sMg: simulated micro, lunar, and Martian gravity, respectively.

| Gravitational Regime | AMG1 Length | ∆*rpoS* Length | ∆*rpoS* Length wrt AMG1 | AMG1 Length wrt 1 g | ∆*rpoS* Length | AMG1 Width | ∆*rpoS* Width | ∆*rpoS* Width wrt AMG1 | AMG1 Width wrt 1 g | ∆*rpoS* Width wrt 1 g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sµg | 3.00 | 2.37 | 79% | 117% \*\*\* | 106% | 0.95 | 0.94 | 99% | 111% \*\*\* | 104% |
| sLg | 2.98 | 2.36 | 79% | 117% \*\*\* | 105% | 0.86 | 0.94 | 110% | 100% | 104% |
| sMg | 2.75 | 2.37 | 86% | 107% \* | 106% \* | 0.87 | 0.90 | 103% | 101% | 100% |
| 1 g | 2.56 | 2.24 | 88% | N/A | N/A | 0.86 | 0.90 | 105% | N/A | N/A |

[Open in a new tab](table/life-12-01399-t003/)

Observations were made for cellular aggregation at the last timestamp. For both strains, no aggregation was observed. Settling however did occur most of all in the 1 g control (FPAs oriented upright) and no settling was observed in simulated microgravity (FPAs oriented horizontally).

#### 4.2.3. MIC of Ciprofloxacin

*E. coli* AMG1 and *E. coli* AMG1 ∆*rpoS* were challenged, separately, with increasing concentrations of Ciprofloxacin (0, 0.125, 0.25, and 0.50 mg/L) to determine the minimum concentration of antibiotic needed to inhibit their growth under each gravitational condition. The MIC was defined as the lowest concentration of antibiotic under which no statistical difference in OD600 (via Kruskal and Dunn tests) was observed between the time of drug introduction and 12 h later.

As summarized in [Table 4](#life-12-01399-t004), lower concentrations of Ciprofloxacin were needed to inhibit *E. coli* AMG1 growth under the simulated reduced gravities with respect to the 1 g control, which continued growing under the highest concentration tested. It is noteworthy that the simulated microgravity and simulated Martian gravity conditions required half of what was needed under simulated lunar gravity to inhibit *E. coli* AMG1′s growth. Similarly, *E. coli* AMG1 ∆*rpoS* growth was inhibited under simulated microgravity at a 0.50 mg/L concentration—a concentration that was not inhibitory under the other four tested gravitational conditions.

##### Table 4.

Identified Minimum Inhibitory Concentration (MIC) (mg/L) of Ciprofloxacin as a function of gravitational condition and *E. coli* strain; > in the table means that the MIC was greater than the highest concentration of antibiotic tested (in this case, 0.50).

| Gravitational Regime | *E. coli* AMG1 | *E. coli* AMG1 ∆*rpoS* |
| --- | --- | --- |
| Simulated microgravity | 0.25 | 0.50 |
| Simulated lunar | 0.50 | >0.50 |
| Simulated Martian | 0.25 | >0.50 |
| 1 g | >0.50 | >0.50 |

[Open in a new tab](table/life-12-01399-t004/)

### 4.3. E. coli 4157

#### 4.3.1. Growth Dynamics

*E. coli* 4157 was cultured over the course of 24 h as shown in [Figure 8](#life-12-01399-f008). The data indicated that the lag phase lasted 0.75 h for all simulated gravities. Exponential growth slopes were calculated between t = 1.5 and 6 h, and were compared to the 1 g control, as summarized in [Table 5](#life-12-01399-t005). The rate of growth during the exponential phase for each regime showed faster growth under the simulated reduced gravities with respect to 1 g, with no specific pattern: simulated lunar gravity had the highest growth rate, 14% greater than the 1 g control, followed by simulated Martian and microgravity (8 and 5% greater than the 1 g control, respectively).

##### Figure 8.

[![Figure 8](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/123157df2227/life-12-01399-g008.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g008.jpg)

[Open in a new tab](figure/life-12-01399-f008/)

*E. coli* 4157 growth in LB Lennox broth in various simulated gravities.

##### Table 5.

Slopes of each gravitational regime between 1.5 and 6 h.

| Gravitational Regime | Slope | Slope wrt 1 g |
| --- | --- | --- |
| Simulated microgravity | 0.044 | 105% |
| Simulated lunar | 0.047 | 114% |
| Simulated Martian | 0.045 | 108% |
| 1 g | 0.042 | N/A |

[Open in a new tab](table/life-12-01399-t005/)

The stationary phase was reached at 12 h, and [Figure 9](#life-12-01399-f009) shows the OD of each regime at this time. No significance was observed between the simulated gravities and the 1 g control. Simulated microgravity exhibited significant differences when compared to the other two simulated regimes (simulated lunar gravity: 10% decrease, *p* = 0.029; simulated Martian gravity: 10% decrease, *p* = 0.025). Simulated Martian and lunar gravity were not significant when compared to each other.

##### Figure 9.

[![Figure 9](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/37eb65aedadb/life-12-01399-g009.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g009.jpg)

[Open in a new tab](figure/life-12-01399-f009/)

*E. coli* 4157 optical densities at 12 h for each gravitational regime. The black lines indicate significance between regimes. The meaning of the asterisks are as follows: \* 0.01 < *p* < 0.05.

At 24 h, significance was only observed between simulated microgravity and the 1 g control, as shown in [Figure 10](#life-12-01399-f010) (17% decrease with respect to 1 g, *p* = 0.041). No significance was observed when comparisons were made between simulated reduced gravitational regimes. No death curves were observed during the 24 h of this analysis.

##### Figure 10.

[![Figure 10](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/0941acfdfcd4/life-12-01399-g010.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g010.jpg)

[Open in a new tab](figure/life-12-01399-f010/)

*E. coli* optical densities at 24 h for each gravitational regime. The black line indicates significance between regimes (in this case, significance only occurred between simulated microgravity and the 1 g control). \*: 0.01 < *p* < 0.05.

#### 4.3.2. Cell Size and Aggregation

No statistical differences were observed in *E. coli* 4157 cell length or diameter as a function of gravitational condition. In contrast to the AMG1 strains, *E. coli* 4157 aggregation was observed in the simulated microgravity regime. No visible aggregation was present in simulated lunar and Martian gravity. The 1 g control also had no aggregation, but settling was present ([Figure 11](#life-12-01399-f011)).

##### Figure 11.

[![Figure 11](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5d9b/9502502/779b2550ce2b/life-12-01399-g011.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9502502_life-12-01399-g011.jpg)

[Open in a new tab](figure/life-12-01399-f011/)

Samples are from the 24 h timepoint for each gravitational regime. Red arrows indicate cellular aggregation (simulated microgravity) or settling (1 g control).

#### 4.3.3. MIC of Gentamicin Sulfate

*E. coli* 4157 was challenged with increasing concentrations (0, 6, 12, 18 mg/L) of Gentamicin Sulfate to determine the MIC. Simulated microgravity, simulated Martian gravity, and the 1 g controls required a 12 mg/L concentration of Gentamicin Sulfate to inhibit *E. coli* 4157 growth. However, the simulated lunar gravity cultures required a higher concentration for growth to be inhibited: 18 mg/L, as summarized in [Table 6](#life-12-01399-t006).

##### Table 6.

**MIC of Gentamicin Sulfate.** Identified Minimum Inhibitory Concentration (MIC) (mg/L) of Gentamicin Sulfate on *E. coli* 4157 as a function of gravitational condition.

| Gravitational Regime | *E. coli* 4157 |
| --- | --- |
| Simulated microgravity | 12 |
| Simulated lunar | 18 |
| Simulated Martian | 12 |
| 1 g | 12 |

[Open in a new tab](table/life-12-01399-t006/)

## 5. Discussion

A clinostat may replicate certain aspects of the quiescent extracellular environment experienced in actual microgravity, but it is not the same as microgravity, as it operates on Earth, and thus weightlessness is not achieved. Furthermore, there are key aspects that need to be taken into account when designing reduced gravity experiments on Earth using simulation devices such as clinostats and rotating wall vessels. Namely, the importance of (i) the appropriate angular speed to minimize centrifugation and sedimentation of cells out of their proposed extracellular depletion zone, and of (ii) the use of the smallest diameter vessel possible. Our code indicated that clinorotating a 1 cm diameter vessel at 5 RPM would allow for bacteria to stay within a 10 µm depletion zone for about a week, more than sufficient for our two-day experiment. Given that centrifugal forces are dependent upon the distance between a cell and the axis of rotation, there is an advantage to having the smallest diameter culture vessel as possible, as a cell farther away from this axis will be centrifuged away from its depletion zone faster, hence limiting the duration of the clinostat experiment. In terms of the inclination of clinostats to simulate some aspects of gravity levels between micro and 1 g, the collinearity between cellular sedimentation and the axis of rotation, regardless of the angle of inclination, is a visual indication that this approach achieves the goal of effective axial g-vector alignment (see [Figure 2](#life-12-01399-f002)). While our code has its limitations, namely that it does not include Brownian motion or cellular motility when applicable, nor does it take into account cellular aggregation, which is initially unknown, it serves as a first-order analysis to determine the best angular speed based on cellular and media parameters. We recommend that future iterations of this code—which is accessible here: <https://github.com/SpaceLuisZea/Clinostat> (accessed on 9 August 2022)—include Brownian motion, and that Monte Carlo simulations be run to obtain further numerical results.

More importantly, it is acknowledged that a systematic verification of the validity of clinostats (and rotating wall vessels like HARV, and of random positioning machines, for that matter) needs to be performed by either including clinostat sets in spaceflight experiments, or flying experiments with clinorotated Earth controls (varying angular velocity, for example) with this very specific goal. Otherwise, simulated reduced gravity research performed in any of these types of simulation devices needs to be considered exploratory in nature and remains suggestive of what may be expected in microgravity, not determinative or conclusive in this regard, which also applies to this study.

The growth dynamics results of our experiments indicate there is a direct correlation between motility and lag phase duration: the non-motile strain (4157) took less time to leave the lag phase (0.75 h), the semi motile strain (AMG1) took 1 h, and the motile strain (∆*rpoS*) took the longest (1.25 h). This correlation supports the theory that non-motile cells, in a quiescent extracellular environment like the one experienced in microgravity, are exposed to a relatively high concentration of their own byproducts and secondary metabolites [[19](#B19-life-12-01399),[20](#B20-life-12-01399),[22](#B22-life-12-01399)], which may include quorum sensing molecules instructing the culture to begin exponential growth [[4](#B4-life-12-01399)]. Comparing these results with those from spaceflight show that our observed reduced lag phase of *E. coli* 4157 matches our previous studies performed on the Space Shuttle [[11](#B11-life-12-01399),[34](#B34-life-12-01399),[49](#B49-life-12-01399)]. This correlation may also be non-conclusively interpreted as an indication that the use of clinostats (specifically at 5 RPM and 1 cm diameter vessel), may indeed replicate certain aspects of microbial response in true microgravity. An important caveat to this comparative analysis is that the AMG1 and ∆*rpoS* strains were cultured in minimal media, whereas 4157 was in rich medium.

Analyses of exponential growth rates showed that the AMG1 and ∆*rpoS* strains grew faster under simulated microgravity (17–23% increase with respect to 1 g); simulated lunar and Martian gravities either grew just as fast as simulated microgravity, or somewhere in between simulated microgravity and 1 g. The 4157 strain also showed a faster growth rate under the simulated reduced gravities with respect to 1 g, but in this case, simulated lunar gravity was the fastest growing (14% with respect to 1 g). Comparing these results with spaceflight data shows that these increases in exponential growth rate do not agree with the EcAMSat spaceflight mission, which found that the growth rate of AMG1 and ∆*rpoS* strains was unaltered by the microgravity environment [[40](#B40-life-12-01399)], although it should be noted that it was acknowledged that their cells may have been under stress from the culturing hardware, and that different media were used in the two experiments. Similarly, Klaus et al. [[34](#B34-life-12-01399)] found that the rate of growth for cells grown in microgravity was ‘unaffected (or slightly slower)’, again contrary to our results, albeit under different experimental conditions. The exposure to cell byproducts and waste described in the latter paragraph has also been discussed to moderate growth during the exponential phase for *E. coli* 4157 [[20](#B20-life-12-01399),[34](#B34-life-12-01399),[50](#B50-life-12-01399)]. This model suggests that nonmotile cells may experience a decrease in exponential growth because of an altered metabolism due to a lack of sedimentation. The results of cultures grown under simulated microgravity do not support this theory, as the nonmotile *E.coli* 4157 strain experienced a slightly higher exponential growth rate in simulated microgravity than the 1 g control. Meanwhile, the sedimentation that occurred in simulated lunar gravity was potentially sufficient to allow cells to ‘escape’ byproducts and have access to more nutrients, thus yielding the highest observed growth rate when compared to the 1 g control for this strain.

In our study, the three strains reached the stationary phase by 12 h. The AMG1 and 4157 strains showed no significant differences in OD as a function of gravitational condition at this time. On the other hand, the ∆*rpoS* strain had the highest OD under simulated microgravity (35% increase with respect to 1 g), the lowest at 1 g, and sLg and sMg in between. At experiment end (t = 24 h), the highest growth was observed under simulated microgravity on the AMG1 strain (48% increase with respect to 1 g) (with simulated lunar and Martian gravities in between), and under simulated micro and Lunar gravities on the ∆*rpoS* strain (44% increase with respect to 1 g) (with simulated Martian gravity in between). The 4157 strain showed the opposite: the highest growth was at 1 g, and the lowest under simulated microgravity (17% decrease with respect to 1 g). In this case, and keeping in mind the caveat regarding different media used for 4157, a correlation was observed that the non-motile strain had less growth in simulated microgravity and most in 1 g, while the opposite was true for the semi-motile and motile strains. The observed higher yield in simulated microgravity with respect to 1 g of the 4157 strain also contradicts observations made on the same flight hardware (albeit in minimal media) in actual microgravity, where a 13 fold increase was observed in the spaceflight samples with respect to Earth controls [[7](#B7-life-12-01399)]. If the increase in growth under simulated micro- and lunar gravities of the uropathogenic strains (AMG1 and AMG1 ∆*rpoS*) holds true in these environments, this may have a negative impact by increasing the likelihood of crewmembers developing UTIs, a problem frequently reported by astronauts [[51](#B51-life-12-01399)].

Cellular size measurements, taken from samples fixed at experiment end (t = 24 h), showed that AMG1 cells grown under simulated microgravity were 17% longer and 11% wider with respect to 1 g controls. In the case of the ∆*rpoS* strain, the only difference in cell size observed was a 6% increase in length with respect to 1 g on the cells cultured under simulated Martian gravities. No statistical differences were observed on *E.coli* 4157 cell length or diameter as a function of gravitational condition. Our overall cell size observations are not in agreement with our previous spaceflight results, where *E. coli* 4157 cells cultured in space were 59% the length, and 83% the diameter, of their Earth controls [[21](#B21-life-12-01399)]. In terms of aggregation, none was observed in the AMG1 and ∆*rpoS* strains, and it was present in 4157 cultures, but exclusively those cultured under simulated microgravity. This is in agreement with our previous 4157 study, where cellular aggregation was observed in spaceflight samples fixed in PFA upon return to Earth, while none was seen in the Earth controls [[21](#B21-life-12-01399)].

Regarding the MICs, the uropathogenic AMG1 strain showed that lower concentrations of Ciprofloxacin, the most commonly used antibiotic against UTIs on Earth [[43](#B43-life-12-01399)], were needed under the three simulated reduced gravities with respect to 1 g, despite the fact that these gravitational conditions yielded higher cell counts in the growth dynamics study. Significantly, it was observed that cultures grown in simulated lunar gravity needed twice the concentration of simulated micro and Martian gravities, but still less than 1 g. Similarly, the ∆*rpoS* strain needed a lower concentration of antibiotics to inhibit growth under simulated microgravity with respect to the other three gravitational conditions. Finally, for the 4157 strain, the simulated lunar gravity cultures required the highest concentration of Gentamicin for growth to be inhibited: 18 mg/L, compared to 12 mg/L needed for the other three gravitational conditions.

Hence, this study showed differences in growth dynamics, cellular size, and aggregation as a function of time and *E. coli* strain under clinorotation, results that may be verified and further studied under axial centrifugation in microgravity, in order to more realistically achieve simulated lunar and Martian gravities. Nevertheless, our inclined clinostat and in-house code methodology may enable preliminary partial gravity studies to be performed on Earth by other teams, with the caveat that this methodology (just like all reduced gravity simulation devices including clinostats, rotating wall vessels, and random positioning machines) still need to go through a thorough verification and validation process using spaceflight assets.

## Acknowledgments

The authors thank BioServe’s Pamela Flores for her support setting up experiments and guidance through her extensive biology and statistics knowledge, Paul Koenig for the development and maturation of the FPA Clinostats, Fredy España for his valuable work on the FPA Clinostats prototype during his internship at BioServe, Katherinne Herrera for cellular and media parameters information, and James Orth for his guidance on microscopy. The authors also thank Maggie Kolicko for her daily administrative support and Stefanie Countryman for making this project possible through her leadership. Finally, the authors thank A.C. Matin for kindly providing the AMG1 and ∆*rpoS E. coli* strains.

## Nomenclature

|  |  |
| --- | --- |
| RPM | revolution per minute |
| MIC | minimum inhibitory concentration |
| UTI | urinary tract infection |
| ISS | International Space Station |
| NASA | National Aeronautics and Space Administration |
| FPA | fluid processing apparatus |
| sµg | simulated microgravity |
| sLg | simulated Lunar gravity |
| sMg | simulated Martian gravity |
| mAUMg | hi-Pi modified artificial urine medium (high concentration of phosphate) |
| OD | optical density |
| PFA | paraformaldehyde |
| ANOVA | Analysis of Variance |
| Nm | nanometer |
| µm | micrometer |
| wrt | with respect to |
| EcAMSat | Esherichia coli Antimicrobial Satellite |

[Open in a new tab](table/array1/)

## Author Contributions

Conceptualization, L.Z.; Formal analysis, L.A.A. and L.Z.; Funding acquisition, L.Z.; Investigation, L.A.A. and A.H.K.; Methodology, L.A.A. and L.Z.; Project administration, L.Z.; Software, F.E. and L.Z.; Supervision, L.Z.; Visualization, L.A.A. and L.Z.; Writing—original draft, L.A.A. and L.Z.; Writing—review and editing, L.A.A., A.H.K., F.E., A.J.R., L.S., D.K. and L.Z. All authors have read and agreed to the published version of the manuscript.

## Data Availability Statement

The code presented in this study is openly available in GitHub at <https://github.com/SpaceLuisZea/Clinostat> (accessed on 9 August 2022).

## Conflicts of Interest

The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

## Funding Statement

This material is based upon work supported by the National Aeronautics and Space Administration under Grant No. 80NSSC18K1468 to L.Z.

## Footnotes

**Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## References

* 1.Sender R., Fuchs S., Milo R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. PLoS Biol. 2016;14:e1002533. doi: 10.1371/journal.pbio.1002533. [[DOI](https://doi.org/10.1371/journal.pbio.1002533)] [[PMC free article](/articles/PMC4991899/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27541692/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20Biol.&title=Revised%20Estimates%20for%20the%20Number%20of%20Human%20and%20Bacteria%20Cells%20in%20the%20Body&author=R.%20Sender&author=S.%20Fuchs&author=R.%20Milo&volume=14&publication_year=2016&pages=e1002533&pmid=27541692&doi=10.1371/journal.pbio.1002533&)]
* 2.Hammond T.G., Stodieck L., Birdsall H.H., Becker J.L., Koenig P., Hammond J.S., Gunter M.A., Allen P.L. Effects of Microgravity on the Virulence of Listeria Monocytogenes, Enterococcus Faecalis, Candida Albicans, and Methicillin-Resistant Staphylococcus Aureus. Astrobiology. 2013;13:1081–1090. doi: 10.1089/ast.2013.0986. [[DOI](https://doi.org/10.1089/ast.2013.0986)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24283929/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Astrobiology&title=Effects%20of%20Microgravity%20on%20the%20Virulence%20of%20Listeria%20Monocytogenes,%20Enterococcus%20Faecalis,%20Candida%20Albicans,%20and%20Methicillin-Resistant%20Staphylococcus%20Aureus&author=T.G.%20Hammond&author=L.%20Stodieck&author=H.H.%20Birdsall&author=J.L.%20Becker&author=P.%20Koenig&volume=13&publication_year=2013&pages=1081-1090&pmid=24283929&doi=10.1089/ast.2013.0986&)]
* 3.Morrison M.D., Nicholson W.L. Meta-Analysis of Data from Spaceflight Transcriptome Experiments Does Not Support the Idea of a Common Bacterial “Spaceflight Response”. Sci. Rep. 2018;8:14403. doi: 10.1038/s41598-018-32818-z. [[DOI](https://doi.org/10.1038/s41598-018-32818-z)] [[PMC free article](/articles/PMC6158273/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30258082/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Sci.%20Rep.&title=Meta-Analysis%20of%20Data%20from%20Spaceflight%20Transcriptome%20Experiments%20Does%20Not%20Support%20the%20Idea%20of%20a%20Common%20Bacterial%20%E2%80%9CSpaceflight%20Response%E2%80%9D&author=M.D.%20Morrison&author=W.L.%20Nicholson&volume=8&publication_year=2018&pages=14403&pmid=30258082&doi=10.1038/s41598-018-32818-z&)]
* 4.Horneck G., Klaus D.M., Mancinelli R.L. Space Microbiology. Microbiol. Mol. Biol. Rev. 2010;74:121–156. doi: 10.1128/MMBR.00016-09. [[DOI](https://doi.org/10.1128/MMBR.00016-09)] [[PMC free article](/articles/PMC2832349/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/20197502/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microbiol.%20Mol.%20Biol.%20Rev.&title=Space%20Microbiology&author=G.%20Horneck&author=D.M.%20Klaus&author=R.L.%20Mancinelli&volume=74&publication_year=2010&pages=121-156&pmid=20197502&doi=10.1128/MMBR.00016-09&)]
* 5.Kim W., Tengra F.K., Shong J., Marchand N., Chan H., Young Z., Pangule R.C., Parra M., Dordick J.S., Plawsky J.L., et al. Effect of Spaceflight on Pseudomonas Aeruginosa Final Cell Density Is Modulated by Nutrient and Oxygen Availability. BMC Microbiol. 2013;13:241. doi: 10.1186/1471-2180-13-241. [[DOI](https://doi.org/10.1186/1471-2180-13-241)] [[PMC free article](/articles/PMC4228280/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24192060/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMC%20Microbiol.&title=Effect%20of%20Spaceflight%20on%20Pseudomonas%20Aeruginosa%20Final%20Cell%20Density%20Is%20Modulated%20by%20Nutrient%20and%20Oxygen%20Availability&author=W.%20Kim&author=F.K.%20Tengra&author=J.%20Shong&author=N.%20Marchand&author=H.%20Chan&volume=13&publication_year=2013&pages=241&pmid=24192060&doi=10.1186/1471-2180-13-241&)]
* 6.McLean R.J.C., Cassanto J.M., Barnes M.B., Koo J.H. Bacterial Biofilm Formation under Microgravity Conditions. FEMS Microbiol. Lett. 2001;195:115–119. doi: 10.1111/j.1574-6968.2001.tb10507.x. [[DOI](https://doi.org/10.1111/j.1574-6968.2001.tb10507.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11179638/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=FEMS%20Microbiol.%20Lett&title=Bacterial%20Biofilm%20Formation%20under%20Microgravity%20Conditions&author=R.J.C.%20McLean&author=J.M.%20Cassanto&author=M.B.%20Barnes&author=J.H.%20Koo&volume=195&publication_year=2001&pages=115-119&pmid=11179638&doi=10.1111/j.1574-6968.2001.tb10507.x&)]
* 7.Zea L., Larsen M., Estante F., Qvortrup K., Moeller R., Dias de Oliveira S., Stodieck L., Klaus D. Phenotypic Changes Exhibited by E. Coli Cultured in Space. Front. Microbiol. 2017;8:1598. doi: 10.3389/fmicb.2017.01598. [[DOI](https://doi.org/10.3389/fmicb.2017.01598)] [[PMC free article](/articles/PMC5581483/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28894439/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Microbiol.&title=Phenotypic%20Changes%20Exhibited%20by%20E.%20Coli%20Cultured%20in%20Space&author=L.%20Zea&author=M.%20Larsen&author=F.%20Estante&author=K.%20Qvortrup&author=R.%20Moeller&volume=8&publication_year=2017&pages=1598&pmid=28894439&doi=10.3389/fmicb.2017.01598&)]
* 8.Zea L., McLean R.J.C., Rook T.A., Angle G., Carter D.L., Delegard A., Denvir A., Gerlach R., Gorti S., McIlwaine D., et al. Potential Biofilm Control Strategies for Extended Spaceflight Missions. Biofilm. 2020;2:100026. doi: 10.1016/j.bioflm.2020.100026. [[DOI](https://doi.org/10.1016/j.bioflm.2020.100026)] [[PMC free article](/articles/PMC7798464/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33447811/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Biofilm&title=Potential%20Biofilm%20Control%20Strategies%20for%20Extended%20Spaceflight%20Missions&author=L.%20Zea&author=R.J.C.%20McLean&author=T.A.%20Rook&author=G.%20Angle&author=D.L.%20Carter&volume=2&publication_year=2020&pages=100026&pmid=33447811&doi=10.1016/j.bioflm.2020.100026&)]
* 9.Wilson J.W., Ott C.M., zu Bentrup K.H., Ramamurthy R., Quick L., Porwollik S., Cheng P., McClelland M., Tsaprailis G., Radabaugh T., et al. Space Flight Alters Bacterial Gene Expression and Virulence and Reveals a Role for Global Regulator Hfq. Proc. Natl. Acad. Sci. USA. 2007;104:16299–16304. doi: 10.1073/pnas.0707155104. [[DOI](https://doi.org/10.1073/pnas.0707155104)] [[PMC free article](/articles/PMC2042201/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17901201/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proc.%20Natl.%20Acad.%20Sci.%20USA&title=Space%20Flight%20Alters%20Bacterial%20Gene%20Expression%20and%20Virulence%20and%20Reveals%20a%20Role%20for%20Global%20Regulator%20Hfq&author=J.W.%20Wilson&author=C.M.%20Ott&author=K.H.%20zu%20Bentrup&author=R.%20Ramamurthy&author=L.%20Quick&volume=104&publication_year=2007&pages=16299-16304&pmid=17901201&doi=10.1073/pnas.0707155104&)]
* 10.Juergensmeyer M.A., Juergensmeyer E.A., Guikema J.A. Long-Term Exposure to Spaceflight Conditions Affects Bacterial Response to Antibiotics. Microgravity Sci. Technol. 1999;12:41–47. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11543359/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microgravity%20Sci.%20Technol.&title=Long-Term%20Exposure%20to%20Spaceflight%20Conditions%20Affects%20Bacterial%20Response%20to%20Antibiotics&author=M.A.%20Juergensmeyer&author=E.A.%20Juergensmeyer&author=J.A.%20Guikema&volume=12&publication_year=1999&pages=41-47&pmid=11543359&)]
* 11.Kacena M.A., Merrell G.A., Manfredi B., Smith E.E., Klaus D.M., Todd P. Bacterial Growth in Space Flight: Logistic Growth Curve Parameters for Escherichia Coli and Bacillus Subtilis. Appl. Microbiol. Biotechnol. 1999;51:229–234. doi: 10.1007/s002530051386. [[DOI](https://doi.org/10.1007/s002530051386)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/10091330/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Appl.%20Microbiol.%20Biotechnol.&title=Bacterial%20Growth%20in%20Space%20Flight:%20Logistic%20Growth%20Curve%20Parameters%20for%20Escherichia%20Coli%20and%20Bacillus%20Subtilis&author=M.A.%20Kacena&author=G.A.%20Merrell&author=B.%20Manfredi&author=E.E.%20Smith&author=D.M.%20Klaus&volume=51&publication_year=1999&pages=229-234&pmid=10091330&doi=10.1007/s002530051386&)]
* 12.Lapchine L., Moatti N., Gasset G., Richoilley G., Templier J., Tixador R. Antibiotic activity in space. Drugs Exp. Clin. Res. 1986;12:933–938. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/3569006/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Drugs%20Exp.%20Clin.%20Res.&title=Antibiotic%20activity%20in%20space&author=L.%20Lapchine&author=N.%20Moatti&author=G.%20Gasset&author=G.%20Richoilley&author=J.%20Templier&volume=12&publication_year=1986&pages=933-938&pmid=3569006&)]
* 13.Moatti N., Lapchine L., Gasset G., Richoilley G., Templier J., Tixador R. Preliminary Results of the Antibio Experiment. Naturwissenschaften. 1986;73:413–414. doi: 10.1007/BF00367282. [[DOI](https://doi.org/10.1007/BF00367282)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/3531874/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Naturwissenschaften&title=Preliminary%20Results%20of%20the%20Antibio%20Experiment&author=N.%20Moatti&author=L.%20Lapchine&author=G.%20Gasset&author=G.%20Richoilley&author=J.%20Templier&volume=73&publication_year=1986&pages=413-414&pmid=3531874&doi=10.1007/BF00367282&)]
* 14.Parra M., Ricco A.J., Yost B., McGinnis M.R., Hines J.W. Studying space effects on microorganisms autonomously: Genesat, pharmasat and the future of bio-nanosatellites. Gravit. Space Biol. 2008;21:9–17. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Gravit.%20Space%20Biol.&title=Studying%20space%20effects%20on%20microorganisms%20autonomously:%20Genesat,%20pharmasat%20and%20the%20future%20of%20bio-nanosatellites&author=M.%20Parra&author=A.J.%20Ricco&author=B.%20Yost&author=M.R.%20McGinnis&author=J.W.%20Hines&volume=21&publication_year=2008&pages=9-17&)]
* 15.Pathak Y., Santos, Zea L. Handbook of Space Pharmaceuticals. Springer; Cham, Switzerland: 2022.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Handbook%20of%20Space%20Pharmaceuticals&author=Y.%20Pathak&author=%20Santos&author=L.%20Zea&publication_year=2022&)]
* 16.Gasset G., Tixador R., Eche B., Lapchine L., Moatti N., Toorop P., Woldringh C. Growth and Division of Escherichia Coli under Microgravity Conditions. Res. Microbiol. 1994;145:111–120. doi: 10.1016/0923-2508(94)90004-3. [[DOI](https://doi.org/10.1016/0923-2508%2894%2990004-3)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/8090991/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Res.%20Microbiol.&title=Growth%20and%20Division%20of%20Escherichia%20Coli%20under%20Microgravity%20Conditions&author=G.%20Gasset&author=R.%20Tixador&author=B.%20Eche&author=L.%20Lapchine&author=N.%20Moatti&volume=145&publication_year=1994&pages=111-120&pmid=8090991&doi=10.1016/0923-2508(94)90004-3&)]
* 17.Tixador R., Richoilley G., Gasset G., Planel H., Moatti N., Lapchine L., Enjalbert L., Raffin J., Bost R., Zaloguev S.N., et al. Preliminary Results of Cytos 2 Experiment. Acta Astronaut. 1985;12:131–134. doi: 10.1016/0094-5765(85)90082-7. [[DOI](https://doi.org/10.1016/0094-5765%2885%2990082-7)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11542841/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Acta%20Astronaut.&title=Preliminary%20Results%20of%20Cytos%202%20Experiment&author=R.%20Tixador&author=G.%20Richoilley&author=G.%20Gasset&author=H.%20Planel&author=N.%20Moatti&volume=12&publication_year=1985&pages=131-134&pmid=11542841&doi=10.1016/0094-5765(85)90082-7&)]
* 18.Tixador R., Richoilley G., Gasset G., Templier J., Bes J.C., Moatti N., Lapchine L. Study of minimal inhibitory concentration of antibiotics on bacteria cultivated in vitro in space (Cytos 2 experiment) Aviat. Space Environ. Med. 1985;56:748–751. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/3899095/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Aviat.%20Space%20Environ.%20Med.&title=Study%20of%20minimal%20inhibitory%20concentration%20of%20antibiotics%20on%20bacteria%20cultivated%20in%20vitro%20in%20space%20(Cytos%202%20experiment)&author=R.%20Tixador&author=G.%20Richoilley&author=G.%20Gasset&author=J.%20Templier&author=J.C.%20Bes&volume=56&publication_year=1985&pages=748-751&pmid=3899095&)]
* 19.Zea L. Drug Discovery and Development in Space; Proceedings of the International Astronautical Congress; Jerusalem, Israel. 12–16 October 2015. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20International%20Astronautical%20Congress&title=Drug%20Discovery%20and%20Development%20in%20Space&author=L.%20Zea&)]
* 20.Zea L., Prasad N., Levy S.E., Stodieck L., Jones A., Shrestha S., Klaus D. A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space. PLoS ONE. 2016;11:e0164359. doi: 10.1371/journal.pone.0164359. [[DOI](https://doi.org/10.1371/journal.pone.0164359)] [[PMC free article](/articles/PMC5091764/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27806055/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20ONE&title=A%20Molecular%20Genetic%20Basis%20Explaining%20Altered%20Bacterial%20Behavior%20in%20Space&author=L.%20Zea&author=N.%20Prasad&author=S.E.%20Levy&author=L.%20Stodieck&author=A.%20Jones&volume=11&publication_year=2016&pages=e0164359&pmid=27806055&doi=10.1371/journal.pone.0164359&)]
* 21.Zea L., Nisar Z., Rubin P., Cortesão M., Luo J., McBride S.A., Moeller R., Klaus D., Müller D., Varanasi K.K., et al. Design of a Spaceflight Biofilm Experiment. Acta Astronaut. 2018;148:294–300. doi: 10.1016/j.actaastro.2018.04.039. [[DOI](https://doi.org/10.1016/j.actaastro.2018.04.039)] [[PMC free article](/articles/PMC6235448/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30449911/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Acta%20Astronaut.&title=Design%20of%20a%20Spaceflight%20Biofilm%20Experiment&author=L.%20Zea&author=Z.%20Nisar&author=P.%20Rubin&author=M.%20Cortes%C3%A3o&author=J.%20Luo&volume=148&publication_year=2018&pages=294-300&pmid=30449911&doi=10.1016/j.actaastro.2018.04.039&)]
* 22.Aunins T.R., Erickson K.E., Prasad N., Levy S.E., Jones A., Shrestha S., Mastracchio R., Stodieck L., Klaus D., Zea L., et al. Spaceflight Modifies Escherichia Coli Gene Expression in Response to Antibiotic Exposure and Reveals Role of Oxidative Stress Response. Front. Microbiol. 2018;9:310. doi: 10.3389/fmicb.2018.00310. [[DOI](https://doi.org/10.3389/fmicb.2018.00310)] [[PMC free article](/articles/PMC5865062/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29615983/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Front.%20Microbiol.&title=Spaceflight%20Modifies%20Escherichia%20Coli%20Gene%20Expression%20in%20Response%20to%20Antibiotic%20Exposure%20and%20Reveals%20Role%20of%20Oxidative%20Stress%20Response&author=T.R.%20Aunins&author=K.E.%20Erickson&author=N.%20Prasad&author=S.E.%20Levy&author=A.%20Jones&volume=9&publication_year=2018&pages=310&pmid=29615983&doi=10.3389/fmicb.2018.00310&)]
* 23.Law J., Cole R., Young M., Mason S. NASA Astronaut Urinary Conditions Associated with Spaceflight; Proceedings of the Annual Scientific Meeting of the Aerospace Medical Association; Atlantic City, NJ, USA. 1 April 2016. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20Annual%20Scientific%20Meeting%20of%20the%20Aerospace%20Medical%20Association&title=NASA%20Astronaut%20Urinary%20Conditions%20Associated%20with%20Spaceflight&author=J.%20Law&author=R.%20Cole&author=M.%20Young&author=S.%20Mason&)]
* 24.MacGowan A.P., Brown N.M., Holt H.A., Lovering A.M., McCulloch S.Y., Reeves D.S. An Eight-Year Survey of the Antimicrobial Susceptibility Patterns of 85,971 Bacteria Isolated from Patients in a District General Hospital and the Local Community. J. Antimicrob. Chemother. 1993;31:543–557. doi: 10.1093/jac/31.4.543. [[DOI](https://doi.org/10.1093/jac/31.4.543)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/8514649/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Antimicrob.%20Chemother.&title=An%20Eight-Year%20Survey%20of%20the%20Antimicrobial%20Susceptibility%20Patterns%20of%2085,971%20Bacteria%20Isolated%20from%20Patients%20in%20a%20District%20General%20Hospital%20and%20the%20Local%20Community&author=A.P.%20MacGowan&author=N.M.%20Brown&author=H.A.%20Holt&author=A.M.%20Lovering&author=S.Y.%20McCulloch&volume=31&publication_year=1993&pages=543-557&pmid=8514649&doi=10.1093/jac/31.4.543&)]
* 25.Klaus D.M. Clinostats and bioreactors. Gravit Space Biol. Bul. 2001;14:55–64. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11865869/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Gravit%20Space%20Biol.%20Bul.&title=Clinostats%20and%20bioreactors&author=D.M.%20Klaus&volume=14&publication_year=2001&pages=55-64&pmid=11865869&)]
* 26.Klaus D.M., Todd P., Schatz A. Functional Weightlessness during Clinorotation of Cell Suspensions. Adv. Space Res. 1998;21:1315–1318. doi: 10.1016/S0273-1177(97)00404-3. [[DOI](https://doi.org/10.1016/S0273-1177%2897%2900404-3)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11541387/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Adv.%20Space%20Res.&title=Functional%20Weightlessness%20during%20Clinorotation%20of%20Cell%20Suspensions&author=D.M.%20Klaus&author=P.%20Todd&author=A.%20Schatz&volume=21&publication_year=1998&pages=1315-1318&pmid=11541387&doi=10.1016/S0273-1177(97)00404-3&)]
* 27.Zea L., Estante F., Rosengren A., Stodieck L., Klaus L. Determining an Appropriate Clinostat Rotational Speed; Proceedings of the American Society for Gravitational and Space Research (ASGSR); Washington, DC, USA. 31 October–3 November 2018. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20American%20Society%20for%20Gravitational%20and%20Space%20Research%20(ASGSR)&title=Determining%20an%20Appropriate%20Clinostat%20Rotational%20Speed&author=L.%20Zea&author=F.%20Estante&author=A.%20Rosengren&author=L.%20Stodieck&author=L.%20Klaus&)]
* 28.Brown R.B., Klaus D., Todd P. Effects of Space Flight, Clinorotation, and Centrifugation on the Substrate Utilization Efficiency of E. coli. Microgravity Sci. Technol. 2002;13:24–29. doi: 10.1007/BF02881678. [[DOI](https://doi.org/10.1007/BF02881678)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/12521048/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microgravity%20Sci.%20Technol.&title=Effects%20of%20Space%20Flight,%20Clinorotation,%20and%20Centrifugation%20on%20the%20Substrate%20Utilization%20Efficiency%20of%20E.%20coli&author=R.B.%20Brown&author=D.%20Klaus&author=P.%20Todd&volume=13&publication_year=2002&pages=24-29&pmid=12521048&doi=10.1007/BF02881678&)]
* 29.Leidich J., Thomas E.A., Klaus D.M. A Novel Testing Protocol for Evaluating Particle Behavior in Fluid Flow under Simulated Reduced Gravity Conditions. SAE Tech. Paper Ser. 2009;2:100026. doi: 10.4271/2009-01-2359. [[DOI](https://doi.org/10.4271/2009-01-2359)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=SAE%20Tech.%20Paper%20Ser.&title=A%20Novel%20Testing%20Protocol%20for%20Evaluating%20Particle%20Behavior%20in%20Fluid%20Flow%20under%20Simulated%20Reduced%20Gravity%20Conditions&author=J.%20Leidich&author=E.A.%20Thomas&author=D.M.%20Klaus&volume=2&publication_year=2009&pages=100026&doi=10.4271/2009-01-2359&)]
* 30.Zea L., Stodieck L., Klaus D.M. Bacterial Growth and Susceptibility to Antibiotics in Simulated Reduced Levels of Gravity; Proceedings of the American Society for Gravitational and Space Research (ASGSR); Orlando, FL, USA. 3–8 November 2013. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20American%20Society%20for%20Gravitational%20and%20Space%20Research%20(ASGSR)&title=Bacterial%20Growth%20and%20Susceptibility%20to%20Antibiotics%20in%20Simulated%20Reduced%20Levels%20of%20Gravity&author=L.%20Zea&author=L.%20Stodieck&author=D.M.%20Klaus&)]
* 31.Forward T., Allen L., Stodieck L., Klaus D., Zea L. Growth Dynamics of Bacteria Under Simulated Lunar and Martian Gravities; Proceedings of the International Astronautical Congress; Washington, DC, USA. 21–25 October 2018. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20International%20Astronautical%20Congress&title=Growth%20Dynamics%20of%20Bacteria%20Under%20Simulated%20Lunar%20and%20Martian%20Gravities&author=T.%20Forward&author=L.%20Allen&author=L.%20Stodieck&author=D.%20Klaus&author=L.%20Zea&)]
* 32.Forward T. Undergraduate Honor’s Thesis. University of Colorado; Boulder, CO, USA: 2020. Preliminary Protocols for the Quantification of Shewanella oneidensis Iron Reduction Performance. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Undergraduate%20Honor%E2%80%99s%20Thesis&author=T.%20Forward&publication_year=2020&)]
* 33.Allen L.A., Kalani A.H., Zea L. Ciprofloxacin Efficacy against Urinary Tract Pathogens cultured Under Simulated Micro-, Lunar, and Martian Gravities; Proceedings of the International Astronautical Congress; Dubai, United Arab Emirates. 25–29 October 2021. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20International%20Astronautical%20Congress&title=Ciprofloxacin%20Efficacy%20against%20Urinary%20Tract%20Pathogens%20cultured%20Under%20Simulated%20Micro-,%20Lunar,%20and%20Martian%20Gravities&author=L.A.%20Allen&author=A.H.%20Kalani&author=L.%20Zea&)]
* 34.Klaus D., Simske S., Todd P., Stodieck L. Investigation of Space Flight Effects on Escherichia Coli and a Proposed Model of Underlying Physical Mechanisms. Microbiology. 1997;143:449–455. doi: 10.1099/00221287-143-2-449. [[DOI](https://doi.org/10.1099/00221287-143-2-449)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/9043122/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Microbiology&title=Investigation%20of%20Space%20Flight%20Effects%20on%20Escherichia%20Coli%20and%20a%20Proposed%20Model%20of%20Underlying%20Physical%20Mechanisms&author=D.%20Klaus&author=S.%20Simske&author=P.%20Todd&author=L.%20Stodieck&volume=143&publication_year=1997&pages=449-455&pmid=9043122&doi=10.1099/00221287-143-2-449&)]
* 35.Lynch S.V., Brodie E.L., Matin A. Role and Regulation of σs in General Resistance Conferred by Low-Shear Simulated Microgravity in Escherichia Coli. J. Bacteriol. 2004;186:8207–8212. doi: 10.1128/JB.186.24.8207-8212.2004. [[DOI](https://doi.org/10.1128/JB.186.24.8207-8212.2004)] [[PMC free article](/articles/PMC532419/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15576768/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Bacteriol.&title=Role%20and%20Regulation%20of%20%CF%83s%20in%20General%20Resistance%20Conferred%20by%20Low-Shear%20Simulated%20Microgravity%20in%20Escherichia%20Coli&author=S.V.%20Lynch&author=E.L.%20Brodie&author=A.%20Matin&volume=186&publication_year=2004&pages=8207-8212&pmid=15576768&doi=10.1128/JB.186.24.8207-8212.2004&)]
* 36.Ito A., Taniuchi A., May T., Kawata K., Okabe S. Increased Antibiotic Resistance of Escherichia Coli in Mature Biofilms. Appl. Environ. Microbiol. 2009;75:4093–4100. doi: 10.1128/AEM.02949-08. [[DOI](https://doi.org/10.1128/AEM.02949-08)] [[PMC free article](/articles/PMC2698376/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19376922/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Appl.%20Environ.%20Microbiol.&title=Increased%20Antibiotic%20Resistance%20of%20Escherichia%20Coli%20in%20Mature%20Biofilms&author=A.%20Ito&author=A.%20Taniuchi&author=T.%20May&author=K.%20Kawata&author=S.%20Okabe&volume=75&publication_year=2009&pages=4093-4100&pmid=19376922&doi=10.1128/AEM.02949-08&)]
* 37.Wang J.-H., Singh R., Benoit M., Keyhan M., Sylvester M., Hsieh M., Thathireddy A., Hsieh Y.-J., Matin A.C. Sigma S-Dependent Antioxidant Defense Protects Stationary-Phase Escherichia Coli against the Bactericidal Antibiotic Gentamicin. Antimicrob Agents Chemother. 2014;58:5964–5975. doi: 10.1128/AAC.03683-14. [[DOI](https://doi.org/10.1128/AAC.03683-14)] [[PMC free article](/articles/PMC4187989/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/25070093/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Antimicrob%20Agents%20Chemother.&title=Sigma%20S-Dependent%20Antioxidant%20Defense%20Protects%20Stationary-Phase%20Escherichia%20Coli%20against%20the%20Bactericidal%20Antibiotic%20Gentamicin&author=J.-H.%20Wang&author=R.%20Singh&author=M.%20Benoit&author=M.%20Keyhan&author=M.%20Sylvester&volume=58&publication_year=2014&pages=5964-5975&pmid=25070093&doi=10.1128/AAC.03683-14&)]
* 38.Matin A., Auger E.A., Blum P.H., Schultz J.E. Genetic basis of starvation survival in nondifferentiating bacteria. Annu Rev. Microbiol. 1989;43:293–314. doi: 10.1146/annurev.mi.43.100189.001453. [[DOI](https://doi.org/10.1146/annurev.mi.43.100189.001453)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/2478072/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Annu%20Rev.%20Microbiol.&title=Genetic%20basis%20of%20starvation%20survival%20in%20nondifferentiating%20bacteria&author=A.%20Matin&author=E.A.%20Auger&author=P.H.%20Blum&author=J.E.%20Schultz&volume=43&publication_year=1989&pages=293-314&pmid=2478072&doi=10.1146/annurev.mi.43.100189.001453&)]
* 39.Matin A. The Molecular Basis of Carbon-Starvation-Induced General Resistance in Escherichia Coli. Molecular Microbiol. 1991;5:3–10. doi: 10.1111/j.1365-2958.1991.tb01819.x. [[DOI](https://doi.org/10.1111/j.1365-2958.1991.tb01819.x)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/2014002/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Molecular%20Microbiol.&title=The%20Molecular%20Basis%20of%20Carbon-Starvation-Induced%20General%20Resistance%20in%20Escherichia%20Coli&author=A.%20Matin&volume=5&publication_year=1991&pages=3-10&pmid=2014002&doi=10.1111/j.1365-2958.1991.tb01819.x&)]
* 40.Padgen M.R., Lera M.P., Parra M.P., Ricco A.J., Chin M., Chinn T.N., Cohen A., Friedericks C.R., Henschke M.B., Snyder T.V., et al. EcAMSat Spaceflight Measurements of the Role of σs in Antibiotic Resistance of Stationary Phase Escherichia Coli in Microgravity. Life Sci. Space Res. 2020;24:18–24. doi: 10.1016/j.lssr.2019.10.007. [[DOI](https://doi.org/10.1016/j.lssr.2019.10.007)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31987476/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Life%20Sci.%20Space%20Res.&title=EcAMSat%20Spaceflight%20Measurements%20of%20the%20Role%20of%20%CF%83s%20in%20Antibiotic%20Resistance%20of%20Stationary%20Phase%20Escherichia%20Coli%20in%20Microgravity&author=M.R.%20Padgen&author=M.P.%20Lera&author=M.P.%20Parra&author=A.J.%20Ricco&author=M.%20Chin&volume=24&publication_year=2020&pages=18-24&pmid=31987476&doi=10.1016/j.lssr.2019.10.007&)]
* 41.Boone T., Cohen A., Chin M., Chinn T., Friedericks C., Jackson E., Keyhan M., Lera M., Matin A., Mayer D., et al. Coli AntiMicrobial Satellite (EcAMSat): Science Payload System Development and Test. NASA Ames Research Center; Moffett Field, CA, USA: 2014.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Coli%20AntiMicrobial%20Satellite%20(EcAMSat):%20Science%20Payload%20System%20Development%20and%20Test&author=T.%20Boone&author=A.%20Cohen&author=M.%20Chin&author=T.%20Chinn&author=C.%20Friedericks&publication_year=2014&)]
* 42.Matin A.C., Benoit M., Chin M., Chinn T.N., Cohen A., Friedericks C., Henschke M.B., Keyhan M., Lera M.P., Padgen M.R., et al. EcAMSat: Effect of Space-Flight on Antibiotic Resistance of a Pathogenic Bacterium and Its Genetic Basis. [(accessed on 25 July 2022)]; Available online: <https://ntrs.nasa.gov/citations/20150022373>.
* 43.Sanchez G.V., Master R.N., Karlowsky J.A., Bordon J.M. In Vitro Antimicrobial Resistance of Urinary Escherichia Coli Isolates among U.S. Outpatients from 2000 to 2010. Antimicrob. Agents Chemother. 2012;56:2181–2183. doi: 10.1128/AAC.06060-11. [[DOI](https://doi.org/10.1128/AAC.06060-11)] [[PMC free article](/articles/PMC3318377/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/22252813/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Antimicrob.%20Agents%20Chemother.&title=In%20Vitro%20Antimicrobial%20Resistance%20of%20Urinary%20Escherichia%20Coli%20Isolates%20among%20U.S.%20Outpatients%20from%202000%20to%202010&author=G.V.%20Sanchez&author=R.N.%20Master&author=J.A.%20Karlowsky&author=J.M.%20Bordon&volume=56&publication_year=2012&pages=2181-2183&pmid=22252813&doi=10.1128/AAC.06060-11&)]
* 44.Flores P., Schauer R., McBride S.A., Luo J., Cortesão M., Hoen C., Doraisingam S., Widhalm D., Chadha J., Meyerson H., et al. Preparation for and Performance of a Pseudomonas aeruginosa Biofilm Experiment on Board the International Space Station; Proceedings of the International Astronautical Congress; Dubai, United Arab Emirates. 25–29 October 2021. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20International%20Astronautical%20Congress&title=Preparation%20for%20and%20Performance%20of%20a%20Pseudomonas%20aeruginosa%20Biofilm%20Experiment%20on%20Board%20the%20International%20Space%20Station&author=P.%20Flores&author=R.%20Schauer&author=S.A.%20McBride&author=J.%20Luo&author=M.%20Cortes%C3%A3o&)]
* 45.Sugar in Urine: What You Should Know. [(accessed on 24 August 2022)]. Available online: <https://www.lencolab.com/publications/2021/4/sugar-in-urine-what-you-should-know.html>.
* 46.Andrews J.M. Determination of Minimum Inhibitory Concentrations. J. Antimicrob. Chemother. 2001;48:5–16. doi: 10.1093/jac/48.suppl\_1.5. [[DOI](https://doi.org/10.1093/jac/48.suppl_1.5)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11420333/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Antimicrob.%20Chemother.&title=Determination%20of%20Minimum%20Inhibitory%20Concentrations&author=J.M.%20Andrews&volume=48&publication_year=2001&pages=5-16&pmid=11420333&doi=10.1093/jac/48.suppl_1.5&)]
* 47.Kessler J.O. The internal dynamics of slowly rotating biological systems. ASGSB Bull. Publ. Am. Soc. Gravit. Space Biol. 1992;5:11–21. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/11537637/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=ASGSB%20Bull.%20Publ.%20Am.%20Soc.%20Gravit.%20Space%20Biol.&title=The%20internal%20dynamics%20of%20slowly%20rotating%20biological%20systems&author=J.O.%20Kessler&volume=5&publication_year=1992&pages=11-21&pmid=11537637&)]
* 48.Ilgrande C., Defoirdt T., Vlaeminck S.E., Boon N., Clauwaert P. Media Optimization, Strain Compatibility, and Low-Shear Modeled Microgravity Exposure of Synthetic Microbial Communities for Urine Nitrification in Regenerative Life-Support Systems. Astrobiology. 2019;19:1353–1362. doi: 10.1089/ast.2018.1981. [[DOI](https://doi.org/10.1089/ast.2018.1981)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/31657947/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Astrobiology&title=Media%20Optimization,%20Strain%20Compatibility,%20and%20Low-Shear%20Modeled%20Microgravity%20Exposure%20of%20Synthetic%20Microbial%20Communities%20for%20Urine%20Nitrification%20in%20Regenerative%20Life-Support%20Systems&author=C.%20Ilgrande&author=T.%20Defoirdt&author=S.E.%20Vlaeminck&author=N.%20Boon&author=P.%20Clauwaert&volume=19&publication_year=2019&pages=1353-1362&pmid=31657947&doi=10.1089/ast.2018.1981&)]
* 49.Klaus D.M., Luttges M.W., Stodieck L.S. Investigation of Space Flight Effects on Escherichia coli Growth. [(accessed on 9 August 2022)];SAE Trans. 1994 103:470–478. Available online: <http://www.jstor.org/stable/44614859>. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=SAE%20Trans.&title=Investigation%20of%20Space%20Flight%20Effects%20on%20Escherichia%20coli%20Growth&author=D.M.%20Klaus&author=M.W.%20Luttges&author=L.S.%20Stodieck&volume=103&publication_year=1994&pages=470-478&)]
* 50.Zea L. Ph.D. Thesis. University of Colorado; Boulder, CO, USA: 2015. Phenotypic and Gene Expression Responses of E. coli to Antibiotics during Spaceflight. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Ph.D.%20Thesis&author=L.%20Zea&publication_year=2015&)]
* 51.Barratt M.R., Pool S.L. Principles of Clinical Medicine for Space Flight. Springer; New York, NY, USA: 2008.  [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Principles%20of%20Clinical%20Medicine%20for%20Space%20Flight&author=M.R.%20Barratt&author=S.L.%20Pool&publication_year=2008&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Data Availability Statement

The code presented in this study is openly available in GitHub at <https://github.com/SpaceLuisZea/Clinostat> (accessed on 9 August 2022).