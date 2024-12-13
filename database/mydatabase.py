from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://babakyousefian1379:dC8w27YrMUPs77Ax@cluster0.lwxtq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.LorestanUniv

student_collection = db["student_collection"]
lecturer_collection = db["lecturer_collection"]
course_collection = db["course_collection"]
CourseRegister_collection = db["course_register_collection"]
PresentedCourses_collection = db["presented_courses_collection"]