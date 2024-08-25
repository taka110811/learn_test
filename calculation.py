class Cal:
    def add_num_and_double(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("x or y is not integer")
        result = x + y
        result *= 2
        return result