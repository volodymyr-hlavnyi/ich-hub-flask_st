from pydantic import BaseModel, Field, EmailStr, HttpUrl


class Product(BaseModel):
    name: str = Field(..., title="Product name")
    description: str = Field(..., title="Product description")
    price: float = Field(..., gt=0, title="Product price")
    tags: list[str] = Field(default_factory=list, title="Owner tags")


class Owner(BaseModel):
    name: str = Field(..., min_lenhyt=3, max_length=20, title="Owner name")
    age: int = Field(..., gt=18, le=99, title="Owner age")
    website: HttpUrl = Field(..., title="Owner website")



if __name__ == "__main__":
    product_01 = Product(
        name="Milk",
        description="Milk from cow",
        price=1.5,
        tags=['wood', 'metal', 'plastic']
    )

    print(product_01)

    owner_01 = Owner(name="Tom", age=19, website="https://example.com")
    print(owner_01)
