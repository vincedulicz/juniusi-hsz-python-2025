class UserSync:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, user_data):
        url = f'{self.base_url}/post'
        response = requests.post(url, json=user_data)
        response.raise_for_status()

        return response.json()

    def get_user(self, user_id):
        url = f'{self.base_url}/get'
        response = requests.get(url, params={"user_id": user_id})

        return response.json()

    def update_user(self, user_id, update_data):
        url = f'{self.base_url}/put'
        response = requests.put(url, json={"user_id": user_id, **update_data})

        return response.json()

    def delete_user(self, user_id):
        url = f'{self.base_url}/delete'
        response = requests.delete(url, params={"user_id": user_id})
        response.raise_for_status()

        return response.json

def main():
    base_url = "httpbin.org"
    user_sync = UserSync(base_url)

    user_sync.create_user({"name": "tesztElek", "email":"mail.com"})

    user_sync.get_user(user_id=1)

    # []...