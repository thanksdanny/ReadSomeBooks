import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(2, nums))
print(heapq.nsmallest(5, nums))