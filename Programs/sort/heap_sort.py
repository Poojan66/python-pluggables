class HeapSort:
    """
    A class that implements the heap sort algorithm.

    Methods:
        sort(arr): Sorts the given array using heap sort.
    """

    @staticmethod
    def heapify(arr, n, i):
        """
        Creates a max-heap from a given node in the array.

        Args:
            arr (list): The array to be heapified.
            n (int): The size of the heap.
            i (int): The node to start heapifying from.
        """
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)

    @staticmethod
    def sort(arr):
        """
        Sorts the given array using heap sort.

        Args:
            arr (list): The array to be sorted.

        Returns:
            The sorted array.
        """
        n = len(arr)

        # Build a max-heap from the array
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)

        # Extract elements from the heap one by one and put them in their correct position
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            HeapSort.heapify(arr, i, 0)

        return arr
arr = [5, 2, 8, 3, 9, 1]
sorter = HeapSort()
sorted_arr = sorter.sort(arr)
print(sorted_arr)
