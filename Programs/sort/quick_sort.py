class QuickSort:
    """
    A class that implements the quicksort algorithm.

    Methods:
        sort(arr): Sorts the given array using quicksort.
    """

    @staticmethod
    def sort(arr):
        """
        Sorts the given array using quicksort.

        Args:
            arr (list): The array to be sorted.

        Returns:
            The sorted array.
        """
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def quicksort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi-1)
                quicksort(arr, pi+1, high)

        n = len(arr)
        quicksort(arr, 0, n-1)

        return arr
arr = [5, 2, 8, 3, 9, 1]
sorter = QuickSort()
sorted_arr = sorter.sort(arr)
print(sorted_arr)
