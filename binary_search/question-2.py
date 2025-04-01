# Question-2 link (https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)

# Find smallest letter greater than target

input_arr = ['c', 'f', 'j']
target = 'c'
output = 'c'


def next_greatest_letter(letters, target):
    start, end = 0, len(letters)

    while start < end:
        mid = (start+end)//2
        if target < letters[mid]:
            end = mid
        else:
            start = mid+1
    return letters[start%len(letters)]



if __name__ == "__main__":
    print(next_greatest_letter(input_arr, target))
