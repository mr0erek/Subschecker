####################################################
# Author    : mr0erek                             #
# Tool-Type : YT-Subscriber Status Checker        #
# API       : Used Google's Youtube analytics api #
###################################################
import os
from flask import Flask, redirect, request, jsonify, session, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS if needed
app.secret_key = os.urandom(24)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://subschecker.vercel.app/api"
CHANNEL_ID = "UCXnBZRpLD7QzcJsUKBF-cKw"  # Replace with your actual channel ID

@app.route("/api/login")
def login():
    auth_url = (
        f"https://accounts.google.com/o/oauth2/auth?"
        f"client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&"
        f"scope=https://www.googleapis.com/auth/youtube.readonly&access_type=offline"
    )
    return redirect(auth_url)

@app.route("/api/callback")
def callback():
    code = request.args.get("code")
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    response = requests.post(token_url, data=token_data)
    if response.status_code != 200:
        return jsonify({"error": "Failed to get access token"}), 400

    access_token = response.json().get("access_token")
    session["access_token"] = access_token
    return redirect(url_for("check_subscription"))

@app.route("/api/check-subscription")
def check_subscription():
    access_token = session.get("access_token")
    if not access_token:
        return jsonify({"error": "Access token missing"}), 403

    headers = {"Authorization": f"Bearer {access_token}"}
    sub_check_url = (
        f"https://www.googleapis.com/youtube/v3/subscriptions?"
        f"part=snippet&forChannelId={CHANNEL_ID}&mine=true"
    )

    sub_response = requests.get(sub_check_url, headers=headers)
    if sub_response.status_code != 200:
        return jsonify({"error": "Failed to fetch subscription status"}), 400

    sub_data = sub_response.json()
    is_subscribed = "items" in sub_data and len(sub_data["items"]) > 0
    return jsonify({"subscribed": is_subscribed})

@app.route("/api/logout")
def logout():
    session.clear()
    return "Logged out"

# For Vercel to recognize this as an entry point
handler = app
