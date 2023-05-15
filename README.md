# Aid Appropriateness Assessment

<img src="https://github.com/m-schildt/AAA/blob/main/paper/Figures/causal_curves2.png?raw=true" alt="Alt text" title="Optional title">

## Overview
By matching information on firm level from two sources this thesis provides insights into the effects of government support during the COVID-19 pandemic in Germany. To provide an impact assessment a quasi-experimental approach with a DiD regression is employed to estimate the causal effect of aid measures on the liquidity and solvency of companies. The results sug- gest that in 2020 loan-based measures supported companies by improving their liquidity by 5.3 %, while grant based aid was insufficient as a liquidity injection since beneficiaries had no improvement in liquidity and relatively higher debt. Only in 2021 grants programs became effective in providing liquidity and preserving the equity of firms. In 2021 the liquidity increase of grant beneficiaries was 7.7 %, twice as high as the effect of grants in 2021.
The analysis of insolvencies amongst aid beneficiaries suggests that they were already significantly weaker before the pandemic and that aid measures were less effective in supporting them. A sector view reveals that the most supported industries gastronomy and accommodation show below average insolvency rates, suggesting that aid measures were successful in reducing the chance of insolvency in their presumed main target sectors.
Finally, the data granularity has been exploited with a combination of generalized propensity scores and a generalized linear model (GLM) to advance the assessment from a binary to a continuous treatment perspective. Overall, the visualizations are in line with the results from the previous DiD approach and don’t show any concerning abnormalities. In greater detail, the visualization reveals heterogeneity amongst beneficiaries from different industries, which connects with the observed heterogeneity in insolvencies of different industries.


## Full Thesis
* [here](https://github.com/m-schildt/AAA/blob/main/paper/main.pdf)

## Topic
**The effect of government support during the COVID-19 pandemic: Firm-level evidence from Germany**  

The project comprises the following components:
1. Data set creation by matching information aid data and financial information on a firm-level
2. Difference-in-Differences methodology to measure the causal effect of aid instruments on the firm liquidity.
3. A Generalized Propensity Scores (GPS) to provide a granular picture of the effects at different levels of aid


## Key Insights

<img src="https://github.com/m-schildt/AAA/blob/main/paper/Figures/chart_ratios_insolvence.png?raw=true?raw=true" alt="Alt text" title="Boxplots with balance sheet ratios from the obtained dataset">

<img src="https://github.com/m-schildt/AAA/blob/main/paper/Figures/causal_curves1.png?raw=true" alt="Alt text" title="Optional title">




## Data
* 
  * **First** European state aid transparency database for data on aid beneficiaries
  * **Second** Bundesanzeiger for Company level financial information
  * **Third** The insolvencies notification platform
  

## Code
* 
  * **1** [Preparation of state aid date](https://github.com/m-schildt/AAA/blob/main/1_main.ipynb)
  * **2** [Scraping of  Company level financial information](https://github.com/m-schildt/AAA/blob/main/2_financial_information.ipynb)
  * **3** [Parsing balance sheet data and calculate ratios](https://github.com/m-schildt/AAA/blob/main/3_KPI_calculator.ipynb)
  * **4** [Data Merge and Dataset creating](https://github.com/m-schildt/AAA/blob/main/4_data_merge.ipynb)
  * **5** [Difference-in-Differences Method](https://github.com/m-schildt/AAA/blob/main/5_diff%26diff.ipynb)
  * **6.1** [Insolvency data scraping](https://github.com/m-schildt/AAA/blob/main/6.1_insolvency_data.ipynb)
  * **6.2** [Insolvency Analysis](https://github.com/m-schildt/AAA/blob/main/6.2_insolvencies%20analysis.ipynb)
  * **7.1** [Step-by-Step Demo on the causal curve calculation](https://github.com/m-schildt/AAA/blob/main/7.1_response_curves_demo.ipynb)
  * **7.2** [Causal curves on liquidity and Solvency](https://github.com/m-schildt/AAA/blob/main/7.2_response_curves.ipynb)
  * **7.3** [Causal curves for different sectors](https://github.com/m-schildt/AAA/blob/main/7.3_response_curves_sectors.ipynb)
  
  


