from flask import Blueprint, jsonify, request
import json, os
titles_bp = Blueprint("titles", __name__)
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "title_templates.json")
@titles_bp.route("/titles", methods=["GET"])
def get_titles():
    with open(DATA_PATH, encoding="utf-8") as f: db = json.load(f)
    t = request.args.get("topic", "this")
    tone = request.args.get("tone", "clickbait")
    return jsonify({"titles": [x.replace("{topic}", t) for x in db.get(tone, db["clickbait"])]})
