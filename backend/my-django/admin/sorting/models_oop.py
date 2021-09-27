from dataclasses import dataclass

@dataclass
class Calculator(object):
    num1: int
    num2: int

    @property
    def num1(self) -> int: return self._num1

    @property
    def num2(self) -> int: return self._num2

    @num1.setter
    def num1(self, num1 :int): self._num1 = num1

    @num2.setter
    def num2(self, num2 :int): self._num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def remain(self):
        return self.num1 % self.num2


class Grade(object):
    kor: int
    eng: int
    math: int

    @property
    def kor(self) -> int: return self._kor

    @kor.setter
    def kor(self, kor: int): self._kor = kor

    @property
    def eng(self) -> int: return self._eng

    @eng.setter
    def eng(self, eng: int): self._eng = eng

    @property
    def math(self) -> int: return self._math

    @math.setter
    def math(self, math: int): self._math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def average(self):
        return float(self.sum() / 3)

    def return_grade(self) -> str:
        aver = self.average()
        if aver >= 90:
            return 'A'
        elif aver >= 80:
            return 'B'
        elif aver >= 70:
            return 'C'
        elif aver >= 60:
            return 'D'
        elif aver >= 50:
            return 'E'
        else:
            return 'F'



@dataclass
class Person(object):
    name: str
    age: int
    address: str

    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name : str): self._name = name
    @property
    def age(self) -> int: return  self._age
    @age.setter
    def age(self, age: int): self._age = age
    @property
    def address(self) -> str: return self._address
    @address.setter
    def address(self, address : str): self._address = address



    def to_string(self):
        return f'안녕하세요, 제 이름은{self.name}이고,나이는{self.age},{self.address}에서 거주합니다.'


@dataclass
class Contacts(object):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        return f'이름{self.name},전화번호{self.phone},이메일{self.email},주소{self.address}'

    @staticmethod
    def set_contact(name,phone, email, address) -> object:
        return Contacts(name,phone, email, address)

    @staticmethod
    def get_contact(ls):
        for i in ls:
            i.to_string()
        return ls

    @staticmethod
    def del_contact(ls, name):
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]
        return ls



        '''
        for index, value in enumerate(ls):
            print(index, value)
        return '\t'.join(ls)
        '''


