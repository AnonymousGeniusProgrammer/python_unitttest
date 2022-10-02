import unittest
from unittest.mock import patch
import calc


class TestCalc(unittest.TestCase):

    # run once for the whole test class, put some expensive loading writing operations here
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # run before every test, use instance variables
    def setUp(self):
        self.x = 10
        self.y = 5
        pass

    # run after every test
    def tearDown(self):
        pass
    
    # this naming convention is required
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_devide(self):
        # self.assertRaises(ValueError, calc.devide, 10, 0)
        # instead of using this, we could use context manager 
        with self.assertRaises(ValueError):
            calc.divide(10,0)
    def test_mock_up(self):
        with patch('calc.requests.get') as mocked_get:
            # this mocked part of the method requestData
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            request_data = calc.requestData('June')
            mocked_get.assert_called_with('http://company.com/June')
            self.assertEqual(request_data, 'Success')

            mocked_get.return_value.ok = False

            request_data = calc.requestData('Janary')
            mocked_get.assert_called_with('http://company.com/Janary')
            self.assertEqual(request_data, 'Bad Response!')
            

if __name__ == "__main__":
    unittest.main()
