from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store value:index
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index

# Taking input from user
nums = list(map(int, input("Enter the numbers (space separated): ").split()))
target = int(input("Enter the target: "))

# Creating object and calling the function
solution = Solution()
result = solution.twoSum(nums, target)

# Printing result
print("Output:", result)
