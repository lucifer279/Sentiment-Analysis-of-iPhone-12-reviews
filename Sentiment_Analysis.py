
#Using Natural Language Tool Kit (nltk) for sentiment analysis

import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string


# nltk.download()   # Download everything to use nltk

#.....................................................................................................

# Reading Text file of Reviews

text = open(r'E:\Python\Python Project Files\Apple iPhone 12 reviews.csv',encoding="utf-8").read()

#......................................................................................................

# Convert text file to lower case

text_str = str(text)    #Convert text format to string

lower_case = text_str.lower()

#.......................................................................................................

# Removing Punctuation

'''
The translate() method returns a string where some specified characters are replaced with the character
described in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

print(string.punctuation) #To check all punctuations
'''

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))


#........................................................................................................

'''
Step 1 = Tokenization  # Spliting sentence into different words
Step 2 = Removing Stop Words (I,is,and,was etc)
Step 3 = Classification of Sentiments (Pos,Neg,Neu)
'''


#Step 1 Tokenization

#use word.tokenize

tokenized_words = nltk.word_tokenize(cleaned_text,"English")


#Step 2 Removing Stop words like the was is and etc

#Using from nltk.corpus import stopwords


final_words =[]

for word in tokenized_words:
    if word not in stopwords.words('english'):   #Use words parameter
        final_words.append(word)

final_words_str = str(final_words)  #Convert to string or else Attribute error : List object has no attribute encode


#..................................................................................................


#Step 3 Classification of sentiments

#Using Sentiment Intensity Analyzer

'''
Note - If we use final_words_str file, output will be
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

Use cleaned_text file for accurate output
'''

Score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)

Pos = Score['pos']
Neg = Score['neg']
Neu = Score['neu']


if (Neg > Pos) and (Neg > Neu):
    print(f"Negative Sentiment as Negative Value:{Neg} is greater than Positive: {Pos} and Neutral: {Neu}")
elif (Pos > Neg) and (Pos > Neu):
    print(f"Positive Sentiment as Positive Value:{Pos} is greater than Negative: {Neg} and Neutral: {Neu}")
else:
    print(f"Neutral Sentiment as Neutral Value:{Neu} is greater than Positive: {Pos} and Negative: {Neg}")





