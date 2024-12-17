import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import TaskCreate, TaskUpdate

client = TestClient(app)

# Authorization Header
headers = {
    "Authorization": "Bearer mynewtoken"  # Ensure you use a valid token
}

@pytest.fixture(scope="function")
def setup_db():
    yield
    pass  # You can add database cleanup logic here

# Test Case 1: Create a Task
def test_create_task():
    task_data = {
        "title": "Learn FastAPI",
        "description": "Learn how to build APIs with FastAPI",
        "status": "to_do",
        "due_date": "2024-12-31"
    }

    # Send POST request to create a new task with the Authorization header
    response = client.post("/tasks/", json=task_data, headers=headers)

    assert response.status_code == 200

    task = response.json()
    assert task["title"] == "Learn FastAPI"
    assert task["description"] == "Learn how to build APIs with FastAPI"
    assert task["status"] == "to_do"
    assert task["due_date"] == "2024-12-31"
    assert "created_at" in task

# Test Case 2: Get All Tasks
def test_get_tasks():
    task_data = {
        "title": "Learn FastAPI",
        "description": "Learn how to build APIs with FastAPI",
        "status": "to_do",
        "due_date": "2024-12-31"
    }
    # Send POST request to create a new task
    response = client.post("/tasks/", json=task_data, headers=headers)
    task = response.json()

    # Send GET request to retrieve tasks
    response = client.get("/tasks/", headers=headers)

    # Assert the response status code is 200
    assert response.status_code == 200

    # Assert that the response returns a list
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) > 0
    assert tasks[0]["title"] == "Learn FastAPI"

# Test Case 3: Update a Task
def test_update_task():
    task_data = {
        "title": "Learn FastAPI",
        "description": "Learn how to build APIs with FastAPI",
        "status": "to_do",
        "due_date": "2024-12-31"
    }
    # Send POST request to create a new task
    response = client.post("/tasks/", json=task_data, headers=headers)
    task = response.json()

    # Prepare the data for the update
    update_data = {
        "title": "Learn FastAPI Updated",
        "description": "Updated description",
        "status": "in_progress",
        "due_date": "2025-01-01"
    }

    # Send PUT request to update the task
    task_id = task["id"]
    response = client.put(f"/tasks/{task_id}", json=update_data, headers=headers)

    assert response.status_code == 200

    updated_task = response.json()
    assert updated_task["title"] == "Learn FastAPI Updated"
    assert updated_task["description"] == "Updated description"
    assert updated_task["status"] == "in_progress"
    assert updated_task["due_date"] == "2025-01-01"
