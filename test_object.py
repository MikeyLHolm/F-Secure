import unittest
from response import ResponseInfo

class TestResponseObject(unittest.TestCase):

    def setUp(self):
        self.obj1 = ResponseInfo('2020-10-06 14:51:29.613189', 'https://www.f-secure.com/fi', 200, 'OK', 0.05, 'long text of doom')
        self.obj2 = ResponseInfo('2020-10-06 14:51:30.144380', 'http://www.foobar.com/login', 403, 'Forbidden', 0.23, 'even longer text of doom')

    def test_date_time(self):
        print('\ntest_date_time')
        self.assertEqual(self.obj1.date_time, '2020-10-06 14:51:29.613189')
        self.assertEqual(self.obj2.date_time, '2020-10-06 14:51:30.144380')

        self.obj1.date_time = '2020-10-06 14:51:30.144380'
        self.obj2.date_time = '2020-10-06 14:51:29.613189'

        self.assertEqual(self.obj1.date_time, '2020-10-06 14:51:30.144380')
        self.assertEqual(self.obj2.date_time, '2020-10-06 14:51:29.613189')

    def test_url(self):
        print('\ntest_url')
        self.assertEqual(self.obj1.url, 'https://www.f-secure.com/fi')
        self.assertEqual(self.obj2.url, 'http://www.foobar.com/login')

        self.obj1.url = 'https://www.f-secure.com/'
        self.obj2.url = 'http://www.foobar.com/'

        self.assertEqual(self.obj1.url, 'https://www.f-secure.com/')
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
        self.assertEqual(self.obj2.status_code, 403)

        self.obj1.status_code = 202
        self.obj2.status_code = 404

        self.assertEqual(self.obj1.status_code, 202)
        self.assertEqual(self.obj2.status_code, 404)

    def test_response_time(self):
        print('\ntest_response_time')
        self.assertAlmostEqual(self.obj1.response_time, 0.049, delta=0.01)
        self.assertEqual(self.obj2.response_time, 0.23)

        self.obj1.response_time = 0.02
        self.obj2.response_time = 0.2

        self.assertEqual(self.obj1.response_time, 0.02)
        self.assertAlmostEqual(self.obj2.response_time, 0.18, delta=0.03)

    def test_response_text(self):
        print('\ntest_response_text')
        self.assertEqual(self.obj1.txt, 'long text of doom')
        self.assertEqual(self.obj2.txt, 'even longer text of doom')

        self.obj1.txt = 'short'
        self.obj2.txt = 'shrt'

        self.assertEqual(self.obj1.txt, 'short')
        self.assertEqual(self.obj2.txt, 'shrt')

if __name__ == '__main__':
    unittest.main()