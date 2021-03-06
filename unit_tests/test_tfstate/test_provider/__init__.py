# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Unit tests
from unit_tests.test_tfstate.test_provider import test_aws, test_other


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_aws.suite())
    suite.addTests(test_other.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
