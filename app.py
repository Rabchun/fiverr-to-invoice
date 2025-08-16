from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    # Симуляція реального IP через заголовок
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    
    if "," in ip:
        ip = ip.split(",")[0].strip()
    
    print("New visit from IP:", ip)
    return f"Hello! Your visit is logged. Detected IP: {ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
