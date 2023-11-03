from __future__ import annotations
from typing import List

import collections
import heapq

from utils import timeout


@timeout(5)
def mazeQ1c(graph: List[List[int]], start: List[int], end: List[int], F: int) -> int:
    ...
    # get inputs
    maze = graph
    M, N = len(maze), len(maze[0])
    Sx, Sy = start
    Ex, Ey = end

    # initialise an empty 2d array
    bfs = []
    for i in range(M):
        bfs.append([])
        for j in range(N):
            bfs[-1].append([])
    bfs[Sx][Sy].append([1,0])

    moves = 0
    while not bfs[Ex][Ey] and (moves < M * N): #while bfs[Ex][Ey] is empty and moves is smaller than the size of the maze
        moves += 1
        for m in range(M):
            for n in range(N):
                if bfs[m][n]: #if bfs[m][n] is not empty
                    for element in bfs[m][n]:
                        if element[0] == moves:
                            for distance in range(1, F - element[1] + 1):
                                # move left
                                if ((m - distance) >= 0) and (maze[m - distance][n] == 0):
                                    if [moves+1,distance] not in bfs[m - distance][n]:
                                        if distance == 1:
                                            bfs[m - distance][n].append([moves + 1, element[1]])
                                        else:
                                            bfs[m - distance][n].append([moves+1, element[1] + distance])
                                        #print(m,n,element,m - distance,n,[moves+1, element[1] + distance])
                                #move right
                                if ((m + distance) <= (M - 1)) and (maze[m + distance][n] == 0):
                                    if [moves+1,distance] not in bfs[m + distance][n]:
                                        if distance == 1:
                                            bfs[m + distance][n].append([moves + 1, element[1]])
                                        else:
                                            bfs[m + distance][n].append([moves+1, element[1] + distance])
                                        #print(m, n, element, m + distance,n, [moves + 1, element[1] + distance])
                                #move up
                                if ((n - distance) >= 0) and (maze[m][n - distance] == 0):
                                    if [moves+1, distance] not in bfs[m][n - distance]:
                                        if distance == 1:
                                            bfs[m][n - distance].append([moves + 1, element[1]])
                                        else:
                                            bfs[m][n - distance].append([moves+1, element[1] + distance])
                                        #print(m, n, element, m ,n-distance, [moves + 1, element[1] + distance])
                                #move down
                                if ((n + distance) <= (N - 1)) and (maze[m][n + distance] == 0):
                                    if [moves+1, distance] not in bfs[m][n + distance]:
                                        if distance == 1:
                                            bfs[m][n + distance].append([moves + 1, element[1]])
                                        else:
                                            bfs[m][n + distance].append([moves+1, element[1] + distance])
                                        #print(m, n, element, m,n+distance, [moves + 1, element[1] + distance])
    #return result
    if not bfs[Ex][Ey]:
        return -1
    return bfs[Ex][Ey][0][0] - 1
