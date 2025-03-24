Title: Fix the Tree

Time Limit:  5 seconds

Memory Limit:  1024 megabytes

Problem Description:

You are given a tree consisting of $n$ vertices. Each vertex $i$ of this tree has a value $w_i$ assigned to it.

Now the vertex $u$ will be broken. Once it's broken, vertex $u$ and all edges with one end at vertex $u$ will be removed from the tree.

To make the tree connected, you can do the following operation any number of times(possibly zero) in any order:

- First choose two vertices $u$ and $v$ from the tree;
- Then pay $w_u+w_v$ coins, and add an edge between vertices $u$ and $v$;
- At last, replace $w_u+1$ with $w_u$, replace $w_v+1$ with $w_v$.

Your task is to calculate the minimum number of coins to be paid.

But you don't know which vertex $u$ is, so you need to find the answer for each $1\le u\le n$. Please answer all the queries independently.

Input Specification:
The first line contains a single integer $n(2\le n\le 10^6)$ --- the number of vertices in this tree.

The next line contains $n$ numbers, the $i$ -th number is $w_i(1\le w_i\le n)$.

The next $n-1$ lines contain a description of the tree's edges. The $i$ -th of these lines contains two integers $u_i$ and $v_i(1\le u_i,v_i\le n) $ --- the numbers of vertices connected by the $i$ -th edge.

It is guaranteed that the given edges form a tree.

Output Specification:
Print $n$ integers, the $i$ -th integer is the answer when $u=i$.

Demo Input:
6
1 1 1 1 1 1
1 2
1 3
1 4
2 5
2 6

Demo Output:
4 4 0 0 0 0


