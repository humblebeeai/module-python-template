try:
    from .src.my_module01 import *  # noqa: F403,F401
except ImportError:
    from src.my_module01 import *  # noqa: F403,F401
