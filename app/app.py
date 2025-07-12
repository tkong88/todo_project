
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB 연결
mongo_host = os.environ.get("MONGO_HOST", "mongo")  # docker-compose 내부 서비스 이름
client = MongoClient(f"mongodb://{mongo_host}:27017/")
db = client["todo_db"]
collection = db["todos"]

@app.route('/add', methods=['POST'])
def add_task():
    new_task = {
        "date": request.form.get("date"),
        "task": request.form.get("task"),
        "person": request.form.get("person"),
        "deadline": request.form.get("deadline")
    }
    collection.insert_one(new_task)
    return "MongoDB에 저장되었습니다!"

@app.route('/list', methods=['GET'])
def get_list():
    tasks = list(collection.find({}, {'_id': False}))
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

