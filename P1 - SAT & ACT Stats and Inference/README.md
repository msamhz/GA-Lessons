# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Testing, Statistical Summaries and Inference


## Problem Statement

The new format for the SAT was released in March 2016. With this new test format, **how can College Board improve the statewide participation rates for the SAT, as compared to the ACT?**


## Executive Summary

The datasets of aggregate SAT and ACT scores and participation rates from each state in the United States for 2017 and 2018 are given. I'll seek to identify trends in the data and combine data analysis with outside research to identify likely factors influencing participation rates in various states.

In this project, I utilize the following skillsets:
- Working with Jupyter notebooks for development and reporting
- Programmatically interacting with files and directories
- Exploratory Data Analysis (EDA) with Pandas
- Data Visualization with Matplotlib & Seaborn
- Basic Statistics (Distributions, Hypothesis Testing, etc.)


## Datasets Used

The following datasets were provided in the form of CSV files for this project:

- [2017 SAT Scores](./data/sat_2017.csv)
- [2017 ACT Scores](./data/act_2017.csv)
- [2018 SAT Scores](./data/sat_2018.csv)
- [2018 ACT Scores](./data/act_2018_updated.csv)

These datasets give the average SAT and ACT scores by state, as well as participation rates, for the graduating class of 2017 and 2018.

The datasets were sourced from the following sources:

