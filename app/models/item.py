from pydantic import BaseModel, Field


class Item(BaseModel):
    shortDescription: str = Field(
        description="The Short Product Description for the item.",
        pattern=r"^[\w\s\-]+$",
    )
    price: str = Field(
        description="The total price paid for this item.",
        pattern=r"^\d+\.\d{2}$",
    )
