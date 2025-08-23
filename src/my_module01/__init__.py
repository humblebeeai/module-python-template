# flake8: noqa

from dotenv import load_dotenv

load_dotenv(override=True)

from .__version__ import __version__
from .config import MyClassConfigPM
from ._base import MyClass


__all__ = [
    "__version__",
    "MyClassConfigPM",
    "MyClass",
]
