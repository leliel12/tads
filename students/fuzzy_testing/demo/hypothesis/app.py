from flask import Flask, request, jsonify
import re
from datetime import datetime

app = Flask(__name__)

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(force=True)

    email = data.get("email")
    password = data.get("password")
    birthdate = data.get("birthdate")  # ISO: "YYYY-MM-DD"

    if not email or not EMAIL_REGEX.fullmatch(email):
        return jsonify({"error": "Invalid email"}), 400

    if not password or len(password) < 6:
        return jsonify({"error": "Password too short"}), 400

    try:
        date = datetime.strptime(birthdate, "%Y-%m-%d")
        if date.year < 1900 or date >= datetime.now():
            return jsonify({"error": "Invalid birthdate"}), 400
    except:
        return jsonify({"error": "Malformed birthdate"}), 400

    return jsonify({"status": "registered"}), 200

@app.route("/sum", methods=["GET"])
def sum_values():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
