from api.user.models import User

user_data = {"username": "test", "password": "11223344", "email": "test@efficienflow.com"}

User.objects.create_user(**user_data)
