# Sentiment Analysis
A movie review classification model is made using a bunch of positive and negative reviews. 
Train data is not included yet. Will add it soon. 
Model is trained using multiple classifiers viz., 
  1. Naive Bayes 
  2. Multinomial Naive Bayes
  3. Stochastic Gradient Descent 
  4. Bernoulli Naive Bayes 
  5. SVC 
  6. LinearSVC 
  7. NuSVC classifier

A separate voting class is made that takes the output of all classifiers and picks the most common output(mode).
This output is pushed into a text file as twitter-out.txt
While this is going on, our visualization code reads the twitter-out.txt file and creats sentiment plot live.
