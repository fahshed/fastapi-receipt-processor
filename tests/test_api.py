from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


client = TestClient(app)


def test_post_receipts_process_ok():
    receipt_data = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
        ],
        "total": "9.00",
    }

    response = client.post("/receipts/process", json=receipt_data)

    assert response.status_code == status.HTTP_200_OK

    assert "id" in response.json()


def test_post_receipts_process_error():
    receipt_data = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "total": "9.00",
    }

    response = client.post("/receipts/process", json=receipt_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_receipts_points_ok():
    receipt_data = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
        ],
        "total": "9.00",
    }

    post_response = client.post("/receipts/process", json=receipt_data)
    receipt_id = post_response.json()["id"]

    get_response = client.get(f"/receipts/{receipt_id}/points")

    assert get_response.status_code == status.HTTP_200_OK

    assert "points" in get_response.json()

    expected_points = 109
    assert get_response.json()["points"] == expected_points


def test_get_receipts_points_error():
    get_response = client.get(f"/receipts/abcd1234/points")

    assert get_response.status_code == status.HTTP_404_NOT_FOUND
