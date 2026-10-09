def insertion_sort(arr: list) -> list:
    """Sorts an array in ascending order using Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example Usage
if __name__ == "__main__":
    sample_list = [12, 11, 13, 5, 6]
    sorted_list = insertion_sort(sample_list)
    print("Sorted array:", sorted_list)  # Output: [5, 6, 11, 12, 13]