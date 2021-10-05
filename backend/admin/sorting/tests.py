from django.test import TestCase
import unittest
# import sys
# sys.path.append('/admin/sorting')
from admin.sorting.models import MySum
from admin.sorting.models import Palindrome


class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_2(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_2()
        # print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        instance = Palindrome()
        instance.input_string = "토마마토"
        res1 = instance.isPalindrome()
        # print(f'Expected Value is {res}')
        print(res1)

    def test_reverse_string(self):
        instance = Palindrome()
        instance.input_string = '안녕하세요'
        res = instance.reverse_string()
        print(res)



if __name__ == '__main__':
    unittest.main()