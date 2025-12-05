# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

pointer = 50
# 0 - 99
zeroCount = 0

input = """
Input in input.txt
"""

for rot in input.strip().split("\n"):
    direction = rot[0]
    distance = int(rot[1:])

    if(direction == "L"):
        pointer = (pointer-distance)%100
    else:
        pointer = (pointer+distance)%100
    
    if(pointer == 0):
        zeroCount += 1
    # print(rot, "=>", pointer)

print("ans", zeroCount)
