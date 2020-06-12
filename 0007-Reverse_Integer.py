def reverse(self, x: int) -> int:
    negFlag = False
    rev = 0
    if (x < 0):
        negFlag = True
        x = -x
    while (x):
        digit = x % 10
        rev = rev * 10 + digit
        if (rev > 2147483647):
            return 0
        x = x // 10
    if (negFlag):
        rev = -rev
    return rev