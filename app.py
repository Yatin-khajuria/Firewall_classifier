from flask import Flask, render_template, request
import joblib
from collections import Counter

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        user_input = request.form["request"]
        model_choice = request.form["model"]

        model_map = {
            "rf": "rf_model.joblib",
            "knn": "knn_model.joblib",
            "svm": "svm_model.joblib"
        }

        model = joblib.load(model_map[model_choice])
        vectorizer = joblib.load("vectorizer.joblib")
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)[0]

        history.insert(0, {"request": user_input, "prediction": prediction})
        if len(history) > 10:
            history.pop()

    counter = Counter([item["prediction"] for item in history])
    chart_data = {"labels": list(counter.keys()), "counts": list(counter.values())}

    return render_template("index.html", prediction=prediction, history=history, chart_data=chart_data)

if __name__ == "__main__":
    app.run(debug=True)
