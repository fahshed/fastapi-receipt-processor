import math

from app.models.receipt import Receipt


def calculate_points(receipt: Receipt) -> int:
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name
    alphanumeric_chars = [c for c in receipt.retailer if c.isalnum()]
    points += len(alphanumeric_chars)

    # Rule 2: 50 points if the total is a round dollar amount with no cents
    total_amount = float(receipt.total)
    if total_amount.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if (total_amount * 100) % 25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt
    points += (len(receipt.items) // 2) * 5

    # Rule 5: For items with description length multiple of 3
    for item in receipt.items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            price = float(item.price)
            item_points = math.ceil(price * 0.2)
            points += item_points

    # Rule 6: 6 points if the day in the purchase date is odd
    purchase_day = int(receipt.purchaseDate.split("-")[2])
    if purchase_day % 2 == 1:
        points += 6

    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm
    hour, minute = map(int, receipt.purchaseTime.split(":"))
    total_minutes = hour * 60 + minute
    if (14 * 60) < total_minutes < (16 * 60):
        points += 10

    return points
