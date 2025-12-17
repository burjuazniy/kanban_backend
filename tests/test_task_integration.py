from fastapi.testclient import TestClient

def test_create_and_list_tasks_integration(client: TestClient):
    user_response = client.post(
        "/users/",
        json={"email": "task_owner@example.com"},
    )
    user_id = user_response.json()["id"]

    task_payload = {
        "title": "Test task",
        "user_id": user_id,
    }

    create_task_response = client.post("/tasks/", json=task_payload)
    assert create_task_response.status_code == 200

    task_data = create_task_response.json()
    assert task_data["title"] == "Test task"
    assert task_data["user_id"] == user_id

    list_response = client.get("/tasks/")
    assert list_response.status_code == 200

    tasks = list_response.json()
    assert len(tasks) >= 1
    assert any(task["title"] == "Test task" for task in tasks)
