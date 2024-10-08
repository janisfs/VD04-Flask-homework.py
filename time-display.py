from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Текущая дата и время: {current_datetime}"

if __name__ == "__main__":
    app.run()