import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data():
    movies = pd.read_csv("C:\\Users\\Pranil\\Desktop\\hackathon project\\ml-latest-small\\movies.csv")
    ratings = pd.read_csv("C:\\Users\\Pranil\\Desktop\\hackathon project\\ml-latest-small\\ratings.csv")
    return movies, ratings

def build_content_based_model(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies_content_based(movie_title, movies, similarity_matrix, top_n=10):
    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:top_n+1]]
    return movies.iloc[movie_indices]

