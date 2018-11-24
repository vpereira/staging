import unittest
from osc import oscerr
from staged_request import StagedRequest
from mock_commandline_object import MockCommandLineObject


class TestStagedRequestCreation(unittest.TestCase):

    def test_creation(self):
        sr = StagedRequest('staged_requests', MockCommandLineObject(**{}))
        self.assertIsNotNone(sr)
        self.assertEquals(sr.apiurl, 'http://frontend:3000')

    def test_apiurl(self):
        sr = StagedRequest('staged_requests', MockCommandLineObject(
            **{'apiurl': 'http://frontend1:3000'}))
        self.assertIsNotNone(sr)
        self.assertEquals(sr.apiurl, 'http://frontend1:3000')

    def test_wrong_command_raises(self):
        with self.assertRaises(oscerr.WrongArgs):
            StagedRequest('foo', MockCommandLineObject())


if __name__ == '__main__':
    unittest.main()
