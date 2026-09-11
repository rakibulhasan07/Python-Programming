import unittest

# 1. unit case class create
class TestMyMath(unittest.TestCase):
    
    # 2.seting or setup oishik
    def setUp(self):
        self.value = 10

    # 3. test method ( obossoi 'test' method diye suru hobe )
    def test_addition(self):
        result = self.value + 5
        self.assertEqual(result, 15) # Assertion

    # 4. cleaning or teardown method
    def tearDown(self):
        
        pass
if __name__ == '__main__':
    unittest.main()