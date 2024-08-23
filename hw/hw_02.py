from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator)


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., gt=0)

    def __str__(self):
        return f"City: {self.city}, Street: {self.street}, Hause number: {self.hause_number}"

    @field_validator("city")
    def city_must_be_alpha(cls, value: str):
        if not value.replace(" ", "").isalpha():
            raise ValueError("City must contain only letters")
        return value

    @field_validator("street")
    def street_must_be_alpha(cls, value: str):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Street must contain only letters")
        return value

    @field_validator("house_number")
    def house_number_must_be_positive(cls, value: int):
        if value < 0:
            raise ValueError(f"Hause number must be positive (greater than 0) - {value}")
        return value


class User(BaseModel):
    name: str = Field(..., min_length=2, pattern="^[a-zA-Z]+$")
    age: int = Field(..., ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Is employed: {self.is_employed}, Address: {self.address}"

    @field_validator("name")
    def name_must_be_alpha(cls, value: str):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")
        return value

    @field_validator("age")
    def age_must_be_positive(cls, value: int):
        if value < 0:
            raise ValueError("Age must be positive")
        return value

    @field_validator('is_employed')
    def check_employment_status(cls, value, values):
        age = values.data.get('age')
        if age is not None:
            if value and age < 16:
                raise ValueError('User cannot be employed if age is less than 16')
            if not value and age >= 65:
                raise ValueError('User should be retired if age is 65 or older')
        return value


def process_user_registration(json_str: str) -> str:
    try:
        user = User.model_validate_json(json_str)
        return user.model_dump_json()
    except ValueError as e:
        return str(e)


if __name__ == "__main__":
    # Примеры JSON строк

    # Error message: User cannot be employed if age is less than 16
    invalid_json_age_employment = '''
    {
        "name": "Bob",
        "age": 14,
        "email": "bob@example.com",
        "is_employed": true,
        "address": {
            "city": "Los Angeles",
            "street": "Main St",
            "house_number": 456
        }
    }
    '''

    # Error message: Email must be a valid email address
    invalid_json_email = '''
    {
        "name": "Charlie",
        "age": 25,
        "email": "charlie[at]example.com",
        "is_employed": false,
        "address": {
            "city": "Chicago",
            "street": "Lake Shore Dr",
            "house_number": 789
        }
    }
    '''

    # Error message: Name must contain only letters
    invalid_json_name = '''
    {
        "name": "David123",
        "age": 40,
        "email": "david@example.com",
        "is_employed": true,
        "address": {
            "city": "San Francisco",
            "street": "Market St",
            "house_number": 101
        }
    }
    '''

    # Correct JSON
    valid_json = '''
        {
            "name": "Alice",
            "age": 30,
            "email": "alice@example.com",
            "is_employed": true,
            "address": {
                "city": "New York",
                "street": "Broadway",
                "house_number": 123
            }
        }
        '''

    print('=' * 20)
    print("Error in employment status:")
    print(process_user_registration(invalid_json_age_employment))

    print('=' * 20)
    print("Error in email:")
    print(process_user_registration(invalid_json_email))

    print('=' * 20)
    print("Error in name:")
    print(process_user_registration(invalid_json_name))

    print('=' * 20)
    print("Correct JSON:")
    print(process_user_registration(valid_json))
