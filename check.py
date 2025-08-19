# import requests

# API_KEY = "2da8257788f09bc44871a71e4a3b480d"
# movie_id = 19995  # Avatar
# url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

# response = requests.get(url)
# print(response.status_code)
# print(response.json())
import streamlit as st

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF1C1C;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎥 Movie Recommender System")
st.write("Pick a movie and click the ▶️ **Recommend** button below!")

if st.button("▶️ Recommend"):
    st.success("Here are your recommendations 🎬🍿")
