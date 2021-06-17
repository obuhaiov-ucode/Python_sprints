from mysql.connector import connect, Error
import yaml
import sys

def get_table_rows(cursor, table):
    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    return cursor.fetchone()[0]

def get_table_cols(cursor, table):
    cursor.execute(f"SELECT COUNT(*) AS tmp "
                   f"FROM information_schema.columns "
                   f"WHERE table_name = '{table}';")
    return cursor.fetchone()[0]

def insert_rows(data, db, cursor, animal):
    try:
        cursor.execute(f"SELECT * FROM {data.get('table')};")
        columns = []
        for cd in cursor.description:
            columns.append(cd[0])
        for key, value in animal.items():
            if key not in columns and key != 'event':
                if isinstance(value, bool):
                    tmp = "BOOLEAN"
                elif isinstance(value, str):
                    tmp = "VARCHAR(300)"
                else:
                    tmp = "INTEGER"
                cursor.execute(f"ALTER TABLE {data.get('table')} "
                               f"ADD {key} {tmp} DEFAULT NULL;")
                db.commit()
                print(f"Column {key} added to table {data.get('table')}.")
    except Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')
            
def insert_animal(data, db, cursor, animal):
    try:
        before = get_table_rows(cursor, data.get('table'))
        cursor.execute(f"INSERT INTO {data.get('table')}(species, name) "
                       f"VALUES('{animal.get('species')}', '{animal.get('name')}');")
        db.commit()

        insert_rows(data, db, cursor, animal)

        for key, value in animal.items():
            if key != 'event' and key != 'name' and key != 'species':
                if isinstance(value, str):
                    cursor.execute(f"UPDATE {data.get('table')} "
                                   f"SET {key} = '{value}' "
                                   f"WHERE species = '{animal.get('species')}' "
                                   f"AND name = '{animal.get('name')}';")
                else:
                    cursor.execute(f"UPDATE {data.get('table')} "
                                   f"SET {key} = {value} "
                                   f"WHERE species = '{animal.get('species')}' "
                                   f"AND name = '{animal.get('name')}';")
                db.commit()

        after = get_table_rows(cursor, data.get('table'))
        if after != before:
            print(f"Inserted {animal.get('species')} {animal.get('name')}"
                  f" into table {data.get('table')} of {data.get('database')}.")
    except Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')

def update_animal(data, db, cursor, animal):
    try:
        insert_rows(data, db, cursor, animal)
        
        cursor.execute(f"SELECT 1 FROM {data.get('table')} "
                       f"WHERE species = '{animal.get('species')}' "
                       f"AND name = '{animal.get('name')}'")
        if cursor.fetchone():
            cursor.execute(f"UPDATE {data.get('table')} SET age = age + 1 "
                           f"WHERE species = '{animal.get('species')}' "
                           f"AND name = '{animal.get('name')}';")
            db.commit()
            print(f"Updated {animal.get('species')} {animal.get('name')}"
                  f" in table {data.get('table')} of {data.get('database')}.")
    except Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')

def delete_animal(data, db, cursor, animal):
    try:
        before = get_table_rows(cursor, data.get('table'))

        cursor.execute(f"DELETE FROM {data.get('table')} "
                       f"WHERE species = '{animal.get('species')}' "
                       f"AND name = '{animal.get('name')}';")
        db.commit()

        after = get_table_rows(cursor, data.get('table'))
        if after != before:
            print(f"Deleted {animal.get('species')} {animal.get('name')}"
                  f" from table {data.get('table')} of {data.get('database')}.")
    except Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')

def move_out_animal(data, db, cursor, animal):
    try:
        before = get_table_rows(cursor, data.get('table'))

        sql = f"DELETE FROM {data.get('table')} WHERE "
        for key, value in animal.items():
            if key != 'event':
                if isinstance(value, str):
                    sql += f"{key} = '{value}' AND "
                else:
                    sql += f"{key} = {value} AND "
        sql = sql[0:-5] + ";"
        cursor.execute(sql)
        db.commit()

        after = get_table_rows(cursor, data.get('table'))
        if after != before:
            print(f"Deleted {before-after} animals from table "
                  f"{data.get('table')} of {data.get('database')}.")
    except Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')

