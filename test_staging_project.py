import unittest
from osc import oscerr
from staging_project import StagingProject


class MockCommandLineObject(object):
    def apiurl(self):
        return 'http://frontend:3000'

    def mainproject(self):
        return "1"

    def project(self):
        return "3"

    def request(self):
        return "1"

class TestStagingProject(unittest.TestCase):

    def test_creation(self):
        self.assertIsNotNone(StagingProject('staging_projects',
                                           MockCommandLineObject()))

    def test_wrong_command_raises(self):
        with self.assertRaises(oscerr.WrongArgs):
            StagingProject('foo', MockCommandLineObject())


if __name__ == '__main__':
    unittest.main()
