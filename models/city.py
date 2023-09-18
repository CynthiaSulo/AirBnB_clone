#!/usr/bin/python3
"""
Contains class City.
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel.
    """
    state_id = ""
    name = ""
