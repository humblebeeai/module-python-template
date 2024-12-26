# -*- coding: utf-8 -*-

try:
    from .src.my_module01 import *
except ImportError:
    from src.my_module01 import *
