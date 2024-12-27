# -*- coding: utf-8 -*-

import logging

import pytest

try:
    from {{cookiecutter.module_name}} import MyClass
except ImportError:
    from src.{{cookiecutter.module_name}} import MyClass


logger = logging.getLogger(__name__)


@pytest.fixture
def my_object():
    _my_object = MyClass()

    yield _my_object

    del _my_object


def test_init(my_object):
    logger.info("Testing initialization of 'MyClass'...")

    assert isinstance(my_object, MyClass)

    logger.info("Done: Initialization of 'MyClass'.\n")
