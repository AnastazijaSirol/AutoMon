import sqlite3
from pathlib import Path

from dotenv import load_dotenv
import os


DB_PATH = "/app/db/traffic.db"

def get_connection():
    return sqlite3.connect(DB_PATH)