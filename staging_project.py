from osc.core import http_GET, makeurl
from osc import oscerr
from xml_parser import XMLParser
from staging_base import StagingBase


class StagingProject(StagingBase):

    commands = ['staging_projects', 'staging_project']

    def __init__(self, cmd, opts):
        if cmd not in self.commands:
            raise oscerr.WrongArgs('{} not accepted'.format(cmd))
        super(self.__class__, self).__init__(cmd, opts)

    def show(self):
        return XMLParser.dump(http_GET(
            self.url(['staging', self.main_project, 'staging_projects', self.project])))

    def list(self):
        return XMLParser.dump(
            http_GET(self.url(['staging', self.main_project, 'staging_projects'])))

    def run(self):
        if self.cmd == 'staging_projects':
            return self.list()
        else:
            raise oscerr.WrongArgs(
                'Unknown %s action. Choose one of %s.' %
                (self.cmd, ', '.join(self.commands)))
