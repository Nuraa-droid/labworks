import psycopg2
from psycopg2 import extras
import csv


def connect():
    try:
        return psycopg2.connect(
            host="localhost",
            dbname="lab11",
            user="postgres",
            password="nurai2007",
            port=5432
        )
    except Exception as error:
        print("Connection error:", error)
        return None

def create_table_and_functions():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(15)
        );
        """,
        """
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'user_type') THEN
                CREATE TYPE user_type AS (
                    first_name VARCHAR,
                    last_name VARCHAR,
                    phone_number VARCHAR
                );
            END IF;
        END
        $$;
        """,
        """
        CREATE OR REPLACE FUNCTION search_phonebook2(pattern TEXT) 
        RETURNS TABLE(id INT, first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR) 
        AS $$
        BEGIN
            RETURN QUERY
            SELECT p.id, p.first_name, p.last_name, p.phone_number
            FROM phonebook2 p
            WHERE p.first_name ILIKE '%' || pattern || '%'
                OR p.last_name ILIKE '%' || pattern || '%'
                OR p.phone_number ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;

        """,
        """
        CREATE OR REPLACE PROCEDURE insert_or_update_user(
            p_first_name VARCHAR, 
            p_last_name VARCHAR, 
            p_phone_number VARCHAR
        ) 
        AS $$
        BEGIN
            IF EXISTS (
                SELECT 1 FROM phonebook2
                WHERE first_name = p_first_name AND last_name = p_last_name
            ) THEN
                UPDATE phonebook2
                SET phone_number = p_phone_number
                WHERE first_name = p_first_name AND last_name = p_last_name;
            ELSE
                INSERT INTO phonebook2(first_name, last_name, phone_number)
                VALUES (p_first_name, p_last_name, p_phone_number);
            END IF;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE FUNCTION insert_many_users(users user_type[])
        RETURNS TABLE(bad_first VARCHAR, bad_last VARCHAR, bad_phone VARCHAR)
        AS $$
        DECLARE
            u user_type;
        BEGIN
            FOREACH u IN ARRAY users LOOP
                IF u.phone_number ~ '^[0-9]{11}$' THEN
                    INSERT INTO phonebook2(first_name, last_name, phone_number)
                    VALUES (u.first_name, u.last_name, u.phone_number);
                ELSE
                    RETURN QUERY SELECT u.first_name, u.last_name, u.phone_number;
                END IF;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
        """
    ]
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            for cmd in commands:
                cur.execute(cmd)
    print("Table and procedures succesfully created")

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
                            "INSERT INTO phonebook2 (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                            (row[0], row[1], row[2])
                        )
    except Exception as e:
        print(f"Error inserting from CSV: {e}")

def insert_or_update_user():
    first = input("first_name: ")
    last = input("last_name: ")
    phone = input("phone_number: ")

    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s, %s)", (first, last, phone))
            print("user inserted or updated")

def insert_many_users():
    print("insert list of users")
    count = int(input("number of users: "))
    users = []

    for i in range(count):
        print(f"user #{i+1}:")
        first = input("first_name: ")
        last = input("last_name: ")
        phone = input("phone_number: ")
        users.append((first, last, phone))

    conn = connect()
    with conn:
        with conn.cursor() as cur:
            user_array = [(first, last, phone) for first, last, phone in users]
            cur.execute("SELECT * FROM insert_many_users(%s::user_type[])", (user_array,))
            bad = cur.fetchall()

            if bad:
                print("some incorrect numbers not inserted:")
                for row in bad:
                    print(f"{row[0]} {row[1]}: {row[2]}")
            else:
                print("list of users inserted succesfully")


def search_pattern():
    pattern = input("enter part of name, lastname or phone: ")

    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook2(%s)", (pattern,))
            rows = cur.fetchall()
            if rows:
                print("results:")
                for row in rows:
                    print(f"{row[1]} {row[2]}: {row[3]}")
            else:
                print("nothing founded")

def delete_user():
    column = input("Enter the column to delete by (first_name, last_name, phone_number): ")
    value = input(f"Enter the value to delete by for {column}: ")
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"DELETE FROM phonebook2 WHERE {column} = %s",
                    (value,)
                )
                print("User data deleted succesfully")
    except Exception as e:
        print(f"Error deleting user: {e}")

def main():
    create_table_and_functions()

    while True:
        print("1 - insert from csv")
        print("2 - insert an user")
        print("3 - insert list of users")
        print("4 - search by pattern")
        print("5 - delete user")
        print("6 - exit")
        choice = input("choose an option: ")

        if choice == "1":
            insert_from_csv("phonebook.csv")
        elif choice == "2":
            insert_or_update_user()
        elif choice == "3":
            insert_many_users()
        elif choice == "4":
            search_pattern()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            print("goodbye")
            break

if __name__ == "__main__":
    main()
