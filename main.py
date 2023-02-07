import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

requete = requests.Session()
# page = requete.get(url)

#soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

url_post = "http://annuairesante.ameli.fr/recherche.html"

payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
}

page = requete.post(url_post, params=payload, headers=header)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
