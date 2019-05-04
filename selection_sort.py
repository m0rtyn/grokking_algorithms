def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_array.append(arr.pop(smallest))
    return sorted_array


array_for_sorting = [9, 8, 5, 1, 1, 4, 6]
print(selection_sort(array_for_sorting))
