# import datetime
# from cryptography.fernet import Fernet
# from flask_jwt_extended import create_access_token

# from db_connection import db

# def registration(data):
#     try:
#         collection = db['users']
#         email = data['email']
#         test = collection.find_one({"email": email})
#         if test:
#             # return jsonify(message="User Already Exist"), 200
#             output = {"Response": "User already exists"}
#         else:
#             key = Fernet.generate_key()
#             file_path = "secretkey"
#             file = open(file_path, 'a+')
#             file.write(email + ':' + str(key) + '\n')
#             file.close()
#             fernet = Fernet(key)
#             print(key)
#             data['password'] = fernet.encrypt(data['password'].encode())
#             collection.insert_one(data)
#             output = {"Response": "User added successfully"}
#         return output

#     except Exception as e:
#         print(e)
#         return 'Error'

# def sign_in(data):
#     try:
#         collection = db['users']
#         email = data['email']
#         password = data['password']
#         file_path = "secretkey"
#         file = open(file_path, 'r')
#         lines = file.readlines()
#         key = ''
#         for line in lines:
#             email_key = line.split(':')
#             if email_key[0] == email:
#                 key = email_key[1][2:-2]
#                 print(key)
#                 break
#         file.close()

#         fernet = Fernet(key)

#         user_check = collection.find_one({'email': email})
#         if user_check:
#             db_password = user_check['password']
#             decoded_password = fernet.decrypt(db_password).decode()
#             print(decoded_password)
#             if decoded_password == password:
#                 access_token = create_access_token(identity=email, fresh=True,
#                                                    expires_delta=datetime.timedelta(minutes=30))
#                 output = {"Response": "Login successful!", "username": user_check['username'], 'access_token': access_token}
#             else:
#                 output = {"Response": "Invalid password"}
#         else:
#             output = {"Response": "Invalid email"}

#         return output
#     except Exception as e:
#         print(e)
#         return 'Error'

import datetime
from cryptography.fernet import Fernet
from flask_jwt_extended import create_access_token

from db_connection import db

def registration(data):
    try:
        collection = db['users']
        email = data['email']
        test = collection.find_one({"email": email})
        if test:
            # return jsonify(message="User Already Exist"), 200
            output = {"Response": "User already exists"}
        else:
            key = Fernet.generate_key()
            file_path = "secretkey"
            file = open(file_path, 'a+')
            file.write(email + ':' + str(key) + '\n')
            file.close()
            fernet = Fernet(key)
            print(key)
            data['password'] = fernet.encrypt(data['password'].encode())
            collection.insert_one(data)
            output = {"Response": "User added successfully"}
        return output

    except Exception as e:
        print(e)
        return f'Error {e}'

def sign_in(data):
    try:
        collection = db['users']
        email = data['email']
        password = data['password']
        file_path = "secretkey"
        file = open(file_path, 'r')
        lines = file.readlines()
        key = ''
        for line in lines:
            email_key = line.split(':')
            if email_key[0] == email:
                key = email_key[1][2:-2]
                print(key)
                break
        file.close()

        fernet = Fernet(key)

        user_check = collection.find_one({'email': email})
        if user_check:
            db_password = user_check['password']
            decoded_password = fernet.decrypt(db_password).decode()
            print(decoded_password)
            if decoded_password == password:
                access_token = create_access_token(identity=email, fresh=True,
                                                   expires_delta=datetime.timedelta(minutes=30))
                output = {"Response": "Login successful!", "username": user_check['username'], 'access_token': access_token}
            else:
                output = {"Response": "Invalid password"}
        else:
            output = {"Response": "Invalid email"}

        return output
    except Exception as e:
        print(e)
        return f'Error {e}'



