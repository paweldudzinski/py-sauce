import json
import requests
import urllib
from requests.auth import HTTPBasicAuth

from lib.exceptions import InvalidApiUrlException

METHOD_TO_FUNCTION = {
    'GET': requests.get,
    'PUT': requests.put,
    'DELETE': requests.delete
}


class Requester:

    def __init__(self, sauce_user, sauce_access_key, base_api_url):
        self.sauce_user = sauce_user
        self._base_api_url = base_api_url
        self._auth = self._auth(sauce_user, sauce_access_key)

    def request(self, endpoint, hmac=None, body=None, query_params={}):
        url = urllib.parse.urljoin(self._base_api_url, 'rest' + endpoint['url'])
        method = endpoint['method']
        body = body and json.dumps(body) or None
        try:
            response = METHOD_TO_FUNCTION[method](
                url,
                auth=self._auth,
                headers={'content-type': 'application/json'},
                data=body,
                params=self._params(hmac, query_params))
            print(response.url)
            return response.json()
        except json.decoder.JSONDecodeError:
            return response.text
        except Exception as e:
            raise InvalidApiUrlException(str(e))

    @staticmethod
    def _auth(username, password):
        return HTTPBasicAuth(username, password)

    @staticmethod
    def _params(hmac, query_params):
        if hmac:
            return query_params.update({'auth': hmac})
        return query_params
