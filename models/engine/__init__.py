#!/usr/bin/python3
"""Creates a  unique FileStorage instance for the app"""
from models.engine.file_storage import FileStorage

"""this for Variable storage, FileStorage inst"""
storage = FileStorage()
storage.reload()
