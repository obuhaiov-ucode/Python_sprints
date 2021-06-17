n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

result = (lambda r: True if (n % a == 0 and n % b == 0) else False)(bool)

print(result)
