from mysql.connector import connect, Error
import yaml
import sys

if __name__ == "__main__" and \
        ((len(sys.argv) == 2 and (sys.argv[1] == 'databases' or sys.argv[1] == 'tables'))
         or (len(sys.argv) == 3 and (sys.argv[1] == 'create' or sys.argv[1] == 'drop'))):
    with open("cfg.yaml", 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)
    try:
        print(f"Connected to MySQL server (version 8.0.25), database"
              f" {config.get('settings').get('database')}.")
        with connect(
                host=config.get('settings').get('host'),
                user=config.get('settings').get('user'),
                password=config.get('settings').get('password'),
                database=config.get('settings').get('database')
        ) as connection:
            cursor = connection.cursor()
            if sys.argv[1] == 'databases' and len(sys.argv) == 2:
                cursor.execute("SHOW DATABASES;")
                lst = cursor.fetchall()
                print("Database list:")
                for db in lst:
                    print(f"        - {db[0]}")
            elif sys.argv[1] == 'tables' and len(sys.argv) == 2:
                if config.get('settings').get('database'):
                    cursor.execute("SHOW TABLES;")
                    lst = cursor.fetchall()
                    if lst:
                        print("Table list:")
                        for tb in lst:
                            print(f"        - {tb[0]}")
                    else:
                        print("No tables.")
                else:
                    print("Error: not connected to a database.")
            elif sys.argv[1] == 'create' and len(sys.argv) == 3:
                cursor.execute(f"CREATE DATABASE `{sys.argv[2]}`;")
                connection.commit()
                print(f"Database '{sys.argv[2]}' is created.")
            elif sys.argv[1] == 'drop' and len(sys.argv) == 3:
                cursor.execute(f"DROP DATABASE `{sys.argv[2]}`;")
                connection.commit()
                print(f"Database '{sys.argv[2]}' is dropped.")
            else:
                print("Error: command-line arguments are invalid.")
        print("MySQL connection is closed.")
    except Error as e:
        print(f"MySQL connection Error: {e}")
else:
    print("Error: command-line arguments are invalid.")
