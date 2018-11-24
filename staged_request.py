from osc.core import makeurl, http_DELETE, http_POST, http_GET
from osc import oscerr
from xml_parser import XMLParser
from staging_base import StagingBase


class StagedRequest(StagingBase):

    staged_requests_commands = [
        'stage_request',
        'unstage_request',
        'staged_requests']

    def __init__(self, cmd, opts):
        if cmd not in self.staged_requests_commands:
            raise oscerr.WrongArgs('{} not accepted'.format(cmd))
        super(self.__class__, self).__init__(cmd, opts)

    def stage(self):
        data = self.request_template()
        return XMLParser.dump(
            http_POST(
                self.url(
                    [
                        'staging',
                        self.main_project,
                        'staging_projects',
                        self.staging_project,
                        'staged_requests']),
                data=data))

    def unstage(self):
        data = request_template(opts.request)
        return XMLParser.dump(
            http_DELETE(
                self.url(
                    [
                        'staging',
                        self.main_project,
                        'staging_projects',
                        self.staging_project,
                        'staged_requests']),
                data=data))

    def list(self):
        return XMLParser.dump(
            http_GET(
                self.url(
                    [
                        'staging',
                        self.main_project,
                        'staging_projects',
                        self.staging_project,
                        'staged_requests'])))

    def run(self):
        if self.cmd == 'stage_request':
            return self.stage()
        elif self.cmd == 'unstage_request':
            return self.unstage()
        elif self.cmd == 'staged_requests':
            return self.list()
        else:
            raise oscerr.WrongArgs(
                'Unknown %s action. Choose one of %s.' %
                (self.cmd, ', '.join(staged_requests_commands)))

    def request_template(self):
        return '<requests><number>{0}</number></requests>'.format(
            self.bs_request)
