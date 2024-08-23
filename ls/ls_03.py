from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    Field)


class User(BaseModel):
    name: str
    email: EmailStr

    @field_validator("email")
    def email_must_be_gmail(cls, value: EmailStr):
        allowed_emails = ['gmail.com', 'yahoo.com', 'outlook.com']
        email_domain = value.split('@')[-1]
        if email_domain not in allowed_emails:
            raise ValueError(f"Only {allowed_emails} domains are allowed")
        return value


if __name__== "__main__":
    user_01 = User(name="Oleg", email="check_olg@gmail.com")
    print(user_01)
    user_01 = User.email_must_be_gmail(user_01.email)
    print(user_01)
