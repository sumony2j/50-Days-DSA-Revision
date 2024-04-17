'''
Question 2: Josephus problem :- 
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, 
and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

1.Start at the 1st friend.

2.Count the next k friends in the clockwise direction including the friend you started at. 
The counting wraps around the circle and may count some friends more than once.

3.The last friend you counted leaves the circle and loses the game.

4.If there is still more than one friend in the circle, 
go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.

5.Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.
'''

## Method 1

def findwinner(n,k):
    def josephus(n):
        if n == 1:
            return 0
        return ((josephus(n-1)+k) % n)
    return josephus(n)+1

## Test

print(findwinner(41,2))

'''
Time & Space Complexity : O(n)
'''

## Method 2

def findwinner_iter(n,k):
    win = 0
    for i in range(2,n+1):
        win = (win+k)%i 
    return win+1

## Test

print(findwinner_iter(41,2))

'''
Time Complexity : O(n)
Space Complexity : O(1)
'''