import unittest
from osc import oscerr
from staging_project import StagingProject
from mock_commandline_object import MockCommandLineObject


class TestStagingProject(unittest.TestCase):

    def test_creation(self):
        self.assertIsNotNone(StagingProject('staging_projects',
                                            MockCommandLineObject(**{})))

    def test_wrong_command_raises(self):
        with self.assertRaises(oscerr.WrongArgs):
            StagingProject('foo', MockCommandLineObject(**{}))

    def test_url(self):
        sp = StagingProject('staging_projects', MockCommandLineObject(**{}))
        self.assertEquals(sp.url(['foo']), 'http://frontend:3000/foo')
        self.assertEquals(
            sp.url(
                ['foo'], {
                    'description': 'foo'}), 'http://frontend:3000/foo?description=foo')


if __name__ == '__main__':
    unittest.main()
