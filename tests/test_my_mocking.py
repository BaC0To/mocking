import unittest
from unittest import mock
from unittest.mock import MagicMock
import tempfile
import os
import shutil
from unittest.mock import patch
from my_print import printing_function, read_input, get_cwd

 
class TestMyPrintFunction(unittest.TestCase):


    def test_print1(self):
        with patch('builtins.print') as mock_print:
            printing_function('TEST_PRINT')
            mock_print.assert_called_with('TEST_PRINT')
        
    @patch('builtins.print')
    def test_print2(self, mock_print):
        printing_function('TEST_PRINT')
        mock_print.assert_called_with('TEST_PRINT')

    def test_print3(self):
        mock_print = MagicMock()
        with patch('builtins.print') as mock_print:
            printing_function('TEST_PRINT')
            mock_print.assert_called_with('TEST_PRINT')
            mock_print.assert_called()
            mock_print.assert_called_once()
    

class TestInputFunction(unittest.TestCase):


    def test_input1(self):
        with patch('builtins.input', return_value = 'test'):
            self.assertTrue(read_input()=='test')

    @patch('builtins.input', lambda *args: 'test')
    def test_input2(self):
        self.assertTrue(read_input()=='test')

    @patch('builtins.input', return_value = 'test')
    def test_input3(self, mock_input):
        self.assertTrue(read_input()=='test')
        #assert mock_input.called()

    def test_input4(self):
        mock_input = MagicMock(return_value = 'test')
        with patch('builtins.input', mock_input):
            self.assertTrue(read_input()=='test')

    def test_input5(self):
        with patch('builtins.input') as mock_input:
            mock_input.return_value = 'test'
            self.assertTrue(read_input()=='test')


class TestCWD(unittest.TestCase):


    def setUp(self) -> None:
        self.temp_dir = tempfile.mkdtemp()
        print(self.temp_dir)
    
    def tearDown(self) -> None:
        if os.path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_cwd(self):
        with patch('os.getcwd', return_value = self.temp_dir):
            self.assertTrue(get_cwd()==self.temp_dir)



if __name__ == "main":
    unittest.main()