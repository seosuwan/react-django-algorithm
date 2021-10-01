from dataclasses import dataclass

@dataclass
class Sorting(object):

    random_arr: []

    @property
    def random_arr(self) -> [] : return self._random_arr

    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self):
        arr = self.random_arr
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def merge_sort(param: []):
        arr = param
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        low_arr = Sorting.merge_sort(arr[:mid])
        high_arr = Sorting.merge_sort(arr[mid:])
        res_arr = []
        l = h = 0
        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] < high_arr[h]:
                res_arr.append(low_arr[l])
                l += 1
            else:
                res_arr.append(high_arr[h])
                h += 1
        res_arr += low_arr[l:]
        res_arr += high_arr[h:]
        return res_arr

    @staticmethod
    def quick_sort(param: []):
        arr = param
        if len(arr) < 2:
            return arr
        # pivot = len(arr) - 3 퀵정렬은 빠르지만 불안정 하기 때문에 안전하게 가기 위해 pivot을 mid로 잡아준다
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [], [], []
        # 하나지만 공간을 파티션으로 나누어 준 것 / 각 부분 부분을 할당한다 
        # arr1 = [], arr2 = [], arr3 = [] 공간을 아예 나누어버린 것(벽으로)
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)