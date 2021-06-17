import sqlite3

def insert_animal(data, db, cursor, animal):
    try:
        cursor.execute(f"SELECT COUNT (*) FROM {data.get('table')}")
        before = cursor.fetchone()[0]
        tmp = f'''
            INSERT INTO {data.get('table')}(species, name) 
            VALUES('{animal.get('species')}', '{animal.get('name')}');
        '''
        cursor.execute(tmp)
        db.commit()
        cursor.execute(f"SELECT COUNT (*) FROM {data.get('table')}")
        after = cursor.fetchone()[0]
        if after != before:
            print(f"Inserted {animal.get('species')} {animal.get('name')}"
                  f" into table {data.get('table')} of {data.get('database')}.")
    except sqlite3.Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')

def delete_animal(data, db, cursor, animal):
    try:
        cursor.execute(f"SELECT COUNT (*) FROM {data.get('table')}")
        before = cursor.fetchone()[0]
        tmp = f'''
            DELETE FROM {data.get('table')} 
            WHERE species = '{animal.get('species')}' 
            AND name = '{animal.get('name')}';
        '''
        cursor.execute(tmp)
        db.commit()
        cursor.execute(f"SELECT COUNT (*) FROM {data.get('table')}")
        after = cursor.fetchone()[0]
        if after != before:
            print(f"Deleted {animal.get('species')} {animal.get('name')}"
                  f" from table {data.get('table')} of {data.get('database')}.")
    except sqlite3.Error as e:
        print(f'Failed to process event: {animal}. Error: {e}')

def update_animal(data, db, cursor, animal):
    cursor.execute(f"SELECT 1 FROM {data.get('table')} "
                   f"WHERE species = '{animal.get('species')}' "
                   f"AND name = '{animal.get('name')}'")
    if cursor.fetchone():
        try:
            tmp = f'''
                UPDATE {data.get('table')} SET age = age + 1 
                WHERE species = '{animal.get('species')}' 
                AND name = '{animal.get('name')}';
            '''
            cursor.execute(tmp)
            db.commit()
            print(f"Updated {animal.get('species')} {animal.get('name')}"
                  f" in table {data.get('table')} of {data.get('database')}.")
        except sqlite3.Error as e:
            print(f'Failed to process event: {animal}. Error: {e}')

def update_zoo(data: dict):
    if isinstance(data, dict) \
            and ['database', 'table', 'news'] == list(data.keys()):
        try:
            db = sqlite3.connect(data.get('database'))
            cursor = db.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {data.get('table')}(
                    species TEXT NOT NULL, 
                    name TEXT NOT NULL, 
                    age INTEGER DEFAULT 0, 
                    primary key (species, name)
                )
            ''')
            db.commit()

            cursor.execute(f"SELECT COUNT (*) FROM {data.get('table')}")
            print(f'*** BEFORE: {cursor.fetchone()[0]} animals in the zoo.')

            for animal in data.get("news"):
                if animal.get('event') == 'born':
                    insert_animal(data, db, cursor, animal)
                elif animal.get('event') == 'died':
                    delete_animal(data, db, cursor, animal)
                elif animal.get('event') == 'birthday':
                    update_animal(data, db, cursor, animal)

            cursor.execute(f"SELECT COUNT (*) FROM {data.get('table')}")
            print(f'*** AFTER: {cursor.fetchone()[0]} animals in the zoo.')

        except sqlite3.Error as e:
            print(e)
