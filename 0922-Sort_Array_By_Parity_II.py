class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1             
        while j < len(A):                          
            if A[j] % 2:
                j += 2                  
            else:
                A[j], A[i] = A[i], A[j]     
                i += 2                        
        return A