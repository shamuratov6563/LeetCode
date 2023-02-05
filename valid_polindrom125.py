class Solution:
    def isPalindrome(self, s: str):
        import re
        s = (re.sub(r'[^a-zA-Z0-9]', '',s)).lower()
        if len(s) % 2 == 0:
            middle = int(len(s)/2)
            left = s[:middle]
            right = s[middle:]
            right = right[::-1]
            return left == right
        else:
            middle = int(len(s)/2)
            left = s[:middle]
            right = s[middle+1:]
            right = right[::-1]
            return left == right
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
