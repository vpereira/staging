from staging_base import StagingBase
from xml_parser import XMLParser
from osc.core import http_POST, http_DELETE
from osc import oscerr


class ExcludedRequest(StagingBase):

    commands = [
        'excluded_requests_create',
        'excluded_requests_delete']

    def __init__(self, cmd, opts):
        if cmd not in self.commands:
            raise oscerr.WrongArgs('{} not accepted'.format(cmd))
        super(self.__class__, self).__init__(cmd, opts)

    def create(self):
        return XMLParser.dump(
            http_POST(
                self.url(
                    [
                        'staging', self.main_project, 'excluded_requests', self.request], {
                        'description': 'excluded'})))

    def delete(self):
        return XMLParser.dump(http_DELETE(
            self.url(['staging', self.main_project, 'excluded_requests', self.request])))

    def run(self):
        if self.cmd == 'excluded_requests_create':
            return self.create()
        elif self.cmd == 'excluded_requests_delete':
            return self.delete()
        else:
            raise oscerr.WrongArgs(
                'Unknown %s action. Choose one of %s.' %
                (self.cmd, ', '.join(self.commands)))
