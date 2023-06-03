from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Gender(str, Enum):
    MASCULINO = "Male"
    FEMENINO = "Female"
    OTRO = "Other"


class User(BaseModel):
    """
    User model represents a user in the system.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        age (int): The age of the user.
        genre (Gender): The gender of the user.
        location (str): The location of the user.
        description (str): The description of the user.

    Example:
        An example JSON representation of a User object:

        {
            "id": 1,
            "name": "Your name",
            "age": 18,
            "genre": "Male",
            "location": "cra 193 d #15b-65",
            "description": "about you"
        }
    """

    id: int = None
    name: str = Field(max_length=50, min_length=1)
    age: int = Field()
    genre: Gender = Field()
    location: str = Field(max_length=100)
    description: str = Field(max_length=300)

    class Config:
        """
        Additional configuration for the User model.

        Attributes:
            schema_extra (dict): Extra schema information for the User model.
        """
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Your name",
                "age": 18,
                "genre": "Male",
                "location": "cra 193 d #15b-65",
                "description": "about you"
            }
        }
