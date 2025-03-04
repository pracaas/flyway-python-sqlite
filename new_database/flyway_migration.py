import subprocess
import sqlite3


# Function to run Flyway migration

def run_flyway_migrations():
    result = subprocess.run(["flyway", "-configFiles=new_database/flyway.conf", "migrate"], capture_output=True,
                            text=True)
    if result.returncode == 0:
        print("Migrations applied successfully.")
    else:
        print(f"Error applying migrations: {result.stderr}")


# Function to interact with the SQLite database using Python
def check_database():
    connection = sqlite3.connect('new_database/new_flyway.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)
    connection.close()


def clean_up_database_to_initial_stage():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('new_database/new_flyway.db')
        cursor = conn.cursor()

        # Delete the 'flyway_schema_history' table if it exists
        cursor.execute("DROP TABLE IF EXISTS flyway_schema_history;")
        cursor.execute("DROP TABLE IF EXISTS USER;")
        cursor.execute("DROP TABLE IF EXISTS PERMISSION;")
        conn.commit()

        print("Successfully deleted all tables.")

    except sqlite3.Error as e:
        print(f"Error occurred while deleting all tables: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()


def init_setup():
    clean_up_database_to_initial_stage()
    check_database()


def start_flyway_migration():
    run_flyway_migrations()  # Run the migrations
    check_database()


if __name__ == "__main__":
    init_setup()
    start_flyway_migration()
