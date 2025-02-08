import pytest

from gitallica.pydantic_core import User, AdultUser


def test_user_creation():
    # Arrange
    user_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    
    # Act
    user = User(**user_data)
    
    # Assert
    assert user.name == "John Doe"
    assert user.age == 30
    assert user.email == "john.doe@example.com"

def test_adult_user_creation():
    # Arrange
    adult_user_data = {
        "name": "Jane Doe",
        "age": 25,
        "email": "jane.doe@example.com",
        "is_employed": True
    }
    
    # Act
    adult_user = AdultUser(**adult_user_data)
    
    # Assert
    assert adult_user.name == "Jane Doe"
    assert adult_user.age == 25
    assert adult_user.email == "jane.doe@example.com"
    assert adult_user.is_employed is True
    # test if extra fields are exported as model json
    user_json = adult_user.model_dump()
    assert "is_employed" in user_json and user_json["is_employed"] == True

def test_adult_user_email_validation():
    # Arrange
    invalid_adult_user_data = {
        "name": "Jane Doe",
        "age": 25,
        "email": "jane.doe@example",
        "is_employed": True
    }
    
    # Act & Assert
    with pytest.raises(ValueError):
        AdultUser(**invalid_adult_user_data)

def test_adult_user_age_validation():
    # Arrange
    invalid_adult_user_data = {
        "name": "Young User",
        "age": 17,
        "email": "young.user@example.com",
        "is_employed": False
    }
    
    # Act & Assert
    with pytest.raises(ValueError):
        AdultUser(**invalid_adult_user_data)


def test_adult_user_diet_validation():
    # Arrange
    valid_adult_user_data = {
        "name": "Jane Doe",
        "age": 25,
        "email": "young.user@example.com",
        "diet": "vegan"
    }
    invalid_adult_user_data = {
        "name": "Jane Doe",
        "age": 25,
        "email": "young.user@example.com",
        "diet": "keto"
    }

    # Act
    AdultUser(**valid_adult_user_data)
    
    # Act & Assert
    with pytest.raises(ValueError):
        AdultUser(**invalid_adult_user_data)

def test_user_json_export():
    # Arrange
    user_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    user = AdultUser(**user_data)
    
    # Act
    user_json = user.model_dump_json()
    
    # Assert
    assert "email" not in user_json

# Add more tests as needed
