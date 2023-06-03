import json
from fastapi.testclient import TestClient
from routers.userRoutes import router

# An instance of the test client is created using the router.
client = TestClient(router)

# Test to verify the starting route
def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello"}

# Test to get all users
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200

# Test to filter users by gender
def test_get_users_by_genre():
    response = client.get("/users/", params={"genre": "Male"})
    assert response.status_code == 200

# Test to create a new user
def test_create_user():
    user_data = {
        "name": "John Doe",
        "age": 25,
        "genre": "Male",
        "location": "Some location",
        "description": "Some description"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201


# Test to update an existing user
def test_update_user():
    user_id = 1
    updated_user_data = {
        "name": "Updated Name",
        "age": 30,
        "genre": "Female",
        "location": "Updated Location",
        "description": "Updated Description"
    }
    response = client.put(f"/users/{user_id}", json=updated_user_data)
    assert response.status_code == 200

# Test to delete an existing user
def test_delete_user():
    user_id = 1
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
