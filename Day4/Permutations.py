'''
Question 1: Permutations :-
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
'''

def permutation(arr):
    size = len(arr)
    res = []
    def calculate(index):
        if index == size-1:
            res.append(arr[:])
            return
        for k in range(index,size):
            arr[index],arr[k] = arr[index],arr[k]
            calculate(index+1)
            arr[index],arr[k] = arr[k],arr[index]
    calculate(0)
    return res

## Test

print(permutation([1,2,3]))

'''
Space Complexity : O(n)
Time Complexity : O(n*n!)
'''