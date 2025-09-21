from flask import Flask, request, render_template_string, redirect
import os

app = Flask(__name__)

REDIRECT_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
FLAG = os.environ.get("FLAG")
CUSTOM_HEADER = "X-Key-Header"
HEADER_VALUE = "My_key_is_not_so_secret"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Robots and Headers</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');
        body {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
            text-align: center;
            backdrop-filter: blur(10px);
        }
        h1 {
            font-size: 28px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #00eaff;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #00eaff;
        }
        input {
            width: 90%;
            padding: 12px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            text-align: center;
        }
        input::placeholder {
            color: #bbb;
        }
        button {
            background: #00eaff;
            color: black;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            text-transform: uppercase;
            font-weight: bold;
            box-shadow: 0 0 10px #00eaff;
            transition: 0.3s;
        }
        button:hover {
            background: #ff0099;
            box-shadow: 0 0 15px #ff0099;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- For web crawlers: Check /robots.txt for guidance -->
        <h1>Robots and Headers</h1>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Access</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/login", methods=["POST"])
def login():
    if request.headers.get(CUSTOM_HEADER) == HEADER_VALUE:
        return FLAG
    return redirect(REDIRECT_URL)

@app.route("/robots.txt")
def robots():
    robots_content = f"""User-agent: *
Disallow: /nothing_interesting
    """
    return robots_content, 200, {'Content-Type': 'text/plain'}

@app.route("/nothing_interesting")
def not_int():
    content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nothing Interesting</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');
            body {{
                font-family: 'Orbitron', sans-serif;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
                text-align: center;
                backdrop-filter: blur(10px);
            }}
            h1 {{
                font-size: 28px;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: #00eaff;
                margin-bottom: 20px;
                text-shadow: 0 0 10px #00eaff;
            }}
            p {{
                font-size: 16px;
                color: #aaa;
                margin-bottom: 20px;
            }}
            .header-info {{
                font-size: 18px;
                color: #00eaff;
                text-align: center;
                margin: 10px 0;
                background: rgba(255, 255, 255, 0.2);
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }}
            .header-info span {{
                font-size: 20px;
                color: #ff0099;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Nothing Interesting</h1>
            <p>Try sending a POST request to /login with:</span></p>
            <div class="header-info">
                <p><strong>Header:</strong> {CUSTOM_HEADER}</p>
                <p><strong>Header Value:</strong> {HEADER_VALUE}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return content, 200, {'Content-Type': 'text/html'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6001)
