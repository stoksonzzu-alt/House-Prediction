import os
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        overall_quality = float(
            request.form["overall_quality"]
        )

        living_area = float(
            request.form["living_area"]
        )

        garage_cars = float(
            request.form["garage_cars"]
        )

        total_basement_sf = float(
            request.form["total_basement_sf"]
        )

        model_choice = request.form["model_choice"]

        # simulasi prediksi
        prediction = (
            overall_quality * 10000 +
            living_area * 50 +
            garage_cars * 5000 +
            total_basement_sf * 20
        )

        return render_template(
            "index.html",
            prediction=round(prediction, 2),
            model_used=model_choice
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
