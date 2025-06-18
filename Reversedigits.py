class Solution:
    def reverseDigits(self, n):
        return int(str(n)[::-1])

# input ouput code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    sol = Solution()
    result = sol.reverseDigits(n)
    print("Reversed number:", result)
