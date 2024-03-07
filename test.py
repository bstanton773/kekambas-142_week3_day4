import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution(45,51), "45 is smaller than 51")
    def test_example_two(self):
        self.assertEqual(solution(1,2),"1 is smaller than 2")
    def test_example_three(self):
        self.assertEqual(solution(-3,2), "-3 is smaller than 2")
    def test_example_four(self):
        self.assertEqual(solution(1,1),"1 is equal to 1")
    def test_example_five(self):
        self.assertEqual(solution(100,100),"100 is equal to 100")
    def test_example_six(self):
        self.assertEqual(solution(100,80), "100 is greater than 80")

if __name__ == '__main__':
    unittest.main()