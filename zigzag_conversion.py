class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = []
        a = numRows
        s = list(s)[::-1]
        string = ""
        # PAYPALISHIRING 3
        while s:
            for i in range(numRows, 0, -1):
                if (a == i or a == 1 or a == numRows) and s:
                    string += s.pop()
                else:
                    if s:
                        string += s.pop() + "1"

            l.append(string)

            string = ""
            a -= 1
        print(l)
        return  ""


# ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = [''] * numRows
        index, step = 0, 1
        for x in s:
            l[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(l)