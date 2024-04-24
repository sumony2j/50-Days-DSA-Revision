'''
Question 1: Combinations Sum 2 :- 
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target. 
Each number in candidates may only be used once in the combination. 

Note: The solution set must not contain duplicate combinations.
'''

'''
Assumption :

1. Input array must be sorted.
'''

def combination_sum(arr,target):
    arr.sort()
    res = []
    def helper(index,com,com_sum):
        if com_sum == target:
            res.append(com[:])
            return
        if com_sum > target:
            return
        if index > len(arr)-1:
            return
        hash = {}
        for i in range(index,len(arr)):
            if arr[i] not in hash:
                hash[arr[i]]=True
                com.append(arr[i])
                helper(i+1,com,com_sum+arr[i])
                com.pop()
    helper(0,[],0)
    return res

## Test

print(combination_sum([1,3,3,5,2],7))
