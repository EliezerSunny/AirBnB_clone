#!/usr/bin/python3
"""
Module for AirBnB_clone project
"""

from models.base_model import BaseModel
import uuid
from datetime import datetime


class User(BaseModel):
    """
    Class representing a user in the AirBnB_clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new user.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """
        Return a string representation of the user.
        """
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute and save the user.
        """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance.
        """
        user_dict = self.__dict__.copy()
        user_dict["__class__"] = self.__class__.__name__
        user_dict["created_at"] = self.created_at.isoformat()
        user_dict["updated_at"] = self.updated_at.isoformat()
        return user_dict
