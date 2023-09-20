import unittest
from unittest.mock import patch

from my_read_input import read_input


 
class TestMyReadInput(unittest.TestCase):


    # the patch creates a special fake object MagicMock object and passes a reference to it
    @patch('my_read_input.read_input', return_value = "TODAY_IS_WEDNESDAY")
    #mock_read_input is my new mocked function
    def test_read_my_cwd(self, mock_read_input):
        test_result = mock_read_input()
        expected_result = 'noinput'
        self.assertNotEqual(test_result, expected_result)
        expected_result2 = 'TODAY_IS_WEDNESDAY'
        self.assertEqual(test_result, expected_result2)


if __name__ == "main":
    unittest.main()