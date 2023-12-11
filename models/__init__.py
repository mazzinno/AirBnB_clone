#!/usr/bin/python3
"""Create unique FileStorage instance for the app"""
from models.engine.file_storage import FileStorage

"""VModule: __init__.py"""
storage = FileStorage()
storage.reload()
