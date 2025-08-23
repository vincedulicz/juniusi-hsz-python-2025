import unittest

class MathTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_subtract(self):
        self.assertEqual(10 - 5, 5)

class StringTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_is_upper(self):
        self.assertFalse("HELLO".isupper()) # FAIL

def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(MathTestCase))
    suite.addTest(unittest.makeSuite(StringTestCase))

    return suite

def main():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

main()