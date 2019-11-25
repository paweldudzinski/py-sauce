def get_test_trends():
    return {
        'url': '/v1/analytics/trends/tests',
        'method': 'GET'
    }


def get_error_aggregations():
    return {
        'url': '/v1/analytics/trends/errors',
        'method': 'GET'
    }


def get_build_tests():
    return {
        'url': '/v1/analytics/trends/builds_tests',
        'method': 'GET'
    }


def get_tests_list():
    return {
        'url': '/v1/analytics/tests',
        'method': 'GET'
    }


def get_test_metrics():
    return {
        'url': '/v1/analytics/insights/test-metrics',
        'method': 'GET'
    }
