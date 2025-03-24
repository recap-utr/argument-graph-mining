import pickle
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Union

import numpy as np
from sklearn.linear_model import LogisticRegression
from spacy.tokens import Doc, Span

from argmining.model.config import config
from argmining.relation.model.relation import Relation, RelationClass


def classify(adus: Iterable[Union[Doc, Span]]) -> Dict[str, List[Relation]]:
    model = _load_model()
    classification = {}

    for adu1 in adus:
        classification[adu1.text] = list()

        for adu2 in adus:
            if adu1 != adu2:
                sample = _transform(adu1, adu2)
                pred_type, pred_prob = _predict(sample, model)
                classification[adu1.text].append(
                    Relation(adu2.text, pred_prob, pred_type)
                )

    return classification


def _load_model():
    if config["nlp"]["language"] == "en":
        model_path = Path(config["relation"]["en_model"])
    elif config["nlp"]["language"] == "de":
        model_path = Path(config["relation"]["de_model"])
    else:
        raise ValueError("Wrong language given.")

    with model_path.open("rb") as f:
        return pickle.load(f)


def _transform(adu1: Union[Doc, Span], adu2: Union[Doc, Span]):
    data1 = [adu1.vector]
    data2 = [adu2.vector]

    data = np.array(list(zip(data1, data2)))
    data = np.reshape(data, (len(data), 600))

    return data


def _predict(
    sample: np.ndarray, model: LogisticRegression
) -> Tuple[RelationClass, float]:
    prediction = model.predict_proba(sample)
    threshold = config["relation"]["threshold"]
    fallback = config["relation"]["fallback"]

    prob_support = prediction[0, 1]
    prob_attack = prediction[0, 0]
    max_prob = max(prob_support, prob_attack)

    if max_prob >= threshold:
        if prob_attack > prob_support:
            return RelationClass.ATTACK, max_prob
        else:
            return RelationClass.SUPPORT, max_prob

    elif fallback == "none":
        return RelationClass.NONE, max_prob
    elif fallback == "attack":
        return RelationClass.ATTACK, max_prob
    elif fallback == "support":
        return RelationClass.SUPPORT, max_prob

    raise ValueError("Wrong value given for 'relation.fallback'.")
