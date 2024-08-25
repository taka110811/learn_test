import os

class Cal:
    def add_num_and_double(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("x or y is not integer")
        result = x + y
        result *= 2
        return result
    
    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('test')