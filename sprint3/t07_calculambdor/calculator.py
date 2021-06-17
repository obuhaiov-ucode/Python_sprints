def valid_oper(oper: str) -> bool:
    if isinstance(oper, str):
        if oper == 'add' or oper == 'sub' or oper == 'mul'\
                or oper == 'div' or oper == 'pow':
            return True
    e = 'Invalid operation. Available operations: add, sub, mul, div, pow.'
    raise ValueError(e)

def valid_nums(n, m) -> bool:
    if isinstance(n, (int, float)) and isinstance(m, (int, float)):
        return True
    e = 'Invalid numbers. Second and third arguments must be numerical.'
    raise ValueError(e)

def create_dict() -> dict:
    res_dict = {}
    keys = ('add', 'sub', 'mul', 'div', 'pow')
    values = (lambda n, m: n + m,
              lambda n, m: n - m,
              lambda n, m: n * m,
              lambda n, m: n / m,
              lambda n, m: n ** m)
    i = 0

    while i < 5:
        res_dict.update({keys[i]: values[i]})
        i += 1
    return res_dict

operations = create_dict()

def calculator(oper: str, n, m):
    if valid_oper(oper) and valid_nums(n, m):
        return operations.get(oper)(n, m)
