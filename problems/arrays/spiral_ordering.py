from typing import List

from test_framework import generic_test

# Fastest: D > A > C > B
# Time: O(n) Space: O(1)
# [ T, T, T, T ]
# [ L, x, x, R ]
# [ L, x, x, R ]
# [ L, B, B, R ]
def matrix_in_spiral_orderD(matrix: List[List[int]]) -> List[int]:
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1): 
            yield r1, c # top
        for r in range(r1 + 1, r2 + 1):
            yield r, c2 # right
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c # bottom
            for r in range(r2, r1, -1):
                yield r, c1 # left

    if not matrix: return []
    result = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            result.append(matrix[r][c])
        r1 += 1; r2 -= 1
        c1 += 1; c2 -= 1
    return result



def matrix_in_spiral_orderC(matrix: List[List[int]]) -> List[int]:
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in matrix]
    ans = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    for _ in range(R * C):
        ans.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return ans


def matrix_in_spiral_orderB(square_matrix: List[List[int]]) -> List[int]:
    SHIFT = ((0,1), (1,0), (0,-1), (-1,0))
    direction = x = y = 0
    spiral_ordering = []
    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


def matrix_in_spiral_orderA(square_matrix: List[List[int]]) -> List[int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 -
                                                          offset:offset:-1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_orderD))
