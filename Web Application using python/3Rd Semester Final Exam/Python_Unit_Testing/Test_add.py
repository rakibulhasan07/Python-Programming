# ### Python Built-in `unittest` ব্যবহার করে Unit Testing


# import unittest

# def add(a, b):
#     return a + b

# class TestAdd(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(add(5, 3), 8)

# if __name__ == "__main__":
#     unittest.main()

# # ### Output

# ```text
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
# ```

# **ব্যাখ্যা:**
# `unittest` দিয়ে `add()` Function-টি পরীক্ষা করা হয়েছে। `assertEqual()` দিয়ে Expected Result `8` এবং Actual Result একই কি না যাচাই করা হয়েছে।

import unittest


class TestMyMath(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_additon(self):
        result = self.a + 5
        self.assertEqual(result, 15) #Assertion

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
