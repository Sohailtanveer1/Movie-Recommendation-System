import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict = pickle.load(open("movie_dict.pkl",'rb'))
similarity=pickle.load(open("similarity.pkl",'rb'))
movies = pd.DataFrame(movie_dict)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    # index of the movie
    index = movies[movies['title'] == movie].index[0]
    #finidng the top 10 movies
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movie_names= []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters


st.title("Movie Recommender System")

selected_movie_list = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_list)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    with col1:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col3:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
