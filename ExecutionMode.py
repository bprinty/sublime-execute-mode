# -*- coding: utf-8 -*-
#
# vim execution mode, for sublime.
#
# @author <bprinty@gmail.com>
# ----------------------------------------------------------


# imports
# -------
# external
import sublime, sublime_plugin
import logging
import os
import uuid
import subprocess


# config
# ------
__version__ = '0.0.1'
__author__ = 'bprinty@gmail.com'


# classes
# -------
class ExecutionModeReplaceCommand(sublime_plugin.TextCommand):
    """
    Run bash command for block of highlighted text.
    """

    def run(self, edit, **kwargs):
        """
        Execute replace command for execution mode.
        """
        for region in self.view.sel():
            if not region.empty():
                # write text to file
                cwd = os.path.dirname(os.path.realpath(__file__))
                uu = os.path.join(cwd, str(uuid.uuid1()))
                with open(uu + '-pre', 'w') as fi:
                    fi.write(self.view.substr(region))

                # cat file and pipe into command
                fesc = uu.replace(' ', '\ ')
                proc = subprocess.check_output(
                    'cat {} | SHELL={} {} > {}'.format(fesc + '-pre', 'bash', kwargs['cmd'], fesc + '-post'),
                    shell=True
                )

                # update selection
                with open(uu + '-post', 'r') as fi:
                    self.view.replace(edit, region, fi.read())

                # clean
                os.remove(uu + '-pre')
                os.remove(uu + '-post')
        return


class ExecutionModeCommand(sublime_plugin.WindowCommand):
    """
    Run bash command for block of highlighted text.
    """

    def execute(self, command):
        """
        Execute command through shell.
        """
        if command == '':
            return

        view = self.window.active_view()
        view.run_command('execution_mode_replace', {'cmd': command})
        return

    def run(self):
        """
        Main logic for managing quick panel.
        """
        sublime.set_timeout(lambda: self.window.show_input_panel(
            '~$',
            '',
            self.execute, None, None
        ), 0)
        return

