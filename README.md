# ReCAP Argument Graph Mining

This program has been used to perform the evaluation of our proposed argument mining pipeline.

## Installation

- Install [uv](https://github.com/astral-sh/uv).
- Change any settings by overriding their values in a file called `settings.local.toml`.
- Create the folders `data/input` and `data/output`.
- If using Docker, please do not edit the web server settings.

## Usage

`uv run argmining`

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
