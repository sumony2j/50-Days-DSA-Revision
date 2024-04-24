'''
Question 1: Subsets :- 
Given an integer array of unique elements, return all possible subsets (the power set). 
The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subsets(arr):
    size = len(arr)
    index = 0
    res = []
    def calculate(index,subs):
        if index == size:
            res.append(subs.copy())
            return
        calculate(index+1,subs)
        subs.append(arr[index])
        calculate(index+1,subs)
        subs.pop()
    calculate(0,[])
    return res

## Test

print(subsets([1,2]))