
class Solution:
    def titleToNumber(self, columnTitle):
        result = 0
        for i in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[i]) - ord('A') + 1

        return result



s = Solution()
print(s.titleToNumber('A'))
print(s.titleToNumber('AA'))
print(s.titleToNumber('AVC'))


# A-1, Z-26
# AA-27=26 + 1, AB= 28 = 26 +2 AZ = 1*26 + 26 = 2*26
# BA = 2*26 + 1  , ZZ = 26*26 + 26
# AAA - 1*26*26 + 1*26 + 1
# AAB = 1*26*26 + 1*26 + 2
# ABA = 1*26*26 + 2*26 +