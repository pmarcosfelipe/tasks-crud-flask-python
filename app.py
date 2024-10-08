from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create():
  global task_id_control
  data = request.get_json()
  new_test = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_test)
  print(tasks)
  return jsonify({ "message" : "New task created successfully!"})

@app.route("/tasks", methods=["GET"])
def get():
  task_list = [task.to_dict() for task in tasks]

  # for task in tasks:
  #   task_list.append(task.to_dict())

  response = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }

  return jsonify(response)

# validation for development server
if __name__ == "__main__":
  app.run(debug=True)