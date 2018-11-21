import unittest
import Students
import Student
from Constants import TEXT


class TestStudentMethods(unittest.TestCase):

    def setUp(self):
        a = Students.Students()
        a.to_read(TEXT)
        self.a = a

    def test_validation(self):
        self.assertEqual(Student.Student("Tony", "Star", "Dacota", "22", "23", "3 4 3 4 5",
                         Student.Student("Tony21", "St2r", "Dac@ta", "twenty second", "101", "-1 4 3 10 b")))

    def test_search(self):
        to_find = Student.Student("David", "Kemeron", "Toronto", "24", "23", "4 4 4 3 5")
        self.assertEqual(len(self.a.r_search(("0"))), 3)
        self.assertEqual(len(self.a.r_search(("David"))), 1)
        self.assertEqual(len(self.a.r_search(("Toronto"))), 2)
        self.assertEqual(len(self.a.r_search(("TORONTO"))), 2)
        self.assertEqual(len(self.a.r_search(("San Diego"))), 0)
        self.assertIn(to_find, [self.a.data[x] for x in self.a.r_search("da")])

    def test_add(self):
        self.assertEqual(len(self.a), 5)
        added = self.a.add_node()
        self.assertEqual(len(self.a), 6)
        self.assertIn(added, self.a.data)

    def test_remove(self):
        self.assertEqual(len(self.a), 6)
        deleted = self.a.remove_node()
        self.assertEqual(len(self.a), 5)
        self.assertNotIn(deleted, self.a.data)

    def test_sort(self):
        self.assertEqual(self.a.sort(lambda x : x.average_mark()), sorted(self.a.data, key = lambda x : x.average_mark()))
        self.assertEqual(self.a.sort(lambda x : x.surname), sorted(self.a.data, key = lambda x : x.surname))
        self.assertEqual(self.a.sort(lambda x : x.group), sorted(self.a.data, key = lambda x : x.group))

    def test_change(self):
        changed = self.a.change()
        self.assertNotIn(changed, self.a.data)


if __name__ == '__main__':
    unittest.main()
