from apps.common.mathUtils import MathUtils
import unittest

class MathTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = MathUtils()

    def tearDown(self):
        pass

    def test_add(self):
        result = self.app.add( 1, 2 )
        print("res = ", result )
        self.assertEqual(result, 3)