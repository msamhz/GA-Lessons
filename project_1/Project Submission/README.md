# SAT & ACT Data: Analyzing test scores and participation rates from 2017-18 and also income levels by States

 - [Problem Statement](#Problem-Statement)
 - [Executive Summary](#Executive-Summary)
 - [ACT-SAT-Data-Recommendations.ipynb Contents](#ACT-SAT-Data-Recommendations.ipynb-Contents)
 - [Data Dictionary](#Data-Dictionary)
 - [External Research](#External-Research)
 - [Conclusions & Recommendations](#Conclusions-&-Recommendations)
 - [Data Sources](#Data-Sources)

## Problem Statement
From Washington’s Post, scores from the ACT show that only 9% of students.<sup>1</sup> in the class of 2017 who came from low-income families are strongly ready for college in 2017. This is a cause of concern, as this disparities in college readiness will put students of lower income to a disadvantage competing with the rest, hence less like to have access to high-quality educational and career planning opportunities and resources. Thus, we will need to evaluate both test across 2017 and 2018 and produce improvement plans. 


**Citations**:
<br>
<sup>1</sup> https://www.washingtonpost.com/local/education/we-didnt-know-it-was-this-bad-new-act-scores-show-huge-achievement-gaps/2017/09/06/c6397f36-9279-11e7-aace-04b862b2b3f3_story.html

---

### ACT-SAT-Data-Recommendations.ipynb Contents:
- Background
- Data-Import-&-Cleaning
- 2017-Data-Import-and-Cleaning
- 2018-Data-Import-and-Cleaning
- Merge-with-Income
- Data-Dictionary
- Exploratory-Data-Analysis
- Visualize-the-Data
- Conclusions-and-Recommendations

---
## Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|**state**|*object*|final_income|Names of all US states and the District of Columbia| 
|**sat_prt_2017**|*float*|final_income|The percentage of 2017 graduating students who took SAT ( units percent to two decimal places, 0.05 means 5%)| 
|**sat_erw_2017**|*float*|final_income|The mean score of SAT Evidence-Based-Reading and Writing (ERW) category in 2017 (Score range from 200-800)| 
|**sat_math_2017**|*float*|final_income|The mean score of SAT Math of the in 2017 (Score range from 200-800)|
|**sat_total_2017**|*float*|final_income|The mean total score of SAT combining Math and ERW (Score range from 200-800)|
|**act_prt_2017**|*float*|final_income|The percentage of 2017 graduating students who took ACT ( units percent to two decimal places, 0.05 means 5%)|
|**act_eng_2017**|*float*|final_income|The mean score of ACT English score (Score range from 1-36)|
|**act_math_2017**|*float*|final_income|The mean score of ACT Math score (Score range from 1-36)|
|**act_read_2017**|*float*|final_income|The mean score of ACT Reading score (Score range from 1-36)|
|**act_sci_2017**|*float*|final_income|The mean score of ACT Science score (Score range from 1-36)|
|**act_comp_2017**|*float*|final_income|The mean total score of ACT combining English, Math, Reading and Science (Score range from 1-36)|
|**sat_prt_2018**|*float*|final_income|The percentage of 2018 graduating students who took SAT ( units percent to two decimal places, 0.05 means 5%)| 
|**sat_erw_2018**|*float*|final_income|The mean score of SAT Evidence-Based-Reading and Writing (ERW) category in 2017 (Score range from 200-800)| 
|**sat_math_2018**|*float*|final_income|The mean score of SAT Math of the in 2018 (Score range from 200-800)|
|**sat_total_2018**|*float*|final_income|The mean total score of SAT combining Math and ERW (Score range from 200-800)|
|**act_prt_2018**|*float*|final_income|The percentage of 2018 graduating students who took ACT ( units percent to two decimal places, 0.05 means 5%)|
|**act_eng_2018**|*float*|final_income|The mean score of ACT English score (Score range from 1-36)|
|**act_math_2018**|*float*|final_income|The mean score of ACT Math score (Score range from 1-36)|
|**act_read_2018**|*float*|final_income|The mean score of ACT Reading score (Score range from 1-36)|
|**act_sci_2018**|*float*|final_income|The mean score of ACT Science score (Score range from 1-36)|
|**act_comp_2018**|*float*|final_income|The mean total score of ACT combining English, Math, Reading and Science (Score range from 1-36)|
|**inc_cap**|*float*|final_income|The mean income per capita by States 2015 (Income range from \\$35444 - $71496)|
|**sat_ave**|*float*|final_income|The average SAT score between 2017 and 2018 (Income range from 963.5 - 1296.5)|
|**act_ave**|*float*|final_income|The average ACT score between 2017 and 2018 (Income range from 25.45 - 25.45)|
|**cat_inc**|*Object*|final_income|The Income category by State (Contains four categories split by 25%, 50% and 75%)|
|**cat_inc_<\\$41,000**|*Object*|final_income|Accounts for states under category, whereby 0 is not in category while 1 indicates state under category of \\$41000 or less (Binary values indicating income <\\$41,000)|
|**cat_inc_<\\$41,000-\\$45,000**|*Object*|final_income|Accounts for states under category, whereby 0 is not in category while 1 indicates state under category of between 41000 to 45000 (Binary values indicating income >\\$41,000-\\$45,000)
|**cat_inc_<\\$45,000-\\$51,000**|*Object*|final_income|Accounts for states under category, whereby 0 is not in category while 1 indicates state under category of 45000 to 51000 or less (Binary values indicating income >\\$45,000-\\$51,000)|
|**cat_inc_>\\$51,000**|*Object*|final_income|Accounts for states under category, whereby 0 is not in category while 1 indicates state under category of more than 51000 (Binary values indicating income >\\$51,000)|

---


**SIGNIFICANT FINDINGS**

When analyzing the datasets, there were substantial findings about SAT and ACT test scores and participation rates. Listed below are the most significant findings, focusing primarily on the SAT: 
- SAT Scores and Participation rates, 2017-18: The distribution of average test scores from all states was bimodal. Distributin seems to be skewed rightwards. Mean of SAT scores decreased from 2017 to 2018, while increasing participation from 2017 to 2018, due to the  
- SAT Test Scores vs Participation Rates, 2017-18: In both years, there was a strong negative correlation between test scores and participation rates.<sup>1</sup>. The higher the participation rate, the lower the test score.
- ACT Test scores exhibits a higher positive correlation with income, showing disparity across income groups. This is further supported by ACT research team that there is such a trend.<sup>2</sup>
- SAT Test Scores exhibits simpson's paradox when combined with participation rates, SAT scores and income group. Initially when plotted income vs SAT scores, there were a small negative correlation. As we proceed to split the data by participation level, the trend of each sub groups tend to be more positvely correlated. Hence, this shows there migth be some underlying marginal association between the two categorical variables. Hence, more careful understanding is needed to decouple before assuming the validity of the relationship between income and the scores. 
- ACT Worst performing countries consistently and low income group: Nevada, South Carolina and Mississipi. SAT Worst perofrming countries and a lower income group: Idaho. 

 
**Citations**:
<br>
<sup>1</sup> https://medium.com/@james.dargan/participation-skews-state-averages-f68969371a01
<br>
<sup>2</sup> https://www.edweek.org/ew/articles/2018/10/31/sat-scores-rise-as-number-of-test-takers.html

---

## External Research
- The higher participation rates the lower the average scores in a state. Research from ACT mentions a 1.22 score poinrts after the adoption for each additional 25% tested.<sup>1</sup>
- Income per capita by US states - 2015.<sup>2</sup>
- ACT scores showing disparity between the rich and the poorer states by ACT Research Team.<sup>3</sup>
- In the 2017-18 school year, nearly one million students participated in SAT School Day, compared to about 800,000 in 2016-17 and 460,000 in 2015-16. In 2014-15, only three states—Delaware, Idaho, Maine—and the District of Columbia participated in SAT School Day. In 2017-18, 10 states—Colorado, Connecticut, Delaware, Idaho, Illinois, Maine, Michigan, New Hampshire, Rhode Island, West Virginia—and the District of Columbia gave the SAT to public school students for free.<sup>4</sup>
- States require students to take the SAT or ACT.<sup>5</sup>
- Participation-skews-state-averages.<sup>6</sup>
- Colorado <sup>7</sup> and Illinois <sup>8</sup> has increased participation for SAT, mandate changed on 2017
- ACT correlation with income.<sup>9</sup>
- US States list.<sup>10</sup>
- Because cultural and socioeconomic factors and the quality of schools vary greatly between districts and states, average SAT scores vary greatly.<sup>11</sup>


---

**Citations**:
<br>
<sup>1</sup> https://www.act.org/content/dam/act/unsecured/documents/Statewide-Adoption.pdf
<br>
<sup>2</sup> https://www.infoplease.com/business/poverty-income/capita-personal-income-state
<br>
<sup>3</sup> https://www.act.org/content/dam/act/unsecured/documents/R1604-ACT-Composite-Score-by-Family-Income.pdf
<br>
<sup>4</sup> https://newsroom.collegeboard.org/more-2-million-students-class-2018-took-sat-highest-ever#:~:text=10%2F25%2F2018-,More%20Than%202%20Million%20Students%20in%20the%20Class%20of%202018,gaining%20greater%20access%20and%20opportunity.
<br>
<sup>5</sup> https://www.edweek.org/teaching-learning/which-states-require-students-to-take-the-sat-or-act
<br>
<sup>6</sup> https://medium.com/@james.dargan/participation-skews-state-averages-f68969371a01
<br>
<sup>7</sup> https://testive.com/colorado-sat-change-2017/
<br>
<sup>8</sup> https://testive.com/illinois/
<br>
<sup>9</sup> https://www.act.org/content/dam/act/unsecured/documents/R1604-ACT-Composite-Score-by-Family-Income.pd
<br>
<sup>10</sup> https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210
<br>
<sup>11</sup> https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/


---

## Conclusions & Recommendations 

From this project, we have seen that there is distinct negative correlation between the participations rates and test performance, where the we see the higher the participation rate, the lower the test scores, across SAT/ACT, and across income groups. Its relative to the size of the students taking part in the test, and the volunteering aspect of students who are interested in taking part in the test for further studies in colleges of their choice. We should focus towards providing more test help resources in order to help the weaker states. 

In addition, we have concluded that there is a positive correlation between the scores (more for ACT than for SAT) with test performances. A higher percentage of states with lower income has lower scores compared to the average. This is also supported by ACT research team, showed showing difference in test performance by the lower and higher income group.<sup>1</sup>

From the EDA analysis and visualizations, we have identified that across two years, out of 4 common states identified, 3 of which were from the lower income group taking mandatory ACTs. Another state, Idaho was identified to be lowest for SAT under lower income group. 


**Recommendations** In order to help bring up the overall likelihood of most students having better chances to enter college and essential prep and resources, we would like to recommend;

- Allocating more funding / test preparation resources in states with lower income per capita such as Nevada, Mississippi, South Carolina and Idaho. 

- Recommend states to provide free waiver especially for lower income to access to OPL, Online prep live. Reports from OPL mentioned that one academic year associated with an average score of 1.64, especially boosting up students from the lower income group. <sup>2</sup>

**Citations**
<br>
<sup>1</sup> https://www.act.org/content/dam/act/unsecured/documents/R1604-ACT-Composite-Score-by-Family-Income.pd
<br>
<sup>2</sup> https://www.act.org/content/dam/act/unsecured/documents/R1705-test-prep-study-2018-08.pdf


--- 
## Data Sources
The sources of the datasets used in this analysis: 
- [sat_2017 dataset](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)
- [sat_2018 dataset](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)
- [act_2017 dataset](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)
- [act_2018 dataset](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)
- [us_income dataset](https://www.infoplease.com/business/poverty-income/capita-personal-income-state)
- [us_states](https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210)