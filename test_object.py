import unittest
from response import ResponseInfo

class TestResponseObject(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.obj1 = ResponseInfo('2020-10-06 13:59:02.668667', 'https://www.f-secure.com/fi', 200, 'OK', 0.05)

    def test_response_code(self):
        print('test_response_code')
        self.assertEqual(self.obj1.status_code, 200)

    def test_response_time(self):
        print('test_response_time')
        self.assertAlmostEqual(self.obj1.response_time, 0.049, delta=0.01)

if __name__ == '__main__':
    unittest.main()