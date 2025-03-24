Title: Make Them Straight

Time Limit: 2 seconds

Memory Limit: 512 megabytes

Problem Description:
There is a sequence $a$ of non-negative integers of length $n$, the $i$-th element of it is $a_i(1\leq i\leq n)$.

A sequence is defined as 'good' if and only if there exists a non negative integer $k(0\leq k\leq 10^6)$ that satisfies the following condition:

$a_{i}=a_{1}+(i-1)k$ for all $1\leq i\leq n$.

To make this sequence 'good', for each $i(1\leq i\leq n)$, you can do nothing, or pay $b_i$ coin to replace $a_i$ with any non-negative integer.

The question is, what is the minimum cost to make this sequence 'good'.

Input Specification:
The first line contains an integer $n(1\leq n\leq 2\times 10^5)$, described in the statement.

The second line contains $n$ integers $a_1,...,a_n(0\leq a_i\leq 10^6)$.

The third line contains $n$ integers $b_1,...,b_n(0\leq b_i\leq 10^6)$.

Output Specification:
One integer, the answer.

Demo Input:
5
1 4 3 2 5
1 1 1 1 1

Demo Output:
2

