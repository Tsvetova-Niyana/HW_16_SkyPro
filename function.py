import json
from models_db import User, Offer, Order, db, app


def open_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        users = json.load(file)

    return users


# загрузка данных
def add_users(path):
    users = open_file(path)
    for data_user in users:
        user = User(
            id=data_user.get("id"),
            first_name=data_user.get("first_name"),
            last_name=data_user.get("last_name"),
            age=data_user.get("age"),
            email=data_user.get("email"),
            role=data_user.get("role"),
            phone=data_user.get("phone")
        )
        with app.app_context():
            db.session.add(user)
            db.session.commit()


def add_orders(path):
    orders = open_file(path)
    for data_orders in orders:
        order = Order(
            id=data_orders.get("id"),
            name=data_orders.get("name"),
            description=data_orders.get("description"),
            start_date=data_orders.get("start_date"),
            end_date=data_orders.get("end_date"),
            address=data_orders.get("address"),
            price=data_orders.get("price"),
            customer_id=data_orders.get("customer_id"),
            executor_id=data_orders.get("executor_id")
        )
        with app.app_context():
            db.session.add(order)
            db.session.commit()


def add_offers(path):
    offers = open_file(path)
    for data_offers in offers:
        offer = Offer(
            id=data_offers.get("id"),
            order_id=data_offers.get("order_id"),
            executor_id=data_offers.get("executor_id")
        )

        with app.app_context():
            db.session.add(offer)
            db.session.commit()


def return_data_users(user):
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone
    }


def return_data_orders(order):
    return {
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    }


def return_data_offers(offer):
    return {
        "id": offer.id,
        "order_id": offer.order_id,
        "executor_id": offer.executor_id
    }
