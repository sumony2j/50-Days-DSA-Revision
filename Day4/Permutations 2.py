'''
Question 2: Permutations 2 :-
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.
'''

def permutation(arr):
    size = len(arr)
    res = []
    def calculate(index):
        hash = {}
        if index == size-1:
            res.append(arr[:])
            return
        for k in range(index,size):
            if arr[k] not in hash:
                hash[arr[k]] = True
                arr[index],arr[k] = arr[k],arr[index]
                calculate(index+1)
                arr[index],arr[k] = arr[k],arr[index]
    calculate(0)
    return res

## Test

print(permutation([1,1,2]))

'''
Space Complexity : O(n)
Time Complexity : O(n*n!)
'''