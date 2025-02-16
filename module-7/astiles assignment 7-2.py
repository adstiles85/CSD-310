import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path('.') / '../module-6/.env'  # Adjust path to reference module-6 where .env is stored
load_dotenv(dotenv_path=env_path)

# Retrieve credentials from .env file
db_config = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE"),
}

try:
    # Connect to MySQL
    db = mysql.connector.connect(**db_config)
    print(f"Connected to MySQL database: {db_config['database']}")

    # Create a cursor object
    cursor = db.cursor()

    # Query 1: Display all records from Studio table
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    for row in cursor.fetchall():
        print(f"Studio ID: {row[0]} \nStudio Name: {row[1]}\n")

    # Query 2: Display all records from Genre table
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    for row in cursor.fetchall():
        print(f"Genre ID: {row[0]} \nGenre Name: {row[1]}\n")

    # Query 3: Display movie names for films with runtime under 2 hours
    print("\n-- DISPLAYING Short Films --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    for row in cursor.fetchall():
        print(f"Film Name: {row[0]} \nRuntime: {row[1]}\n")

    # Query 4: Display movies and directors grouped by director
    print("\n-- DISPLAYING Director Records in Order --")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    for row in cursor.fetchall():
        print(f"Film Name: {row[0]} \nDirector: {row[1]}\n")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")

finally:
    # Close the connection
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nConnection closed.")
