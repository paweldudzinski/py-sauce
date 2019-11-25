from lib.apis.endpoints import account as endpoints


class Account:
    def __init__(self, requester):
        self._requester = requester

    def get_user(self, username=None):
        return self._do('get_user', username)

    def get_user_concurrency(self, username=None):
        return self._do('get_user_concurrency', username)

    def get_user_organization(self, username=None):
        return self._do('get_user_organization', username)

    def get_user_activity(self, username=None):
        return self._do('get_user_activity', username)

    def get_user_monthly_minutes(self, username=None):
        return self._do('get_user_monthly_minutes', username)

    def get_user_subaccounts(self, username=None):
        return self._do('get_user_subaccounts', username)

    def get_user_subaccounts_info(self, username=None):
        return self._do('get_user_subaccounts_info', username)

    def get_user_sibling_accounts(self, username=None):
        return self._do('get_user_subaccounts_info', username)

    def create_user_subaccount(self, username, password, name, email, concurrency=1):
        payload = {
            'username': username,
            'password': password,
            'name': name,
            'email': email,
            'concurrency': concurrency
        }
        endpoint = endpoints.create_user_subaccount(self._requester.sauce_user)
        return self._requester.request(endpoint, body=payload)

    def whoami(self):
        endpoint = endpoints.whoami()
        return self._requester.request(endpoint)

    def _do(self, func_name, username):
        username = username or self._requester.sauce_user
        func = getattr(endpoints, func_name)
        endpoint = func(username)
        return self._requester.request(endpoint)
