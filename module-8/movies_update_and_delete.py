import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file explicitly
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Retrieve credentials from .env file
db_config = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE"),
}

def show_films(cursor, title):
    """ Function to display the films with genre and studio names """
    query = """
    SELECT 
        film_name AS Name, 
        film_director AS Director, 
        genre_name AS Genre, 
        studio_name AS Studio
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()
    
    print("\n", title)
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre: {film[2]}")
        print(f"Studio: {film[3]}\n")

try:
    # Connect to MySQL
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Show initial films
    show_films(cursor, "-- DISPLAYING FILMS --")

    # Insert a new film
    insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES ('Jurassic Park', '1993', 127, 'Steven Spielberg',
        (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),
        (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));
    """
    cursor.execute(insert_query)
    db.commit()
    show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")

    # Update film genre
    update_query = """
    UPDATE film
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien';
    """
    cursor.execute(update_query)
    db.commit()
    show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --")

    # Delete a film
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator';"
    cursor.execute(delete_query)
    db.commit()
    show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE --")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nConnection closed.")
