#!usr/bin/python3
"""
Base Model Class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base Model Class
    """

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """String representation of the BaseModel"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Update the updated time"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Returns a dictionary representation of an instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
