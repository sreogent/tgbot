import sqlite3
from datetime import datetime

# Подключение к базе данных
conn = sqlite3.connect("db.sqlite", check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы логов
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    target_id INTEGER,
    reason TEXT,
    date TEXT
)
""")
conn.commit()

def log_action(user_id, action, target_id=None, reason=None):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO logs (user_id, action, target_id, reason, date) VALUES (?, ?, ?, ?, ?)",
        (user_id, action, target_id, reason, date)
    )
    conn.commit()
