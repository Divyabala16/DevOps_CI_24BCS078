import sys
sys.path.append("src")

import unittest
from app import calculate_average, get_result

class TestApp(unittest.TestCase):
      def test_calculate_average(self):
          self.assertEqual(calculate_average([80, 75, 90, 65, 85]), 79.0)
      def test_pass_result(self):
          self.assertEqual(get_result(79.0), "Pass")
      def test_fail_reult(self):
          self.assertEqual(get_result(40.0), "Fail")
      def test_zero_average(self):
          self.assertEqual(calculate_average([0,0,0,0]),0.0)
if __name__ == "__main__":
    unittest.main()


