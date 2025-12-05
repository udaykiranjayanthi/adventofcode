

banksInput = """
Input in input.txt
"""

banks = banksInput.strip().split("\n")

ans = 0

def rec(bank, start, length, n):
    maxInd = start
    for i in range(start+1, n-length+1):
        if(bank[i] > bank[maxInd]):
            maxInd = i
    
    # print(length, maxInd)
    if(length == 1):
        return bank[maxInd]
    
    return bank[maxInd] + rec(bank, maxInd+1, length-1, n)

for bank in banks:
    n = len(bank)
    maxJoltage = int(rec(bank, 0, 12, n))
    
    ans += maxJoltage
    
print("ans", ans)