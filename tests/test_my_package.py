# -*- coding: utf-8 -*-

import logging

import pytest

from my_template import MyBase


logger = logging.getLogger(__name__)


@pytest.fixture
def my_base():
    _my_base = MyBase()

    yield _my_base

    del _my_base


def test_init(my_base):
    logger.info("Testing initialization of 'MyBase'...")

    assert isinstance(my_base, MyBase)
    assert my_base.item == "item"

    logger.info("Done: Initialization of 'MyBase'.\n")
