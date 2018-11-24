class MockCommandLineObject(object):
    def __init__(self, **args):
        if 'apiurl' in args:
            self._apiurl = args['apiurl']
        else:
            self._apiurl = 'http://frontend:3000'

        if 'mainproject' in args:
            self._mainproject = args['mainproject']
        else:
            self._mainproject = None

        if 'project' in args:
            self._project = args['project']
        else:
            self._project = None

        if 'request' in args:
            self._request = args['request']
        else:
            self._request = None

    @property
    def apiurl(self):
        return self._apiurl

    @property
    def mainproject(self):
        return self._mainproject

    @property
    def project(self):
        return self._project

    @property
    def request(self):
        return self._request
