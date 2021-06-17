def read_file(file: str):
    if isinstance(file, str):
        try:
            f = open(file, 'r')
            tmp = f.read()

            print(f'File "{file}" has the following message:')
            print(tmp)
            f.close()
        except FileNotFoundError:
            print(f'Failed to read file "{file}".')
        except PermissionError:
            print(f'Failed to read file "{file}".')
