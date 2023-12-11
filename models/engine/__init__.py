#!/usr/bin/python3
"""Create unique FileStorage instance for the app"""
from models.engine.file_storage import FileStorage

"""Variable storage, FileStorage instance"""
storage = FileStorage()
storage.reload()
