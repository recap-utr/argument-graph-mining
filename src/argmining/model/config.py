from dynaconf import Dynaconf

config = Dynaconf(
    envvar_prefix="ARGMINING",
    settings_files=["settings.toml"],
)
