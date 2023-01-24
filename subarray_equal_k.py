

class Solution:
    def subarraySum(self, nums: list, k: int):
        sumdict = {0:1}
        count = 0
        s = 0
        for num in nums:
            s += num
            if s-k in sumdict:
                count += sumdict[s-k]
            if s in sumdict:
                sumdict[s] += 1
            else:
                sumdict[s] = 1

        return count


s = Solution()
print(s.subarraySum([3,4, 7, 2, -3, 1, 4, 2], 7))