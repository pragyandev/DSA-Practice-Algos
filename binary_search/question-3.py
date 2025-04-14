# Question Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Statement: Find First and Last Position of Element in Sorted Array

def find_first_element(target, nums):
    start, end = 0, len(nums) -1
    index = -1

    while start <= end:
        mid = (start+end)//2

        if nums[mid] == target:
            index = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid - 1
    return index


def find_end_element(target, nums):
    start, end = 0, len(nums)-1
    index = -1

    while start <= end:
        mid = (start+end)//2

        if nums[mid] == target:
            start = mid + 1
            index = mid

        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return index
def search_range(nums: list, target: int) -> list:

    start = find_first_element(target, nums)
    end = find_end_element(target, nums)

    return [start, end]


if __name__=="__main__":
    input_arr = [5, 7, 7, 8, 8, 10]
    target = 8
    output = [3, 4]
    func_output = search_range(input_arr, target)
    print(func_output)
