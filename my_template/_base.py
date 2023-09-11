# -*- coding: utf-8 -*-

## Standard libraries
import logging

## Third-party libraries
# from pydantic import BaseModel, validate_call

## Internal modules
from .__version__ import __version__


logger = logging.getLogger(__name__)


class MyBase:

    def __init__(self, item: str = "item"):
        self.item = item


    @property
    def item(self) -> str:
        try:
            return self.__item
        except AttributeError:
            self.__item = "item"

        return self.__item

    @item.setter
    def item(self, item: str):
        if not isinstance(item, str):
            raise TypeError(
                f"`item` attribute type {type(item)} is invalid, must be a <str>!"
            )

        self.__item = item
