import re

sum = 0


def mul(x, y):
    global sum
    sum += x * y


with open('input.txt', 'r') as file:
    string = file.read()
    multiplies = re.findall(r"mul\(\d+,\d+\)", string)

    for i in multiplies:
        exec(i)

print(sum)
