import unittest
from osc import oscerr
from excluded_request import ExcludedRequest
from mock_commandline_object import MockCommandLineObject


class TestStagedRequestCreation(unittest.TestCase):

    def test_creation(self):
        sr = ExcludedRequest('excluded_requests_create', MockCommandLineObject(**{}))
        self.assertIsNotNone(sr)
        self.assertEquals(sr.apiurl, 'http://frontend:3000')

    def test_wrong_command_raises(self):
        with self.assertRaises(oscerr.WrongArgs):
            ExcludedRequest('foo', MockCommandLineObject())


if __name__ == '__main__':
    unittest.main()
