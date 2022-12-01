# class UserAcount:
#     def __init__(self, user, passwd):
#         self._username = user
#         self._password = passwd
#
#     def get_username(self):
#         return self._username
#
#     def set_username(self, user):
#         self._username = user
#
#     def get_password(self):
#         return self._password
#
#     def set_username(self, passwd):
#         self._password = passwd
class UserAccount:
    def __init__(self, user, passwd):
        self._username = user
        self._password = passwd

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd):
        self._password = passwd
