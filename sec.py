from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "password1234",
    "mary": "secret4567"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return True
    return False

@app.route('/api/protected')
@auth.login_required
def protected_resource():
    return jsonify({"message": "This is a protected resource!"})

if __name__ == '__main__':
    app.run(debug=True)