# Question-1 link (https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

# Count negative numbers in a sorted matrix

# You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to
# return the number of negative numbers present in the matrix.

input_arr = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]


def counter(arr: [list]):
    count = 0

    def negative_count(row, target=0):
        start, end = 0, len(row)

        while end > start:
            mid = (start + end) // 2
            if row[mid] < 0:
                end = mid
            else:
                start = mid + 1
        return len(row) - start

    for i in arr:
        count += negative_count(i)

    return count






