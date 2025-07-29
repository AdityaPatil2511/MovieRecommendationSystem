import pandas as pd

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Merge datasets on movieId
data = pd.merge(ratings, movies, on="movieId")

# Fill missing values in genres
movies['genres'] = movies['genres'].fillna('')

# (Optional) Convert genres into list format (can be helpful later)
movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

# Print preview
print(movies.head())
print(ratings.head())
