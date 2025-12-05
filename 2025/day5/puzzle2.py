inputData = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


[ranges, ingredients] = inputData.strip().split("\n\n")

ranges = list(map(lambda x: list(map(int, x.split("-"))), ranges.split("\n")))

ranges.sort()

count = 0
prevEnd = 0

for i in range(len(ranges)):
    [start, end] = ranges[i]
    
    if(i == 0 or ranges[i][0] > prevEnd):
        count += (end - start +1)
    elif(end > prevEnd):
        count += (end - prevEnd)
    
    prevEnd = max(prevEnd, end)
    print(start, end, count)
        

print("count", count)

