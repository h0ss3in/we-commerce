from enum import Enum


class Errors(str, Enum):
    ITEM_DOES_NOT_EXIST = "Item {} does not exist!"
