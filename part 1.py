from __future__ import annotations
from typing import List

import collections
import heapq

from utils import timeout


@timeout(10)
def mazeQ1a(graph: List[List[int]], start: List[int], end: List[int]) -> int:
    ...
    #get inputs
    maze = graph
    M, N = len(maze), len(maze[0])
    Sx, Sy = start
    Ex, Ey = end

    #initialise an empty 2d array
    bfs = []
    for i in range(M):
        bfs.append([])
        for j in range(N):
            bfs[-1].append(0)
    bfs[Sx][Sy] = 1

    #move the hero to neighbouring cells
    moves = 0
    while (bfs[Ex][Ey] == 0):
        moves += 1
        for i in range(M):
            for j in range(N):
                if (bfs[i][j] == moves):
                    #move left
                    if (i > 0) and (bfs[i-1][j] == 0) and (maze[i-1][j] == 0):
                        bfs[i-1][j] = moves + 1
                    #move right
                    if (i < (M-1)) and (bfs[i+1][j] == 0) and (maze[i+1][j] == 0):
                        bfs[i+1][j] = moves + 1
                    #move up
                    if (j > 0) and (bfs[i][j-1] == 0) and (maze[i][j-1] == 0):
                        bfs[i][j-1] = moves + 1
                    #move down
                    if (j < (N-1)) and (bfs[i][j+1] == 0) and (maze[i][j+1] == 0):
                        bfs[i][j+1] = moves + 1
        #find the maximum value of the bfs array
        max = 1
        for i in range(M):
            for j in range(N):
                if (bfs[i][j] > max):
                    max = bfs[i][j]
        #break if max == moves
        if (max == moves):
            break
    #return -1 when there is no solution
    if (bfs[Ex][Ey] == 0):
        return -1
    #return move time when there is a solution
    return (bfs[Ex][Ey] - 1)







