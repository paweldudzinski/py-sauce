from lib import helpers

from lib.apis.endpoints import analytics as endpoints


class Analytics:
    def __init__(self, requester):
        self._requester = requester

    def get_test_trends(
            self,
            start=None,
            end=None,
            time_range=None,
            scope="me",
            owner=None,
            status=None,
            pretty=None,
            interval="1d",
            os=None,
            browser=None):
        endpoint = endpoints.get_test_trends()
        params = self._set_global_params(start, end, time_range, scope, owner, status, pretty)
        params.update({
            'interval': interval,
            'os': os,
            'browser': browser
        })
        return self._requester.request(endpoint, query_params=params)

    def get_error_aggregations(
            self,
            start=None,
            end=None,
            time_range=None,
            scope="me",
            owner=None,
            status=None,
            pretty=None,
            os=None,
            browser=None):
        endpoint = endpoints.get_error_aggregations()
        params = self._set_global_params(start, end, time_range, scope, owner, status, pretty)
        params.update({
            'os': os,
            'browser': browser
        })
        return self._requester.request(endpoint, query_params=params)

    def get_build_tests(
            self,
            start=None,
            end=None,
            time_range=None,
            scope="me",
            owner=None,
            status=None,
            pretty=None,
            os=None,
            browser=None):
        endpoint = endpoints.get_build_tests()
        params = self._set_global_params(start, end, time_range, scope, owner, status, pretty)
        params.update({
            'os': os,
            'browser': browser
        })
        return self._requester.request(endpoint, query_params=params)

    def get_tests_list(
            self,
            start=None,
            end=None,
            time_range=None,
            scope="me",
            owner=None,
            status=None,
            pretty=None,
            build=None,
            size=None,
            missing_build=None,
            query=None,
            desc=False):
        endpoint = endpoints.get_tests_list()
        params = self._set_global_params(start, end, time_range, scope, owner, status, pretty)
        params.update({
            'build': build,
            'size': size,
            'missing_build': missing_build,
            'query': query,
            'desc': desc
        })
        return self._requester.request(endpoint, query_params=params)

    def get_test_metrics(
            self,
            start=None,
            end=None,
            time_range=None,
            scope="me",
            owner=None,
            status=None,
            pretty=None,
            query=None,
            os=None,
            browser=None):
        endpoint = endpoints.get_test_metrics()
        params = self._set_global_params(start, end, time_range, scope, owner, status, pretty)
        params.update({
            'query': query,
            'os': os,
            'browser': browser
        })
        return self._requester.request(endpoint, query_params=params)

    @staticmethod
    def _set_global_params(start, end, time_range, scope, owner, status, pretty):
        return {
            'start': start and helpers.date_to_pyrfc3339(start),
            'end': end and helpers.date_to_pyrfc3339(end),
            'time_range': time_range,
            'scope': scope,
            'owner': owner,
            'status': status,
            'pretty': pretty
        }
