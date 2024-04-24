'''
Question 1: Combinations :- 
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
'''


def combination(k,n):
    res = []
    def helper(index,com=[]):
        if len(com) == k:
            res.append(com.copy())
            return
        need = k-len(com)
        for i in range(index,n-(need-1)+1):
            com.append(i)
            helper(i+1,com)
            com.pop()
    helper(1,[])
    return res


## Test

print(combination(2,4))

