# user.py

from abc import ABC, abstractmethod 
from pathlib import Path 
import random

class User(ABC):
    """
    abstract user class
    farmer and buyer will inherit from this
    """

    def __init__(self, name, phone, location, pin):
        self.name = name
        self.phone = phone 
        self.location = location
        self.pin = pin

    @abstractmethod 
    def get_role(self):
        """Return role of the user"""
        pass 

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "phone": self.phone,
            "location": self.location,
            "pin":self.pin,
            "role": self.get_role()
        }
    
    @classmethod 
    def from_dict(cls, data):
        pass 

    def __str__(self):
        return f"{self.get_role()} - {self.name}, {self.phone}, {self.location}"