# Saving Kids From Toxicity

This project is a result of collaboration between students from the Georgia Tech to save kids from toxic comments by classifying toxic comments from Wikipedia and also explore the different ways to create toxic comments.

Not Toxic                              |  Toxic
:-------------------------------------:|:----------------------------------:
![](/dataset/complete_word_cloud.png)  |  ![](/dataset/toxic_word_cloud.png)

## Requirements
To run the code:
1. We recommend setting a python3 virtual environment
2. Skip this step if you have Python3 installed, otherwise install Python 3.6.5 from: ["https://python.org/downloads/"](link) 
3. Run commands from below

## Commands to run:
```
1. python3 -m pip install virtualenv
2. virtualenv toxic_comments
3. source toxic_comments/bin/activate
4. python3 -m pip install -r requirements.txt
```

## Dataset

We retrieved our dataset from a Kaggle competition : <a href="https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge">Toxic Comments</a>. Using the dataset, we found interesting trends within the content of toxic comments, so we also created word clouds of comments.

## Visualization

Before applying or creating any models to classify the toxic comments, we decided it was best to visualize the different comment categories and look at the most common word tokens within each category.

## Classifier
We first tried the most simple models that we know to test the dataset. Using a model based on Logistic Regression paired with TfidfVectorizer, we were able to create a multi-class model with average of 98%~.

Upon researching more about the different models that may improve overall accuracy for this dataset, we found Long Short-Term Memory Neural Network (LSTM) to be the one of the performing models for Natural Language Processing. So, we tried implementing a LSTM using Keras module for Python. Also, we tried a variation of LSTMs called Bi-directional LSTM. We achieved a CV accuracy around 98.3% with the Bi-directional LSTM model.

## Comment Generation

We thought it would interesting to create a model for generating toxic comments.It turns out that such a model would be rudimentary at best with a LSTM model because the model seems to gravitate toward a select few phrases to generate. One of the most common is : 'pig pig pig'. While the phrase is certainly toxic, we wanted more variety, so we build a markov chain text generator, which produced a more satisfying result.
