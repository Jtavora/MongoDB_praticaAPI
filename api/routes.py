# routes.py
from flask import request, jsonify
from database import connect_db, insert_customer, search_customer
from datetime import datetime

def configure_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return "<h1>API de Prática</h1><p>Esta API é um exemplo de como criar uma API usando Flask e MongoDB.</p>"

    @app.route('/Clients', methods=['GET', 'POST'])
    def handle_clients():
        if request.method == 'GET':
            db = connect_db()
            customers = db["Clients"]
            output = []

            for customer in customers.find():
                formatted_customer = {
                    'Index': customer['Index'],
                    'First_Name': customer['First Name'],
                    'Last_Name': customer['Last Name'],
                    'Company': customer['Company'],
                    'City': customer['City'],
                    'Country': customer['Country'],
                    'Phone_1': customer['Phone 1'],
                    'Phone_2': customer['Phone 2'],
                    'Email': customer['Email'],
                    'Subscription_Date': customer['Subscription Date'].strftime('%Y-%m-%d %H:%M:%S'),
                    'Website': customer['Website']
                }
                output.append(formatted_customer)

            return jsonify(output)

        elif request.method == 'POST':
            new_customer = request.json
            id_cliente = insert_customer(new_customer)
            return jsonify({'id': str(id_cliente), 'message': 'Cliente inserido com sucesso!'})

    @app.route('/Clients/<id>', methods=['GET'])
    def handle_client(id):
        if request.method == 'GET':
            customer = search_customer(id)
            formatted_customer = {
                'Index': customer['Index'],
                'First_Name': customer['First Name'],
                'Last_Name': customer['Last Name'],
                'Company': customer['Company'],
                'City': customer['City'],
                'Country': customer['Country'],
                'Phone_1': customer['Phone 1'],
                'Phone_2': customer['Phone 2'],
                'Email': customer['Email'],
                'Website': customer['Website']
            }
            return jsonify(formatted_customer)
