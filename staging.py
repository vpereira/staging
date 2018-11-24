import os
import sys
from osc import cmdln
from osc import oscerr
from osc import conf
from osc import core
from staged_request import StagedRequest
from staging_project import StagingProject


@cmdln.option('-r', '--request', metavar='request',
              help='request to stage/unstage')
@cmdln.option('-m', '--mainproject', metavar='main_staging_project',
              help='staging workflow main project')
@cmdln.option('-p', '--project', metavar='staging_project',
              help='project to stage/unstage the requests from/to')
def do_staging(self, subcmd, opts, *args):
    """${cmd_name}: PoC new staging workflow.

    Options:


    Usage:

        osc staging stage_request -r $REQ -m $MAIN_PROJECT -p $STAGING_PROJECT
        osc staging unstage_request -r $REQ -m $MAI_PROJECT -p $STAGING_PROJECT
        osc staging staged_requests -m $MAIN_PROJECT -p $STAGING_PROJECT
        osc staging staged_projects -p $MAIN_PROJECT

        i.e:
        osc staged_requests -m openSUSE:Factory -p openSUSE:Staging:A
    """

    staged_requests_commands = [
        'stage_request',
        'unstage_request',
        'staged_requests']
    staging_projects_commands = ['staging_projects']

    plugin_name = self.lastcmd[0]

    cmds = staged_requests_commands + staging_projects_commands

    if not args or args[0] not in cmds:
        raise oscerr.WrongArgs(
            'Unknown %s action. Choose one of %s.' %
            (plugin_name, ', '.join(cmds)))

    apiurl = conf.config['apiurl']

    opts.apiurl = apiurl

    cmd = args[0]

    if cmd in staged_requests_commands:
        print StagedRequest(cmd, opts).run()
    else:
        print StagingProject(cmd, opts).run()
