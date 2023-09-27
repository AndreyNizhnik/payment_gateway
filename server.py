#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request
import stripe

# Launch the code and go here:
# http://localhost:4242/checkout.html

# This is your test secret API key.
stripe.api_key = \
    'sk_test_51NupjbB2kbHRylMdlLDfEWnIfkBv7iH2oLBSNQHfeNqX4i6gV8C9WnUKkIvHB1hG3hGO7mnCUK63L6Mg6uDogZkz00acrjK3jU'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

YOUR_DOMAIN = 'http://localhost:4242'


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NuqT9B2kbHRylMdOZdJqI1m',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


if __name__ == '__main__':
    app.run(port=4242)
