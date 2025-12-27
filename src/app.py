from flask import Flask, render_template
from flask_mysqldb import MySQL
import os
import time

app = Flask(__name__)

# -------------------------
# Configuration
# -------------------------
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST", "mysql")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER", "appuser")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD", "password")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DATABASE", "appdb")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# -------------------------
# Routes
# -------------------------
@app.route("/")
def index():
    messages = []

    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT message FROM messages")
        rows = cur.fetchall()
        messages = [row["message"] for row in rows]
        cur.close()
    except Exception as e:
        app.logger.error(f"DB error while fetching messages: {e}")

    return render_template("index.html", messages=messages)


@app.route("/health")
def health():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT 1")
        cur.close()
        return "OK", 200
    except Exception as e:
        app.logger.error(f"Health check failed: {e}")
        return "DB DOWN", 500


# -------------------------
# App Entrypoint
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
