'''
Question 1: Tower of Hanoi :- 
We have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. 
Initially, these discs are in the rod 1. 
You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, find & return the total moves.

Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. 
Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. 
You can only move 1 disk at a time.
'''

def tower_of_hanoi(n,src,dst,aux):
    count = 0
    def helper(n,src,dst,aux):
        nonlocal count
        if n == 1:
            print(f"Move disk {n} from {src} to {dst}")
            count += 1
            return
        helper(n-1,src,aux,dst)
        print(f"Move disk {n} from {src} to {dst}")
        count += 1
        helper(n-1,aux,dst,src)
    helper(n,src,dst,aux)
    return count

## Test

print(tower_of_hanoi(4,"r1","r2","r3"))

'''
Space Complexity : O(n)
Time Complexity : O(2**n-1)
'''
    