import pytest
import logging
from controllers.pet_controller import PetController
from helpers.pet_helper import PetHelper
from reportportal_client import RPLogger


@pytest.fixture(scope="module")
def add_new_pet():
    pet_controller = PetController()
    pet_helper = PetHelper()
    body = pet_helper.valid_body()
    response = pet_controller.add_new(body)
    return {
        'json': response.json,
        'text': str(response.json),
        'pet_id': response.json["id"]
        }


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.setLoggerClass(RPLogger)
    return logger
