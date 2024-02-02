import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-34050-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendencerealtime-34050.appspot.com"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Kartikeya Swarup",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Melissa",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)