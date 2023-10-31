# Key Idea 1: This is a problem of mathematical functions
# Key Idea 2: Create different identites, and thus possible states
# Key Idea 3: Do each combination of (n, m) manually to see the pattern

class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if m==0: return 1
        if n==1: return 2
        if n==2: return 3 if m==1 else 4
        if n>=3: return 4 if m==1 else (7 if m==2 else 8)

'''
Ref: https://leetcode.com/problems/bulb-switcher-ii/description/comments/1565085
So it's a somewhat interesting problem, but only if you think of it as a math problem. As a programming problem, i think it's lame.

Given a set of operations, what state would the lights end up in?
Let's call f(a) the new state of the lights after performing a

Let's add another switch, switch 0, the identity switch (switch 0 does nothing).
l1: f(0a) = f(a)

First, note that flipping is commutative: order does not matter.
l2: f(ab) = f(ba)

second, each function is an inverse of itself:
l3: f(aa) = f(0)

finally, note that there flipping odds and evens is the same as flipping all:
l4: f(23) = f(1)
f(12) = f(3)
f(13) = f(2)

Now we can reduce any sequence to something much simpler.
take a sequence like:
14342
by lemma 2 we can re-order:
12344
using l4:
1144
then by l3:
00
which is just the starting position.

It turns out that we only care then if there is an even or odd number of each flip. The total enumeration of states is:
0
1
2
3
4
12
13
14
23
24
34
123
124
134
234
1234

16 states... but wait, using lemma 4, some of these are the same (eg 134 = 24). Removing the redundancies from the list above:
0
1
2
3
4
14
24
34

we get 8 states.
So for a sufficiently high m (turns out its >= 3), we get:
flipLights(0) = 1
flipLights(1) = 4
flipLights(2) = 7
flipLights(3+) = 8

I am done. This was a waste.

'''