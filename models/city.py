#!/usr/bin/env python3
""" Class City -> City where AirBnB is located in"""

from .base_model import BaseModel


class City(BaseModel):
    """ City Attributes"""
    state_id = ""
    name = ""