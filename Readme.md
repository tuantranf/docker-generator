# dgen: Docker configuration generator

## Python version

```bash
$ python3 -m venv env
$ source env/bin/activate
$ python --version
$ pip install -r requirements.txt
```

## Usage:
```bash
  $ git clone [REPOSITORY_URL]
  $ cd docker-generator
  $ pip install --editable .
  $ dgen --help
```

## Generate docker config from YAML file

### Config file

Set project name, maintainer, programing language
* Only support php 7.1 now

```YAML
# examples/test.yml
name: "sample"
maintainer: "username"
language: "php"
```

### Generate

```bash
$ cd examples
$ dgen --config test.yml
Initialized docker setup in /Users/tranminhtuan/ws-podder/click/examples/docker-generator/examples
Project name sample
Language php
Maintainer username
Done.
$ ls
Dockerfile	docker-data/	test.yml
```

### Set output path

```Bash
$ dgen --config [CONFIG_FILE_PATH] [YOUR PATH]
$ dgen --config examples/test.yml examples

```