import json

def make_eq(a, b, c) -> str:
    get_minus = lambda n: '' if n != -1 else '-'
    get_plus = lambda n: '' if n <= 0 else '+'
    get_num = lambda n: '' if (n == 1 or n == -1 or n == 0) else str(n)

    if a == 1 or a == -1:
        res = get_minus(a) + 'x^2'
    else:
        res = str(a) + 'x^2'
    if b != 0:
        res += get_minus(b) + get_plus(b) + get_num(b) + 'x'
    if c != 0:
        res += get_plus(c) + str(c)
    return res + '=0'

def quad(a, b, c):
    if all(isinstance(i, (int, float)) for i in [a, b, c]) and a != 0:
        discr = (b * b) - (4 * a * c)
        res = {"equation": make_eq(a, b, c),
               "solution": {
                   "discriminant": round(float(discr), 3),
                   "x": None}}

        if discr == 0:
            tmp = float((b / (2 * a)) * -1)
            if round(tmp) == 0.0:
                res["solution"]["x"] = 0.0
            else:
                res["solution"]["x"] = round(tmp, 3)
        elif discr > 0:
            x1 = ((b * -1) - (((b * b) - (4 * a * c)) ** (0.5))) / (2 * a)
            x2 = ((b * -1) + (((b * b) - (4 * a * c)) ** (0.5))) / (2 * a)
            res["solution"]["x"] = list([round(x1, 3), round(x2, 3)])
        return json.dumps(res, indent=3)
    return 'Cannot generate a quadratic equation.'
