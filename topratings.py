# Simple Recommenders - For top Recommendations
import pandas as pd 


data = pd.read_csv("entireBookList8700Final.csv",header=0)
# data = data[0:3000]
print(data['PeopleVoted'][0])


# Calculating "C"
C = data['Ratings'].astype(float).mean()
# print(C)

# Calulating minimum number of votes required  -- Calculating in 90th Percentile
m = data['PeopleVoted'].astype(float).quantile(0.90)
# print(m)

# Filtering all the qualified books into a new DataFrame
q_books = data.copy().loc[data['PeopleVoted'] >= m]
# print(q_books.shape)

# # Creating a function that computes the weighted rating (WR) of each Book
def weighted_rating(text, m=m, C=C):
    v = text['PeopleVoted']
    R = text['Ratings']
    # Calculation based on the Existing formula which is used by many websites
    return (v/(v+m) * R) + (m/(m+v) * C)


# # Creating a new feature called 'Metrics' and calculate its value with `weighted_rating()`
q_books['Metrics'] = q_books.apply(weighted_rating, axis=1)

# #Sort Books based on score calculated above
q_books = q_books.sort_values('Metrics', ascending=False)
# print(q_books)

# #Print the top 15 Books based on the Ratings from all the categories
print(q_books[['BookName', 'PeopleVoted', 'Ratings', 'Metrics']].head(15))

