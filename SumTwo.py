4. Two Sum
nums = [2, 7, 11, 15]
target = 9
d = {}

for i, n in enumerate(nums):
    if target - n in d:
        print(d[target - n], i)
    d[n] = i
