import os
import shutil

from jinja2 import Environment, FileSystemLoader

LANG_PHP = "php"

def generate_docker_file_php(path, options):

    generate_docker_file(LANG_PHP, path, options)

def generate_docker_file(language, path, params):

    template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), './templates/', language))

    # Dockerfile
    jinja2_env = Environment(loader=FileSystemLoader(template_folder), trim_blocks=True)
    content = jinja2_env.get_template('Dockerfile-tpl').render(params)

    docker_file_path = os.path.join(path, 'Dockerfile')
    with open(docker_file_path, "w") as fh:
        fh.write(content)

    # copy docker ignore file
    ignore_src_file = os.path.join(template_folder, '.dockerignore')
    ignore_dst_file = os.path.join(path, '.dockerignore')
    shutil.copy(ignore_src_file, ignore_dst_file)

    # copy docker-data file
    docker_data_path = os.path.join(path, 'docker-data')
    if not os.path.exists(docker_data_path):
        os.mkdir(docker_data_path)
    vhost_src_file = os.path.join(template_folder, 'vhost.conf')
    vhost_dst_file = os.path.join(path, 'docker-data', 'vhost.conf')
    shutil.copy(vhost_src_file, vhost_dst_file)



