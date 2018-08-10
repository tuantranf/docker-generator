import click

from generator.context import pass_context
from generator.generator import Generator

@click.command(cls=Generator)
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose mode.')

@pass_context
def cli(ctx, verbose):
    """A generator command line interface."""
    ctx.verbose = verbose