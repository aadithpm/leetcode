class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        if not A or (len(A) == 1):
            return [int(i) for i in str(K + A[0])]
        if K == 0:
            return A

        k = K
        stack = []
        res = []
        carry = 0
        
        while A or k > 0:
            add = (k % 10) + carry
            add += A.pop() if A else 0
            carry = add // 10
            rem = add % 10
            
            stack.append(rem)
            
            k //= 10
        
        while A:
            stack.append(A.pop())
        
        if carry > 0:
            stack.append(carry)
            
        while stack:
            res.append(stack.pop())
        
        return res
