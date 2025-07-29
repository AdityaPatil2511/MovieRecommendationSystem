import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load ratings
ratings = pd.read_csv("data/ratings.csv")

# Prepare Surprise dataset
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train/test split
trainset, testset = train_test_split(data, test_size=0.2)

# SVD algorithm
algo = SVD()
algo.fit(trainset)

# Predict ratings
predictions = algo.test(testset)

# Evaluate using RMSE
print("RMSE of SVD model:")
accuracy.rmse(predictions)

# Recommend top movies for a user
def recommend_for_user(user_id, n=10):
    all_movie_ids = ratings['movieId'].unique()
    pred_ratings = [algo.predict(user_id, mid) for mid in all_movie_ids]
    pred_ratings.sort(key=lambda x: x.est, reverse=True)
    top_n = [pred.iid for pred in pred_ratings[:n]]

    # Get movie titles
    movies = pd.read_csv("data/movies.csv")
    return movies[movies['movieId'].isin(top_n)]['title'].tolist()
