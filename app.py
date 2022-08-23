from statistics import mode
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Stock Data for Covid-19 Vaccinations"

@app.route("/visuals")
def viz():
    print("Server received request for 'Visualizations' page...")
    return "Welcome to the Visualizations Page"


if __name__ == '__main__':
    app.run(debug=True)
