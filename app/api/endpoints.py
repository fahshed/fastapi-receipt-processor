import uuid

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from app.models.receipt import Receipt
from app.models.responses import IdResponse, PointsResponse, ErrorResponse
from app.utils.receipt import calculate_points
from app.utils.storage import store_receipt, get_receipt_points


router = APIRouter(prefix="/receipts", tags=["Point Calculation"])


@router.post(
    path="/process",
    summary="Submits a receipt for processing",
    responses={
        200: {
            "model": IdResponse,
            "description": "Returns the ID assigned to the receipt",
        },
        400: {"model": ErrorResponse, "description": "Validation Error"},
    },
    status_code=status.HTTP_200_OK,
)
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    store_receipt(receipt_id, points)
    return JSONResponse(content={"id": receipt_id}, status_code=status.HTTP_200_OK)


@router.get(
    path="/{id}/points",
    summary="Returns the points awarded for the receipt",
    responses={
        200: {"model": PointsResponse, "description": "The number of points awarded"},
        404: {"model": ErrorResponse, "description": "Not Found"},
    },
    status_code=status.HTTP_200_OK,
)
def get_points(id: str):
    points = get_receipt_points(id)
    if points is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No receipt found for that id"
        )
    return JSONResponse(content={"points": points}, status_code=status.HTTP_200_OK)
