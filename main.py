from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

USERS_FILE = r"C:\Users\touti\Desktop\servers\users.json"  

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([], f)


    with open(USERS_FILE, "r") as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            users = []


    users.append({"email": email, "password": password})

    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)
    print(users)
    return jsonify({"message": "User registered successfully"}), 200

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8000)
