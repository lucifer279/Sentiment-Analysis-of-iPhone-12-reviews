
# Data Visualization of Sentiment Analysis

from matplotlib import pyplot as plt
import Sentiment_Analysis as sa
import numpy as np


#............................................................................................

# Importing Score data from Sentiment Analysis file

Sentiment_Score = sa.Score

Pos = sa.Pos
Neg = sa.Neg
Neu = sa.Neu


#.............................................................................................


# Plotting Data of Sentiment Analysis


def Sentiment_Analysis():

    xpoint = np.array(["Positive","Negative","Neutral"])
    ypoint = np.array([Pos,Neg,Neu])

    plt.bar(xpoint,ypoint,width=0.50)
    plt.xlabel("Sentiment")
    plt.ylabel("Score 0 to 1")
    plt.title("Sentiment Analysis of Apple iPhone 12 Reviews")
    print(plt.show())


#...............................................................................................


#Importing Data of Ratings

Rating_Data = open(r'E:\Python\Python Project Files\Apple iPhone 12 ratings.csv').read()

#Cleaning '.0 out of 4 stars' and '\n'

RD1 = Rating_Data.replace('.0 out of 5 stars','')
RD2 = RD1.replace('\n','')

#Converting data to list

RD_list = list(RD2)

Rating_Cleaned =[]

for i in RD_list:
    Rating_Cleaned.append(i)


# Storing each rating 1-5 seperately

R1 =[]
R2 =[]
R3 =[]
R4 =[]
R5 =[]


for i in Rating_Cleaned:
    if (i == '1'):
        R1.append(i)

for i in Rating_Cleaned:
    if (i == '2'):
        R2.append(i)

for i in Rating_Cleaned:
    if (i == '3'):
        R3.append(i)

for i in Rating_Cleaned:
    if (i == '4'):
        R4.append(i)

for i in Rating_Cleaned:
    if (i == '5'):
        R5.append(i)


# print(len(R1))
# print(len(R2))
# print(len(R3))
# print(len(R4))
# print(len(R5))

#.............................................................................................

Rating_1 = 11
Rating_2 = 1
Rating_3 = 5
Rating_4 = 22
Rating_5 = 101

#.............................................................................................

# Plotting Data of Ratings


def Rating_Analysis():

    xpoint = np.array([1,2,3,4,5])
    ypoint = np.array([Rating_1,Rating_2,Rating_3,Rating_4,Rating_5])

    plt.bar(xpoint,ypoint,width=0.50)
    plt.xlabel("Rating Scale 1-5")
    plt.ylabel("Number of Ratings")
    plt.title("Product Rating Analysis of Apple iPhone 12")
    plt.show()


#................................................................................................

Sentiment_Analysis()
Rating_Analysis()