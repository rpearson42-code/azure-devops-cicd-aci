from flask import Flask, jsonify, request
import os, socket, time
app = Flask(__name__)
START_TIME = time.time()
VERSION = os.environ.get("APP_VERSION", "1.0.0")
ENV_NAME = os.environ.get("APP_ENV", "dev")

@app.route("/", methods=["GET"])
def root():
    return jsonify(message="Hello from Azure CI/CD demo!", host=socket.gethostname(), env=ENV_NAME, version=VERSION)

@app.route("/healthz", methods=["GET"])
def health():
    return jsonify(status="ok")

@app.route("/readyz", methods=["GET"])
def ready():
    uptime = time.time() - START_TIME
    return jsonify(status="ready", uptime_seconds=int(uptime))

@app.route("/api/v1/info", methods=["GET"])
def info():
    return jsonify(service="azure-devops-cicd-aci", version=VERSION, environment=ENV_NAME, docs="/api/v1/echo (POST json)")

@app.route("/api/v1/echo", methods=["POST"])
def echo():
    payload = request.get_json(silent=True) or {}
    return jsonify(received=payload, count=len(payload))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
