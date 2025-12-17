from behave import given, when, then
import httpx


@given("API server is running")
def step_server_running(context):
    pass


@when('I create a user with email "{email}"')
def step_create_user(context, email):
    context.last_response = httpx.post(
        f"{context.base_url}/users/",
        json={"email": email},
    )


@given('I have a user with email "{email}"')
def step_have_user(context, email):
    r = httpx.post(f"{context.base_url}/users/", json={"email": email})
    context.user = r.json()
    context.last_response = r


@when('I create a task with title "{title}" for that user')
def step_create_task(context, title):
    user_id = context.user["id"]
    context.last_response = httpx.post(
        f"{context.base_url}/tasks/",
        json={"title": title, "user_id": user_id},
    )


@given('I have a task with title "{title}" for that user')
def step_have_task(context, title):
    user_id = context.user["id"]
    r = httpx.post(
        f"{context.base_url}/tasks/",
        json={"title": title, "user_id": user_id},
    )
    context.task = r.json()
    context.last_response = r


@when("I request tasks list")
def step_list_tasks(context):
    context.last_response = httpx.get(f"{context.base_url}/tasks/")


@then("response status should be {code:d}")
def step_status(context, code):
    assert context.last_response.status_code == code, context.last_response.text


@then('response should contain field "{field}"')
def step_has_field(context, field):
    data = context.last_response.json()
    assert field in data, data


@then("response json should match:")
def step_json_match_table(context):
    data = context.last_response.json()
    for row in context.table:
        key = row["title"] if "title" in row.headings else row[0]
    for r in context.table:
        k = r[0]
        v = r[1]
        assert str(data.get(k)) == v, data


@then('tasks list should contain a task with title "{title}"')
def step_list_contains(context, title):
    items = context.last_response.json()
    assert any(t.get("title") == title for t in items), items
