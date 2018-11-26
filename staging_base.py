from osc.core import makeurl


class StagingBase(object):
    def __init__(self, cmd, opts):
        self.cmd = cmd
        self.main_project = opts.mainproject
        self.apiurl = opts.apiurl
        self.project = opts.project
        self.request = opts.request

    def url(self, *args, **kargs):
        return makeurl(self.apiurl, *args)
