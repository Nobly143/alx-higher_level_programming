#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """ Only the first name atrribute can be used
    by the user."""

     __slots__ = ["first_name"]
