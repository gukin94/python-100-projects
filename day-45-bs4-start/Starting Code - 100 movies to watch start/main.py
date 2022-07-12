import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
best_movies_page = response.text
soup = BeautifulSoup(best_movies_page, "html.parser")

movie_rank_lst = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movie_rank_lst.reverse()
print(movie_rank_lst)

with open("movies.txt", mode="w") as file:
    for movie in movie_rank_lst:
        file.write(f"{movie}\n")
