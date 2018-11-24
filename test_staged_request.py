import unittest
from osc import oscerr
from staged_request import StagedRequest


class MockCommandLineObject(object):
    def apiurl(self):
        return 'http://frontend:3000'

    def mainproject(self):
        return "1"

    def project(self):
        return "3"

    def request(self):
        return "1"


class TestStagedRequest(unittest.TestCase):

    def test_creation(self):
        self.assertIsNotNone(StagedRequest('staged_requests',
                                           MockCommandLineObject()))

    def test_wrong_command_raises(self):
        with self.assertRaises(oscerr.WrongArgs):
            StagedRequest('foo', MockCommandLineObject())


if __name__ == '__main__':
    unittest.main()
