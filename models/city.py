#!/usr/bin/python3
"""
The implementation of the city class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Implementation of the city class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
