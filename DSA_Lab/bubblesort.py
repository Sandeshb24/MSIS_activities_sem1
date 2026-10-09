def bubble_sort(arr: list) -> list:
    """Sorts an array in ascending order using Bubble Sort."""
    n = len(arr)
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
            
    return arr


# Example Usage
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(sample_list)
    print("Sorted array:", sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]