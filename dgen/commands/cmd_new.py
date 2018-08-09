import click
from complex.cli import pass_context


@click.command('new', short_help='Generate new docker setup.')
@click.argument('path', required=False, type=click.Path(resolve_path=True))
@click.option('--maintainer', prompt=True,
              help='The maintainer\'s name.')
@click.option('--email', prompt='E-Mail',
              help='The developer\'s email address')
@pass_context
def cli(ctx, path, username, email):
    """Initializes a repository."""
    if path is None:
        path = ctx.home
    ctx.log('Initialized docker setup in %s', click.format_filename(path))
    ctx.log('Initialized docker setup in %s', username)
    click.echo('Changed credentials.')
