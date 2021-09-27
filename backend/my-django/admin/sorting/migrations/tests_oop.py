import unittest
from admin.sorting.models_oop import Calculator, Grade, Person, Contacts


class TestCalculator(unittest.TestCase):
    cal = Calculator()
    cal.num1 = 8
    cal.num2 = 5

    def test_add(self):
        self.assertEqual(self.cal.add(), 13)

    def test_sub(self):
        self.assertEqual(self.cal.subtract(), 3)

    def test_multi(self):
        self.assertEqual(self.cal.multiple(), 40)

    def test_div(self):
        self.assertEqual(self.cal.divide(), 1.6)

    def test_mod(self):
        self.assertEqual(self.cal.remain(), 3)


class TestGrade(unittest.TestCase):

    def test_grade(self):
        grade = Grade()
        grade.kor = 92
        grade.eng = 78
        grade.math = 85
        self.assertEqual(grade.return_grade(), 'B')


class TestPerson(unittest.TestCase):

    def test_person(self):
        per = Person()
        per.name = "sw"
        per.age = 29
        per.address = "울랄라"
        #print(per.to_string())
        self.assertEqual(per.to_string(), "안녕하세요, 제 이름은sw이고,나이는29,울랄라에서 거주합니다.")

class TestContacts(unittest.TestCase): #getter setter 를 안만드는것은  update를 안할경우에만..

    def test_get_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom', '1234-1234', 'tom@qwe.com', 'Seoul'))
        ls.append(Contacts.set_contact('Jane', '1224-1234', 'jane@qwe.com', 'UK'))
        ls.append(Contacts.set_contact('SSW', '1234-2234', 'sw@qwe.com', 'Busan'))
        ls = Contacts.get_contact(ls)
        # print(ls)
        [print (i.to_string()) for i in ls]
        self.assertEqual(ls[0].name, 'Tom')

    def test_del_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom', '010-1234', 'tom@test.com', 'Seoul'))
        ls.append(Contacts.set_contact('Jane', '1224-1234', 'jane@qwe.com', 'UK'))
        ls.append(Contacts.set_contact('SSW', '1234-2234', 'sw@qwe.com', 'Busan'))
        ls = Contacts.del_contact(ls, 'Tom')
        [print(x.to_string()) for x in ls]
        self.assertEqual(len(ls), 2)


if __name__ == '__main__':
    unittest.main()