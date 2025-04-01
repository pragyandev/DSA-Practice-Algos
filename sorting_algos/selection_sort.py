def selection_sort(arr: list) -> list:

    size = len(arr)

    for i in range(size-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__=="__main__":
    arr = [23, 21, 24, 72, 16, 54, 57, 89, 80]

    arr = selection_sort(arr)
    print(arr)