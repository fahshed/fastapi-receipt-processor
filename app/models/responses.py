from pydantic import BaseModel, Field


class IdResponse(BaseModel):
    id: str = Field(
        description="The unique ID assigned to the receipt",
        pattern=r"^\S+$",
    )


class PointsResponse(BaseModel):
    points: int = Field(
        description="The number of points awarded for the receipt",
    )


class ErrorResponse(BaseModel):
    detail: str = Field(description="Error detail")
