from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print("New visit from IP:", ip)
    return "Hello! Your visit is logged."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
