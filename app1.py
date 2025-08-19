import streamlit as st
import pickle
import pandas as pd
import requests

# ========================
# CONFIG
# ========================
API_KEY = "2da8257788f09bc44871a71e4a3b480d"
BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"
IMG_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Load your movies dataset
movies_dict = pickle.load(open("movie_list.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity_matrix.pkl", "rb"))

# ========================
# CUSTOM CSS
# ========================
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #0f2027;
        background-image: linear-gradient(315deg, #2c5364 0%, #203a43 50%, #0f2027 100%);
        color: white;
    }

    /* Title */
    h1 {
        color: #ffcc00;
        text-align: center;
        font-size: 2.5em;
    }

    /* Subheader (Movie names) */
    h3 {
        color: #00e6e6;
        margin-bottom: 5px;
    }

    /* Recommendation Card */
    .movie-card {
        padding: 15px;
        margin: 15px 0;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.08);
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
    }

    /* Overview text */
    .overview {
        font-size: 15px;
        line-height: 1.6;
        color: #f0f0f0;
    }

    /* Rating text */
    .rating {
        color: #ffcc00;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ========================
# FETCH MOVIE DETAILS
# ========================
def fetch_details(movie_id, fallback_info=None):
    url = BASE_URL.format(movie_id, API_KEY)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        overview = data.get("overview", fallback_info.get("overview") if fallback_info else None)
        rating = data.get("vote_average", fallback_info.get("rating") if fallback_info else None)

        poster_path = data.get("poster_path")
        poster_url = IMG_BASE_URL + poster_path if poster_path else None

        return poster_url, overview, rating

    except Exception:
        if fallback_info:
            return None, fallback_info.get("overview"), fallback_info.get("rating")
        return None, None, None

# ========================
# RECOMMENDATION FUNCTION
# ========================
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        fallback_info = {
            "overview": movies.iloc[i[0]].get("overview"),
            "rating": movies.iloc[i[0]].get("vote_average")
        }
        poster, overview, rating = fetch_details(movie_id, fallback_info)
        recommendations.append((movies.iloc[i[0]].title, poster, overview, rating))
    return recommendations

# ========================
# STREAMLIT UI
# ========================
st.title("🎥 Movie Recommender System")
st.write("Select a movie and get recommendations with posters (if available), ratings, and overviews.")

selected_movie = st.selectbox("🎬 Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for name, poster, overview, rating in recommendations:
        st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

        st.subheader(name)
        if poster:
            st.image(poster, width=200)
        st.markdown(f"<p class='rating'>⭐ Rating: {rating if rating else 'N/A'}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='overview'>📖 {overview if overview else 'No overview available'}</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

=======
import streamlit as st
import pickle
import pandas as pd
import requests

# ========================
# CONFIG
# ========================
API_KEY = "2da8257788f09bc44871a71e4a3b480d"
BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"
IMG_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Load your movies dataset
movies_dict = pickle.load(open("movie_list.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity_matrix.pkl", "rb"))

# ========================
# CUSTOM CSS
# ========================
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #0f2027;
        background-image: linear-gradient(315deg, #2c5364 0%, #203a43 50%, #0f2027 100%);
        color: white;
    }

    /* Title */
    h1 {
        color: #ffcc00;
        text-align: center;
        font-size: 2.5em;
    }

    /* Subheader (Movie names) */
    h3 {
        color: #00e6e6;
        margin-bottom: 5px;
    }

    /* Recommendation Card */
    .movie-card {
        padding: 15px;
        margin: 15px 0;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.08);
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
    }

    /* Overview text */
    .overview {
        font-size: 15px;
        line-height: 1.6;
        color: #f0f0f0;
    }

    /* Rating text */
    .rating {
        color: #ffcc00;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ========================
# FETCH MOVIE DETAILS
# ========================
def fetch_details(movie_id, fallback_info=None):
    url = BASE_URL.format(movie_id, API_KEY)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        overview = data.get("overview", fallback_info.get("overview") if fallback_info else None)
        rating = data.get("vote_average", fallback_info.get("rating") if fallback_info else None)

        poster_path = data.get("poster_path")
        poster_url = IMG_BASE_URL + poster_path if poster_path else None

        return poster_url, overview, rating

    except Exception:
        if fallback_info:
            return None, fallback_info.get("overview"), fallback_info.get("rating")
        return None, None, None

# ========================
# RECOMMENDATION FUNCTION
# ========================
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        fallback_info = {
            "overview": movies.iloc[i[0]].get("overview"),
            "rating": movies.iloc[i[0]].get("vote_average")
        }
        poster, overview, rating = fetch_details(movie_id, fallback_info)
        recommendations.append((movies.iloc[i[0]].title, poster, overview, rating))
    return recommendations

# ========================
# STREAMLIT UI
# ========================
st.title("🎥 Movie Recommender System")
st.write("Select a movie and get recommendations with posters (if available), ratings, and overviews.")

selected_movie = st.selectbox("🎬 Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for name, poster, overview, rating in recommendations:
        st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

        st.subheader(name)
        if poster:
            st.image(poster, width=200)
        st.markdown(f"<p class='rating'>⭐ Rating: {rating if rating else 'N/A'}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='overview'>📖 {overview if overview else 'No overview available'}</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
>>>>>>> e5d8730 (Initial commit with movie_list and similarity_matrix using LFS)
