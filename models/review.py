#!/usr/bin/python3
""" Module: review """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes Review """
    place_id = ""
    user_id = ""
    text = ""
