class InsertionSort:
    """
    A class that implements the insertion sort algorithm.

    Methods:
        sort(arr): Sorts the given array using insertion sort.
    """

    @staticmethod
    def sort(arr):
        """
        Sorts the given array using insertion sort.

        Args:
            arr (list): The array to be sorted.

        Returns:
            The sorted array.
        """
        n = len(arr)

        for i in range(1, n):
            # Get the current element to be inserted
            current_element = arr[i]

            # Find the index where the current element should be inserted
            j = i - 1
            while j >= 0 and arr[j] > current_element:
                arr[j+1] = arr[j]
                j -= 1

            # Insert the current element into its correct position
            arr[j+1] = current_element

        return arr
arr = [5, 2, 8, 3, 9, 1]
sorter = InsertionSort()
sorted_arr = sorter.sort(arr)
print(sorted_arr)
