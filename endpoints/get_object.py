import requests
from jsonschema import validate, ValidationError

from utils import schema


class GetFact:
    def __init__(self, request, desired_status):
        self.desired_status = desired_status
        self.response = requests.get(f"https://cat-fact.herokuapp.com/facts/{request}")

    def result(self):
        return True if self.is_response_valid() and self.is_request_succeeded(self.desired_status) else False

    @property
    def response_status(self):
        return self.response.status_code

    @property
    def response_json(self):
        return self.response.json()

    def is_response_valid(self):
        try:
            if isinstance(self.response_json, list):
                for _ in self.response_json:
                    validate(instance=self.response_json, schema=schema(f'get_{self.desired_status}'))
            else:
                validate(instance=self.response_json, schema=schema(f'get_{self.desired_status}'))
        except ValidationError:
            return False
        else:
            return True

    def is_request_succeeded(self, desired_status):
        if self.response_status == desired_status:
            return True
        else:
            return False
