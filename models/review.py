#!usr/bin/python3
"""
Review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""