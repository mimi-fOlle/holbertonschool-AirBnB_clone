#!/usr/bin/python3
"Initializes our File Storage"
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
