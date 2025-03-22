import pendulum
import typing as t

ova_format = "DD/MM/YYYY - HH:mm:ss"
aif_format = "YYYY-MM-DD HH:mm:ss"
analysis_format = "DD/MM/YYYY"


def from_ova(text: t.Optional[str]) -> t.Optional[pendulum.DateTime]:
    return pendulum.from_format(text, ova_format) if text else None


def to_ova(dt: t.Optional[pendulum.DateTime]) -> str:
    # return "{date:%d/%m/%Y - %H:%M:%S}".format(date=datetime.datetime.now())
    return dt.format(ova_format) if dt else ""


def from_aif(text: t.Optional[str]) -> t.Optional[pendulum.DateTime]:
    return pendulum.from_format(text, aif_format) if text else None


def to_aif(dt: t.Optional[pendulum.DateTime]) -> str:
    # return "{date:%Y-%m-%d %H:%M:%S}".format(date=datetime.datetime.now())
    return dt.format(aif_format) if dt else ""


def from_analysis(text: t.Optional[str]) -> t.Optional[pendulum.DateTime]:
    return pendulum.from_format(text, analysis_format) if text else None


def to_analysis(dt: t.Optional[pendulum.DateTime]) -> str:
    return dt.format(analysis_format) if dt else ""
