class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        b = (sorted(A, reverse = True))
        for i in range(len(b) - 2):
            if (b[i] < (b[i+1] + b[i+2])):
                return sum(b[i:i+3])
        return 0