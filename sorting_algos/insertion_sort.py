def insertion_sort(arr: list) -> list:

    size = len(arr)

    for i in range(1, size):
        current_ele = arr[i]
        correct_idx = i-1
        while correct_idx >= 0:
            if arr[correct_idx] > current_ele:
                arr[correct_idx+1] = arr[correct_idx]
                correct_idx -= 1
            else:
                break
            arr[correct_idx+1] = current_ele

    return arr

def insertion_sort_1(arr: list):

    size = len(arr)

    for i in range(1, size):
        current_ele = arr[i]

        if arr[i-1] > current_ele:
            for j in reversed(range(len(arr[:i]))):
                if arr[j] > current_ele:
                    arr[j+1] = arr[j]
                    i -= 1
                else: break
            arr[i] = current_ele

    return arr




if __name__ == "__main__":
    array = [23, 21, 24, 72, 16, 54, 57, 89, 80]

    array = insertion_sort_1(array)

    print(array)