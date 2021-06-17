import sqlite3
import re

def run_help():
    print("Available commands:")
    print("- help")
    print("- connect [database]")
    print("- close [database]")
    print('- execute [database] "[SQL statement]"')
    print("- show")
    print("- exit")

def run_connect(data: str):
    if data in connections.keys():
        print(f'Already connected to database "{data}".')
        return
    try:
        db = sqlite3.connect(data)
        connections.update({data: db})
        print(f'Created connection to database "{data}".')
    except sqlite3.Error as e:
        print(e)

def run_close(data: str):
    if data not in connections.keys():
        print(f'Cannot close connection to "{data}". Not connected.')
        return
    try:
        db = connections.pop(data)
        db.close()
        print(f'Closed connection to database "{data}".')
    except sqlite3.Error as e:
        print(e)

def run_execute(data: str, cmd: str):
    if data not in connections.keys():
        print(f'Cannot execute SQL statement. Not connected to "{data}".')
        return
    try:
        cur = connections.get(data).cursor()
        tmp = re.search(r'".+"$', cmd).group(0)[1:-1]
        cur.execute(tmp)
        connections.get(data).commit()
        print(f'Executed SQL statement.')
    except sqlite3.Error as e:
        print(e)

def run_show():
    if not connections:
        print(f'No connections.')
        return
    print("Connected to:")
    print(list(connections.keys()))

if __name__ == '__main__':
    connections = {}
    exit = False

    while not exit:
        cmd = input("Enter command: ")
        lst = cmd.split()

        if lst[0] == "help" and len(lst) == 1:
            run_help()
        elif lst[0] == "show" and len(lst) == 1:
            run_show()
        elif lst[0] == "exit" and len(lst) == 1:
            exit = True
        elif len(lst) > 1 and len(lst) > 1:
            if lst[0] == "connect" and len(lst) == 2:
                run_connect(lst[1])
            elif lst[0] == "close" and len(lst) == 2:
                run_close(lst[1])
            elif lst[0] == "execute" and re.search(r'".+"$', cmd):
                run_execute(lst[1], cmd)
            else:
                print('Invalid command. Try "help" to see available commands.')
        else:
            print('Invalid command. Try "help" to see available commands.')

    for db in connections.keys():
        print(f'Closed connection to database "{db}".')
