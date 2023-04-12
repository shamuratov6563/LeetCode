class Solution:
    def isHappy(self, n: int) -> bool:
        result = False
        circle = 1
        while True:
            if circle == 10:
                result = False
                break
            a = 0
            for i in range(len(str(n))):
                a += int(str(n)[i]) ** 2
            n = a
            if n == 1:
                result = True
                break
            circle += 1

        return result


s = Solution()
# print(s.isHappy(19)) ---->>>1 True
# print(s.isHappy(2)) ---->>>1 False