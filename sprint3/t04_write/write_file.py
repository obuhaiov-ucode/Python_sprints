import re

def write_file(file: str, mess = None):
    if re.match(r'[\w\-]+\.txt$', file):
        try:
            with open(file, 'w') as f_obj:
                if mess is not None:
                    f_obj.write(mess)
            with open(file, 'r') as f_obj:
                tmp = f_obj.read()
                if tmp != mess and not mess is None:
                    print('Something went wrong...')
                else:
                    print(f'Your message has been written to file "{file}".')
                    print(f'File "{file}" now contains the following text:')
                    print(mess)
        except FileNotFoundError:
            print('Something went wrong...')
    else:
        print('Please enter the filename in the format "filename.txt".')
        print(f'Failed to write to file "{file}".')
