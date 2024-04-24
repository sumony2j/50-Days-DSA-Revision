'''
Question 2: Subsets 2 :- 
Given an integer array nums that may contain duplicates, 
return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subset(arr):
    res = []
    def calculate(index,sub = []):
        if index == len(arr):
            res.append(sub.copy())
            return
        sub.append(arr[index])
        calculate(index+1,sub)
        sub.pop()
        while len(arr)-1 > index and arr[index] == arr[index+1]:
            index +=1
        calculate(index+1,sub)
    calculate(0,[])
    return res

## Test

print(subset([1,3,3,7]))