class SelectionSort:
    """
    A class that implements the selection sort algorithm.

    Methods:
        sort(arr): Sorts the given array using selection sort.
    """

    @staticmethod
    def sort(arr):
        """
        Sorts the given array using selection sort.

        Args:
            arr (list): The array to be sorted.

        Returns:
            The sorted array.
        """
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr
arr = [5, 2, 8, 3, 9, 1]
sorter = SelectionSort()
sorted_arr = sorter.sort(arr)
print(sorted_arr)
