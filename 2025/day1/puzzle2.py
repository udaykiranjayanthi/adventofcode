
pointer = 50
# 0 - 99
zeroStopCount = 0
zeroCount = 0

input = """
Input in input.txt
"""

for rot in input.strip().split("\n"):
    direction = rot[0]
    distance = int(rot[1:])
    
    # print()
    if(direction == "L"):
        pointer = (pointer-distance)
    else:
        pointer = (pointer+distance)
    
    count = 0
    if(pointer >= 100):
        count = pointer//100
    elif(pointer <= 0):
        count = 1 if abs(pointer) < distance else 0
        count += abs(pointer)//100

    zeroCount += count
    pointer = pointer%100
    
    if(pointer == 0):
        zeroStopCount += 1
    # print(rot, "=>", pointer, count)

print("ans", zeroStopCount, zeroCount)

