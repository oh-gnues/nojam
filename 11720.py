# 11720 : 숫자의 합

# code for submitting
N = int(input())
nums = str(input())
sum = 0

for i in range(N):
    sum += int(nums[i])

print(sum)