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