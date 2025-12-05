# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

inputGrid = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

matrix = list(map(list, inputGrid.strip().split("\n")))

m = len(matrix)
n = len(matrix[0])

ans = 0

while(True):
    positions = []
    for i in range(m):
        for j in range(n):
            if(matrix[i][j] != "@"):
                continue
            count = 0
            if(i > 0 and matrix[i-1][j] == "@"):
                count += 1
            if(i < m-1 and matrix[i+1][j] == "@"):
                count += 1
            if(j > 0 and matrix[i][j-1] == "@"):
                count += 1
            if(j < n-1 and matrix[i][j+1] == "@"):
                count += 1
            if(i > 0 and j > 0 and matrix[i-1][j-1] == "@"):
                count += 1
            if(i > 0 and j < n-1 and matrix[i-1][j+1] == "@"):
                count += 1
            if(i < m-1 and j > 0 and matrix[i+1][j-1] == "@"):
                count += 1
            if(i < m-1 and j < n-1 and matrix[i+1][j+1] == "@"):
                count += 1
            
            if(count < 4):
                positions.append((i,j))
                # print(i,j, count)
                ans += 1
    
    if(len(positions) == 0):
        break
    for (i,j) in positions:
        matrix[i][j] = "x"

# for row in matrix:
#     print(row)

print("ans", ans)










