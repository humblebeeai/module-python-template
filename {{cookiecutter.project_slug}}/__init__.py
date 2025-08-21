try:
    from .src.{{cookiecutter.module_name}} import *  # noqa: F403,F401
except ImportError:
    from src.{{cookiecutter.module_name}} import *  # noqa: F403,F401
