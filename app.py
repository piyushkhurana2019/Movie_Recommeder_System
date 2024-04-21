import streamlit as st # type: ignore
import pickle
import requests # type: ignore

movies_list=pickle.load(open('movies.pkl copy','rb'))
movies=movies_list['title'].values
similarity = pickle.load(open('similarity.pkl copy','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5b0d540551d74d6da14f4ee767988265&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

def recommend(movie):
    index = movies_list[movies== movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in distances[1:6]:
        movie_id=movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies,recommended_movies_posters

st.title('Movie Recommeder System')

selected_movie_name=st.selectbox(
    'Choose The Movie',
    movies
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])