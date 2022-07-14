from bs4 import BeautifulSoup
import requests

date_user_input = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
billboard_url = "https://www.billboard.com/charts/hot-100/"
completed_url = "".join([billboard_url, date_user_input])

response = requests.get(completed_url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# print(soup.find(name="div", class_="o-chart-results-list-row-container").find(name='h3').getText().strip())

song_div_list = soup.find_all(name="div", class_="o-chart-results-list-row-container")

song_list = []
for song in song_div_list:
    song_list.append(song.find(name='h3').getText().strip())

print(song_list)
