from dataclasses import dataclass

from Cython.Compiler.ExprNodes import ListNode


@dataclass
class Sorting(object):

    random_arr: []


    @property
    def val(self) -> 0: return self._val
    @val.setter
    def val(self, val): self._val = val

    @property
    def next(self) -> None:
        return self.next

    @next.setter
    def next(self, next):
        self.next = next

    @property
    def random_arr(self) -> []: return self._random_arr
    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self):
        arr = self.random_arr
        n = len(arr) # 배열길이를 뽑는다
        for i in range(n - 1): #
            for j in range(n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def merge_sort(param : []):
        arr = param
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        arr1 = Sorting.merge_sort(arr[:mid])
        arr2 = Sorting.merge_sort(arr[mid:])
        merge_arr = []
        i = h = 0
        while i < len(arr1) and h < len(arr2):
            if arr1[i] < arr2[h]:
                merge_arr.append(arr1[i])
                i += 1
            else:
                merge_arr.append(arr2[h])
                h += 1
        merge_arr += arr1[i:]
        merge_arr += arr2[h:]
        return merge_arr

    @staticmethod
    def quick_sort(param : []):
        arr = param
        if len(arr) < 2:
            return arr
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [], [], [] #하나의공간을 나눠쓰기에 파티션으로 나눈다
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)

    @staticmethod
    def merge_two_sorted(l1: ListNode ,l2 : ListNode) -> ListNode:
        if (not l1) or (l2 and l1 > l2):
            l1, l2 = l2, l1
        if l1:
            l1.next = Sorting.merge_two_sorted(l1.next, l2)
        return l1


