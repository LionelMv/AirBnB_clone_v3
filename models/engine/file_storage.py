#!usr/bin/python3
"""
File Storage
"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (__file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict, f)

    def reload(self):
        """Deserializes to __objects the JSON file (__file_path)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                  }

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                dict = json.load(f)

            for key, val in dict.items():
                # class_name = key.split(".")[0]
                # obj = eval(class_name)(**val)
                # or
                # key = BaseModel.id
                # obj = BaseModel(**kwargs)
                # obj = classes["BaseModel"](**val)
                obj = classes[val["__class__"]](**val)
                self.all()[key] = obj
        except FileNotFoundError:
            pass
