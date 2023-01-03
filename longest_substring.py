

class Solution:
    def longest_substrnig(self, a: str):
        if len(a) == 0:
            return 0
        res = []
        end = len(a)
        for i in range(end):
            s = a[i]
            start =  i + 1
            stop =  False
            while start < end and not stop:
                   if a[start] in s :
                        stop = True
                   else:
                        s += a[start]
                        start += 1
            res.append(len(s))

        return max(res)

s = Solution()
# print(s.longest_substrnig('abcabcbb'))
#result:3
# print(s.longest_substrnig('bbbbb'))
#result:1
# print(s.longest_substrnig('pwwkew'))
#result:3

