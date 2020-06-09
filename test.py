import unittest
from unittest import TestCase
from mock import patch, Mock
 
class UserTest(TestCase):

    @patch("inherited.Inherited")
    def test_read(self, mock_b):
        mock_b.read.return_value = "mocked"
 

if __name__ == '__main__':
    unittest.main()
