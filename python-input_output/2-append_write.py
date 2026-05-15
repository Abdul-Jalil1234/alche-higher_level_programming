#!/usr/bin/python3
"""Defines a text file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
