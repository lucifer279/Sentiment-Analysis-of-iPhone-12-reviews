
#Project Summary

# Product - Apple iphone 12 (128) Gb
# Price - Rs 84,799

Data_Analysis = '''What is Data Analysis ?\n
Data Analysis is a process used by researchers for reducing data to a story and interpreting it to derive
insights. The data analysis process helps in reducing a large chunk of data into smaller fragments,which
makes sense.Three essential thingstake place during the data analysis process — the first data organization.
Summarizationand categorization together contribute to becoming the second known method used for data reduction. 
It helps in finding patterns and themes in the data for easy identification and linking.\n '''


def Summary():

    S = ":"*100

    Overview = ('''    Overview\n ----------------------------------------------------------------
   
    Sentiment Analysis of Apple iPhone 12 (128)Gb.\n 
    Collecting data of reviews and ratings from Amazon.com and analyzing the data to 
    understand the sentiments of customers towards this product with data representation.\n\n ''')


    Research_Methodology = ('''  Research Methodology\n-----------------------------------------------------------------
    \nData Type in Research\n
    Qualitative data: When the data presented has words and descriptions, then 
    we call it qualitative data.Quality data represents everything describing 
    taste, experience,texture, or an opinion that is considered quality data.\n 
    Customer reviwes and rating sample size is 140.\n
    Data is collected from Amazon.com by using Webscraping tools and analyzed 
    using Natural Language Tool Kit python library.\n\n ''')

    Findings = ('''  Findings of the study\n------------------------------------------------------------
                   
    Sentiment Analysis of reviews is classified into 3 parts.\n
    Score from O to 1\n
    Positive = 0.238 
    Negative = 0.046
    Neutral  = 0.716\n
                   
    The above score shows that the majority of the customers has neutral sentiment towards 
    Apple iPhone 12. This shows that product is good and satisfactory as negative score is 
    very less.\n
                    
    Product Rating Analysis\n
    Rating from 1 to 5 stars\n
    Rating 1 = 11 
    Rating 2 = 1
    Rating 3 = 5
    Rating 4 = 22
    Rating 5 = 101\n                       
                           
    The above data shows that maximum customers rated this product as 5 stars.This 
    shows the product rating is excellent.\n
                   
    Comparison between Reviews and Ratings.\n
    If we compare the data of reviews and ratings,we can see that the sentiments on 
    reviews is Neutral and the product rating is excellent (101 customers has given
    5 stars for this product)\n.
                   
    We can assume that customer has rated 5 stars but have expressed neutral sentiments 
    for the product.Customers have rated the product on brand image of iPhone and expressed
    reviews basis on their personal usage of the product.\n\n ''')
                   
                   
    Conclusion = (''' Conclusion\n--------------------------------------------------------------------------------------
                      
    After analyzing the entire data, Apple iphone 12 (128)Gb is overall a good product to buy. ''')


    print(f"{Overview}{S}\n\n\n {Research_Methodology}{S}\n\n\n {Findings}{S}\n\n\n {Conclusion}\n")


#.......................................................................................................................


print(Data_Analysis)
print(" ")
print("*"*120)
print(" ")
Summary()