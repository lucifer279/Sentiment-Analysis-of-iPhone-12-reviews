
#Webscrapping data of new Apple iPhone 12 (128) Gb reviews from Amazon.com

import requests
from bs4 import BeautifulSoup
import pandas as pd


#Creating empty list

UserName =[]
Rating =[]
ReviewTitle =[]
Review =[]


pages = list(range(1,21))  #Total number of pages for reviews is 21

for page in pages:
    #URL of the website
    #Use format to scrape multiple pages and add range of pages
    req = requests.get("https://www.amazon.in/New-Apple-iPhone-12-128GB/product-reviews/B08L5TNJHG/ref=cm_cr_getr_d_paging_btm_next_21?ie=UTF8&reviewerType=all_reviews&pageNumber={}".format(page)).text
    #Using BeautifulSoup
    soup = BeautifulSoup(req,'html.parser')

    username = soup.find_all('span',class_ = 'a-profile-name')
    for i in range (len(username)):
        UserName.append(username[i].text)
    len(username)

    rating = soup.find_all('i',{"data-hook":"review-star-rating"})
    for i in range(len(rating)):
        Rating.append(rating[i].text)
    len(Rating)

    reviewtitle = soup.find_all('a', class_ = "review-title-content")
    for i in range(len(reviewtitle)):
        ReviewTitle.append(reviewtitle[i].text)
    len(ReviewTitle)

    review = soup.find_all("span",{"data-hook":"review-body"})
    for i in range(len(review)):
        Review.append(review[i].text)
    len(Review)



# Pop first 2 username as it is repeating

UserName.pop(0)
UserName.pop(0)

#Striping /n from ReviewTitle

ReviewTitle[:] = [r.rstrip('\n') for r in ReviewTitle ]  #Using List Comphrehension r for rightstrip
ReviewTitle[:] = [l.lstrip('\n') for l in ReviewTitle ]  #Using List Comphrehension l for lefttstrip

#Striping /n and unwanted message from Review

Review[:] = [r.rstrip('\n') for r in Review]
Review[:] = [l.lstrip('\n') for l in Review]
Review[:] = [s.lstrip('Your browser does not support HTML5 video.\n\n\n  \xa0') for s in Review]


#Using Pandas to save data in csv format

Data = {"User Name": UserName[0:120],"Rating":Rating[0:120], "Review Title":ReviewTitle[0:120],"Review":Review[0:120]}


# Creating Index

range1 = range(1,121)

index =[]
for i in range1:
    index.append(i)

Final_Data = pd.DataFrame(Data,index)

# print(Final_Data.head())

# Final_Data.to_csv(r'E:\Python\Python Project Files\Apple iPhone 12 reviews New Apple iPhone 12 (128) GB Reviews.csv')

Review_Data = pd.DataFrame(Review)

# Review_Data.to_csv(r'E:\Python\Python Project Files\Apple iPhone 12 reviews.csv')

Rating1 = pd.DataFrame(Rating)

# Rating1.to_csv(r'E:\Python\Python Project Files\Apple iPhone 12 ratings.csv')


