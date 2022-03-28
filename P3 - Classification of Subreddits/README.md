# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Classification of Subreddits


## Problem Statement

People seek advice from each other all the time, especially on social media platforms like **Reddit** (where they can maintain their anonymity). Given a post from a user seeking advice on a subreddit, is it possible to **categorize the post into different categories (by employing different Machine Learning techniques)**? If yes, **how accurately can this advice request categorization be done?**


## Executive Summary

According to this [page](https://foundationinc.co/lab/reddit-statistics/), Reddit is a rapidly growing social media sharing platform with a 330 million active users count as of 2018, and a 30% increase in the active users count in 2019. People come to Reddit for all different types of reasons, ranging from just browsing the latest [meme content](https://www.reddit.com/r/funny/) or news to connecting with people of similar interests, sharing their experiences, etc. **One important reason for people to visit Reddit is to seek and give advice (on a broad range of topics), or just about their situations/experiences in life in general.**

Reddit is trying to introduce **a new feature to automatically suggest categories/subreddits to users for posting their requests for advice**, based on the text of the user's post seeking the advice. The feature is being introduced to better guide people seeking advice to the appropriate subreddits, so that their requests can be answered in a better and effective manner by the dedicated subreddit community. To introduce this feature, Reddit is trying to understand whether or not it is possible to automatically categorize the advice posts based on their text. And if it is indeed possible to categorize such posts, how effectively/accurately can this done?

To answer this question and give Reddit a brief sample of the possibilities of machine learning, in this project, I seek to apply different data classification techniques to classify textual posts from **two subreddits - [r/relationship_advice](https://www.reddit.com/r/relationship_advice/) (dedicated for people seeking advice on their personal relationships) and [r/legaladvice](https://www.reddit.com/r/legaladvice/) (dedicated for people seeking semi-professional/professional advice on legal issues)**.

For ease of organization and understanding, the project has been **divided into 2 separate Jupyter notebooks**. The first notebook focuses on data gathering via web-scraping from the Reddit API. In order to do the classification modelling, about a 1000 posts were scraped from each of the two subreddits (sorted by newest at the time of scraping). The second notebook then focuses on data cleaning, EDA and different techniques of classification modelling.

In order to classify the posts from the two subreddits, I employ different techniques of classification, such as:
- Logistic Regression
- K-Nearest Neighbors classifier
- Naive Bayes classifier
- Random Forests

Each of the models and their hyperparameters are optimized by passing them through **Cross-Validated Grid Searching (GridSearchCV)**. As I am dealing with textual data, I also employ different **NLP techniques** to convert text into machine-understandable forms of data, such as **Count Vectorization and TF-IDF Vectorization**. Each of the classification models built are assessed for generalizability using the **Accuracy metric**, with the final selected model being evaluated on further metrics such as **Sensitivity (True Positive Rate), Specificity (True Negative Rate) and ROC AUC**.


## Conclusions and Recommendations

Beginning with the problem statement of automatically categorizing the posts seeking advice on different subreddits, this project started with scraping a thousand posts each from two subreddits - *r/relationship_advice* and *r/legaladvice* - via the Reddit API. The posts were then verified, cleaned and pre-processed for EDA and classification modelling later on.

The next step of the process was EDA, which highlighted the significant differences in the levels of user activity between the two subreddits. Even though both the subreddits were created only months apart in 2009, *r/relationship_advice* has grown tremendously since then and currently has more than 3 million subscribers. In contrast, *r/legaladvice* currently only has about 1.2 million subscribers. The EDA process also showed that people in general comment more than twice as much on *r/relationship_advice* than on *r/legaladvice*. Furthermore, the posts on *r/relationship_advice* are generally much longer (avg. 368 words per post) than those on *r/legaladvice* (avg. 220 words per post). This EDA process gave an initial indication of the possibility that the classification model may be skewed towards *r/relationship_advice* because of the larger amount of word tokens being fed into the classification model from this subreddit. The EDA process, through wordclouds, also showed the similarities and differences in the words used in posts from both subreddits.

Following the EDA process, different classification models were built and evaluated using the *accuracy* metric. A final model *(MultinomialNB with TfidfVectorizer)* was then chosen, and built again on the entire training corpus for further evaluation using metrics such as *sensitivity (true positive rate), specificity (true negative rate) and ROC AUC*. The important features (word tokens) in both subreddits were also visualized, along with a brief analysis of the misclassified posts.

It was observed from the evaluation metrics that **the *MultinomialNB* model with *TfidfVectorizer* has a very high classification accuracy on the testing corpus**. It was also seen that the value of accuracy calculated while training the model on k-folds of cross validation *(estimated test set accuracy)* was quite similar to when the model was used to classify the posts from the test dataset *(actual test set accuracy)*, with only a slight increase or decrease. This implies that **this classification model would mostly generalize well on new unseen data**.

The *ROC AUC* value is also very close to 1, implying that **the feature populations (bag of tokens) from the positive class *(r/relationship_advice)* and negative class *(r/legaladvice)* are separated almost perfectly**. And so, this model is a very good classifier for these two subreddits.

Looking at the *Sensitivity* and *Specificity*, and the numbers of false positives and false negatives, it is also seen that **a lot more posts from *r/legaladvice* got misclassified as being from *r/relationship_advice*, than the other way around**. So, it can be said that the **classification model has a slight skewness towards the positive class *(r/relationship_advice)***. One of the reasons for this could be the fact that the **posts from *r/relationship_advice* were, on average, much longer than the posts from *r/legaladvice*** (as seen during the EDA process) - 368 words/post (avg.) in *r/relationship_advice* as compared to 220 words/post (avg.) in *r/legaladvice*. This means that in general, the documents from *r/relationship_advice* contributed more tokens to the model as compared to documents from *r/legaladvice*. And this may have resulted in the classification model being slightly skewed towards *r/relationship_advice*.

So, to answer the problem statement, **it is indeed possible to automatically categorize posts seeking advice into different categories/subreddits**. This feature, if implemented, should help to better guide users seeking advice to the appropriate subreddits, so that their requests can be answered in a better and effective manner by the dedicated subreddit community. **In the case of the two subreddits chosen here - *r/relationship_advice* and *r/legaladvice*, it can be said that the posts can be classified with a very high degree of accuracy, which would imply that the automatic suggestions of subreddits given to the users based on their posts would be very appropriate and helpful.**

**However, this may not always be the case, especially if some subreddits are closely related to each other in terms of the topics being discussed in them.** Further in-depth studies could be carried out with combinations of different subreddits dedicated to advice seeking to see how well they can be classified. This would help to improve the suggestions feature even further.