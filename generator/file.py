import os
from jinja2 import Environment, FileSystemLoader

def generate_file(path,
                  name,
                  language,
                  version):

    template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), './templates/docker_files'))

    j2_env = Environment(loader=FileSystemLoader(template_folder),
                         trim_blocks=True)

    content = j2_env.get_template(language).render(
        name='Hellow Gist from GutHub',
        image='php7:0-jessie',
        packages=['test', 'testdd']
    )

    print (os.path.join(path, 'Dockerfile'))

    output_path = os.path.join(path, 'Dockerfile')

    with open(output_path, "w") as fh:
        fh.write(content)