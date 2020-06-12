class Solution:
    def romanToInt(self, s: str) -> int:
        
        def rconvert(r):
            if (r == 'I'):
                return 1
            if (r == 'V'):  
                return 5
            if (r == 'X'):
                return 10
            if (r == 'L'):
                return 50
            if (r == 'C'):
                return 100
            if (r == 'D'):
                return 500
            if (r == 'M'):
                return 1000
            return 0
        
        if type(s) is not str or s is None:
            return 0
        result = 0
        rlen = len(s)
        for i in range(rlen):
            vcurrent = rconvert(s[i])
            if (i < rlen - 1):
                vnext = rconvert(s[i+1])
                result += vcurrent if vcurrent >= vnext else -vcurrent
            else:
                result += vcurrent
        return result