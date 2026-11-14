
import os
from flask import Flask, jsonify, render_template

# Create the Flask application
app = Flask(__name__)

# Application configuration
APP_NAME = "CloudOps Health Monitor"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")


# Homepage route
@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_version=APP_VERSION,
        app_env=APP_ENV
    )


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME
    }), 200


# Application version endpoint
@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


# Environment endpoint
@app.route("/environment", methods=["GET"])
def environment():
    return jsonify({
        "environment": APP_ENV
    }), 200


# Start the development server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
