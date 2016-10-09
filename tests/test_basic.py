# -*- coding: utf-8 -*-

from context import source

import unittest


class BasicTestSuite(unittest.TestCase):
    """Test all import and project structure"""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()
