from django.test import TestCase
import unittest
import sys
sys.path.append('/admin/sorting')

from models import MySum, Palindrome


class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

    def test_palindrome(self):
        instance = Palindrome()
        #instance.str_to_list("A man, a plan, a canal: Panama")
        #print(str_arr)
        self.assertEqual(instance.isPalindrome(instance.str_to_list("A man, a plan, a canal: Panama"))["Result"], True)



if __name__ == '__main__':
    unittest.main()