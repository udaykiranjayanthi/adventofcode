# inputData = """
# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# """ 

with open('input.txt', 'r') as file:
    inputData = file.read()

def splitRow(row):
    arr = list(filter(lambda x: x != "", map(lambda x: x.strip(), row.split(" "))))
    return arr

data = list(map(splitRow, inputData.strip().split("\n")))
m = len(data)
n = len(data[0])
ans = 0

for i in range(n):
    op = data[m-1][i]
    res = 0 if op == '+' else 1

    for j in range(m-2, -1, -1):
        if(op == "+"):
            res += int(data[j][i])
        else:
            res *= int(data[j][i])
    
    ans += res

print("ans", ans)