class Solution:
    def bitwiseComplement(self, N: int) -> int:
        x = ""
        for c in bin(N)[2:]:
            x += '1' if c is '0' else '0'
        return int(x, 2)