import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"
r = requests.get(url)

soup = BeautifulSoup(r.text ,  "html.parser")
# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)

# response = requests.get("https://www.codewithharry.com")

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     print(response.text)  # Print the HTML content of the page
# else:
#     print("Request failed with status code:", response.status_code)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" : "priya's request module",
#     "body" :"json palceholder",
#     "userId" : "123456789"
# }
# headers = {
#     "Content-type" :"application/json; charset = UTF-8",
# }

# response = requests.post(url , headers = headers , json=data)
# print(response.text)
