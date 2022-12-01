import pytest
from json import dumps
from controllers.pet_controller import PetController
from helpers.pet_helper import PetHelper
from helpers.body_prettifier import prettifier
from assertpy.assertpy import assert_that

pet_controller = PetController()
pet_helper = PetHelper()

@pytest.mark.smoke
@pytest.mark.positive
def test_add_new_pet():
    body = pet_helper.valid_body()
    response = pet_controller.add_new(body)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text).is_equal_to(prettifier(body))

@pytest.mark.smoke
@pytest.mark.positive
def test_find_pet_by_id(add_new_pet):
    response = pet_controller.find_by_id(add_new_pet.pet_id)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text).is_equal_to(prettifier(add_new_pet.text))


@pytest.mark.smoke
@pytest.mark.positive
def test_update_pet(add_new_pet):
    body = pet_helper.valid_body(status='sold', pet_id=add_new_pet.pet_id)
    response = pet_controller.update(body)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text).is_equal_to(prettifier(body))


@pytest.mark.smoke
@pytest.mark.positive
def test_delete_pet(add_new_pet):
    response = pet_controller.delete(pet_id=add_new_pet.pet_id)
    assert_that(response.status_code).is_equal_to(200)

