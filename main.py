import json
from flask import request
from function import add_users, add_offers, add_orders, return_data_users, return_data_offers, return_data_orders
from models_db import User, Order, Offer, app, db

RESOURCE_USER = 'users.json'
RESOURCE_ORDERS = 'orders.json'
RESOURCE_OFFERS = 'offers.json'

user_load = add_users(RESOURCE_USER)
order_load = add_orders(RESOURCE_ORDERS)
offer_load = add_offers(RESOURCE_OFFERS)


@app.route("/users", methods=['GET', 'POST'])
def page_get_all_user():
    """
    Создайте представление для пользователей, которое обрабатывало бы GET-запросы получения всех пользователей /users
    """
    if request.method == 'GET':
        users = User.query.all()
        result = []

        for user in users:
            result.append(return_data_users(user))

        return json.dumps(result, ensure_ascii=False, indent=4)

    if request.method == 'POST':
        data_user = request.json

        if User.query.get(data_user.get("id")):
            return f'ВНИМАНИЕ! Запись c id {data_user.get("id")} уже существует'
        else:
            user = User(
                    id=data_user.get("id"),
                    first_name=data_user.get("first_name"),
                    last_name=data_user.get("last_name"),
                    age=data_user.get("age"),
                    email=data_user.get("email"),
                    role=data_user.get("role"),
                    phone=data_user.get("phone")
                    )

            db.session.add(user)
            db.session.commit()

            return json.dumps(return_data_users(user), ensure_ascii=False, indent=4)


@app.route("/users/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def page_get_user_by_id(uid):
    """
    Создайте представление для пользователей, которое обрабатывало бы GET-запросы получения
    одного пользователя по идентификатору /users/1
    """
    user = User.query.get(uid)

    if user:
        if request.method == 'GET':
            return json.dumps(return_data_users(user), ensure_ascii=False, indent=4)

        if request.method == 'PUT':
            data = request.json

            user.id = data.get("id")
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.age = data.get("age")
            user.email = data.get("email")
            user.role = data.get("role")
            user.phone = data.get("phone")

            db.session.commit()

            return f'Запись с id {uid} изменена'

        if request.method == 'DELETE':
            # user = db.session.query(User).get(uid)
            db.session.delete(user)
            db.session.commit()

            return f'Запись с id {uid} удалена'

    else:
        return f'ВНИМАНИЕ! Запись с id {uid} не существует'


@app.route("/orders", methods=['GET', 'POST'])
def page_get_all_orders():
    """
    Создайте представление для заказов, которое обрабатывало бы GET-запросы получения всех заказов /orders
    """
    if request.method == 'GET':
        orders = Order.query.all()
        result = []

        for order in orders:
            result.append(return_data_orders(order))

        return json.dumps(result, ensure_ascii=False, indent=4)

    if request.method == 'POST':
        data_order = request.json

        if Order.query.get(data_order.get("id")):
            return f'ВНИМАНИЕ! Запись c id {data_order.get("id")} уже существует'
        else:
            order = Order(
                id=data_order.get('id'),
                name=data_order.get('name'),
                description=data_order.get('description'),
                start_date=data_order.get('start_date'),
                end_date=data_order.get('end_date'),
                address=data_order.get('address'),
                price=data_order.get('price'),
                customer_id=data_order.get('customer_id'),
                executor_id=data_order.get('executor_id')
            )

            db.session.add(order)
            db.session.commit()

            return json.dumps(return_data_orders(order), ensure_ascii=False, indent=4)


@app.route("/orders/<int:oid>", methods=['GET', 'PUT', 'DELETE'])
def page_get_orders_by_id(oid):
    """Создайте представление для заказов, которое обрабатывало бы GET-запросы получения
    заказа по идентификатору /orders/1"""
    order = Order.query.get(oid)

    if order:
        if request.method == 'GET':
            return json.dumps(return_data_orders(order), ensure_ascii=False, indent=4)

        if request.method == 'PUT':
            data_ord = request.json

            order.id = data_ord.get('id')
            order.name = data_ord.get('name')
            order.description = data_ord.get('description')
            order.start_date = data_ord.get('start_date')
            order.end_date = data_ord.get('end_date')
            order.address = data_ord.get('address')
            order.price = data_ord.get('price')
            order.customer_id = data_ord.get('customer_id')
            order.executor_id = data_ord.get('executor_id')

            db.session.commit()

            return f'Запись с id {oid} изменена'

        if request.method == 'DELETE':
            db.session.delete(order)
            db.session.commit()

            return f'Запись с id {oid} удалена'
    else:
        return f'ВНИМАНИЕ! Запись с id {oid} не существует'


@app.route("/offers", methods=['GET', 'POST'])
def page_get_all_offers():
    """
    Создайте представление для предложений, которое обрабатывало бы GET-запросы получения всех предложений /offers
    """
    if request.method == 'GET':
        offers = Offer.query.all()

        result = []
        for offer in offers:
            result.append(return_data_offers(offer))

        return json.dumps(result, ensure_ascii=False, indent=4)

    if request.method == 'POST':
        data_offer = request.json

        if Offer.query.get(data_offer.get('id')):
            return f'ВНИМАНИЕ! Запись c id {data_offer.get("id")} уже существует'
        else:
            offer = Offer(
                id=data_offer.get('id'),
                order_id=data_offer.get('order_id'),
                executor_id=data_offer.get('executor_id')
            )

            db.session.add(offer)
            db.session.commit()

            return json.dumps(return_data_offers(offer), ensure_ascii=False, indent=4)


@app.route("/offers/<int:ofid>", methods=['GET', 'PUT', 'DELETE'])
def page_get_offers_by_id(ofid):
    """
    Создайте представление для предложений, которое обрабатывало бы GET-запросы получения
    предложения по идентификатору /offers/<id>
    """
    offer = Offer.query.get(ofid)

    if offer:
        if request.method == 'GET':
            return json.dumps(return_data_offers(offer), ensure_ascii=False, indent=4)

        if request.method == 'PUT':
            data_offer = request.json

            offer.id = data_offer.get("id")
            offer.order_id = data_offer.get("order_id")
            offer.executor_id = data_offer.get("executor_id")

            db.session.commit()

            return f'Запись с id {ofid} изменена'

        if request.method == 'DELETE':
            db.session.delete(offer)
            db.session.commit()

            return f'Запись с id {ofid} удалена'
    else:
        return f'ВНИМАНИЕ! Запись с id {ofid} не существует'


if __name__ == '__main__':
    app.run(debug=True)
