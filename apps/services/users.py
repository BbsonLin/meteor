from uuid import UUID
from apps.datacontracts.commands import CreateUserCommand
from apps.datacontracts.commands import EditUserCommand
from apps.datacontracts.commands import LoginCommand
from apps.datacontracts.results import UserResult
from apps.datacontracts.results import UserLoginResult


class UserService(object):
    def __init__(self):
        pass

    def create_user(self, command: CreateUserCommand):
        pass

    def edit_user(self, command: EditUserCommand):
        pass

    def get_user(self, user_id: UUID):
        pass

    def login(self, command: LoginCommand):
        pass
