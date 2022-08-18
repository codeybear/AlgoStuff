### Permutations
Permutation are ordered arrangement of objects  

The lexicographic permutations of 0, 1 and 2 are:  
012   021   102   120   201   210

There are 3 objects so the number of combinations are N! = 3! = 6
If they are in order then finding a combination in a specific position is given here:

https://codereview.stackexchange.com/questions/224516/project-euler-24-lexicographic-permutations-in-python

Thats the best reference found so far

### Lattice Paths
From euler #15

Roots through a matrix are given by binomial coefficients - 
https://en.m.wikipedia.org/wiki/Binomial_coefficient

knowing this makes it a simple calculation:

n=40 as there are 40 steps to reach the end  
k=20 are the combinations  
This needs more thinking about but the formula is as follows:  
40!/((20!)(40-20)!)
