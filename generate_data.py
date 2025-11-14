import csv
import os
import random
from datetime import timedelta

from faker import Faker

fake = Faker()

DATA_DIR = "data"
NUM_CUSTOMERS = 200
NUM_PRODUCTS = 100
NUM_ORDERS = 300

os.makedirs(DATA_DIR, exist_ok=True)

customers = [
    {
        "customer_id": customer_id,
        "name": fake.name(),
        "email": fake.unique.email(),
        "signup_date": fake.date_between(start_date="-2y", end_date="today").isoformat(),
    }
    for customer_id in range(1, NUM_CUSTOMERS + 1)
]

product_categories = [
    "Electronics",
    "Home",
    "Books",
    "Fashion",
    "Beauty",
    "Sports",
    "Toys",
    "Automotive",
    "Garden",
    "Grocery",
]
products = [
    {
        "product_id": product_id,
        "product_name": fake.catch_phrase(),
        "category": random.choice(product_categories),
        "price": round(random.uniform(5, 500), 2),
    }
    for product_id in range(1, NUM_PRODUCTS + 1)
]

orders = []
order_items = []
payments = []
item_id_counter = 1

for order_id in range(1, NUM_ORDERS + 1):
    customer = random.choice(customers)
    order_date = fake.date_between(start_date="-1y", end_date="today")
    line_items = []
    for _ in range(random.randint(1, 5)):
        product = random.choice(products)
        quantity = random.randint(1, 3)
        line_items.append(
            {
                "item_id": item_id_counter,
                "order_id": order_id,
                "product_id": product["product_id"],
                "quantity": quantity,
                "item_price": product["price"],
            }
        )
        item_id_counter += 1

    total_amount = round(
        sum(item["quantity"] * item["item_price"] for item in line_items), 2
    )

    orders.append(
        {
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "order_date": order_date.isoformat(),
            "total_amount": total_amount,
        }
    )
    order_items.extend(line_items)

    payments.append(
        {
            "payment_id": order_id,
            "order_id": order_id,
            "payment_method": random.choice(
                ["Credit Card", "PayPal", "Bank Transfer", "Gift Card"]
            ),
            "payment_status": random.choice(["Completed", "Pending"]),
            "payment_date": (order_date + timedelta(days=random.randint(0, 5))).isoformat(),
        }
    )


def write_csv(filename, fieldnames, rows):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Created {path} ({len(rows)} rows)")


write_csv(
    "customers.csv",
    ["customer_id", "name", "email", "signup_date"],
    customers,
)
write_csv(
    "products.csv",
    ["product_id", "product_name", "category", "price"],
    products,
)
write_csv(
    "orders.csv",
    ["order_id", "customer_id", "order_date", "total_amount"],
    orders,
)
write_csv(
    "order_items.csv",
    ["item_id", "order_id", "product_id", "quantity", "item_price"],
    order_items,
)
write_csv(
    "payments.csv",
    ["payment_id", "order_id", "payment_method", "payment_status", "payment_date"],
    payments,
)

