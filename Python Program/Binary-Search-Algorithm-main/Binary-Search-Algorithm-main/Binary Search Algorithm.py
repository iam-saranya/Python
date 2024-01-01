def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Element found, return its index
        elif mid_element < target:
            low = mid + 1  # Discard left half
        else:
            high = mid - 1  # Discard right half

    return -1  # Element not found

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 10

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
