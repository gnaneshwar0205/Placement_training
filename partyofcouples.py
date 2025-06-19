class Solution:
    def findSingle(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter the numbers separated by space: ").split()))
    obj = Solution()
    print("Single person in party:", obj.findSingle(arr))
