import streamlit as st
import pickle
import pandas as pd
import requests

# Load the movie data and similarity scores
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity_matrix.pkl', 'rb'))

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return None

# Recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Page config with emoji
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# Custom CSS → change lower background to yellow
st.markdown(
    """
    <style>
        /* Keep default Streamlit header */
        .stApp {
            background-color: #ffffff;
        }

        /* Change only content area to soft yellow */
        .block-container {
            background-color: #fff8dc; /* light yellow */
            border-radius: 12px;
            padding: 20px;
        }

        /* Center align text under posters */
        .movie-title {
            text-align: center;
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with icon
st.markdown(
    '<h1 style="display:flex; align-items:center;"><span style="margin-right:10px;">🎬</span> Movie Recommender System</h1>',
    unsafe_allow_html=True
)

st.write("Discover movies with posters, ratings, and overviews.")

# Dropdown for movies
selected_movie = st.selectbox("🎥 Select a movie:", movies['title'].values)

if st.button("✨ Recommend"):
    names, posters = recommend(selected_movie)

    # Display recommended movies in 5 columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            if posters[idx]:
                st.image(posters[idx], use_container_width=True)
            st.markdown(f"<p class='movie-title'>{names[idx]}</p>", unsafe_allow_html=True)
