Title: Holes and Balls

Time Limit: 3 seconds

Memory Limit: 512 megabytes

Problem Description:
You are given $n$ balls, the $i$ -th ball's value is $p_i$. It's guaranteed that $p_1,p_2,\dots,p_n$ is a permutation of $1,2,3\dots,n$.

There is also a rooted tree of $n$ vertices, each of the vertices is a hole, and each hole can only hold one ball.

The tree's root is the first vertex.

Now you need to fill the holes with the balls.

You need to throw each ball in order of $1$ to $n$ in the following steps:

1. Throw the ball into vertex $1$.
2. Let the vertex where the ball is be $p$.
3. If the $p$ -th vertex has already been filled with other balls, you need to choose a vertex $x$ and throw the ball into the $x$ -th vertex, then return to step $2$. You need to guarantee that the $x$ -th vertex is the $p$ -th vertex's son and at least one vertex in the subtree of the $x$ -th vertex is not filled.
4. Otherwise, the ball will fill the $p$ -th vertex.

After throwing all the balls, let $a_i$ express the value of the ball in the $i$ -th vertex.

You need to find the minimum lexicographical order of $\{a_n\}$.

We define $dep_i$ as the number of vertices on the path from the $i$ -th vertex to the tree's root(the first vertex).

Specially, for any two vertices $x<y$, it's guaranteed that $dep_x\le dep_y$.

Input Specification:
The first line contains a single integer $n(1\le n\le 5\times 10^5)$ - the number of vertices in this tree.

The next line contains $n$ numbers, the $i$ -th number is $p_i(1\le p_i\le n)$. It's guaranteed that $p_1,p_2,\dots,p_n$ is a permutation of $1,2,3\dots,n$.

The next $n-1$ lines contain a description of the tree's edges. The $i$ -th of these lines contains two integers $u_i$ and $v_i(1\le u_i,v_i\le n) $ - the numbers of vertices connected by the $i$ -th edge.

It is guaranteed that the given edges form a tree.

And for any vertices $x<y$, it's guaranteed that $dep_x\le dep_y$.

Output Specification:
Output $n$ integers, the minimum lexicographical order of $\{a_n\}$.

Demo Input:
5
3 1 5 4 2
1 2
2 3
3 4
4 5

Demo Output:
3 1 5 4 2