- [2017 SAT Scores](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)
- [2017 ACT Scores](https://www.act.org/content/dam/act/unsecured/documents/cccr2017/ACT_2017-Average_Scores_by_State.pdf)
- [2018 SAT Scores](https://reports.collegeboard.org/sat-suite-program-results/state-results)
- [2018 ACT Scores](http://www.act.org/content/dam/act/unsecured/documents/cccr2018/Average-Scores-by-State.pdf)


## Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**states**|object|SAT 2017, ACT 2017, SAT 2018 & ACT 2018|The states (50) and federal districts (1) of the USA.|
|**sat17_participation**|float|SAT 2017|The percentage of students from the graduating class of 2017 who took the 2017 SAT (units percent, where 0.02 represents 2%).|
|**sat17_ebrw**|int|SAT 2017|Average scaled scores for the 2017 SAT Evidence-Based Reading and Writing (EBRW) section (without decimal places, in a range of 200 - 800 (inclusive)).|
|**sat17_math**|int|SAT 2017|Average scaled scores for the 2017 SAT Math section (without decimal places, in a range of 200 - 800 (inclusive)).|
|**sat17_total**|int|SAT 2017|Average scaled total scores for the 2017 SAT (without decimal places, in a range of 400 - 1600 (inclusive)). In SAT, the *individual* total scores are calculated by adding the two sections' scores.|
|**act17_participation**|float|ACT 2017|The percentage of students from the graduating class of 2017 who took the 2017 ACT (units percent, where 0.02 represents 2%).|
|**act17_english**|float|ACT 2017|Average scaled scores for the 2017 ACT English section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act17_math**|float|ACT 2017|Average scaled scores for the 2017 ACT Math section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act17_reading**|float|ACT 2017|Average scaled scores for the 2017 ACT Reading section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act17_science**|float|ACT 2017|Average scaled scores for the 2017 ACT Science section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act17_composite**|float|ACT 2017|Average scaled composite scores for the 2017 ACT (with one decimal place, in a range of 1 - 36 (inclusive)). In ACT, the *individual* composite scores are calculated by averaging the four sections' scores.|
|**sat18_participation**|float|SAT 2018|The percentage of students from the graduating class of 2018 who took the 2018 SAT (units percent, where 0.02 represents 2%).|
|**sat18_ebrw**|int|SAT 2018|Average scaled scores for the 2018 SAT Evidence-Based Reading and Writing (EBRW) section (without decimal places, in a range of 200 - 800 (inclusive)).|
|**sat18_math**|int|SAT 2018|Average scaled scores for the 2018 SAT Math section (without decimal places, in a range of 200 - 800 (inclusive)).|
|**sat18_total**|int|SAT 2018|Average scaled total scores for the 2018 SAT (without decimal places, in a range of 400 - 1600 (inclusive)). In SAT, the *individual* total scores are calculated by adding the two sections' scores.|
|**act18_participation**|float|ACT 2018|The percentage of students from the graduating class of 2018 who took the 2018 ACT (units percent, where 0.02 represents 2%).|
|**act18_english**|float|ACT 2018|Average scaled scores for the 2018 ACT English section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act18_math**|float|ACT 2018|Average scaled scores for the 2018 ACT Math section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act18_reading**|float|ACT 2018|Average scaled scores for the 2018 ACT Reading section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act18_science**|float|ACT 2018|Average scaled scores for the 2018 ACT Science section (with one decimal place, in a range of 1 - 36 (inclusive)).|
|**act18_composite**|float|ACT 2018|Average scaled composite scores for the 2018 ACT (with one decimal place, in a range of 1 - 36 (inclusive)). In ACT, the *individual* composite scores are calculated by averaging the four sections' scores.|


## Conclusions and Recommendations

From all the analysis of the given data, we have seen that the SAT participation rates in US states, on average, are generally lower as compared to ACT participation rates. From [these histogram plots](./plot_images/histogram_1.png), we see that while the participation rates of US states for both SAT & ACT are spread out across the 0-100% range, a significant number of states have very high (~95-100%) participation rates for ACT, and a significant number of states have very low (~0-10%) participation rates for SAT, for both 2017 and 2018.

We see similar trends from [these box plots](./plot_images/box_plot_1.png) - ACT participation rates are generally higher than those of SAT in both 2017 and 2018. The median ACT participation rates are 69% (in 2017) and 66% (in 2018), while the median SAT participation rates are only 38% (in 2017) and 52% (in 2018). However, this also shows that there is an increase in the median SAT participation rates from 2017 (38%) to 2018 (52%).

We also see from [these scatter plots](./plot_images/scatter_plot_4.png) that there is a negative correlation between average SAT and ACT participation rates for 2017 & 2018. In general, if states have a higher participation rate for SAT, they have a lower participation rate for ACT, and vice-versa. As seen in [this heatmap](./plot_images/heatmap.png) also, SAT and ACT participation rates have a strong negative correlation for both 2017 (-0.84) and 2018 (-0.87). This implies that students in each state on average take either the SAT or the ACT, and not both the tests. So, **in order to increase the SAT participation rates, College Board will have to explore strategies to take over the ACT market share and make the SAT more appealing than the ACT to students, schools and colleges**.

Furthermore, [these scatter plots](./plot_images/scatter_plot_5.png) show that there is a strong correlation between SAT and ACT participation rates for both 2017 & 2018. In general, the participation rates of states do not vary much year-to-year (2017 to 2018). States with low (or high) participation rates in 2017 also have low (or high) participation in 2018. This is also seen in the [heatmap](./plot_images/heatmap.png) - 2017 and 2018 participation rates have a strong positive correlation for both SAT (+0.87) and ACT (+0.92), which implies that the year-to-year participation rates are generally consistent across states.

However, there are a few notable exceptions to this trend. There are a few states which had very low SAT participation rates in 2017, but they increased significantly in 2018. Colorado and Illinois are clear examples of this trend. On further research, we see that this is mainly because of the fact that College Board has '[expanded its market share through contracts with states and school systems that enable students to take the SAT free](https://www.washingtonpost.com/local/education/a-shake-up-in-elite-admissions-u-chicago-drops-satact-testing-requirement/2018/06/13/442a5e14-6efd-11e8-bd50-b80389a4e569_story.html)'.

Hence, based on the above seen trends, I put forth the following **recommendations for College Board**:

- **Explore possibilities of expansion through contracts with more states, schools and colleges.** As seen above, state-wide testing contracts with states like [Illinois](https://www.chicagotribune.com/news/ct-illinois-chooses-sat-met-20160211-story.html) and [Colorado](https://www.denverpost.com/2017/03/06/colorado-juniors-sat-college-exam/), have definitely swung the participation rates in favour of the SAT by a very significant margin.
- **Explore potential avenues to make the SAT more accessible and affordable for students.**
    - Accessibility implies making more centres and test dates available across the US.
    - Affordability implies making more financial aid available for the students, esp. from lower income groups.
    - One way this could be achieved is through state-wide testing contracts, as seen [here](https://blog.prepscholar.com/which-states-require-the-sat).
    - The implications of these methods could be analysed if the following additional data were made available:
        - **Data on offering greater flexibility in test dates (eg. possibility of taking the test on weekday in school), and proportions of students that avail this increase in availability of test slots.**
        - **Data on proportions of students that utilize/avail financial aid to take the SAT/ACT in each state.**
- **Explore ways to get ahead of the '[test-optional](https://www.washingtonpost.com/local/education/a-shake-up-in-elite-admissions-u-chicago-drops-satact-testing-requirement/2018/06/13/442a5e14-6efd-11e8-bd50-b80389a4e569_story.html)' trend being adopted by colleges and universities.** As more and more colleges drop the requirement for students to submit SAT/ACT scores during the admissions process, SAT may require a complete and creative overhaul of the testing system so as to cater to the new admissions landscape while retaining market share.