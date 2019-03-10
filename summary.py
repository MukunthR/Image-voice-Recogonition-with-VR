import numpy as np
import pandas as pd
import nltk
# nltk.download('punkt') # one time execution
# nltk.download('stopwords')
import re
import networkx as nx
#pip install networkx
#pip install sklearn


text = """American football, referred to as football in the United States and Canada and also known as gridiron,[nb 1] is a team sport played by two teams of eleven players on a rectangular field with goalposts at each end. The offense, which is the team controlling the oval-shaped football, attempts to advance down the field by running with or passing the ball, while the defense, which is the team without control of the ball, aims to stop the offense's advance and aims to take control of the ball for themselves. The offense must advance at least ten yards in four downs, or plays, and otherwise they turn over the football to the defense; if the offense succeeds in advancing ten yards or more, they are given a new set of four downs. Points are primarily scored by advancing the ball into the opposing team's end zone for a touchdown or kicking the ball through the opponent's goalposts for a field goal. The team with the most points at the end of a game wins.

American football evolved in the United States, originating from the sports of association football (known in the U.S. as soccer) and rugby football. The first match of American football was played on November 6, 1869, between two college teams, Rutgers and Princeton, under rules based on the association football rules of the time.[4] During the latter half of the 1870s, colleges playing association football switched to the Rugby Union code, which allowed carrying the ball. A set of rule changes drawn up from 1880 onward by Walter Camp, the "Father of American Football", established the snap, the line of scrimmage, eleven-player teams, and the concept of downs; later rule changes legalized the forward pass, created the neutral zone, and specified the size and shape of the football. The sport is closely related to Canadian football, which evolved parallel and contemporary to the American game, and most of the features that distinguish American football from rugby and soccer are also present in Canadian football.

American football as a whole is the most popular sport in the United States. The most popular forms of the game are professional and college football, with the other major levels being high school and youth football. As of 2012, nearly 1.1 million high school athletes and 70,000 college athletes play the sport in the United States annually, almost all of them men, with a few exceptions. The National Football League, the most popular American football league, has the highest average attendance of any professional sports league in the world; its championship game, the Super Bowl, ranks among the most-watched club sporting events in the world, and the league has an annual revenue of around US$10 billion."""


text = text.split(".")

sentences = text.copy()

word_embeddings = {}
f = open('C:\\Users\\murak\\Downloads\\glove\\glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()


# remove punctuations, numbers and special characters
clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

# make alphabets lowercase
clean_sentences = [s.lower() for s in clean_sentences]

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# function to remove stopwords
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new


# remove stopwords from the sentences
clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]


sentence_vectors = []
for i in clean_sentences:
    if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
    else:
        v = np.zeros((100,))
    sentence_vectors.append(v)


# similarity matrix
sim_mat = np.zeros([len(sentences), len(sentences)])


from sklearn.metrics.pairwise import cosine_similarity
for i in range(len(sentences)):
    for j in range(len(sentences)):
        if i != j:
            sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]


nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

# Extract top 5 sentences as the summary
for i in range(5):
    print(ranked_sentences[i][1])

