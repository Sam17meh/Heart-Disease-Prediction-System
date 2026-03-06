from flask import Blueprint, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

DB_NAME = "users.db"


def get_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    db.commit()
    return db



@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
        """)

        cursor.execute(
            "INSERT INTO users (username,password) VALUES (?,?)",
            (username, password)
        )

        db.commit()
        db.close()

        return redirect("/login")

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        db.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
