matrix = [[0,0,0],[0,0,0],[0,0,0]]

matrix[0][1] = 2
matrix[1][2] = 2

print(matrix)

cells = []

for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
        if cell == 2:
            cells.append([y, x])
            row[x] = 0

for i, cell in enumerate(cells):
    matrix[cells[i][0] + 1][cells[i][1]] = 2

print(matrix)