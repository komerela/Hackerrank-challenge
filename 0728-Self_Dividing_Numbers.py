class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range (left, right + 1):
            flag = True
            for digit in str(i):
                if digit is "0" or i%int(digit) != 0:
                    flag = False
            if flag:
                output.append(i)
        return output