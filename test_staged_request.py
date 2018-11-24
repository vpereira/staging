import unittest
from osc import oscerr
from staged_request import StagedRequest


class MockCommandLineObject(object):
    def __init__(self, **args):
        if 'apiurl' in args:
            self._apiurl = args['apiurl']
        else:
            self._apiurl = 'http://frontend:3000'

    @property
    def apiurl(self):
        return self._apiurl

    def mainproject(self):
        return "1"

    def project(self):
        return "3"

    def request(self):
        return "1"


class TestStagedRequestCreation(unittest.TestCase):

    def test_creation(self):
        sr = StagedRequest('staged_requests', MockCommandLineObject(**{}))
        self.assertIsNotNone(sr)
        self.assertEquals(sr.apiurl, 'http://frontend:3000')

    def test_apiurl(self):
        sr = StagedRequest('staged_requests', MockCommandLineObject(**{'apiurl': 'http://frontend1:3000'}))
        self.assertIsNotNone(sr)
        self.assertEquals(sr.apiurl, 'http://frontend1:3000')

    def test_wrong_command_raises(self):
        with self.assertRaises(oscerr.WrongArgs):
            StagedRequest('foo', MockCommandLineObject())


if __name__ == '__main__':
    unittest.main()
