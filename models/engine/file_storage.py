#!/usr/bin/python3
"Serializes and deserializes JSON instances to/from files"
import json
from os.path import exists
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes and deserializes JSON instances to/from files

    Attributes:
        Class attributes:
            __file_path: string - path to the JSON file
            __objects: dictionary - stores all objects by <class name>.id
    """
    __file_path = "storage.json"
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
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        "Serializes all objects to the JSON file file_path"
        serializable_objects = {}
        for key, obj in FileStorage.__objects.items():
            serializable_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_objects, f)

    def reload(self):
        "Deserializes the JSON file to __objects if it exists"
        file_exists = exists(FileStorage.__file_path)

        if file_exists:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                FileStorage.__objects = {}
                for key, data in json_dict.items():
                    class_name = date["__class__"]
                    class_name = models.classes[class_name]
                    FileStorage.__objects[key] = class_name(**data)
