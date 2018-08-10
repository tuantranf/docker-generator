import os
import sys
import click

CMD_PREFIX = 'cmd_'

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))

# TODO refactor: @see http://click.pocoo.org/5/advanced/#command-aliases
class Generator(click.MultiCommand):

    def list_commands(self, ctx):
        list = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(CMD_PREFIX):
                list.append(os.path.basename(filename))
        list.sort()
        return list

    def get_command(self, ctx, name):
        namespace = {}
        fn = os.path.join(cmd_folder, CMD_PREFIX + name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, namespace, namespace)
        return namespace['cli']
