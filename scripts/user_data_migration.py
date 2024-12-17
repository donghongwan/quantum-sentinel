import json
import sqlite3

def migrate_user_data(source_file, db_file):
    """Migrate user data from a JSON file to a SQLite database."""
    with open(source_file, 'r') as f:
        user_data = json.load(f)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )
    ''')

    # Insert user data into the database
    for user in user_data:
        cursor.execute('''
            INSERT INTO users (name, email, age) VALUES (?, ?, ?)
        ''', (user['name'], user['email'], user['age']))

    conn.commit()
    conn.close()
    print(f"User data migrated to {db_file}.")

if __name__ == "__main__":
    source_file = "data/user_data.json"  # Replace with your actual source file
    db_file = "data/users.db"  # Destination SQLite database
    migrate_user_data(source_file, db_file)
