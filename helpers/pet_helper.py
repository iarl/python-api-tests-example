from json import dumps
from faker import Faker


fake = Faker()
valid_statuses = ['available', 'pending' ,'sold']

class PetHelper():
    

    def valid_body(self):
        body = {
                "id": fake.random.randint(1, 1000),
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
                "status": fake.word(3, valid_statuses)
                }
        return dumps(body)


