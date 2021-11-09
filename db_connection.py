from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://dbUser1:admin%40123@cluster0.wvv94.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(CONNECTION_STRING)
db = client['seatAllocation'] 
