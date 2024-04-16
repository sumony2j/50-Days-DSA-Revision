'''
Question 1: Sorted Squared Array :-
You are given an array of Integers in which each subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.
'''

'''
Assumptions :

1. Input array can have -ve/+ve elements.
2. Input array can be empty.
'''

def sorted_squared_array(A):
    size = len(A)
    start = 0
    end = size-1
    Result = size*[0]
    i = end
    while start <= end:
        if A[start]**2 > A[end]**2:
            Result[i] = A[start]**2
            start = start+1
            i=i-1
        else:
            Result[i] = A[end]**2
            end = end -1
            i = i -1
    return Result

## Test 
print(sorted_squared_array([-7,-3,-2,4,5,6]))
print(sorted_squared_array([]))

'''
Time & Space Complexity : O(n)
'''
