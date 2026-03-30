# Movie Recommendation System using Cosine Similarity

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Step 1: Create Dataset
# -----------------------------
data = {
    "title": [
        "Inception", "Interstellar", "The Dark Knight", "Tenet",
        "Avengers", "Iron Man", "Thor", "Captain America",
        "Titanic", "The Notebook", "La La Land", "Pride and Prejudice"
    ],
    "genre": [
        "sci-fi thriller", "sci-fi space", "action crime", "sci-fi action",
        "action superhero", "action superhero", "fantasy superhero", "action superhero",
        "romance drama", "romance drama", "romance musical", "romance drama"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Convert text to vectors
# -----------------------------
cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

# -----------------------------
# Step 3: Compute similarity
# -----------------------------
similarity = cosine_similarity(matrix)

# -----------------------------
# Step 4: Recommendation Function
# -----------------------------
def recommend(movie):
    movie = movie.lower()
    
    if movie not in df["title"].str.lower().values:
        print("❌ Movie not found in database.")
        return
    
    idx = df[df["title"].str.lower() == movie].index[0]
    
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    
    print(f"\n🎯 Recommendations for '{df.iloc[idx]['title']}':\n")
    
    count = 0
    for i in movie_list:
        if i[0] != idx:
            print("👉", df.iloc[i[0]].title)
            count += 1
        if count == 5:
            break

# -----------------------------
# Step 5: User Input
# -----------------------------
while True:
    user_input = input("\nEnter a movie name (or 'exit'): ")
    
    if user_input.lower() == "exit":
        print("👋 Exiting...")
        break
    
    recommend(user_input)
