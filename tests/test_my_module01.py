# -*- coding: utf-8 -*-

import logging

import pytest

from my_module01 import MyClass


logger = logging.getLogger(__name__)


@pytest.fixture
def my_class():
    _my_class = MyClass()

    yield _my_class

    del _my_class


def test_init(my_class):
    logger.info("Testing initialization of 'MyClass'...")

    assert isinstance(my_class, MyClass)

    logger.info("Done: Initialization of 'MyClass'.\n")
