import unittest
from unittest.mock import patch

from my_read_cwd import read_cwd


 
class TestReadCwd(unittest.TestCase):


    # the patch creates a special fake object MagicMock object and passes a reference to it
    @patch('my_read_cwd.read_cwd', return_value = "SOME_PATH")
    #mock_cws is my new mocked function
    def test_read_my_cwd(self, mock_cwd):
        test_result = mock_cwd()
        expected_result = 'C:\Appl\BG0VVK_Work\mocking'
        self.assertNotEqual(test_result, expected_result)
        self.assertEqual(test_result, "SOME_PATH")


if __name__ == "main":
    unittest.main()