import pyrfc3339


def date_to_pyrfc3339(date):
    return pyrfc3339.generate(date, accept_naive=True)
