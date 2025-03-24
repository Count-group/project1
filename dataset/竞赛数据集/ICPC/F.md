Title: XOR Game

Time Limit: 1 second

Memory Limit: 512 megabytes

Problem Description:
Alice and Bob are playing a game against each other.

In front of them are a multiset $\{a_i\}$ of non-negative integers and a single integer $x$. Each number in $a$ is $0$ or $2^i(0\le i<k)$ before the game.

This game will be a turn-based game, and Alice will go first. In one person's turn, he or she will choose an integer from $a$. Let this number be $p$. Then this person will choose whether or not to make $x\gets x\oplus p$, then remove $p$ from $a$. Here, operation $\oplus$ means bitwise xor.

Alice wants to make $x$ as big as possible, and Bob wants to make $x$ as small as possible.

You are a bystander who wants to know the final value of $x$. However, the size of $a$ is a huge number. Formally, there are $b_i$ numbers whose values are $2^i$ in $a$ for all $0\le i<k$, and $z$ is the number of numbers whose values are $0$. But you still want to challenge this impossible problem.

If Alice and Bob are smart enough, please output the final value of $x$.


Input Specification:
The first line contains two integers $k,z(1\le k\le10^5,0\le z\le 10^9)$.

The next line contains $k$ integers, the $i$ -th integer is $b_{i-1}(0\le b_{i-1}\le10^9)$.

Output Specification:
Output the answer in binary format. Note that you should output exactly $k$ digit from high to low even though this number has leading $0$s.

Demo Input:
2 0
2 1

Demo Output:
11
