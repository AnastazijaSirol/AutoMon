import sqlite3
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = os.environ.get("DB_PATH", "/app/db/traffic.db")

def get_connection():
    return sqlite3.connect(DB_PATH)