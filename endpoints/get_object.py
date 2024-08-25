import requests
from utils import schema
from jsonschema import validate, ValidationError


class GetFact:
    def __init__(self, request=None, desired_status=200):
        self.response = requests.get(f"https://cat-fact.herokuapp.com/facts/{request}")
        self.is_response_valid()
        self.is_request_succeeded(desired_status)

    @property
    def response_status(self):
        return self.response.status_code

    @property
    def response_json(self):
        return self.response.json()

    def is_response_valid(self):
        try:
            validate(instance=self.response_json, schema=schema('get'))
        except ValidationError:
            return False
        else:
            return True

    def is_request_succeeded(self, desired_status):
        if self.response_status == desired_status:
            return True
        else:
            return False
