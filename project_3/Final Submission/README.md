# Project 3 - Classification of Subreddits

Journal 1: ImportingData_Reddit

Journal 2: Import_New_Test_data

Journal 3: EDA and Cleanup

Journal 4: Classification Modelling

--

## Contents:
- [Data Importing](#Data-Importing)
- [Classification metrics](#Classification-metrics)
- [Vectorizer Selection via GridSeachCV](#Vectorizer-Selection-via-GridSeachCV)
- [Hyper-parameter tuning](#Hyper-parameter-tuning)
- [Error Analysis](#Error-Analysis)
- [Redefine Data set and run models](#Redefine-Data-set-and-run-models)
- [Production Model Selection](#Production-Model-Selection)
- [Conclusion and Recommendation](#Conclusion-and-Recommendation)

--

## Problem Statement
To provide model and incorporate into business process of social centers to accurately identify people with PTSD so that quick remedy can be provided.   

--

## Background 
Having Anxiety can be common among people as compared to people having PTSD. PTSD is a type of Anxiety problem, but not all people with Anxiety has PTSD. 
Distinguishing between the two accurately will be key in helping provide early treatment<sup>1</sup>  

--

**Citations**
<br>
<sup>1</sup> https://adaa.org/understanding-anxiety/facts-statistics

--

## The Modeling Process

1. Pre- processing
-Tokenizing
-Removed HTML
-Removed stopwords
-Remove subreddit names
-Lemmatize and Stem

2. Classification metric: Accuracy, Sensitivity and ROC_AUC
-Mainly to minimize people from classifying as not having PTSD when they actually have PTSD, which might lead to permanent damage to the brain.<sup>2</sup> 

3. Vectorizer Selection- TfidVec, and CountVec

4. Hyparameter tuning of 
- Logistic Regression
- MultinomialNB
- RandomForest

5. Error analysis 

6. Redefine Data set

7. Production Model Selection based on Accuracy score, Sensitivity and ROC_AUC



**Citations**
<br>
<sup>2</sup> https://blackbearrehab.com/mental-health/ptsd/putting-your-family-at-risk-because-of-untreated-ptsd/#:~:text=Untreated%20PTSD%20can%20cause%20permanent,Anxiety%20disorder

--

## Significant findings

Through EDA, I have highlighted on the signficant difference in subrreddict activity levels, where there were orginally 93 users who post in both subreddits suggesting that we may consider removing their post as they might bring ambiguity and inaccruacy as to whether users actually has PTSD or not. Users in r/PTSD generally do post longer text, with longer word count, and are not as active as compared to users fromr/Anxiety.


--


In addition, we do observe there is cyclical trend, which suggest that there might be effects from SAD, that only affects people when there is lesser sunlight. Further works can be done to deep dive into other areas that may have attributed to this seasonal effects.  

![image](https://user-images.githubusercontent.com/98629542/161173397-956a4cf8-1dde-47e0-8d60-a08c526f592b.png)

--



Furthermore, through EDA on the common words, I did not find any distinguishing words that is able to differentiate subreddits if searched in the whole data set. But when split by subreddit groups, r/PTSD has `Therapy` singled out, unique for PTSD. It could imply users might need to go for therapy as often as compared to people with Anxiety.


From r/Anxiety, common words like `panic` and `attack` are common symtoms from people having Anxiety. It is peculiar that users in r/PTSD do not experience this as a common effect. For bigrams and trigrams, `panic attack` were found in both subreddits and `sexual assault` were identified in r/PTSD as probably one of the common causes of users with PTSD. I did observe that `years ago` as top common words in bigram illustrating a long term time effect, suggesting it might take longer to overcome it as compared to r/Anxiety. 


--


Related to the cyclical trend, found that there was firework identifed as one of the top features to skew towards r/PTSD. Found that most post on fireworks were on July, all coming from r/PTSD expressing agony and complaing about triggers about shooting and rockets. In fact, people with `past trauma` realated to sound are impacted significantly worse by `loud explosion` causing them to `reminisce the threat` and may their brain's threat detectos activated.<sup>3</sup>
Linking back to the EDA, found that we see spike on July 2021, there is seasonal fireworks on every 4th July across many states in US. <sup>=4</sup>

![image](https://user-images.githubusercontent.com/98629542/161173353-49ed4f2e-9ae0-4fed-8130-38e7a1fb3610.png)


--


Found users common in both subreddit groups. Removed them after EDA found that some were misclassified wrongly because they were likely to be in wrong post based on the words and context they have used. Also because of the ambiguity, its best to remove since there is no clear indication which group they belong to.

![image](https://user-images.githubusercontent.com/98629542/161172631-6c1426a6-e408-4eec-8cc8-6716141bc802.png)


After refining data, ROC_AUC and accuracy increased by 3.5% and 6% respectively.

Logistic regression has the highest ROC_AUC and Accuracy score. 

![image](https://user-images.githubusercontent.com/98629542/161172653-ccb20343-649f-4600-9ec8-6ffc81b0a4ab.png)

**Citations**
<br>
<sup>3</sup>https://www.insider.com/how-fireworks-affect-you-from-increased-anxiety-and-memory-problems-2020-7#:~:text=Repetitive%20fireworks%20launched%20at%20night,can%20weaken%20your%20immune%20system.
<br>
<sup>4</sup>https://wgntv.com/news/fireworks-retailer-warns-of-july-4-shortage-here-are-the-states-where-its-legal-to-stock-up/


Conclusion and recommendation

A final model - `Logistic Regression with tfidVectorizer` was picked for its incredible performance in ROC_AUC and overall Accuracy score. It's sensitivity score is relatively high too compared to MultinomialNB. Its accuracy is currently at 0.848 compared to its baseline score of 0.801, an overall increase of 5.8%.  The ROC_AUC however, increase larger by 9% from 0.88 to 0.95. Also, the value of accuracy can be seen when we trained the model on k-folds of crocss validation (estimated test set accuracy) was similar to the model test holdout data, by +- 5%. This implies that this classification model would `decently generalize well on new unseen data`

The ROC AUC value is at 0.96, an improvement from 0.88, implying that the `bag of tokens` from the positve class (r/PTSD) and the negative class (r/Anxiety) are separated almostly perfectly. 

Looking at the initial phase of modelling, referencing to MultinomialNB with the numbers of false postives and false negatives, it was seen to have alot of post from r/Anxiety got misclassified as positve. So it can be said that the classification model has a skewness towards the positive class (r/PTSD). One of the reason for this could be the fact that on average, much longer post in r/PTSD (as seen in the EDA process) - 1146 length of text as compared to 856 for r/Anxiety. This means in general, the documents from r/PTSD contributed more tokens to the model as compared to documents from r/Anxiety, thus slightly skewing towards r/PTSD. Another reason could be that r/PTSD shares similar symtoms to those suffering from Anxiety, hence if there is no strong predictive features existing in the document, it might be classified wrongly too. 

Answering the problem statement, indeed with the Logistic Regression model, the optimised ROC_AUC and sensitivity is able to reduce misclassification from, ie. for every 5057 people examined, a reduction of 994 people to 585 were misclassified. Specifically we focus on maximising sensitivity by reducing false negatives, from 623 to 352 people for every 5057 people are falsely classified negative (r/Anxiety) instead of being truely postive (r/PTSD). This feature, if implemented in the business process of social centers like entry forums for new patients having difficulty with Anxiety related disorder, will provide a **more automated guide to identify new patients who might sufferfrom PTSD so that we can quickly refer him/her to the neccessary treatment facility**. In this case, because there are **still a considerable number of overlaps**, it would be good to be used as a **trial first**, slowly beefing up **data feed into the model for better predicting accuracy and sensitivity**. This would however, **be a good platform as a quick guide for social workers to look out for pertinent signs that has been highlighted in the feature importance**. I believe if the model has been used more in the real world context, it should one day be more and more accurate. 

Keeping in mind having high peaks of the number of post in June and Dec, you may consider running a campaign to beef up support for people and use these high peaks as a matrix in the following years to track the effectiveness of the campaigns.

