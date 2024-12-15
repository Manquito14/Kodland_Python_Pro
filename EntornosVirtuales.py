from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/pan"> Hello, World! </a>'

@app.route("/pan")
def pan():
    return '<a href="/video"> ¿Pan? </a>'

@app.route("/video")
def pan_video():
    return "<h1>¡pan!</h1>"

app.run(debug=True)
