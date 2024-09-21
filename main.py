import pandas as pd
from surprise import Dataset, SVD
from surprise.model_selection import cross_validate

'''
    1. Importación y carga de datos
    Se importan los datos de las películas y las reseñas de los usuarios y se cargan en un DataFrame de Pandas.
'''

# Importación del dataset
movies_df = pd.read_csv('data/movies.csv')
ratings_df = pd.read_csv('data/ratings.csv')

#  Dimensión del dataset
print("La dimensión de las películas es: ", movies_df.shape, "\nLa dimensión de las reseñas es: ", ratings_df.shape)

movies_df.head()
ratings_df.head()

movie_names = movies_df.set_index('movieId')['title'].to_dict()
n_users = len(ratings_df.userId.unique())
n_items = len(ratings_df.movieId.unique())

print("Número de usuarios: ", n_users)
print("Número de películas: ", n_items)
print("La matriz de reseñas tendra:", n_users*n_items, "valores")