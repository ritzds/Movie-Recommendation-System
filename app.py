# Importing necessary libraries
from turtle import width
import streamlit as st
import pandas as pd
import requests as re
import numpy as np
import pickle as pkl
from PIL import Image


# Changing the name and title of the webpage
img = Image.open('Poster.jpeg')
st.set_page_config(page_title='Movie Recommender',page_icon=img)


# Hiding the header and footer
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)

# Importing the dataset as a pickle file
movies = pkl.load(open('movies.pkl','rb'))

# Importing the similarity vectors as a pickle file
similarity = pkl.load(open('similarity.pkl','rb'))

# Fetching the Poster of the movie
def fetch_poster(movie_id):
    data = re.get('https://api.themoviedb.org/3/movie/{}?api_key=35fe996d08b5c283267480f40729bb10'.format(movie_id))
    picture = data.json()
    return "https://image.tmdb.org/t/p/w500/" + picture['poster_path']

# Function to recommend movies
def recommend(option,score):
    score = score/100
    index = movies[movies['title'] == option].index[0]
    similarity_list = similarity[index]
    movie_list = sorted(list(enumerate(similarity_list)), reverse=True, key=(lambda x: x[1]))[1:11]

# This temp list holds the movies filtered according to filter score
    temp = []
    for x in movie_list:
        if x[1] >= score:
            temp.append(x)

    

# Itterrating throught the list of the similar movies
    recommended_movies = []
    posters = []
    for i in temp:
        posters.append(fetch_poster(movies['movie_id'].iloc[i[0]]))
        recommended_movies.append(movies['title'].iloc[i[0]])

    return recommended_movies,posters

# Title of the movie
st.title('Movie Recommendation System')

# Option bar displaying the list of the movies
option = st.selectbox(
    'Which movie did you liked and want recommendation for?',
     movies.title.values)

# The recommendation button
filter_score = st.slider('Similarity Score (The Higher, The Better)', 0, 20, 5)
filter_score = filter_score*1.5
if st.button('Recommend'):
    recommendations,posters = recommend(option,filter_score)
    col1,col2,col3= st.columns(3)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0],width=150)
    with col2:
        st.text(recommendations[1])
        st.image(posters[1],width=150)
    with col3:
        st.text(recommendations[2])
        st.image(posters[2],width=150)
    
    col4,col5,col6= st.columns(3)
    with col4:
        st.text(recommendations[3])
        st.image(posters[3],width=150)
    with col5:
        st.text(recommendations[4])
        st.image(posters[4],width=150)
    with col6:
        st.text(recommendations[5])
        st.image(posters[5],width=150)
    
    col7,col8,col9 = st.columns(3)
    with col7:
        st.text(recommendations[6])
        st.image(posters[6],width=150)
    with col8:
        st.text(recommendations[7])
        st.image(posters[7],width=150)
    with col9:
        st.text(recommendations[8])
        st.image(posters[8],width=150)

    col10,col1,col2 = st.columns(3)
    with col10:
        st.text(recommendations[9])
        st.image(posters[9],width=150)