import streamlit as st
import pandas as pd
from recommender import load_data, build_content_based_model, recommend_movies_content_based
from tmdb_api import fetch_movie_details, fetch_poster_path
movies, ratings = load_data()
similarity_matrix = build_content_based_model(movies)
st.title("🎬 Movie Recommendation System")
movie_titles = movies['title'].tolist()
selected_movie = st.selectbox("Select a movie:", movie_titles)
if st.button("Recommend"):
    recommended_movies = recommend_movies_content_based(selected_movie, movies, similarity_matrix)
    for _, movie in recommended_movies.iterrows():
        movie_details = fetch_movie_details(movie['movieId'])
        poster_url = fetch_poster_path(movie_details.get('poster_path'))
        st.image(poster_url, width=200)
        st.subheader(movie['title'])
        st.text(f"Genres: {movie['genres']}")
        st.text(f"Overview: {movie_details.get('overview', 'No overview available.')}")
