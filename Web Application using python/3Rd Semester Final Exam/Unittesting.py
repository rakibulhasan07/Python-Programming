# import unittest

# def add(a, b):
#     return a + b

# class TestMyMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(0, 0), 0)

# if __name__ == '__main__':
#     unittest.main()






import unittest
def add(a, b):
     return a - b 
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 2)
if __name__ == "__main__":
    unittest.main()