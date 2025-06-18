from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    
n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the numbers (space separated): ").split()))

sol = Solution()
print("The single number is:", sol.singleNumber(nums))