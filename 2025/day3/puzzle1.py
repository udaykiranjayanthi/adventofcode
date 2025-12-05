
banksInput = """
Input in input.txt
"""

banks = banksInput.strip().split("\n")

ans = 0

for bank in banks:
    n = len(bank)
    maxInd = 0
    for i in range(n-1):
        if(bank[i] > bank[maxInd]):
            maxInd = i
    
    maxInd2 = maxInd+1
    for i in range(maxInd+1, n):
        if(bank[i] > bank[maxInd2]):
            maxInd2 = i
            
    maxJoltage = int(bank[maxInd] + bank[maxInd2])
    # print(maxJoltage)
    ans += maxJoltage
    
print("ans", ans)