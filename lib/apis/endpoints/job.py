def get_job(id):
    return {
        'url': '/v1.1/jobs/{id}'.format(id=id),
        'method': 'GET'
    }


def get_user_jobs(username):
    return {
        'url': '/v1.1/{username}/jobs'.format(username=username),
        'method': 'GET'
    }


def get_build_failed_jobs(username, id):
    return {
        'url': '/v1/{username}/builds/{id}/failed-jobs'.format(username=username, id=id),
        'method': 'GET'
    }


def get_build_jobs(id):
    return {
        'url': '/v1/builds/{id}/jobs'.format(id=id),
        'method': 'GET'
    }


def stop_job(username, id):
    return {
        'url': '/v1/{username}/jobs/{id}/stop'.format(username=username, id=id),
        'method': 'PUT'
    }


def update_job(username, id):
    return {
        'url': '/v1/{username}/jobs/{id}'.format(username=username, id=id),
        'method': 'PUT'
    }


def delete_job(username, id):
    return {
        'url': '/v1/{username}/jobs/{id}'.format(username=username, id=id),
        'method': 'DELETE'
    }


def get_job_asset_names(username, id):
    return {
        'url': '/v1/{username}/jobs/{id}/assets'.format(username=username, id=id),
        'method': 'GET'
    }


def get_job_asset_files(username, asset_file_name, id):
    return {
        'url': '/v1/{username}/jobs/{id}/assets/{asset_file_name}'.format(
            username=username,
            id=id,
            asset_file_name=asset_file_name),
        'method': 'GET'
    }


def delete_job_assets(username, id):
    return {
        'url': '/v1/{username}/jobs/{id}/assets'.format(username=username, id=id),
        'method': 'DELETE'
    }
