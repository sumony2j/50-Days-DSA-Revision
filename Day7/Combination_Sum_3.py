'''
Question 2: Combinations Sum 3 :-
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

•Only numbers 1 through 9 are used.

•Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.
'''

def combination_sum(k,n):
    res = []
    def helper(index,com,com_sum):
        if com_sum == n and len(com) == k:
            res.append(com[:])
            return
        if com_sum > n or len(com) > k:
            return
        for i in range(index,10):
            com.append(i)
            helper(i+1,com,com_sum+i)
            com.pop()
    helper(1,[],0)
    return res

## Test

print(combination_sum(3,9))