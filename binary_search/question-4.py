# Question-4 Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Statement: Minimum in Rotated Sorted Array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]


if __name__ == "__main__":
    input_arr = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    answer = sol.findMin(input_arr)
    print(answer)
