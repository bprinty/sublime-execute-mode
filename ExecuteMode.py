# -*- coding: utf-8 -*-
#
# vim execute mode, for sublime.
#
# @author <bprinty@gmail.com>
# ----------------------------------------------------------


# imports
# -------
import sublime
import sublime_plugin
import os
import uuid
import subprocess


# config
# ------
__version__ = '0.0.1'
__author__ = 'bprinty@gmail.com'
settings = sublime.load_settings('ExecuteMode.sublime-settings')


# classes
# -------
class ExecuteModeReplaceCommand(sublime_plugin.TextCommand):
    """
    Run bash command for block of highlighted text.
    """

    def run(self, edit, **kwargs):
        """
        Execute replace command for execute mode.
        """
        for region in self.view.sel():
            if not region.empty():
                # write text to file
                cwd = os.path.dirname(os.path.realpath(__file__))
                uu = os.path.join(cwd, str(uuid.uuid1()))
                with open(uu + '-pre', 'w') as fi:
                    fi.write(self.view.substr(region))

                # write command to script
                shell = settings.get('default_shell', 'bash')
                with open(uu + '.sh', 'w') as fi:
                    fi.write('\n'.join([
                        '#!{}'.format(shell),
                        kwargs['cmd']
                    ]))

                # cat file and pipe into command
                fesc = uu.replace(' ', '\ ')
                subprocess.check_output(
                    'sh {} < {} > {}'.format(
                        fesc + '.sh',
                        fesc + '-pre',
                        fesc + '-post'
                    ),
                    shell=True
                )

                # update selection
                with open(uu + '-post', 'r') as fi:
                    self.view.replace(edit, region, fi.read().rstrip())

                # clean
                os.remove(uu + '-pre')
                os.remove(uu + '-post')
                os.remove(uu + '.sh')
        return


class ExecuteModeCommand(sublime_plugin.WindowCommand):
    """
    Run bash command for block of highlighted text.
    """

    def run(self):
        """
        Main logic for managing window command.
        """
        def execute(command):
            if command == '':
                return
            view = self.window.active_view()
            view.run_command('execute_mode_replace', {'cmd': command})
            return

        sublime.set_timeout(
            lambda: self.window.show_input_panel(
                '~$', '', execute, None, None
            ), 0
        )
        return
