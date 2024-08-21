from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr

# Расширенная модель пользователя с дополнительными полями
class AdminUser(User):
    is_superuser: bool
    access_level: int


user1 = User(
    name="Oleg",
    email="olejka@gmail.com"
)

print(user1)

admin_user_1 = AdminUser(
    name='OLga',
    email='olechka@gmail.com',
    is_superuser = True,
    access_level = 10
)

print(admin_user_1)