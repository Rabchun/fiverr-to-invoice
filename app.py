import logging
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Налаштування логування у консоль (Render збирає ці логи)
logging.basicConfig(level=logging.INFO)

# Локальний файл для тимчасового збереження логів
LOG_FILE = "visits.log"

def log_visit(ip):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] New visit from IP: {ip}"

    # Лог у консоль (Render Logs)
    logging.info(log_line)

    # Лог у тимчасовий файл
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")

@app.route("/")
def home():
    # Беремо реальний IP через проксі (Render додає X-Forwarded-For)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    
    # Якщо кілька IP у заголовку, беремо перший
    if "," in ip:
        ip = ip.split(",")[0].strip()

    log_visit(ip)
    return f"Hello! Your visit is logged. Detected IP: {ip}"

if __name__ == "__main__":
    # Для локальної перевірки
    print("Запуск Flask локально на 0.0.0.0:3000")
    app.run(host="0.0.0.0", port=3000)


