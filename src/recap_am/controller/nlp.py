import datetime
import logging

import spacy
from spacy.tokens import Doc

from recap_am.model.config import Config

logger = logging.getLogger(__name__)
config = Config.get_instance()

# Use this attribute as nlp .parse("text")
parse = spacy.load(config["nlp"]["spacy_model"])
Doc.set_extension("key", default=datetime.datetime.now().isoformat("_"))
