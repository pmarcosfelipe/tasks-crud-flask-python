import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
TASKS = []

def test_create_task():
  mock_task = {
    "title":  "Tast Title",
    "description": "This is a Task description",
  }

  response = requests.post(f"{BASE_URL}/tasks", json=mock_task)
  assert response.status_code == 200

  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json

  TASKS.append(response_json["id"])


def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json


def test_get_task_by_id():
  if(TASKS):
    task_id = TASKS[0]

  response = requests.get(f"{BASE_URL}/tasks/{task_id}")
  assert response.status_code == 200
  response_json = response.json()
  assert task_id == response_json["id"]


def test_update_task_by_id():
  if(TASKS):
    task_id = TASKS[0]

    payload = {
      "title":  "UPDATED Tast Title",
      "description": "This is a Task description",
      "completed": True
    }

    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["description"] == payload["description"]
    assert response_json["completed"] == payload["completed"]


def test_delete_task_by_id():
  if(TASKS):
    task_id = TASKS[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404