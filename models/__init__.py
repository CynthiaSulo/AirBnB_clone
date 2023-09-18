#!/usr/bin/python3
"""
Module contains storage variable.
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
