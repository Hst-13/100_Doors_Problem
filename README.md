# 100_Doors_Problem
A corridor has 100 closed doors. On first whistle all the doors open. On second whistle, all the alternate doors are toggled (i.e. closed if open and open if closed) from 2nd door. On third whistle, doors 3,6,9,12 and so on are toggled. Find the state of the doors after the 100th whistle.
## Solution
From observation, we conclude that a door is toggled when whistle number is a factor of the door number. So, at the 100th whistle obly those doors which have odd number of factors will remain open.
\nFor example :
1. Factors of 50 = 1,2,5,10,25,50 (even)
2. Factor of 64 = 1,2,4,8,16,32,64 (odd)
\nOnly perfect squares have odd number of factors.
We can conclude that only those doors which are perfect squares will be open at the 100th whistle.
Time Complexity = O(n)
