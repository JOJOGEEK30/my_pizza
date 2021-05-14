
import unittest

from tests.test_maker import TestMaker, TestFullMakingGain
from tests.test_fridge import TestFridge, TestFridgeCount

try:
    from tests.test_sauce import TestSauce
except (ModuleNotFoundError, ImportError):
    TestSauce = None


class ValidationTests(unittest.TestCase):
    def test_sauce_feature(self):
        self.assertTrue(TestSauce is not None, msg='Sauce feature not found')


if __name__ == '__main__':
    unittest.main()
