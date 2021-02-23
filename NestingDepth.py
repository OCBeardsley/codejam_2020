inputs = int(input())
outputs = []
for i in range(inputs):
    line = input()
    openedbrackets = 0
    output = ''
    for digit in line:
        brackets = int(digit)-openedbrackets
        if brackets == 0:
            pass
        elif brackets > 0:
            output += '(' * brackets
        elif brackets < 0:
            output += ')' * (brackets * -1)
        openedbrackets += brackets
        output += digit
    output += ')' * (openedbrackets)
    outputs.append(f"Case #{i+1}: {output}")

for output in outputs:
    print(output)
