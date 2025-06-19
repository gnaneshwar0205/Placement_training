from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the numbers (only 0, 1, 2) separated by space: ").split()))

Solution().sortColors(nums)

print("Sorted colors:", nums)
