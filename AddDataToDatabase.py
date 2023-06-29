import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://markmyface-7b7a5-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')

data = {
    "852741":
        {
            "name": "sreelrxmi",
            "major":"cse",
            "starting_year":2021,
            "total_attendance": 1,
            "standing": "B",
            "year":2,
            "last_attendance_time": "2023-6-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon musk",
            "major":"civil",
            "starting_year":2017,
            "total_attendance": 50,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2023-6-11 00:54:34"
        },
    "321654":
        {
            "name": "nevin sebastian",
            "major":"cse",
            "starting_year":2020,
            "total_attendance": 50,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2023-6-11 00:54:34"
        }

}

for key,value in data.items():
    ref.child(key).set(value)