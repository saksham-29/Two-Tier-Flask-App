import os
import time
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

# ----------------------------
# Flask App Setup
# ----------------------------
app = Flask(__name__)

# ----------------------------
# MySQL Configuration
# ----------------------------
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'mysql').strip()
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'root')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'devops')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))

mysql = MySQL(app)

# ----------------------------
# Database Initialization (NON-FATAL)
# ----------------------------
def init_db_with_retry(retries=10, delay=3):
    """
    Try to initialize the database.
    Failure should NOT crash the app.
    """
    for attempt in range(retries):
        try:
            cur = mysql.connection.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    message TEXT
                )
            """)
            mysql.connection.commit()
            cur.close()
            print("Database initialized successfully")
            return
        except Exception as e:
            print(f"DB init failed (attempt {attempt + 1}/{retries}): {e}")
            time.sleep(delay)

    # IMPORTANT: do NOT crash Flask
    print("WARNING: Database initialization failed. App will continue running.")

# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT message FROM messages")
        messages = cur.fetchall()
        cur.close()
    except Exception as e:
        print("DB read failed:", e)
        messages = []

    return render_template("index.html", messages=messages)

@app.route("/submit", methods=["POST"])
def submit():
    new_message = request.form.get("new_message")

    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO messages (message) VALUES (%s)",
            (new_message,)
        )
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": new_message})
    except Exception as e:
        print("DB write failed:", e)
        return jsonify({"error": "Database unavailable"}), 500

# ----------------------------
# Healthcheck (NO DB ACCESS)
# ----------------------------
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

# ----------------------------
# App Startup
# ----------------------------
if __name__ == "__main__":
    init_db_with_retry()
    app.run(host="0.0.0.0", port=5000)
