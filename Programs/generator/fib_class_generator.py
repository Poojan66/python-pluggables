"""
    _summary_

"""


class Fibonacci:
    """
     _summary_
    """

    def fibonacci_generator(self):
        """
        fibonacci_generator _summary_

        :yield: _description_
        :rtype: _type_
        """
        countera, counterb = 0, 1
        while True:
            yield countera
            countera, counterb = counterb, countera + counterb

    def demo_meth(self):
        """
        demo_meth _summary_
        """
        pass


class AnotherClass:
    """
     _summary_
    """

    def __init__(self, fib_instance):
        """
        __init__ _summary_

        :param fib_instance: _description_
        :type fib_instance: _type_
        """
        self.fib_instance = fib_instance

    def use_generator(self):
        """
        use_generator _summary_
        """
        gen = self.fib_instance.fibonacci_generator()
        for _ in range(10):
            print(next(gen))

    def demo_meth(self):
        """
        demo_meth _summary_
        """
        pass


fib = Fibonacci()
another_instance = AnotherClass(fib)
another_instance.use_generator()
