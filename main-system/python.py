import imp
from bs4 import BeautifulSoup
with open("index.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
print(soup)