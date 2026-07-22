from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Load common passwords list at startup
COMMON_PASSWORDS = set()
wordlist_path = os.path.join(os.path.dirname(__file__), "10-million-password-list-top-1000.txt")
if os.path.exists(wordlist_path):
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            COMMON_PASSWORDS.add(line.strip().lower())

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if password.lower() in COMMON_PASSWORDS:
        return False, "Password is too common. Please choose a stronger password."
    return True, ""

@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        password = request.form.get("password", "")
        is_valid, error = validate_password(password)
        if is_valid:
            return redirect(url_for("welcome", password=password))
    return render_template("index.html", error=error)

@app.route("/welcome")
def welcome():
    password = request.args.get("password", "")
    return render_template("welcome.html", password=password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)