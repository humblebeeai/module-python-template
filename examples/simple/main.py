#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

from my_template import MyBase


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    _my_base = MyBase(item="item-01")
    logger.info(f" My item => {_my_base.item}")
