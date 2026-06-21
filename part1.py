import random


# -----------------------------
# Randomized Quickselect
# -----------------------------
def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]

    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    store_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index


def randomized_select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_index = random.randint(left, right)

    pivot_index = partition(arr, left, right, pivot_index)

    if k == pivot_index:
        return arr[k]

    elif k < pivot_index:
        return randomized_select(arr, left, pivot_index - 1, k)

    else:
        return randomized_select(arr, pivot_index + 1, right, k)


def quickselect(arr, k):
    arr_copy = arr.copy()
    return randomized_select(arr_copy, 0, len(arr_copy) - 1, k)


# -----------------------------
# Median of Medians
# -----------------------------
def median_of_medians(arr, k):

    if len(arr) <= 5:
        return sorted(arr)[k]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    medians = [sorted(group)[len(group) // 2] for group in groups]

    pivot = median_of_medians(medians, len(medians) // 2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)

    elif k < len(lows) + len(pivots):
        return pivot

    else:
        return median_of_medians(
            highs,
            k - len(lows) - len(pivots)
        )


# -----------------------------
# Test Program
# -----------------------------
if __name__ == "__main__":

    data = [12, 3, 5, 7, 19, 26, 4, 8]

    k = 3  # 4th smallest element (0-based index)

    print("Array:", data)

    print(
        "Quickselect:",
        quickselect(data, k)
    )

    print(
        "Median of Medians:",
        median_of_medians(data, k)
    )
