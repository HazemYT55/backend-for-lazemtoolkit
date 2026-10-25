from flask import Blueprint, jsonify, request
import re
thumbnails_bp = Blueprint("thumbnails", __name__)
@thumbnails_bp.route("/thumbnails", methods=["GET"])
def get_thumbnails():
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", request.args.get("url", ""))
    if not match: return jsonify({"error": "Invalid URL"}), 400
    v = match.group(1)
    return jsonify({"thumbnails": {s: f"https://img.youtube.com/vi/{v}/{s}.jpg" for s in ["default","mqdefault","hqdefault","maxresdefault"]}})
