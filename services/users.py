from models.users import User as UserModel
from schemas.user import User


class UserService():

    def __init__(self, db):
        self.db = db

    def get_users(self):
        """
        Gets all users.

        Returns:
            list: List of all users.
        """
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id):
        """
        Gets a user by their ID.

        Args:
            id (int): id of the user to get.

        Returns:
            User: User found or None if not found.
        """
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def get_users_by_genre(self, genre):
        """
        Gets users filtered by gender.

        Args:
            genre (str): genre to filter users.

        Returns:
            list: List of users filtered by genre.
        """
        result = self.db.query(UserModel).filter(
            UserModel.genre == genre).all()
        return result

    def create_user(self, user: User):
        """
        Create a new user.

        Args:
            user (User): data of the user to create.
        """
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def update_user(self, id: int, data: User):
        """
        Updates an existing user.

        Args:
            id (int): ID of the user to update.
            data (User): Updated user data.
        """
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        user.name = data.name
        user.age = data.age
        user.genre = data.genre
        user.location = data.location
        user.description = data.description
        self.db.commit()
        return

    def delete_user(self, id: int):
        """
        Deletes an existing user.

        Args:
            id (int): id of the user to delete.
        """
        delete_movie = self.db.query(UserModel).filter(
        UserModel.id == id).delete()
        self.db.commit()
        return
