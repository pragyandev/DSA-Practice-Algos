def bubble_sort(arr: list) -> list:

    if len(arr) == 0: return []
    if len(arr) == 1: return arr

    for _ in range(len(arr)):
        for i in range(len(arr) - 1 - _):
            ele_1, ele_2 = arr[i], arr[i+1]
            if ele_1 > ele_2:
                arr[i], arr[i+1] = ele_2, ele_1

    return arr


if __name__=="__main__":
    arr = [23, 21, 24, 72, 53, 54, 57, 89, 80]

    arr = bubble_sort(arr)

    print(arr)