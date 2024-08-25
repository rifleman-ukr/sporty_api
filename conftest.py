from endpoints.get_object import GetFact
from pytest import fixture


@fixture(scope='function')
def get_fact():
    def _get_fact(request=None, desired_status=200):
        return GetFact(request, desired_status)
    return _get_fact
