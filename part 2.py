from __future__ import annotations
from typing import List

import collections
import heapq

from utils import timeout


@timeout(5)
def mazeQ1b(graph: List[List[int]], start: List[int], end: List[int], F: int) -> int:
    ...
    maze = graph
    M, N = len(maze), len(maze[0])
    Sx, Sy = start
    Ex, Ey = end

    #make sure F is not greater than both M & N
    if (F >= M) and (F >= N):
        F = max(M, N) - 1

    #initialise an empty 2d array: "bfs"
    bfs = []
    for i in range(M):
        bfs.append([])
        for j in range(N):
            bfs[-1].append(0)
    bfs[Sx][Sy] = 1

    #initialise an empty 1d array: "F_result"
    F_result = []
    for i in range(F):
        F_result.append(-1)

    #check result for jump_size = 1
    jump_size = 1
    moves = 0
    while (bfs[Ex][Ey] == 0):
        moves += 1
        for i in range(M):
            for j in range(N):
                if (bfs[i][j] == moves):
                    # move left
                    if (i > 0) and (bfs[i - 1][j] == 0) and (maze[i - 1][j] == 0):
                        bfs[i - 1][j] = moves + 1
                    # move right
                    if (i < (M - 1)) and (bfs[i + 1][j] == 0) and (maze[i + 1][j] == 0):
                        bfs[i + 1][j] = moves + 1
                    # move up
                    if (j > 0) and (bfs[i][j - 1] == 0) and (maze[i][j - 1] == 0):
                        bfs[i][j - 1] = moves + 1
                    # move down
                    if (j < (N - 1)) and (bfs[i][j + 1] == 0) and (maze[i][j + 1] == 0):
                        bfs[i][j + 1] = moves + 1
        # find the maximum value of the bfs array
        maximum = 1
        for i in range(M):
            for j in range(N):
                if (bfs[i][j] > maximum):
                    maximum = bfs[i][j]
        # break if max == moves
        if (maximum == moves):
            break
    # return -1 when there is no solution
    if (bfs[Ex][Ey] == 0):
        F_result[0] = -1
    # return move time when there is a solution
    else:
        F_result[0] = bfs[Ex][Ey] - 1

    bfs_result = []
    #check result for jump_size >= 2
    for f in range(2,F+1):
        #initialise an empty 1d array: "bfs_result"
        bfs_result = []

        if F_result[f-1] == -1:
            max_step = M*N
        else:
            max_step = F_result[f-1]

        for j in range(1, max_step+1):
            #bfs초기화
            for m in range(M):
                for n in range(N):
                    bfs[m][n] = 0
            bfs[Sx][Sy] = 1

            moves = 0
            while (bfs[Ex][Ey] == 0):
                moves += 1
                for m in range (M):
                    for n in range(N):
                        if (bfs[m][n] == moves):
                            #j번째에 f만큼 이동
                            if (moves == j):
                                # move left
                                if ((m - f) >= 0) and (bfs[m - f][n] == 0) and (maze[m - f][n] == 0):
                                    bfs[m - f][n] = moves + 1
                                # move right
                                if ((m + f) <= (M - 1)) and (bfs[m + f][n] == 0) and (maze[m + f][n] == 0):
                                    bfs[m + f][n] = moves + 1
                                # move up
                                if ((n - f) >= 0) and (bfs[m][n - f] == 0) and (maze[m][n - f] == 0):
                                    bfs[m][n - f] = moves + 1
                                # move down
                                if ((n + f) <= (N - 1)) and (bfs[m][n + f] == 0) and (maze[m][n + f] == 0):
                                    bfs[m][n + f] = moves + 1
                            else:
                                # move left
                                if (m > 0) and (bfs[m - 1][n] == 0) and (maze[m - 1][n] == 0):
                                    bfs[m - 1][n] = moves + 1
                                # move right
                                if (m < (M - 1)) and (bfs[m + 1][n] == 0) and (maze[m + 1][n] == 0):
                                    bfs[m + 1][n] = moves + 1
                                # move up
                                if (n > 0) and (bfs[m][n - 1] == 0) and (maze[m][n - 1] == 0):
                                    bfs[m][n - 1] = moves + 1
                                # move down
                                if (n < (N - 1)) and (bfs[m][n + 1] == 0) and (maze[m][n + 1] == 0):
                                    bfs[m][n + 1] = moves + 1
                # find the maximum value of the bfs array
                maximum = 1
                for m in range(M):
                    for n in range(N):
                        if (bfs[m][n] > maximum):
                            maximum = bfs[m][n]
                # break if max == moves
                if (maximum == moves):
                    break
            # return -1 when there is no solution
            if (bfs[Ex][Ey] == 0):
                bfs_result.append(-1)
            # return move time when there is a solution
            else:
                bfs_result.append(bfs[Ex][Ey] - 1)
        #minimum bfs_result
        min_bfs = M*N
        for element in bfs_result:
            if (element < min_bfs) and (element != -1):
                min_bfs = element
        if (min_bfs == M*N):
            min_bfs = -1
            F_result[f - 1] = -1
        else:
            F_result[f-1] = min_bfs
    #return final value
    minimum = M * N
    for element in F_result:
        if (element < minimum) and (element != -1):
            minimum = element
    if (minimum == M * N):
        return -1
    return minimum
