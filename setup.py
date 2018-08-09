from setuptools import setup

setup(
    name='docker-generator',
    version='1.0',
    packages=['dgen', 'dgen.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        dgen=dgen.cli:cli
    ''',
)
