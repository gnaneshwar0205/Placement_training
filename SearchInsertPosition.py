def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Input section
n = int(input("Enter the number of elements in the sorted array: "))
nums = list(map(int, input("Enter the elements (sorted): ").split()))
target = int(input("Enter the target number: "))

# Function call and output
index = search_insert(nums, target)
print("Target should be at index:", index)
