import requests
import urllib.parse
from bs4 import BeautifulSoup

URL = ""

suffix = ""
suffixEncoded = urllib.parse.quote(suffix, safe='')
# Se mi servono cookie di sessione, devo fare session = requests.Session() e poi session.get(URL)
r = requests.get(URL + suffixEncoded)
html = r.text
soup = BeautifulSoup(html, "html.parser")