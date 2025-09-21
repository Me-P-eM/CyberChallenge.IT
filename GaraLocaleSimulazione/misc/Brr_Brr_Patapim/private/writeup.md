# Brr Brr Patapim

## Overview
To get the flag, you need to enter the correct password into the only available form. The password can be easily obtained by using the indices provided in the file 'brainroot_list.txt' and retrieving one character for each row-column combination. This can be done manually or with a simple Python script.

## Exploit
```py
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:6006"

animals = """Bombardiro_Crocodilo
Tralalero_Tralala
Tung_Tung_Tung_Tung_Tung_Tung_Tung_Tung_Tung_Sahur
Lirilì_Larilà
Boneca_Ambalabu
Chimpanzini_Bananini
Bombombini_Gusini
Cappuccino_Assassino
Trippi_Troppi
Frigo_Camelo
Ballerina_Cappuccina
U_Din_Din_Din_Din_Dun_Ma_Din_Din_Din_Dun
Trulimero_Trulicina
Garamaraman_dan_Madudungdung_tak_tuntung_perkuntung
Bobrito_Bandito
Girafa_Celeste
Fruli_Frula
Brri_Brri_Bicus_Dicus_Debicus_Dedicus
Glorbo_Fruttodrillo""".split("\n")

animals = [list(animal) for animal in animals]
index = ["1-8", "2-4", "1-11", "1-3", "1-18", "1-2", "2-10", "5-5", "2-3", "6-5", "8-4",
         "2-7", "4-5", "5-12", "1-10", "3-5", "9-4", "4-2", "13-7", "3-3", "1-14", "10-6",
         "1-7", "4-11", "6-12", "7-14", "11-3", "7-15", "5-9"]

rows = [int(el.split("-")[0]) for el in index]
columns = [int(el.split("-")[1]) for el in index]

password = ""
for r, c in zip(rows, columns):
    password += animals[r-1][c-1]

resp = requests.post(url, data={"password": password})
flag = BeautifulSoup(resp.text, "html.parser").find("div", class_="message success").get_text()

print(flag)
```