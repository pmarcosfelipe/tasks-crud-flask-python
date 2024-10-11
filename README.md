# Battle Game Python

This project consists in create REST API for a Task List CRUD using Python's framework [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Requirements

- The Task must to have the attributes:
  - id: int;
  - title: string;
  - description: string;
  - completed: boolean;
- The API must to have the following endpoints to:
  - create;
  - get all tasks;
  - get task by task id;
  - update task;
  - delete task;

## Run project

```python
python app.py
```

## Run Tests

```python
python app.py
pytest tests.py -v
```
