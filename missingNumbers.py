def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the numbers (space separated): ").split()))

print("The missing number is:", missingNumber(nums))
