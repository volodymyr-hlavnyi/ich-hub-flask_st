from pydantic import BaseModel, EmailStr
from setuptools.extern import names


class User(BaseModel):
    name: str
    email: EmailStr


class AdminUser(User):
    is_superuser: bool
    access_level: int

    def promote_user(self, user: User):
        print("congratulations, you are promoted!")
        return AdminUser(
            name=user.name,
            email=user.email,
            is_superuser=True,
            access_level=2)


if __name__ == "__main__":
    user_1 = User(name="Tom", email="example@admin.com")
    print(user_1)
    admin_user_1 = AdminUser(
        name="Sergej",
        email="email@example.com",
        is_superuser=True,
        access_level=2)

    print(admin_user_1)

    admin_user_1.promote_user(user_1)
    print(user_1)