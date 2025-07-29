import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("data/movies.csv")

st.title("🎬🎭 Movie Recommendation System")

# Initialize session state
if "region_selected" not in st.session_state:
    st.session_state.region_selected = False
if "genre_selected" not in st.session_state:
    st.session_state.genre_selected = False
if "selected_region" not in st.session_state:
    st.session_state.selected_region = ""
if "selected_genre" not in st.session_state:
    st.session_state.selected_genre = ""

# Step 1: Select Region
st.subheader("Select Region:")
region_list = ["Choose a region"] + sorted(df['region'].dropna().unique().tolist())
selected_region = st.selectbox("Region:", region_list)

if st.button("OK✅"):
    if selected_region != "Choose a region":
        st.session_state.selected_region = selected_region
        st.session_state.region_selected = True
        st.session_state.genre_selected = False  # Reset genre selection
    else:
        st.warning("Please choose a region before continuing.")

# Step 2: Select Genre
if st.session_state.region_selected:
    st.success(f"Region selected: {st.session_state.selected_region}")

    st.subheader("Select Genre:")
    filtered_df = df[df['region'] == st.session_state.selected_region]
    genre_list = ["Choose a genre"] + sorted(filtered_df['genre'].dropna().unique().tolist())
    selected_genre = st.selectbox("Genre:", genre_list)

    if st.button("Submit✅"):
        if selected_genre != "Choose a genre":
            st.session_state.selected_genre = selected_genre
            st.session_state.genre_selected = True
        else:
            st.warning("Please choose a genre before continuing.")

# Step 3: Show Movies
if st.session_state.genre_selected:
    st.success(f"Genre selected: {st.session_state.selected_genre}")

    result = df[
        (df['region'] == st.session_state.selected_region) &
        (df['genre'] == st.session_state.selected_genre)
    ]

    st.subheader("🎥 Recommended Movies:")
    if not result.empty:
        for title in result['title']:
            st.markdown(f"✅ {title}")
    else:
        st.warning("No movies found for this selection.")
