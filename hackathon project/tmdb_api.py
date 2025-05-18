import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "YOUR_TMDB_API_KEY")

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url).json()
    return response

def fetch_poster_path(poster_path):
    base_url = "https://image.tmdb.org/t/p/w500"
    return f"{base_url}{poster_path}" if poster_path else None
