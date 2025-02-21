#!/usr/bin/python3
"""flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """accueil"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    """liste d'utilisateurs enregistres"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """verification du statut de l'API"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """recuperer un utilisateur"""
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


    @app.route("/add_user", methods=["POST"])
def add_user():
    """ajouter un utilisateur"""
    data = request.get_json()
    username = data.get("username")

    if not username :
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
