
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    diet: Optional[str] = None

    model_config = ConfigDict(extra='allow')

    @field_validator('age')
    def check_age(cls, value):
        if value < 0:
            raise ValueError('must be greater than 0')
        return value
    
    @field_validator('diet')
    def check_diet(cls, value):
        if value and value not in ['vegan', 'vegetarian', 'pescatarian', 'omnivore']:
            raise ValueError('must be one of vegan, vegetarian, pescatarian, omnivore')
        return value
    
    def say_hello(self):
        return f'Hello {self.name}, I am {self.age} years old'
    

class AdultUser(User):
    age: int = Field(..., gt=17)
    email: Optional[str] = Field(default=None, exclude=True, pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    def say_hello(self):
        return f'Hello {self.name}, I am {self.age} years old, I am an adult'
    
    