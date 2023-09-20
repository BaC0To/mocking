import unittest
from unittest.mock import patch

from my_print import printing_function


 
class TestMyPrintFunction(unittest.TestCase):


    # the patch creates a special fake object MagicMock object and passes a reference to it
    @patch('my_print.printing_function', return_value = "SOMETHING_PRINTED")
    #mock_print is my new mocked function
    def test_read_my_cwd(self, mock_print):
        test_result = mock_print("noinput")
        expected_result = 'noinput'
        self.assertEqual(test_result, expected_result)


if __name__ == "main":
    unittest.main()