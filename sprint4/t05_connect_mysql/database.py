from mysql.connector import connect, Error
import yaml

if __name__ == "__main__":
    with open("cfg.yaml", 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)
    try:
        with connect(
                host=config.get('settings').get('host'),
                user=config.get('settings').get('user'),
                password=config.get('settings').get('password')
        ) as connection:
            print("Connected to MySQL server (version 8.0.25).")
        print("MySQL connection is closed.")
    except Error as e:
        print(e)
