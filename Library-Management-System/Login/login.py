class LoginPage:
    def __init__(self, user_name, password, confirm_password):
        self.user_name = user_name
        self.password = password
        self.confirm_password = confirm_password

    def login(self):
        if all([self.user_name, self.password, self.confirm_password]):
            if self.password == self.confirm_password:
                try:
                    from Deshboard.deshboard import UserProfile
                    return 'Login Successful'
                except Exception as er:
                    return er
            else:
                return 'Password not match'
        else:
            return 'Write all Required Fields'
