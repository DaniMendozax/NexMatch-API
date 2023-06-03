from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.users import UserService
from schemas.user import User

router = APIRouter()

@router.get("/")
def index():
    return JSONResponse({"Message": "Hello"})

@router.get("/users", tags=['Get'], status_code=200)
def get_users():
    """
    Path to get all users.

    Returns:
        JSONResponse: JSON response with the fetched users.
    """
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@router.get("/users/", tags=['Get'],status_code=200)
def get_users_by_genre(genre: str = Query(min_length=2, max_length=15)) -> User:
    """
    Path to get users filtered by gender.

    Args:
        genre (str): genre to filter users.

    Returns:
        JSONResponse: JSON response with users filtered by genre.
    """
    db = Session()
    result = UserService(db).get_users_by_genre(genre)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return JSONResponse(content=jsonable_encoder(result))



@router.post("/users", tags=['POST'],response_model=dict, status_code=200)
def create_user(user: User):
    """
    Path to create a new user.

    Args:
        user (User): Data of the user to create.

    Returns:
        JSONResponse: JSON response with a success message.
    """
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(content={"message": "Successfully registered"}, status_code=201)

@router.put('/users/{id}', tags=['PUT'],response_model=dict, status_code=200)
def update_user(id: int, user: User) -> dict:
    """
    Ruta para actualizar un usuario existente.

    Args:
        id (int): ID del usuario a actualizar.
        user (User): Datos actualizados del usuario.

    Returns:
        JSONResponse: Respuesta JSON con un mensaje de éxito o error.
    """
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(content={"message": "User not found"})
    UserService(db).update_user(id, user)
    return JSONResponse(content={"message": "It has been successfully updated"})

@router.delete('/users/{id}',tags=['DELETE'],status_code=200)
def delete_movie(id: int):
    """
    Path to delete an existing user.

    Args:
        id (int): id of the user to delete.

    Returns:
        JSONResponse: JSON response with a success or error message.
    """
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(content={'message': 'User not found'})
    UserService(db).delete_user(id)
    return JSONResponse(content={"message": "Successfully deleted"})


