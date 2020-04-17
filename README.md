# ReCAP Argument Graph Mining

This program has been used to perform the evaluation of our proposed argument mining pipeline.

## System Requirements

- [Docker](www.docker.com) and [Docker-Compose](https://github.com/docker/compose)
- Alternatively: [Python](https://www.python.org) 3.7 and [Poetry](https://python-poetry.org) 1.0

## Installation

- Duplicate the file `config-example.yml` to `config.yml` and adapt the settings to your liking.
- Create the folders `data/input` and `data/output`.
- If using Docker, please do not edit the web server settings.


## Pipeline Usage

Docker will download all required data on the first run and thus may take a while.
Future runs are cached and the app available immediately.

Using **Docker**, start the program with:

```docker-compose run app python -m recap_am.{entrypoint}```

Using **Poetry**, start the program with:

```poetry run python -m recap_am.{entrypoint}```

The following entry points are available:

- `server`: Starts a flask server providing a website to perform interactive mining. The address is printed in the terminal.
- `cli`: Start the pipeline without interaction.
- `evaluate`: Perform a grid computation with the parameters major claim method, relationship type threshold and graph construction method.


## Training the Classifiers

### ADU and Claim/Premise

TODO


### Relationship Type

TODO
