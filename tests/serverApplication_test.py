from apps.serverApplication import app
import unittest

class ErrorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_pagenotfound_statuscode(self):
        result = self.app.get('/missing-page')
        self.assertEqual(result.status_code, 404)

    def test_pagenotfound_data(self):
        result = self.app.get('/missing-page')
        print( "error = ", result.data )
        self.assertIn('404 NOT FOUND', str(result.data))

    # def test_unhandledexception_statuscode(self):
    #     result = self.app.put('/user/tts')
    #     self.assertEqual(result.status_code, 500)
