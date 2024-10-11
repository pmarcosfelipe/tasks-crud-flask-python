from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_task)

  return jsonify({ "message" : "New task created successfully!", "id": new_task.id})


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

      return jsonify(task_response)
    
  return jsonify({ "message" : "No task found!"}), 404

@app.route("/tasks/<int:taskId>", methods=["PUT"])
def update_task_by_id(taskId):
  task = None
  for t in tasks:
    if(t.id == taskId):
      task = t

  if task == None:
    return jsonify({ "message" : "No task found!"}), 404
  
  data = request.get_json()
  task.title = data["title"]
  task.description = data["description"]
  task.completed = data["completed"]

  return jsonify({ "message" : "Task updated successfully!"})


@app.route("/tasks/<int:taskId>", methods=["DELETE"])
def delete_task_by_id(taskId):
  task = None
  for t in tasks:
    if(t.id == taskId):
      task = t
      break

  if not task:
    return jsonify({ "message" : "No task found!"}), 404
  
  tasks.remove(task)

  return jsonify({ "message" : "Task deleted successfully!"})

# validation for development server
if __name__ == "__main__":
  app.run(debug=True)