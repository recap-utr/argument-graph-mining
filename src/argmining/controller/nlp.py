import datetime
import logging

import spacy
from spacy.tokens import Doc

from argmining.model.config import config

logger = logging.getLogger(__name__)


# Use this attribute as nlp .parse("text")
parse = spacy.load(config["nlp"]["spacy_model"])
Doc.set_extension("key", default=datetime.datetime.now().isoformat("_"))
