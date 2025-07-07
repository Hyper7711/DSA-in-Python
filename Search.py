class SearchAlgorithms:

    # Linear Search
    def linear_search(self, arr, target):
        """checks each element until the target is found."""
        for i, value in enumerate(arr):
            if value == target:
                print(f"Linear Search: Found {target} at index {i}.")
                return i
        print(f"Linear Search: {target} not found.")
        return -1

    # Binary Search
    def binary_search(self, arr, target):
        """Divides the array in half, searching in a sorted array."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                print(f"Binary Search: Found {target} at index {mid}.")
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"Binary Search: {target} not found.")
        return -1

    # Jump Search
    def jump_search(self, arr, target):
        """Checks elements by jumping in blocks to reduce comparisons."""
        import math

        length = len(arr)
        jump = int(math.sqrt(length))  # Optimal block size
        prev, current = 0, 0

        while current < length and arr[current] < target:
            prev = current
            current += jump
            if current >= length:
                current = length  # Bounds the search within array size

        for i in range(prev, min(current, length)):
            if arr[i] == target:
                print(f"Jump Search: Found {target} at index {i}.")
                return i
        print(f"Jump Search: {target} not found.")
        return -1

    # Interpolation Search
    def interpolation_search(self, arr, target):
        """Estimates the position of the target based on value distribution."""
        low, high = 0, len(arr) - 1

        while low <= high and arr[low] <= target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    print(f"Interpolation Search: Found {target} at index {low}.")
                    return low
                print(f"Interpolation Search: {target} not found.")
                return -1

            pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))

            if arr[pos] == target:
                print(f"Interpolation Search: Found {target} at index {pos}.")
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1

        print(f"Interpolation Search: {target} not found.")
        return -1


# Test
search_algos = SearchAlgorithms()
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Method Calling
search_algos.linear_search(array, 7)
search_algos.binary_search(array, 7)
search_algos.jump_search(array, 7)
search_algos.interpolation_search(array, 7)

