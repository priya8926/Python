import requests
import json

query = input("Which Type of news are you intrested in?")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-03&sortBy=publishedAt&apiKey=7f7272ab38604849b70c3b958a152780"
r = requests.get(url)
news = json.loads(r.text)
# print(news , type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("_________________________________________")