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
                    value = datetime.fromisoformat(value)
                if "__class__" != key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = current_datetime
            self.updated_at = current_datetime
            models.storage.new(self)

    def __str__(self):
        "Prints the str representation of BaseModel"
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        "Updates the updated_at instance attribute with current datetime"
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        result = {**self.__dict__}
        result['__class__'] = self.__class__.__name__
        result['created_at'] = datetime.isoformat(result['created_at'])
        result['updated_at'] = datetime.isoformat(result['updated_at'])
        return result
