#!/usr/bin/python3
"BaseModel class, defines all common attributes/methods"
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes

    Args/Attributes:
        id: unique id of any created instance
        created_at: datetime object of creation of instance
        updated_at: datetime object of update of instance
    """

    def __init__(self, *args, **kwargs):
        current_datetime = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if "__class__" != key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = current_datetime
            self.updated_at = current_datetime
            models.storage.new(self)

    def __str__(self):
        "Prints the str representation of BaseModel"
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        "Updates the updated_at instance attribute with current datetime"
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        result_dict = self.__dict__
        result_dict.update({"__class__": BaseModel.__name__})
        if isinstance(self.created_at, datetime):
            result_dict.update({"created_at": self.created_at.isoformat()})
        if isinstance(self.updated_at, datetime):
            result_dict.update({"updated_at": self.updated_at.isoformat()})

        return result_dict
