import os
import click
from yaml import load, dump

from generator.context import pass_context
from generator.file import generate_docker_file_php

@click.command('new', short_help='Generate new docker setup.')
@click.option('--config', type=click.File('r'))
@click.argument('path', required=False, default=".", type=click.Path(resolve_path=True))

@pass_context
def cli(
        ctx,
        path,
        config
   ):
    """Initializes a repository."""
    if path is None:
        path = ctx.home

    config_data = load(config)
    options = dict(
        name=config_data.get('name', 'docker-sample'),
        maintainer=config_data.get('maintainer', lambda: os.environ.get('USER', '')),
    )

    ctx.log('Initialized docker setup in %s', click.format_filename(path))
    ctx.log('Project name %s', config_data['name'])
    ctx.log('Language %s', config_data['language'])
    ctx.log('Maintainer %s', config_data['maintainer'])

    if config_data['language'] == 'php':
        generate_docker_file_php(path, options)
    else:
        click.echo('Language not found. Skip.')

    click.echo('Done.')
