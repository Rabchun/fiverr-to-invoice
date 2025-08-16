from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "visits.log"

def log_visit(ip):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] New visit from IP: {ip}\n"
    
    # Вивід у консоль
    print(log_line.strip())
    
    # Додати у файл
    with open(LOG_FILE, "a") as f:
        f.write(log_line)

@app.route("/")
def home():
    # Беремо реальний IP через проксі (Render додає X-Forwarded-For)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    
    # Якщо заголовок містить кілька IP (ланцюжок проксі), беремо перший
    if "," in ip:
        ip = ip.split(",")[0].strip()
    
    log_visit(ip)
    return "Hello! Your visit is logged."

if __name__ == "__main__":
    # Для локальної перевірки
    app.run(host="0.0.0.0", port=3000)
