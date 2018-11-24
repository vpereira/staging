from osc.core import makeurl, http_DELETE, http_POST, http_GET
from osc import oscerr
from xml_parser import XMLParser


class StagedRequest(object):

    staged_requests_commands = [
        'stage_request',
        'unstage_request',
        'staged_requests']

    def __init__(self, cmd, opts):
        if cmd not in self.staged_requests_commands:
            raise oscerr.WrongArgs('{} not accepted'.format(cmd))
        self.cmd = cmd
        self.main_project = opts.mainproject
        self.staging_project = opts.project
        self.bs_request = opts.request
        self.apiurl = opts.apiurl

    def url(self):
        return makeurl(self.apiurl,
                       ['staging',
                        self.main_project,
                        'staging_projects',
                        self.staging_project,
                        'staged_requests'])

    def stage(self):
        data = self.request_template()
        return XMLParser.dump(http_POST(self.url(), data=data))

    def unstage(self):
        data = request_template(opts.request)
        return XMLParser.dump(http_DELETE(self.url(), data=data))

    def list(self):
        return XMLParser.dump(http_GET(self.url()))

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
