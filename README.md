# Aid Appropriateness Assessment (Thesis)


## Overview
By matching information on firm level from two sources this thesis provides insights into the effects of government support during the COVID-19 pandemic in Germany. To provide an impact assessment a quasi-experimental approach with a DiD regression is employed to estimate the causal effect of aid measures on the liquidity and solvency of companies. The results sug- gest that in 2020 loan-based measures supported companies by improving their liquidity by 5.3 %, while grant based aid was insufficient as a liquidity injection since beneficiaries had no improvement in liquidity and relatively higher debt. Only in 2021 grants programs became effective in providing liquidity and preserving the equity of firms. In 2021 the liquidity increase of grant beneficiaries was 7.7 %, twice as high as the effect of grants in 2021.
The analysis of insolvencies amongst aid beneficiaries suggests that they were already significantly weaker before the pandemic and that aid measures were less effective in supporting them. A sector view reveals that the most supported industries gastronomy and accommodation show below average insolvency rates, suggesting that aid measures were successful in reducing the chance of insolvency in their presumed main target sectors.
Finally, the data granularity has been exploited with a combination of generalized propensity scores and a generalized linear model (GLM) to advance the assessment from a binary to a continuous treatment perspective. Overall, the visualizations are in line with the results from the previous DiD approach and don’t show any concerning abnormalities. In greater detail, the visualization reveals heterogeneity amongst beneficiaries from different industries, which connects with the observed heterogeneity in insolvencies of different industries.

## Topic
Topic: **The effect of government support during the COVID-19 pandemic: Firm-level evidence from Germany**  

The project comprises the following components:
1. Data set creation by matching information from the European state aid transparency database of beneficiaries with data from the Bundesanzeiger
2. A DiD regression to measure the causal effect of aid instruments on the firm liquidity.
3. A approach with generalized propensity scores (GPS) to provide a granular picture of the effects at different levels of aid
 

## Key Findings
<img src="https://github.com/m-schildt/AAA/blob/main/paper/Figures/causal_curves1.png?raw=true" alt="Alt text" title="Optional title">

<img src="https://github.com/m-schildt/AAA/blob/main/paper/Figures/chart_ratios_insolvence.png?raw=true?raw=true" alt="Alt text" title="Boxplots with balance sheet ratios from the obtained dataset">


## Data
* 
  * **First** European state aid transparency database for data on aid beneficiaries
  * **Second** Bundesanzeiger for Company level financial information
  * **Third** The insolvencies notification platform
  

## Code
* 
  * [**1** preparation of state aid date](https://github.com/m-schildt/AAA/blob/main/paper/main.pdf)
  * **Second** Bundesanzeiger for Company level financial information
  * **Third** The insolvencies notification platform
  
  
  

## Full Thesis
* [here](https://github.com/m-schildt/AAA/blob/main/paper/main.pdf)

