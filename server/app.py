from flask import Flask, render_template, request
import pickle
import json
import numpy as np
import os

app = Flask(__name__)

# Get absolute path (SAFE WAY)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "Model", "banglore_home_prices_model.pickle")
COLUMNS_PATH = os.path.join(BASE_DIR, "..", "Model", "columns.json")

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Load columns
with open(COLUMNS_PATH, "r") as f:
    data_columns = json.load(f)["data_columns"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        total_sqft = float(request.form["total_sqft"])
        bath = int(request.form["bath"])
        bhk = int(request.form["bhk"])
        location = request.form["location"].lower()

        x = np.zeros(len(data_columns))
        x[0] = total_sqft
        x[1] = bath
        x[2] = bhk

        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1

        price = model.predict([x])[0]

        return render_template(
            "index.html",
            prediction_text=f"Estimated House Price: ₹ {round(price, 2)} Lakhs"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error in input. Please enter valid values."
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


