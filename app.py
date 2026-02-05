from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
DAD_JOKE_API_URL = "https://icanhazdadjoke.com/"

@app.route('/', methods=['GET'])
def get_joke():
    response = requests.get(DAD_JOKE_API_URL, headers={"Accept": "application/json"})
    try:
        data = response.json()
    except ValueError:
        data = 'Error retrieving joke.'

    return render_template('index.html', data=data['joke'])

if __name__ == '__main__':
    app.run(debug=True)