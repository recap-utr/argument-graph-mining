# ReCAP Argument Graph Mining

This program has been used to perform the evaluation of our proposed argument mining pipeline.

## System Requirements

- [Docker](www.docker.com) and [Docker-Compose](https://github.com/docker/compose)
- Alternatively: [Python](https://www.python.org) 3.7 and [Poetry](https://python-poetry.org) 1.0

## Installation

- Duplicate the file `config-example.yml` to `config.yml` and adapt the settings to your liking.
- Create the folders `data/input` and `data/output`.
- Please do not edit the webserver settings as Docker depends on them.


## Pipeline Usage

Docker will download all required data on the first run and thus may take a while.
Future runs are cached and the app available immediately.

Using Docker, the program is run with:

```docker-compose run app python -m recap_am.{entrypoint}```

With poetry, you can invoke it using:

```poetry run python -m recap_am.{entrypoint}```

The following entry points are available

- `server`: Starts a flask server providing a website to start the mining. The address is printed in the terminal.
- `cli`: Start the pipeline based on the contents of `config.toml`.
- `evaluate`: Perform a grid computation with the parameters major claim method, relationship type threshold and graph construction method.

## Training the Classifiers

### ADU and Claim/Premise

TODO: Sean


### Relationship Type

TODO: Premtim
