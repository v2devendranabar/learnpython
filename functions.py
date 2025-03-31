import sys

def add(a,b):
    result = a + b
    return result

def sub(a,b):
    return a - b

def mul(a,b):
    result = a * b
    return result

a = float(sys.argv[1])
operator = sys.argv[2]
b = float(sys.argv[3])

if operator == 'add':
    output = add(a,b)
    print(output)

# print(add(10,5))
# print(sub(10,5))
# print(mul(10,5))