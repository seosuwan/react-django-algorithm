import unittest
import sys
sys.path.append('/admin/sorting')
from models_sort import Sorting




class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = instance.bubble_sort()
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        arr = [5, 8, 2, 6, 3, 1, 7, 9, 4]
        arr = Sorting.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        arr = [5, 8, 2, 6, 3, 1, 7, 9, 4]
        arr = Sorting.quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_two_sorted(self):
        l1 = [1,4,7,8]
        l2 = [1,6,2,9]
        arr = Sorting.merge_two_sorted(l1, l2)
        self.assertEqual(arr,[1,1,2,4,6,7,8,9])


if __name__ == '__main__':
    unittest.main()