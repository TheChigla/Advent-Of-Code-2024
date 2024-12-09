import re

sum = 0

with open('input.txt', 'r') as file:
    text = file.read()
    modes = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", text)
    mode_on = True

    for mode in modes:
        if mode == 'do()':
            mode_on = True
        elif mode == "don't()":
            mode_on = False
        elif mode_on and mode.startswith('mul('):
            x, y = map(int, re.findall(r'\d+', mode))
            sum += x * y

print(sum)
