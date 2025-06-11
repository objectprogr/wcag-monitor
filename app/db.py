import psycopg2
import datetime

def init_db():
    with psycopg2.connect(dbname="wcagmonitor", user="wcaguser", password="wcagpass") as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id SERIAL PRIMARY KEY,
                url TEXT,
                content TEXT,
                diff TEXT,
                audit TEXT,
                timestamp TIMESTAMP
            );
            """)
            conn.commit()

def save_result(url, html, diff, audit):
    with psycopg2.connect(dbname="wcagmonitor", user="wcaguser", password="wcagpass") as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO results (url, content, diff, audit, timestamp) VALUES (%s, %s, %s, %s, %s)",
                        (url, html, diff, audit, datetime.datetime.now()))
            conn.commit()
