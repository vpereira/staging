from osc.core import http_GET, makeurl
from osc import oscerr
from xml_parser import XMLParser


class StagingProject(object):
    staging_projects_commands = ['staging_projects']

    def __init__(self, cmd, opts):
        if cmd not in self.staging_projects_commands:
            raise oscerr.WrongArgs('{} not accepted'.format(cmd))
        self.cmd = cmd
        self.main_project = opts.mainproject
        self.apiurl = opts.apiurl

    def url(self):
        return makeurl(
            self.apiurl, [
                'staging', self.main_project, 'staging_projects'])

    def list(self):
        return XMLParser.dump(http_GET(self.url()))

    def run(self):
        if self.cmd == 'staging_projects':
            return self.list()
        else:
            raise oscerr.WrongArgs(
                'Unknown %s action. Choose one of %s.' %
                (self.cmd, ', '.join(staging_projects_commands)))
