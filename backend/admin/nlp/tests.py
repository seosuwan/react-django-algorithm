from django.test import TestCase
if __name__ == '__main__':
    #방법 1
    dc1 = {}
    dc2 = {}
    dc3 = {}

    ls1 = ['10', '20', '30', '40', '50']
    ls2 = [10, 20, 30, 40, 50]

    # for i in range(0, len(ls1)):
    #     dc1[ls1[i]] = ls2[i]
    dc1 = {ls1[i]: ls2[i] for i in range(0, len(ls1))}
    #zip 방법
    # for i, j in zip(ls1, ls2):
    #     dc2[j] = j
    dc2 = {i:j for i, j in zip(ls1, ls2)}
    # for i, j in enumerate(ls1):
    #     dc3[j] = ls2[i]
    dc3 = {j:ls2[i] for i, j in enumerate(ls1)}
    print('*'*30)
    print(dc1)
    print('*'*30)
    print(dc2)
    print('*' * 30)
    print(dc3)
# Create your tests here.
