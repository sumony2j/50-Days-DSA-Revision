'''
Question 2: Monotonic Array :- 
An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing. 
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise.
'''

'''
Assumption :

1. An monotonic array can have all the elements same.
2. An monotonic array can be a single element.
'''

def monotonic_array(A):
    if len(A) == 0:
        return True
    if A[0] > A[len(A)-1]:
        for k in range(len(A)-1):
            if A[k] < A[k+1]:
                return False
    elif A[0] < A[len(A)-1]:
        for k in range(len(A)-1):
            if A[k] > A[k+1]:
                return False
    elif A[0] == A[len(A)-1]:
        for k in range(len(A)-1):
            if A[k] != A[k+1]:
                return False
    return True

# Test

print(monotonic_array([-3,-1,5,6,9]))
print(monotonic_array([3,3,3,3]))
print(monotonic_array([9,-7,-9,-67]))
print(monotonic_array([9,6,-3,99]))
print(monotonic_array([]))

'''
Time Complexity : O(n)
Space Complexity : O(1)
'''