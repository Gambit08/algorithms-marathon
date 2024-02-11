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

# Optimal approach
# Double binary search

def _matrix_search(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    # initialize top and bottom
    t = 0
    b = rows-1

    while t <= b:

        row_idx = (t+b)//2

        if matrix[row_idx][-1] < target:
            t = row_idx + 1
        elif matrix[row_idx][0] > target:
            b = row_idx - 1
        else:
            # we are at the right row
            break

    if not t <= b:
        return False
    
    target_row = matrix[row_idx]
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

