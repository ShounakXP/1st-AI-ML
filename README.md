# Movie Recommendation System

# Project Description
A content-based movie recommendation system that suggests similar movies using genre analysis and cosine similarity. Built with Python and machine learning libraries, it helps users discover new films based on their preferences in a simple and efficient way.


# Features
- Recommend similar movies based on genre
- Simple and fast content-based filtering
- User-friendly command-line interface
- Uses cosine similarity for accurate suggestions


# Tech Stack
- Python
- Pandas
- Scikit-learn


# Project Structure
movie-recommender/
│── movie_predictor.py
│── README.md


# How to Run

1. Install dependencies:
pip install pandas scikit-learn

2. Run the program:
python movie_predictor.py

3. Enter a movie name and get recommendations.

# How It Works
- Converts movie genres into vectors using CountVectorizer
- Calculates similarity using cosine similarity
- Recommends top 5 similar movies


# Example
Input: Inception  
Output: Interstellar, Tenet, The Dark Knight, etc.


# Author:
Shounak Gupta
