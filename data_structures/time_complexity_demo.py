import time

nums = list(range(1000000))

start = time.time()
total = sum(nums)
end = time.time()

print("Time taken:", end - start)
