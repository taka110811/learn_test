class Cal:
    def add_num_and_double(self, x, y):
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4

        >>> c.add_num_and_double('1','1')
        Traceback (most recent call last):
        ...
        ValueError: x or y is not integer
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("x or y is not integer")
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()