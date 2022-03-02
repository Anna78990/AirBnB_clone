#!/usr/bin/python3
"""Define a class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity

    Attribute:
        - name (str): name of the amenity
    """

    name = ""
