import os
from jinja2 import Environment, FileSystemLoader

TYPE_DOCKER_FILE = 1

def generate_docker_file(path,
                  name,
                  language,
                  version):

    params = dict(
        name=name,
        language=language,
        image='php7:0-jessie',
        packages=['test', 'testdd']
    )

    generate_file(TYPE_DOCKER_FILE, path, params)

def generate_file(type,
                  path,
                  params
                  ):

    template_folder = ''
    output_path = ''
    if type == TYPE_DOCKER_FILE:
        template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), './templates/docker_files'))
        output_path = os.path.join(path, 'Dockerfile')

    jinja2_env = Environment(loader=FileSystemLoader(template_folder), trim_blocks=True)
    content = jinja2_env.get_template(params['language']).render(params)

    with open(output_path, "w") as fh:
        fh.write(content)