5. Kadane’s Algorithm (Maximum Subarray Sum)
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = curr = arr[0]

for i in arr[1:]:
    curr = max(i, curr + i)
    max_sum = max(max_sum, curr)

print(max_sum)
