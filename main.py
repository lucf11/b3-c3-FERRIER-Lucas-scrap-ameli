import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/"

header = {
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

requete = requests.Session();
page = requete.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup)