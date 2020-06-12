class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for c in S:
            if stack and c is ')' and stack[-1] is '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)