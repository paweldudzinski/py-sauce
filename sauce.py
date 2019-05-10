from lib.requester import Requester
from lib.apis.job import Job


class Sauce:
    def __init__(self, sauce_user=None, sauce_access_key=None, base_api_url='https://saucelabs.com'):
        self._sauce_user = sauce_user
        self._sauce_access_key = sauce_access_key
        self._base_api_url = base_api_url
        self._requester = Requester(sauce_user, sauce_access_key, base_api_url)

        self.jobs = Job(self._requester)
