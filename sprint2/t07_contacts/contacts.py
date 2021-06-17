import re

def valid_operation(oper: str) -> bool:
    if oper == 'add' or oper == 'delete' or oper == 'update':
        return True
    return False

def valid_info(dct: dict) -> bool:
    for key in dct:
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        tmp = str(dct[key])

        if key == 'name' and not re.match(r"[\w\s]+", tmp):
            return False
        elif key == 'email' and not re.match(email_pattern, tmp):
            return False
        elif not dct.get('name') or not dct.get('email'):
            return False
    return True


def contacts(container: dict, info: dict, operation: str) -> bool:
    if valid_operation(operation) and valid_info(info)\
            and isinstance(container, dict) and isinstance(info, dict):
        new_key = info.pop('email')

        if operation == 'add':
            container.update({new_key: info})
        if operation == 'update' or operation == 'delete':
            if not container.get(new_key):
                return False
            if operation == 'update':
                container.get(new_key).update(info)
            if operation == 'delete':
                container.pop(new_key)
        return True
    return False
