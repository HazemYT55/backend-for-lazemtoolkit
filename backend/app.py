from flask import Flask, jsonify
from flask_cors import CORS
from routes.hashtags import hashtags_bp
from routes.titles import titles_bp
from routes.thumbnails import thumbnails_bp
from routes.monetization import monetization_bp
from routes.youtube import youtube_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(hashtags_bp, url_prefix="/api")
app.register_blueprint(titles_bp, url_prefix="/api")
app.register_blueprint(thumbnails_bp, url_prefix="/api")
app.register_blueprint(monetization_bp, url_prefix="/api")
app.register_blueprint(youtube_bp, url_prefix="/api")

@app.route("/")
def home():
    return jsonify({"app": "Lazem Toolkit API", "status": "running"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
