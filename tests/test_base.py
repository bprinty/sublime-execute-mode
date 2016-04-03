# -*- coding: utf-8 -*-
#
# tests for sublime execute mode
#
# @author <bprinty@gmail.com>
# ----------------------------------------------------------


# imports
# -------
import sublime
from unittest import TestCase

# config
# ------
version = sublime.version()


# testing
# -------
class Base(TestCase):
    """
    Test for all basic functionality.
    """

    def setUp(self):
        self.view = sublime.active_window().new_file()
        s = sublime.load_settings('Preferences.sublime-settings')
        s.set('close_windows_when_empty', False)
        return

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command('close_file')
        return

    def setText(self, string):
        self.view.run_command('insert', {'characters': string})

    def getRow(self, row):
        return self.view.substr(self.view.line(self.view.text_point(row, 0)))

    def selectAll(self):
        return self.view.sel().add(sublime.Region(0, self.view.size()))

    def test_simple_command(self):
        self.setText('\n'.join(['foo', 'bar', 'baz']))
        self.selectAll()
        self.view.run_command('execute_mode_replace', {'cmd': 'grep "bar"'})
        first_row = self.getRow(0)
        self.assertEqual(first_row, 'bar')
        return

    def test_complex_command(self):
        self.setText('\n'.join(['foo', 'bar', 'foo', 'baz']))
        self.selectAll()
        self.view.run_command(
            'execute_mode_replace',
            {'cmd': 'sort | uniq -c | grep "2"'}
        )
        first_row = self.getRow(0)
        self.assertEqual(first_row, '   2 foo')
        return
