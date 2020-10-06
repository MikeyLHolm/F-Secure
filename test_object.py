import unittest
from response import ResponseInfo

class TestResponseObject(unittest.TestCase):

    def setUp(self):
        self.obj1 = ResponseInfo('2020-10-06 14:51:29.613189', 'https://www.f-secure.com/fi', 200, 'OK', 0.05)
        self.obj2 = ResponseInfo('2020-10-06 14:51:30.144380', 'http://www.foobar.com/login', 403, 'Forbidden', 0.23)

    def test_url(self):
        print('\ntest_url')
        self.assertEqual(self.obj1.url, 'https://www.f-secure.com/fi')
        self.assertEqual(self.obj2.url, 'http://www.foobar.com/login')
        self.obj2.url = 'http://www.foobar.com/n'
        self.assertEqual(self.obj2.url, 'http://www.foobar.com/')

    def test_status_msg(self):
        print('\ntest_status_message')
        self.assertEqual(self.obj1.status_msg, 'OK')
        self.assertEqual(self.obj2.status_msg, 'Forbidden')

        self.obj1.status_msg = 'SUPERB'
        self.obj2.status_msg = 'REKT'

        self.assertEqual(self.obj1.status_msg, 'SUPERB')
        self.assertEqual(self.obj2.status_msg, 'REKT')

    def test_response_code(self):
        print('\ntest_response_code')
        self.assertEqual(self.obj1.status_code, 200)
        self.assertEqual(self.obj2.status_code, 201)

    def test_response_time(self):
        print('\ntest_response_time')
        self.assertAlmostEqual(self.obj1.response_time, 0.049, delta=0.01)
        self.assertEqual(self.obj2.response_time, 0.23)

if __name__ == '__main__':
    unittest.main()