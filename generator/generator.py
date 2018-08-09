import os
import sys
import click

# TODO refactor: @see http://click.pocoo.org/5/advanced/#command-aliases
class Generator(click.MultiCommand):

    def list_commands(self, ctx):
        list = []
        cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                list.append(os.path.basename(filename))
        list.sort()
        return list

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('generator.commands.cmd_' + name, None, None, ['cli'])
        except ImportError:
            return
        return mod.cli