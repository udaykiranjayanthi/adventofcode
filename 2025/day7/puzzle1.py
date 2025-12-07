# inputData = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............
# """

with open('input.txt', 'r') as file:
    inputData = file.read()

data = list(map(list, inputData.strip().split("\n")))
m = len(data)
n = len(data[0])

def printData(data):
    for r in data:
        print("".join(r))

def dfs(i, j):
    if(i == m):
        return 0

    result = 0

    if(data[i][j] == "."):
        data[i][j] = "|"
        result = dfs(i+1, j)
    elif(data[i][j] == "^"):
        data[i][j-1] = "|"
        data[i][j+1] = "|"
        result = 1
        result += dfs(i+1, j-1)
        result += dfs(i+1, j+1)
    
    return result


# finding S
for j in range(n):
    if(data[0][j] == "S"):
        # print("start at: ", data[0][j])
        print(dfs(1, j))
        break