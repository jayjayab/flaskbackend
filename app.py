from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required

from register_login import registration, sign_in
from responses import incomplete_details_response, response
from seats_related_methods import fetch_available_seats, bookCancel, fetch_bookings

app = Flask(__name__)
jwt = JWTManager(app)
cors = CORS(app)

app.config["JWT_SECRET_KEY"] = "secret-key"
app.config['JWT_TOKEN_LOCATION'] = ['json']

@app.route("/", methods=["GET"])
def health():
    return 'Hello'

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if data is None or data == {} or data['email'] == '' or data['username'] == '' or data['password'] == '':
        return incomplete_details_response()
    output = registration(data)
    return response(output)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data is None or data == {} or data['email'] == '' or data['password'] == '':
        return incomplete_details_response()
    output = sign_in(data)
    return response(output)


@app.route("/login/get_available_seats", methods=["POST"])
@jwt_required(fresh=True)
def get_available_seats():
    data = request.json
    if data is None or data == {} or data['date'] == '' or data['shift'] == '':
        return incomplete_details_response()
    output = fetch_available_seats(data)
    return response(output)


@app.route("/login/book_cancel_seat", methods=["POST"])
@jwt_required(fresh=True)
def book_cancel():
    data = request.json
    if data is None or data == {} or data['seatNo'] == '' or data['shift'] == '' or data['date'] == '' or \
            data['user_email'] == '' or data['status'] not in ['book', 'cancel']:
        return incomplete_details_response()
    output = bookCancel(data)
    return response(output)


@app.route("/login/get_bookings", methods=["POST"])
@jwt_required(fresh=True)
def get_bookings():
    data = request.json
    if data['user_email'] =='':
        return incomplete_details_response()
    output = fetch_bookings(data)
    return response(output)


if __name__ == '__main__':
    #app.run(debug=True, port=5001, host='0.0.0.0')
    app.run()