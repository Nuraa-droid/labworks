# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def is_above_5_5(movie):
    for movie in movies:
        if movie['imdb'] > 5.5:
            return True
    

def get_movie_name(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

def by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

def average(movies):
    total = sum(movie['imdb'] for movie in movies)
    return total / len(movies)

def average_by_category(movies, category):
    movie_category = by_category(movies, category)
    return average(movie_category)
movie = input()
print(is_above_5_5(movie))
print("movies with imdb score above 5.5:", get_movie_name(movies))
category = input()
print(f"{category} movies:", by_category(movies, category))
print("average imdb score:", average(movies))
print(f"avearge imdb score of {category} movies:", average_by_category(movies, category))