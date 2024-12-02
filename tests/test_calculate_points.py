from app.api.endpoints import calculate_points
from app.models.receipt import Receipt
from app.models.item import Item


def test_calculate_points():
    data = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
            {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
            {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
        ],
        "total": "35.35",
    }

    receipt = Receipt(**data)

    expected_points = 28

    calculated_points = calculate_points(receipt)

    assert calculated_points == expected_points
