
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

# Importing the dataset
data=pd.read_csv("entireBookList8700.csv",header=0)

#### Data pre-processing

# Changing the name of the category ya to Young adult - handling the duplication of the categories 
data['Category'].replace('ya', 'young-adult',inplace=True)
data['Category'].replace('teen', 'children',inplace=True)
data['Category'].replace('non-fiction','nonfiction',inplace=True)
# print(data['Category'].unique())


# Changing the Column name
df = data.rename(columns={'OtherLinks': 'Other Categories'})
# print(df['Other Categories'][0])


# Using the re function to edit the other category column based on our pattern
token = []
for  text in df['Other Categories']:
    # segments the lowercased string into tokens - Based on the requirements
    pattern = r'[A-Z]\w+'
    tokens = nltk.regexp_tokenize(str(text), pattern)
    token.append(tokens)
# print(len(token))


# Overwriting the Other Categories with the modified tokens as per the requirements
df['Other Categories'] = token
# print(df['Other Categories'][0])


# Joining the words in 'Other Categories' from a list to line
df['Other Categories'] = df['Other Categories'].apply(lambda x: ' '.join(x))
# print(df['Other Categories'][0])


# Converting the entire dataframe to lower case
data = df.apply(lambda x: x.astype(str).str.lower())
# print(data['Other Categories'])
#finding the count of the categories
# print(data['Category'].value_counts())
# print(len(data))

# Removing the null values
data.dropna(axis='columns')
# print(data.head())
# print(len(data))

# dealing with the duplicate records
data = data.drop_duplicates(subset = 'Book Name')
data.head()
# print(len(data))

data['Training Text'] = data['Description'].astype(str)  + ' ' + data['Other Categories'] + ' ' + data['Author Name'] + ' ' +  data['Book Name']



data['Training Text'] = data['Description'].astype(str) + ' ' + data['Other Categories'] + ' ' + data['Book Name'] + ' ' + data['Author Name'] 
data = data.drop_duplicates(subset = 'Book Name')

# Description of the first 5 Books
data['Description'].head()


#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
data['Description'] = data['Description'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(data['Training Text'])

#Output the shape of tfidf_matrix
tfidf_matrix.shape

#### The matrix output shows the 8700 books and the 36233 words used to describe those books ####

# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# print(cosine_sim)

#Construct a reverse map of indices and Book titles
indices = pd.Series(data.index, index=data['Book Name']).drop_duplicates()
# print(indices)


title = "harry potter and the deathly hallows"
print("Please enter the name of the Book in Lower Case:", title)
# Get the index of the book that matches the title
idx = indices[title]
# print(idx)

# Get the pairwsie similarity scores of all books with that book
sim_scores = list(enumerate(cosine_sim[idx]))
# print(sim_scores)


# Sort the books based on the similarity scores
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# print(sim_scores[0:10])

# Get the scores of the 10 most similar books
sim_scores = sim_scores[1:16]
# print(sim_scores)

#Get the bookindices
book_indices = [i[0] for i in sim_scores]

# Return the top 10 most similar books
print(data['Book Name'].iloc[book_indices])

