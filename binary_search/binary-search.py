def main(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        
        mid = (end + start) // 2
        if arr[mid] == target:
            return mid
        else:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


if __name__=="__main__":
    arr = [23, 50, 55, 70, 100 , 200]
    target = 200
    result = main(arr, target)
    print(result)

