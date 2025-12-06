# inputData = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """ 

with open('input.txt', 'r') as file:
    inputData = file.read()

data = inputData.split("\n")
m = len(data)
ans = 0

prev = 0
for i in range(1, len(data[m-1])+1):
    start = None
    end = None
    if(i == len(data[m-1])):
        start = prev
        end = i
    elif(data[m-1][i] != " "):
        start = prev
        end = i-1
        prev = i
    
    if(start != None and end != None):
        # found a the length of numbers
        operator = data[m-1][start]
        res = 0 if operator == '+' else 1

        for c in range(start, end):
            # create number by combining all digits in same column from all rows
            num = ""
            for r in range(m-1):
                num += data[r][c]

            if(operator == '+'):
                res += int(num)
            else:
                res *= int(num)
        
        ans += res

print("ans", ans)
