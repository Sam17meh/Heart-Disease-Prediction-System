from flask import Blueprint, render_template, request, redirect, session, current_app
import numpy as np

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return redirect("/login")


@main.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@main.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        try:
            model = current_app.model

            features = np.array([[
                int(request.form.get("age", 0)),
                int(request.form.get("gender", 0)),
                int(request.form.get("heart_rate", 0)),
                int(request.form.get("sbp", 0)),
                int(request.form.get("dbp", 0)),
                float(request.form.get("blood_sugar", 0)),
                float(request.form.get("ck_mb", 0)),
                float(request.form.get("troponin", 0)),
            ]])

            prediction = model.predict(features)[0]

            if hasattr(model, "predict_proba"):
                probability = model.predict_proba(features)[0][1] * 100
            else:
                probability = 80 if prediction == 1 else 20

            result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"
            level = "High" if prediction == 1 else "Low"

            return render_template(
                "result.html",
                result=result,
                probability=round(probability, 2),
                level=level
            )

        except Exception as e:
            return render_template("predict.html", error=str(e))

    return render_template("predict.html")
