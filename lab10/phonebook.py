import psycopg2
import csv

def connect():
    try:
        conn = psycopg2.connect(
            host="localhost", 
            dbname = "lab10", 
            user = "postgres", 
            password = "nurai2007", 
            port = 5432
        )
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        return None
    
def create_table():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone_number VARCHAR(15)
        );
        """
    ]
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                for command in commands:
                    if command.strip():
                        print(f"Executing: {command}")
                        cur.execute(command)
                    else:
                        print("skipping empty command")
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_from_csv(csv_file):
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                with open(csv_file, 'r') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                            (row[0], row[1], row[2])
                        )
    except Exception as e:
        print(f"Error inserting from CSV: {e}")

def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (first_name, last_name, phone_number)
                )
                print("Data inserted succesfully!!")
    except Exception as e:
        print(f"Error inserting from console: {e}")

def update_user_data():
    user_id = input("Enter the user ID to update: ")
    column = input("Enter column to update (first_name, last_name, phone_number): ")
    new_value = input(f"Enter the new value for {column}: ")

    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"UPDATE phonebook SET {column} = %s WHERE id = %s",
                    (new_value, user_id)                  
                )
                print("User data updated succesfully")
    except Exception as e:
        print(f"Error updating user data: {e}")

def query_data():
    column = input("Enter the column to filter by (first_name, last_name, phone_number): ")
    value = input(f"Enter the value to filter by for {column}: ")

    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"SELECT * FROM phonebook WHERE {column} = %s",
                    (value,)
                )
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print(f"Error querying data: {e}")

def delete_user():
    column = input("Enter the column to delete by (first_name, last_name, phone_number): ")
    value = input(f"Enter the value to delete by for {column}: ")
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"DELETE FROM phonebook WHERE {column} = %s",
                    (value,)
                )
                print("User data deleted succesfully")
    except Exception as e:
        print(f"Error deleting user: {e}")

if __name__ == "__main__":
    create_table()
    choice = input("Choose an option to insert data (1 - CSV, 2 - Console): ")
    if choice == "1":
        insert_from_csv("phonebook.csv")
    elif choice == "2":
        insert_from_console()

    while True:
        print("\nSelect an option:")
        print("1. Update user data")
        print("2. Query phonebook data")
        print("3. Delete user")
        print("4. Exit")
        option = input("Enter your choice: ")

        if option == "1":
            update_user_data()
        elif option == "2":
            query_data()
        elif option == "3":
            delete_user()
        elif option == "4":
            break