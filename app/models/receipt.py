from typing import List
from pydantic import BaseModel, Field

from app.models.item import Item


class Receipt(BaseModel):
    retailer: str = Field(
        description="The name of the retailer or store the receipt is from.",
        pattern=r"^[\w\s\-&]+$",
    )
    purchaseDate: str = Field(
        description="The date of the purchase printed on the receipt.",
    )
    purchaseTime: str = Field(
        description="The time of the purchase printed on the receipt. 24-hour time expected.",
    )
    items: List[Item] = Field(description="List of items on the receipt.", min_length=1)
    total: str = Field(
        description="The total amount paid on the receipt.",
        pattern=r"^\d+\.\d{2}$",
    )
