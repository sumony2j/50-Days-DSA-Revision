'''
Question 2: Combinations Sum 1 :-
 Given an array of distinct integers candidates and a target integer target, 
 return a list of all unique combinations of candidates where the chosen numbers sum to target. 
 You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency

of at least one of the chosen numbers is different.
'''

def combination_sum(arr,target):
    res = []
    def helper(index,com,com_sum):
        if com_sum>target:
            return
        if com_sum==target:
            res.append(com.copy())
            return
        for i in range(index,len(arr)):
            com.append(arr[i])
            helper(i,com,com_sum+arr[i])
            com.pop()
    helper(0,[],0)
    return res

## Test

print(combination_sum([2,3,4,7],7))