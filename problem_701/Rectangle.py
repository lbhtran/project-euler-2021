import numpy as np
import itertools


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.area_matrix = np.zeros((width, height))
        self.possible_arrays = [np.reshape(np.array(i), (width, height)) for i in itertools.product([0, 1], repeat=width * height)]

    # @staticmethod
    # def max_area(mtx, width, height):
    #     dp = np.zeros_like(mtx)
    #
    #     print(dp)
    #     return np.amax(dp)
    #
    # def transform(self):
    #     print(len(self.possible_arrays))
    #     for m in self.possible_arrays:
    #         print('original array')
    #         print(m)
    #         print('max area')
    #         print(Rectangle.max_area(m, self.width, self.height))
    #
    # def expected_max_area(self):
    #     exp_value = 0
    #     for m in self.possible_arrays:
    #         max_value = Rectangle.max_area(m, self.width, self.height)
    #         exp_value += max_value
    #     return exp_value


if __name__ == "__main__":
    rectangle = Rectangle(2, 2)
    print(rectangle.possible_arrays)
    # rectangle.transform()
    # print(rectangle.expected_max_area())