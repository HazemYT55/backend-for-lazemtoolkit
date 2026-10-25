from flask import Blueprint, jsonify, request
monetization_bp = Blueprint("monetization", __name__)
@monetization_bp.route("/monetization", methods=["GET"])
def check():
    s, h = int(request.args.get("subs", 0)), int(request.args.get("hours", 0))
    return jsonify({"eligible": s >= 1000 and h >= 4000})
