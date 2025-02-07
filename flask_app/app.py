from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Subaru_logo_%28transparent%29.svg/1200px-Subaru_logo_%28transparent%29.svg.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXgaGpzW-c6R_D1uRD886hTdZ887p0SKX6yA&s",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Honda.svg/1280px-Honda.svg.png",
    "https://1000logos.net/wp-content/uploads/2018/02/Toyota-logo.png",
    "https://images.seeklogo.com/logo-png/8/1/lexus-logo-png_seeklogo-83673.png",
    "https://asilverliningfoundation.org/wp-content/uploads/2021/07/ford-logo.png.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSne_AdN5t-wooRwrmQmIsCHe56J4rkyrpiNpVRJwkZ89xTZulxz8WAoL9-qt-QfXWdv-Q&usqp=CAU"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")