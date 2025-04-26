import unittest
from katas.matrix_rotate import rotate_matrix

class TestMatrixRotate(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        rotated_matrix = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        rotate_matrix(matrix)
        self.assertEqual(matrix, rotated_matrix)

    def test_rotate_empty_matrix(self):
        matrix = []
        rotate_matrix(matrix)
        self.assertEqual(matrix, [])
