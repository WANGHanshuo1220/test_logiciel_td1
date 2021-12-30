import ex1
import unittest

class test(unittest.TestCase):
    def test_cal_moyenne(self):
        self.assertEqual(ex1.cal_moyenne([1, 2, 3, 4, 5]), 3)
        self.assertEqual(ex1.cal_moyenne([10, 2, 3, 1]), 4)
        self.assertEqual(ex1.cal_moyenne([1, 2, 3, 4]), 2.5)
        self.assertEqual(ex1.cal_moyenne([1, 0, 0, 0]), 0.25)


    def test_cal_mediane(self):
        self.assertEqual(ex1.cal_mediane([1, 2, 3, 4, 5]), 3)
        self.assertEqual(ex1.cal_mediane([10, 2, 3, 1]), 2.5)
        self.assertEqual(ex1.cal_mediane([1, 2, 3, 4, 1, 2]), 2)
        self.assertEqual(ex1.cal_mediane([1, 0, 0, 0]), 0)


    def test_cal_ecart(self):
        self.assertEqual(ex1.cal_ecart([1, 2, 3, 4, 5]), 10)
        self.assertEqual(ex1.cal_ecart([10, 2, 3, 1]), 50)
        self.assertEqual(ex1.cal_ecart([1, 2, 3, 4]), 5)
        self.assertEqual(ex1.cal_ecart([1, 0, 0, 0]), 0.75)


    def test_is_geometrique(self):
        self.assertEqual(ex1.is_geometrique([1, 2, 4, 8, 16]), True)
        self.assertEqual(ex1.is_geometrique([10, 2, 3, 1]), False)
        self.assertEqual(ex1.is_geometrique([2, -2, 2, -2, 2]), True)
        self.assertEqual(ex1.is_geometrique([1, 0, 0, 0]), False)


    def test_is_arithmetique(self):
        self.assertEqual(ex1.is_arithmetique([1, 2, 3, 4, 5]), True)
        self.assertEqual(ex1.is_arithmetique([10, 2, 3, 1]), False)
        self.assertEqual(ex1.is_arithmetique([2, 1, 0, -1, -2]), True)
        self.assertEqual(ex1.is_arithmetique([1, 0, 0, 0]), False)


    def test_is_geometrique2(self):
        self.assertEqual(ex1.is_geometrique2(3, [1, 2, 4, 8, 16]), (True, [32, 64, 128]))
        self.assertEqual(ex1.is_geometrique2(1, [10, 2, 3, 1]), False)
        self.assertEqual(ex1.is_geometrique2(2, [2, -2, 2, -2, 2]), (True, [-2, 2]))
        self.assertEqual(ex1.is_geometrique2(1, [1, 0, 0, ]), False)


    def test_is_arithmetique2(self):
        self.assertEqual(ex1.is_arithmetique2(2, [1, 2, 3, 4, 5]), (True, [6, 7]))
        self.assertEqual(ex1.is_arithmetique2(1, [10, 2, 3, 1]), False)
        self.assertEqual(ex1.is_arithmetique2(3, [2, 1, 0, -1, -2]), (True, [-3, -4, -5]))
        self.assertEqual(ex1.is_arithmetique2(1, [1, 0, 0, 0]), False)


if __name__ == "__main__":
    unittest.main()