from flask import Blueprint, jsonify, request
import os, re, requests
from dotenv import load_dotenv
load_dotenv()
youtube_bp = Blueprint("youtube", __name__)
API_KEY = os.getenv("YOUTUBE_API_KEY")
@youtube_bp.route("/tags", methods=["GET"])
def get_tags():
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", request.args.get("url", ""))
    if not match or not API_KEY: return jsonify({"tags": []})
    r = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={match.group(1)}&key={API_KEY}").json()
    return jsonify({"tags": r["items"][0]["snippet"].get("tags", []) if r.get("items") else []})
