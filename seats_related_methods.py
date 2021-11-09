from db_connection import db

seats_collection = db['seats']
bookings_collection = db['bookings']

def fetch_available_seats(data):
    try:
        seat_details = seats_collection.find()
        output_seat = [{item: data[item] for item in data if item != '_id'} for data in seat_details]
        print(f'output_seat: {output_seat}')
        booking_details = bookings_collection.find()
        output_booking = [{item: data[item] for item in data if item != '_id'} for data in booking_details]
        print(f'output_booking: {output_booking}')

        seat_list = []
        for s in output_seat:
            seat_id = s['id']
            check_booking = bookings_collection.find_one(
                {'seatNo': seat_id, 'shift': data['shift'], 'date': data['date']})
            print(check_booking)
            if check_booking:
                dict = {'seatNo': seat_id, 'group': s['group'], 'status': 'booked'}
            else:
                dict = {'seatNo': seat_id, 'group': s['group'], 'status': 'available'}
            seat_list.append(dict)
        output = {"Response": seat_list}
        return output
    except Exception as e:
        print(e)
        return 'Error'

def bookCancel(data):
    try:
        if data['status'] == 'book':
            check_availability = bookings_collection.find_one(
                {'seatNo': data['seatNo'], 'shift': data['shift'], 'date': data['date']})
            if check_availability:
                output = {"Response": "Seat is no longer available"}
            else:
                group = seats_collection.find_one({'id': data['seatNo']})['group']
                print(group)
                data['group'] = group
                data.pop('status')
                data.pop('access_token')
                bookings_collection.insert_one(data)
                output = {"Response": "Seat has been booked successfully"}
        else:
            check_booking = bookings_collection.find_one({'seatNo': data['seatNo'], 'shift': data['shift'], 'date': data['date']})
            if check_booking:
                bookings_collection.delete_one(check_booking)
                output = {"Response": "Booking cancelled successfully"}
            else:
                output = {"Response": "Booking not found"}

        return output

    except Exception as e:
        print(e)
        return 'Error'

def fetch_bookings(data):
    try:
        booking_details = bookings_collection.find({'user_email': data['user_email']})
        output_seat = [{item: doc[item] for item in doc if item != '_id'} for doc in booking_details]
        if output_seat != []:
            output = output_seat
        else:
            output = {"Response": "No bookings found"}
        return output
    except Exception as e:
        print(e)
        return 'Error'
