"""
    _summary_

"""
class BinarySearch:
    """
     _summary_
    """
    def __init__(self, array):
        self.array = array

    def search(self, target):
        """
        search _summary_

        :param target: _description_
        :type target: _type_
        :return: _description_
        :rtype: _type_
        """
        low = 0
        high = len(self.array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == target:
                return mid
            if self.array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def demo_meth(self):
        """
        demo_meth _summary_
        """
        pass

array_list = [1, 2, 3, 4, 5, 7, 8, 9]
searcher = BinarySearch(array_list)
TARGET = 4
index = searcher.search(TARGET)
if index == -1:
    print(f"{TARGET} not found in the array")
else:
    print(f"{TARGET} found at index {index}")
