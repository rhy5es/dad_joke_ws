from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
#dad_joke_api = requests.get("https://icanhazdadjoke.com/api", headers={"Accept" : "application/json"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)