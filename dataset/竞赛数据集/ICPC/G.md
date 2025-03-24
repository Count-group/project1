Title: The Last Cumulonimbus Cloud

Time Limit: 1 second

Memory Limit: 512 megabytes

Problem Description:
Every April, the city is always shrouded under cumulonimbus clouds.

This city is connected by $n$ buildings and $m$ two-way streets. In order to facilitate people's travel, any two buildings can directly or indirectly reach each other through the streets. At the same time, no street connects the same building, and there is at most one street that connects each pair of buildings.

The pace of life in this city is very slow because the city layout is not very bulky.

Specifically,if we consider this city as an undirected graph $G$ ,it is guaranteed that for any non empty subgraph in this graph,there is at least one building inside it that connects up to 10 streets within the subgraph.

The rain is not stopping, and the number of cumulonimbus clouds is constantly increasing. At the beginning, there are $a_i$ cumulonimbus clouds above the $i$ -th building, but in the following $q$ days, one of the following two events will occur every day:

- $\text{1 x v}$ $v$ cumulonimbus clouds have been added over the $x$ -th building.
- $\text{2 x}$ you need to report how many cumulonimbus clouds are in total over all buildings directly connected to building $x$.

Input Specification:
The first line contains three integers $n,m,q(1\le n\le 3\times 10^5,1\leq m\leq 3\times 10^6, 1\leq q\leq 2\times 10^6)$.

Each of the next $m$ lines contains two integers $x,y(1\leq x,y\leq n,x\neq y)$, which represents a street connecting the $x$ -th and $y$ -th buildings.

Each of the next $n$ lines contains an integer $a_i(0\leq a_i\leq 100)$.

Each of the next $q$ lines contains two or three integers, if the first integer is $1$, it represents a first type of event, and the next two integers represent $x,v(0\leq v\leq 100)$. If the first integer is $2$, it represents a second type of event, the next integer represents $x$.

Output Specification:
Several rows, each representing a query result for a second type of event.

Demo Input:
4 6 10
2 4
2 3
4 3
3 1
4 1
2 1
0
7
1
6
2 4
2 2
1 3 3
2 1
1 1 9
2 4
2 2
1 3 6
2 4
2 2

Demo Output:
8
7
17
20
19
26
25

