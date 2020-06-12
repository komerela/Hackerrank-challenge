class Solution:
    def isHappy(self, n: int) -> bool:
        a = b = n
        # Using Floyd's cycle-finding algorithm
        while (1):
            a = (sum([int(x)**2 for x in str(a)]))
            b = (sum([int(x)**2 for x in str(b)]))
            b = (sum([int(x)**2 for x in str(b)]))
            if (a == 1 or b == 1):
                return True
            if (a == b):
                return False