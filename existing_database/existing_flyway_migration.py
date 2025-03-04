import subprocess
import sqlite3


def create_baseline():
    result = subprocess.run(["flyway", "baseline", "-configFiles=flyway.conf",
                             "-baselineVersion=1.0", "-baselineDescription=\"Initial schema\""],
                            capture_output=True, text=True)
    if result.returncode == 0:
        print("flyway baseline applied successfully.")
    else:
        print(f"Error applying baseline: {result.stderr}")


def run_flyway_migrations():
    result = subprocess.run(["flyway", "-configFiles=flyway.conf", "migrate"], capture_output=True,
                            text=True)
    if result.returncode == 0:
        print("Migrations applied successfully.")
    else:
        print(f"Error applying migrations: {result.stderr}")


def check_database():
    connection = sqlite3.connect('existing_flyway.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)
    connection.close()


def clean_up_database_to_initial_stage():
    try:
        conn = sqlite3.connect('existing_flyway.db')
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS flyway_schema_history;")
        cursor.execute("DROP TABLE IF EXISTS SCHOOL;")
        cursor.execute("DROP TABLE IF EXISTS BOOKS;")
        cursor.execute("DROP TABLE IF EXISTS TEST;")
        conn.commit()

        print("Successfully deleted 'flyway_schema_history' table.")

    except sqlite3.Error as e:
        print(f"Error occurred while deleting 'flyway_schema_history': {e}")
    finally:
        if conn:
            conn.close()


def init_setup():
    clean_up_database_to_initial_stage()
    check_database()


def create_baseline_and_migrate():
    create_baseline()  # create baseline
    run_flyway_migrations()  # Run the migrations
    check_database()


if __name__ == "__main__":
    init_setup()
    create_baseline_and_migrate()