def print_table(data, cursor):
    print(f"Table animals: {get_table_rows(cursor, data.get('table'))} rows, "
          f"{get_table_cols(cursor, data.get('table'))} columns.")

    cursor.execute(f"SELECT * FROM {data.get('table')}")
    results = cursor.fetchall()
    columns = []
    widths = []
    rows = []
    separator = '+'
    
    for cd in cursor.description:
        columns.append(cd[0])
     
    for item in results:
        i = 0
        line = '| '
        for s in item:
            cursor.execute(f"SELECT DATA_TYPE "
                           f"FROM INFORMATION_SCHEMA.COLUMNS "
                           f"WHERE TABLE_NAME = '{data.get('table')}' "
                           f"AND COLUMN_NAME = '{columns[i]}'")
            type = cursor.fetchone()[0]
            if type == "int" and isinstance(s, int):
                sp = ' ' * (max((len(columns[i]) + 2), len(str(s))) - len(str(s)))
                line += sp + str(s) + ' | '
            elif type == "varchar" and isinstance(s, str):
                sp = ' ' * (max((len(columns[i]) + 3), (len(str(s)) + 1)) - len(str(s)))
                line += str(s) + sp + '| '
            elif type == "tinyint" and isinstance(s, int):
                if s:
                    tmp = 'True'
                else:
                    tmp = 'False'
                sp = ' ' * (max((len(columns[i]) + 3), (len(str(tmp)) + 1)) - len(str(tmp)))
                line += tmp + sp + '| '
            else:
                sp = ' ' * max((len(columns[i]) + 3), (len(str(s)) + 1))
                line += sp + '| '
            i += 1
        rows.append(line[0:-1])

    if rows:
        lst = rows[0].split('|')
        for u in lst:
            if u:
                widths.append(len(u))
    else:
        for col in columns:
            widths.append(len(col) + 4)
    
    columns_line = '| '
    for i in range(len(columns)):
        separator += '-' * widths[i] + '+'
        cursor.execute(f"SELECT DATA_TYPE "
                       f"FROM INFORMATION_SCHEMA.COLUMNS "
                       f"WHERE TABLE_NAME = '{data.get('table')}' "
                       f"AND COLUMN_NAME = '{columns[i]}'")
        type = cursor.fetchone()[0]
        if type == "int" and results:
            sp = ' ' * (widths[i] - len(columns[i]) - 2)
            columns_line += sp + columns[i] + ' | '
        else:
            sp = ' ' * (widths[i] - len(columns[i]) - 1)
            columns_line += columns[i] + sp + '| '
    columns_line = columns_line[0:-1]     
    
    print(separator)
    print(columns_line)
    print("|" + separator[1:-1] + "|")
    for r in rows:
        print(r)
    print(separator)

def update_zoo(data: dict):
    if isinstance(data, dict) \
            and ['database', 'table', 'news'] == list(data.keys()):
        with open("cfg.yaml", 'r') as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
        try:
            print(f"Connected to MySQL server (version 8.0.25).")
            with connect(
                    host=config.get('settings').get('host'),
                    user=config.get('settings').get('user'),
                    password=config.get('settings').get('password')
            ) as connection:
                print(f"Using database '{data.get('database')}'.")

                cursor = connection.cursor(buffered=True)
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {data.get('database')};")
                cursor.execute(f"USE {data.get('database')};")
                connection.commit()
                
                cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {data.get('table')}(
                                    species VARCHAR(100) NOT NULL, 
                                    name VARCHAR(100) NOT NULL, 
                                    age INT UNSIGNED DEFAULT 0, 
                                    primary key (species, name)
                                )
                            ''')
                connection.commit()

                print_table(data, cursor)
                
                for animal in data.get("news"):
                    if animal.get('event') == 'born' or animal.get('event') == 'moved in':
                        insert_animal(data, connection, cursor, animal)
                    elif animal.get('event') == 'birthday':
                        update_animal(data, connection, cursor, animal)
                    elif animal.get('event') == 'died':
                        delete_animal(data, connection, cursor, animal)
                    elif animal.get('event') == 'moved out':
                        move_out_animal(data, connection, cursor, animal)

                print_table(data, cursor)

                if get_table_rows(cursor, data.get('table')) == 0:
                    cursor.execute(f"DROP TABLE {data.get('table')};")
                    connection.commit()
                    print(f"Table {data.get('table')} is dropped.")

            print("MySQL connection is closed.")
        except Error as e:
            print(f"MySQL connection Error: {e}")
