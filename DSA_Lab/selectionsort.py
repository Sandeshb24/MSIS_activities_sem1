def selection_sort(arr: list) -> list:
    """Sorts an array in ascending order using Selection Sort."""
    n = len(arr)
    
    for i in range(n - 1):
        # Assume the current position holds the minimum element
        min_idx = i
        
        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first unsorted element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr


# Example Usage
if __name__ == "__main__":
    sample_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(sample_list)
    print("Sorted array:", sorted_list)  # Output: [11, 12, 22, 25, 64]