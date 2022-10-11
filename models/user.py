#!/usr/bin/python3
""" Module: user """


from models.base_model import BaseModel


class User(BaseModel):
    """ Public class attributes for User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
