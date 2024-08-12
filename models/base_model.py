#!usr/bin/python3
"""
Base Model Class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model Class
    """

    def __init__(self):
        """Constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Update the updated time"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Returns a dictionary representation of an instance"""
        dict = self.__dict__
        dict["__class__"] = __class__.__name__
        dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict

