"""
    _summary_

"""


class LinearSearch:
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
        for index, value in enumerate(self.array):
            if value == target:
                return index
        return -1

    def demo_meth(self):
        """
        demo_meth _summary_
        """
        pass


array_list = [1, 5, 3, 8, 2, 9, 4, 7]
searcher = LinearSearch(array_list)
TARGET = 8
index_val = searcher.search(TARGET)
if index_val == -1:
    print(f"{TARGET} not found in the array")
else:
    print(f"{TARGET} found at index {index_val}")
