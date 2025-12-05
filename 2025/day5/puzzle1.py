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
# print(ranges)
ingredients = list(map(int, ingredients.split("\n")))
# print(ingredients)

count = 0

for i in ingredients:
    for [low, high] in ranges:
        if(low <= i <= high):
            # print("match", i)
            count += 1
            break

print("count", count)
