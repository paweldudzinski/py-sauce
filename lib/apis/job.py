from lib.apis.endpoints import job as endpoints


class Job:
    def __init__(self, requester):
        self._requester = requester

    def get_job(self, id, hmac=None):
        endpoint = endpoints.get_job(id)
        return self._requester.request(endpoint, hmac=hmac)

    def get_user_jobs(
            self,
            username=None,
            limit=None,
            subaccounts=None,
            full=False,
            manual_only=False,
            auto_only=False,
            name=None,
            owner_type=None,
            owner=None,
            start=None,
            end=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.get_user_jobs(username)
        params = {
            'limit': limit,
            'subaccounts': subaccounts,
            'full': full,
            'manual_only': manual_only,
            'auto_only': auto_only,
            'name': name,
            'owner_type': owner_type,
            'owner': owner,
            'from': start,
            'to': end
        }
        return self._requester.request(endpoint, query_params=params)

    def get_build_failed_jobs(self, id, username=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.get_build_failed_jobs(username, id)
        return self._requester.request(endpoint)

    def get_build_jobs(self, id):
        endpoint = endpoints.get_build_jobs(id)
        return self._requester.request(endpoint)

    def update_job(self, id, username=None, body=None, hmac=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.update_job(username, id)
        return self._requester.request(endpoint, body=body, hmac=hmac)

    def stop_job(self, id, username=None, hmac=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.stop_job(username, id)
        return self._requester.request(endpoint, hmac=hmac)

    def delete_job(self, id, username=None, hmac=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.delete_job(username, id)
        return self._requester.request(endpoint, hmac=hmac)

    def get_job_asset_names(self, id, username=None, hmac=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.get_job_asset_names(username, id)
        return self._requester.request(endpoint, hmac=hmac)

    def get_job_asset_files(self, id, asset_file_name, username=None, hmac=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.get_job_asset_files(username, asset_file_name, id)
        return self._requester.request(endpoint, hmac=hmac)

    def delete_job_assets(self, id, username=None, hmac=None):
        username = username or self._requester.sauce_user
        endpoint = endpoints.delete_job_assets(username, id)
        return self._requester.request(endpoint, hmac=hmac)
