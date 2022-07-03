import unittest
import my_dice_ver_5

class SortTest(unittest.TestCase):

    def test_sort_poly1(self):
        self.assertEqual(my_dice_ver_5.sort_set(1, [0, 0, 0, 0, 0, 0], [0]), ['0'])
    def test_sort_poly2(self):
        self.assertEqual(my_dice_ver_5.sort_set(2, [0, 0, 0, 0, 0, 0], [0, 0]), ['0', '0'])
    def test_sort_poly3(self):
        self.assertEqual(my_dice_ver_5.sort_set(3, [0, 0, 0, 0, 0, 0], [0, 0, 0]), ['0', '0', '0'])
    def test_sort_poly4(self):
        self.assertEqual(my_dice_ver_5.sort_set(4, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0]), ['0', '0', '0', '0'])
    def test_sort_poly5(self):
        self.assertEqual(my_dice_ver_5.sort_set(5, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0'])
    def test_sort_poly6(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0', '0'])
    def test_sort_poly7(self):
        self.assertEqual(my_dice_ver_5.sort_set(7, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0', '0', '0'])
    def test_sort_poly8(self):
        self.assertEqual(my_dice_ver_5.sort_set(8, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0', '0', '0', '0'])

    def test_sort_with_numbers1(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]), ['10', '0', '0', '0', '0', '0'])
    def test_sort_with_numbers2(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 0, 0, 0, 0, 0]), ['20', '0', '0', '0', '0', '0'])
    def test_sort_with_numbers3(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [100, 0, 0, 0, 0, 0]), ['110', '0', '0', '0', '0', '0'])
    def test_sort_with_numbers4(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [2, 2, 2, 2, 2, 2, 2, 2], [1, 0, 0, 0, 0, 0]), ['1', '8', '0', '0', '0', '0'])
    def test_sort_with_numbers5(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0]), ['1', '1', '1', '1', '1', '1'])
    def test_sort_with_numbers6(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0', '20'])
    def test_sort_with_numbers7(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [], [0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0', '0'])
    def test_sort_with_numbers8(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [], [1, 1, 1, 1, 1, 1]), ['1', '1', '1', '1', '1', '1'])
    def test_sort_with_numbers9(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [0, 0, 0, 0, 0, 0]), ['0', '0', '10', '0', '0', '0'])
    def test_sort_with_numbers10(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0]), ['0', '0', '0', '10', '0', '0'])
    def test_sort_with_numbers11(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '10', '0'])
    def test_sort_with_numbers12(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [0, 0, 0, 0, 0, 0]), ['0', '0', '0', '0', '0', '10'])
    def test_sort_with_numbers13(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, ], [0, 0, 0, 0, 0, 0]), ['10', '3', '5', '0', '0', '0'])
    def test_sort_with_numbers14(self):
        self.assertEqual(my_dice_ver_5.sort_set(6, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,], [0, 0, 0, 0, 0, 0]), ['50', '0', '0', '0', '0', '0'])



if __name__ == '__main__':
    unittest.main()