from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG")

IMAGES = [f"/static/images/{i}.jpg" for i in range(1, 10)]

TEMPLATE = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Brainroot Animals</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 0;
            padding: 20px;
        }

        h1, h2 {
            color: #333;
        }

        #slideshow-container {
            width: 320px;
            height: 300px;
            overflow: hidden;
            border: 3px solid #ccc;
            border-radius: 10px;
            margin-bottom: 20px;
            background: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        #slideshow {
            width: 100%;
            height: 100%;
        }

        #slideshow img {
            display: none;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        #slideshow img.active {
            display: block;
        }

        form {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 300px;
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }

        input[type="text"] {
            padding: 10px;
            font-size: 16px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            padding: 10px;
            font-size: 16px;
            border: none;
            background: #28a745;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #218838;
        }

        .message {
            margin-top: 15px;
            font-weight: bold;
        }

        .error {
            color: red;
        }

        .success {
            color: green;
        }
    </style>
</head>
<body>
    <h1>My fav animals</h1>
    <div id="slideshow-container">
        <div id="slideshow">
            {% for img in images %}
                <img src="{{ img }}" class="{% if loop.index == 1 %}active{% endif %}">
            {% endfor %}
        </div>
    </div>

    <h2>Insert password</h2>
    <form method="POST">
        <input type="text" name="password" placeholder="Password" required>
        <button type="submit">Click</button>

        {% if flag %}
            <center>
                <div class="message success">{{ flag }}</div>
            </center>
        {% elif error %}
            <center>
                <div class="message error">Wrong password</div>
            </center>
        {% endif %}
    </form>

    <script>
        const images = document.querySelectorAll("#slideshow img");
        let index = 0;

        setInterval(() => {
            images[index].classList.remove("active");
            index = (index + 1) % images.length;
            images[index].classList.add("active");
        }, 1000);
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    flag = None
    error = False

    if request.method == "POST":
        password = request.form.get("password", "")
        if password == "il_mio_cappello_pieno_di_slim":
            flag = FLAG
        else:
            error = True

    return render_template_string(TEMPLATE, images=IMAGES, flag=flag, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6006)