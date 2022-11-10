import pytest
from json import dumps
from controllers.pet_controller import Pet
from helpers.pet_helper import PetHelper
from assertpy.assertpy import assert_that

pet = Pet()
pet_helper = PetHelper()

@pytest.mark.smoke
def test_add_new_pet():
    body = pet_helper.valid_body()
    response = pet.add_new(body)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(str(response.json)).is_equal_to(body.replace("\"","'"))

