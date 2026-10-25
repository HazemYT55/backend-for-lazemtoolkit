from flask import Blueprint, jsonify, request
import json, os
hashtags_bp = Blueprint("hashtags", __name__)
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "hashtags.json")
@hashtags_bp.route("/hashtags", methods=["GET"])
def get_hashtags():
    with open(DATA_PATH, encoding="utf-8") as f: db = json.load(f)
    t = request.args.get("topic", "").lower()
    for k in db:
        if k in t: return jsonify({"hashtags": db[k]})
    return jsonify({"hashtags": db["default"]})
