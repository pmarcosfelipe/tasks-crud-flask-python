from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
  global task_id_control
  data = request.get_json()
  new_test = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_test)
  print(tasks)
  return jsonify({ "message" : "New task created successfully!"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
  task_list = [task.parse_to_dictionary() for task in tasks]

  response = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }

  return jsonify(response)


@app.route("/tasks/<int:taskId>", methods=["GET"])
def get_task_by_id(taskId):
  for t in tasks:
    if(t.id == taskId):
      task_response = t.parse_to_dictionary()
      # del task_response["id"]

      return jsonify(task_response)
    
  return jsonify({ "message" : "No task found!"}), 400


# validation for development server
if __name__ == "__main__":
  app.run(debug=True)