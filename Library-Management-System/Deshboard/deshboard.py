from Membership.membership import Payment

# Can add payment details to the Deshboard


class UserProfile:
    def __init__(self, user_profile, user_history):
        self.user_profile = user_profile
        self.user_history = user_history

    def get_user_details(self):
        # get user details from the database
        # user history is book history with date
        pass
