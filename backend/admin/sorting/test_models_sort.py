import unittest
# import sys
# sys.path.append('/admin/basic')
from admin.sorting.models_sort import Sorting


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_arr = [8,4,6,2,9,1,3,7,5]
        arr = instance.bubble_sort()
        self.assertEqual(arr, [1,2,3,4,5,6,7,8,9])



    def test_merge_sort(self):
        arr = [8,4,6,2,9,1,3,7,5]
        arr = Sorting.merge_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8,9])


    def test_quick_sort(self):
        arr = [8,4,6,2,9,1,3,7,5]
        arr = Sorting.quick_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8,9] )


if __name__ == '__main__':
    unittest.main()