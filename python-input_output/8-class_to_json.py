#!/usr/bin/python3
"""Defines a function that returns a dictionary description of an object."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures

    for JSON serialization of an object.
    """
    return obj.__dict__
