def get_user(username):
    return {
        'url': '/v1/users/{username}'.format(username=username),
        'method': 'GET'
    }


def get_user_concurrency(username):
    return {
        'url': '/v1.1/users/{username}/concurrency'.format(username=username),
        'method': 'GET'
    }


def get_user_organization(username):
    return {
        'url': '/v1.1/users/{username}/organization'.format(username=username),
        'method': 'GET'
    }


def get_user_activity(username):
    return {
        'url': '/v1/users/{username}/activity'.format(username=username),
        'method': 'GET'
    }


def get_user_monthly_minutes(username):
    return {
        'url': '/v1/users/{username}/monthly-minutes'.format(username=username),
        'method': 'GET'
    }


def get_user_subaccounts(username):
    return {
        'url': '/v1/users/{username}/list-subaccounts'.format(username=username),
        'method': 'GET'
    }


def get_user_subaccounts_info(username):
    return {
        'url': '/v1/users/{username}/subaccounts'.format(username=username),
        'method': 'GET'
    }


def create_user_subaccount(username):
    return {
        'url': '/v1/users/{username}'.format(username=username),
        'method': 'POST'
    }


def whoami():
    return {
        'url': '/v1/whoami',
        'method': 'GET'
    }
