from json import dumps
from faker import Faker


fake = Faker()
valid_statuses = ['available', 'pending', 'sold']


class PetHelper():

    def valid_body(self, status=None, pet_id=None):
        if status is None:
            status = fake.word(3, valid_statuses)
        elif status == 'available':
            status = 'available'
        elif status == 'pending':
            status = 'pending'
        elif status == 'sold':
            status = 'sold'
        if pet_id is None:
            pet_id = fake.random.randint(1, 1000)
        else:
            pet_id = pet_id
        body = {
            "id": pet_id,
            "category": {
                "id": fake.random.randint(1, 100),
                "name": fake.word()
            },
            "name": fake.name(),
            "photoUrls": [

            ],
            "tags": [
                {
                    "id": fake.random.randint(1, 100),
                    "name": fake.word()
                }
            ],
            "status": status
        }
        return dumps(body)

    def body_with_invalid_id(self, id):
        body = {
            "id": id,
            "category": {
                "id": fake.random.randint(1, 100),
                "name": fake.word()
            },
            "name": fake.name(),
            "photoUrls": [

            ],
            "tags": [
                {
                    "id": fake.random.randint(1, 100),
                    "name": fake.word()
                }
            ],
            "status": 'available'
        }
        return dumps(body)
