class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([c in J for c in S])
        """
        Without list comprehension solution
        
        count = 0
        for c in S:
            if c in J:
                count += 1
        return count
        """