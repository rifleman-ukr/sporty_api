from pytest import fixture

from endpoints.get_object import GetFact


@fixture(scope='function')
def get_fact():
    def _get_fact(request="", desired_status=200):
        return GetFact(request, desired_status)
    return _get_fact
