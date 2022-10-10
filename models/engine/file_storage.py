#!/usr/bin/python3
"Serializes and deserializes JSON instances to/from files"


class FileStorage:
    """
    Serializes and deserializes JSON instances to/from files

    Attributes:
        Class attributes:
            __file_path: string - path to the JSON file
            __objects: dictionary - stores all objects by <class name>.id
    """
    __file_path = ""
    __objects = {}

    def all(self):
        "Returns all objects"
        return FileStorage.__objects
