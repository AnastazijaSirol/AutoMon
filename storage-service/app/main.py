from app.database import init_db
from app.mqtt_listener import start_listener

if __name__ == "__main__":
    print("Starting storage-service...")
    init_db()
    start_listener()