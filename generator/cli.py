import click

from context import Context
from generator import Generator

CONTEXT_SETTINGS = dict(
    auto_envvar_prefix='DGEN',
    ignore_unknown_options=True,
)
pass_context = click.make_pass_decorator(Context, ensure=True)

@click.command(cls=Generator, context_settings=CONTEXT_SETTINGS)
@click.option('--home', type=click.Path(exists=True, file_okay=False, resolve_path=True),
              help='Changes the folder to operate on.')
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@pass_context
def cli(ctx, verbose, home):
    """A generator command line interface."""
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home
