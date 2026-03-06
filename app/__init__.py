from flask import Flask
import joblib
import os

def create_app():
    app = Flask(__name__)

    app.secret_key = "heart-secret-key"

    model_path = os.path.join("app", "model", "heart_model.pkl")
    app.model = joblib.load(model_path)

    from app.routes import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
