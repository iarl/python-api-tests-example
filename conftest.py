import pytest
from dataclasses import dataclass
from controllers.pet_controller import PetController
from helpers.pet_helper import PetHelper


@dataclass
class Response:
    json: object
    text: str
    pet_id: str


@pytest.fixture(scope="module")
def add_new_pet():
    pet_controller = PetController()
    pet_helper = PetHelper()
    body = pet_helper.valid_body()
    response = pet_controller.add_new(body)
    return Response(response.json, str(response.json), response.json["id"])

