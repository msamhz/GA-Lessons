# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 5 (Capstone): Age Classification using Facial Images


## Problem Statement

**Given an image of someone's face, is it possible for a computer to guess their age? If yes, how accurately can their age be guessed?**


## Executive Summary

Computer vision is a rapidly growing field with many interesting applications. A huge area of study within this field is about the facial features of humans, and how they relate to an individual's characteristics, such as age, gender, race, etc. The field also has shown a huge potential in terms of increasing security through applications in facial recognition.

In this project, I explore one such application of computer vision - to guess someone's age based on an image of their face. Such an application can have a variety of use-cases. For instance, it could be deployed in certain types of physical stores or places such as amusements parks, and the video-feed from such places can be used to study the age-profile of customers or people who frequent such places. The insights gained from this deployment could aid the business in making better and more effective decisions, such as targeted marketing campaigns, provision of better facilities catered to their patrons, etc.

Computer vision applications nowadays rely more and more on deep learning techniques and neural networks, because of an increase in availability and ease of access to computers with much higher processing capabilities. However, to appreciate the **traditional machine learning** way of doing things in data science and to truly appreciate the power and possibilities of **deep learning**, in this project, I seek to explore the traditional machine learning approach to this problem as well (image feature extraction followed by classification modelling using the ***scikit-learn*** library). To explore the deep learning approach in this project, I utilize the ***TensorFlow*** library.

The project is done entirely on **Google Colab** (instead of Jupyter Notebooks on a personal computer). The primary reason for this is to utilize the free GPUs offered by Google to train the deep learning neural networks. That being said, it may also be possible to complete this project using a traditional CPU, although the process may take slightly longer.

I utilize the following methods and libraries to train age classification models for facial images:
- ***OpenCV*** and ***scikit-image*** for Image Processing and Feature Extraction
- *scikit-learn RandomForestClassifier* & Support Vector Classifier *(SVC)* for traditional Machine Learning approach
- **Convolutional Neural Networks (CNNs)** using *TensorFlow* for Deep Learning approach

The description and walkthrough for the entire project is available as an **[article on Towards Data Science](https://towardsdatascience.com/age-detection-using-facial-images-traditional-machine-learning-vs-deep-learning-2437b2feeab2)**. The **[source code](https://drive.google.com/drive/folders/1Z-yE8YDbf_C8nWmcqpkeSf06a23PvrqJ?usp=sharing) Google Colab notebooks** and the **[datasets](https://drive.google.com/drive/folders/1dZhJNGmdoO1La6MOJRfUYxDZwIa-hXNX?usp=sharing)** for this project are accessible **on Google Drive**.


## Conclusions and Recommendations

Beginning with the problem statement of guessing a person's age from an image of their face, this project showed that it is indeed possible for a computer to do that. Using the **traditional machine learning** approach in this scenario, though possible, **does not yield models with very high performance and success rate (accuracy)**. Furthermore, this approach **requires a significant amount of domain knowledge and data processing expertise for substantial features to be extracted from the images** for use in the classification models. This approach is also very **time intensive**, and may become more and more unproductive as the size of the images dataset increases.

The **deep learning and neural networks approach**, on the other hand, **does not require any significant domain knowledge and data processing expertise**, as it does not require any image features to be extracted manually. This approach also **yields much better performing models with higher accuracy scores** as compared to the traditional machine learning approach. Thus, this comparison between the two approaches in this project highlights the true power and possibilities of deep learning with neural networks, and provides a good understanding behind their increasing popularity in the recent years.