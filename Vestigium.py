testcases = int(input())
matricies = []
for i in range(testcases):
    size = int(input())
    lines = []
    for j in range(size):
        line = input()
        lines.append([])
        for num in line.split(" "):
            lines[j].append(int(num))
    matricies.append(lines)

for i in range(len(matricies)):
    duprow = 0
    dupcol = 0
    trace = 0
    for j in range(len(matricies[i])):

        column = []
        for k in range(len(matricies[i])):
            column.append(matricies[i][k][j])
        columnset = set(column)
        if len(columnset) != len(column):
            dupcol += 1

        trace += matricies[i][j][j]
        row = set(matricies[i][j])
        if len(row) != len(matricies[i][j]):
            duprow += 1
    print(f"Case #{i+1}: {trace} {duprow} {dupcol}")

    