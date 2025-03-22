# ReCAP Argument Graph Mining

This program has been used to perform the evaluation of our proposed argument mining pipeline.

## System Requirements

- [Docker](www.docker.com) and [Docker-Compose](https://github.com/docker/compose)
- Alternatively: [uv](https://github.com/astral-sh/uv)

## Installation

- Duplicate the file `config-example.yml` to `config.yml` and adapt the settings to your liking.
- Create the folders `data/input` and `data/output`.
- If using Docker, please do not edit the web server settings.

## Pipeline Usage

Docker will download all required data on the first run and thus may take a while.
Future runs are cached and the app available immediately.

Using **Docker**, start the program with:

`docker-compose run argmining-{entrypoint}`

Using **uv**, start the program with:

```uv run argmining-{entrypoint}```

The following entry points are available:

- `app`: Starts a flask server providing a website to perform interactive mining. The address is printed in the terminal.
- `grpc`: Starts a gRPC server to perform mining via API using the [arg-services](https://github.com/recap-utr/arg-services) library.
- `eval`: Perform a grid computation with the parameters major claim method, relationship type threshold and graph construction method.

Per default, the program will look for input data in `data/input`.
If you just want to convert plain text to argument graph, a `.txt` file is enough.
If you want to compare a benchmark graph to the generated on, please provide a `.json` file conforming to the [OVA-format](http://ova.uni-trier.de).


## Linguistic Features

| Category   | Features                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------------|
| Structural | Punctuation, sentence length and position.                                                                       |
| Indicators | Claim-premise and first-person indicators.                                                                       |
| Syntactic  | Depth of constituency parse trees, presence of modal verbs, number of grammatical productions in the parse tree. |
| Embeddings | GloVe sentence embeddings (arithmetic mean of its word vectors).                                                 |

## Training the Classifiers

### ADU and Claim/Premise

To start training, run the program with:

`uv run -m argmining.adu.training.train_adu`

or

`uv run -m argmining.adu.training.train_clpr`

for the ADU or Claim/Premise classifier respectively.

### Relationship Type

Start the jupyter notebook `argmining/preprocessing/pipeline.ipynb` within the container:

- Run cells & import libraries.
- Load your CSV data with the rows `child, parent, stance` into a DataFrame `df`.
- Run the following call to generate a dataset using GloVe Embeddings for either "english" or "german": `data = prep_dataset(df, model = "glove", language = "english")`.
- Use `data` to train any classifier.
