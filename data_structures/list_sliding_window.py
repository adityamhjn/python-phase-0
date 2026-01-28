nums = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0
window_sum = sum(nums[:k])

for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i - k]
    max_sum = max(max_sum, window_sum)

print("Maximum window sum:", max_sum)
