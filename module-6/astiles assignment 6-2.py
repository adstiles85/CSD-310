from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
from pathlib import Path

# Load .env file explicitly
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Print environment variables to check if they loaded correctly
print("USER:", os.getenv("USER"))
print("PASSWORD:", "*" * len(os.getenv("PASSWORD")))  # Mask password
print("HOST:", os.getenv("HOST"))
print("DATABASE:", os.getenv("DATABASE"))

# Exit if environment variables are not loading correctly
if not os.getenv("PASSWORD"):
    print("ERROR: Environment variables are not loading correctly.")
    exit()

# Connect to MySQL
db_config = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE")
}

try:
    db = mysql.connector.connect(**db_config)
    print(f"Connected to MySQL database: {db_config['database']}")

    # Show tables
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")

    print("\nAvailable Tables:")
    for table in cursor:
        print(table[0])

except Error as err:
    print(f"MySQL Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nConnection closed.")
