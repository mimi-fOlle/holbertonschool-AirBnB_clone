#!/usr/bin/python3
"Serializes and deserializes JSON instances to/from files"
import json
from os.path import exists


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

    def new(self, obj):
        """
        Adds an object to the class dictionary of objects

        args:
            obj: The object to add
        """
        FileStorage.__objects.update({f"{obj.id}": obj})

    def save(self):
        "Serializes all objects to the JSON file file_path"
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        "Deserializes the JSON file to __objects if it exists"
        file_exists = exists(FileStorage.__file_path)

        if file_exists:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
