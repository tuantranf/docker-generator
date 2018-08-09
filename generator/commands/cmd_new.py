import os
import click

from generator.cli import pass_context
from generator.file import generate_file

@click.command('new', short_help='Generate new docker setup.')
@click.option('--dryrun', required=False, default=False, type=bool)
@click.option('--name',
              prompt='Project\'s name',
              default="sample",
              help='Project\'s name')
@click.option('--maintainer',
              prompt='The maintainer\'s name',
              default=lambda: os.environ.get('USER', ''),
              help='The maintainer\'s name'
              )
@click.option('--email',
              prompt='The developer\'s email address',
              default="test@test.com",
              help='The developer\'s email address'
              )
# TODO show a select list here
@click.option('--language',
              prompt='Programing language',
              default="PHP",
              help='Programing language'
              )
# TODO using dynamic options here @see https://github.com/pallets/click/issues/72
@click.option('--version',
              prompt='PHP version',
              default="5.6",
              help='PHP version'
              )
@click.argument('path', required=False, default=".", type=click.Path(resolve_path=True))
@pass_context
def cli(
        ctx,
        path,
        dryrun,
        name,
        maintainer,
        email,
        language,
        version
   ):
    """Initializes a repository."""
    if path is None:
        path = ctx.home
    ctx.log('Initialized docker setup in %s', click.format_filename(path))
    ctx.log('Dryrun %s', dryrun)
    ctx.log('Project name %s', name)
    ctx.log('Maintainer %s', maintainer)
    ctx.log('Email in %s', email)
    ctx.log('Language %s', language)
    ctx.log('Version %s', version)
    click.echo('Changed credentials.')

    language = language.lower();
    if language == 'php':
        generate_file(path, name, language, version)
    click.echo('Create ./Dockerfile')

