from flask import Flask, request, jsonify
import os

app = Flask(__name__)
tasks = []

@app.route('/')
def home():
    return jsonify({"message": "Task Microservice is running"})

@app.route('/health')
def health():
    return jsonify({"status": "Service is healthy"})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json

    if not data.get("title") or not data.get("priority"):
        return jsonify({"error": "Title and Priority required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "priority": data["priority"]
    }

    tasks.append(task)
    return jsonify({"message": "Task added successfully", "task": task})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/high', methods=['GET'])
def get_high_priority():
    high_tasks = [task for task in tasks if task["priority"].lower() == "high"]
    return jsonify(high_tasks)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)