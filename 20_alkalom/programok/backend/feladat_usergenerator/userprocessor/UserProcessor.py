class UserProcessor:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def filter_expiring_users(self, days=180):
        expiring_users = {}
        for user_id, user_info in self.data.items():
            valid_until = datetime.strptime(user_info['valid_until'], "%Y.%m.%d")
            if (valid_until - datetime.now()).days <= days:
                expiring_users[user_id] = user_info
        return expiring_users

    def filter_no_workers(self):
        return {user_id: user_info for user_id, user_info in self.data.items() if not user_info['worker']}

    def filter_over_age(self, age_limit):
        return {user_id: user_info for user_id, user_info in self.data.items() if user_info['age'] > age_limit}

    def filter_by_country(self, country):
        return {user_id: user_info for user_id, user_info in self.data.items() if user_info['country'] == country}