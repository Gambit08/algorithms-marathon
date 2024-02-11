# https://leetcode.com/problems/search-a-2d-matrix/

# Approach 1

def matrix_search(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    row_index = 0

    for i in range(rows):

        if target <= matrix[i][cols-1]:
            row_index = i
            break

    target_row = matrix[row_index]
    l = 0
    r = cols-1

    while l <= r:

        mid = (l+r)//2

        if target_row[mid] == target:
            return True
        elif target_row[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False

