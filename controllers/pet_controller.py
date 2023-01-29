from controllers.base_controller import BaseController


class PetController(BaseController):

    endpoint = 'pet'

    def add_new(self, body):
        return self.request.post(
            f'{self.base_url}/{self.endpoint}', body, self.headers)

    def find_by_id(self, pet_id):
        return self.request.get(f'{self.base_url}/{self.endpoint}/{pet_id}')

    def find_by_status(self, status):
        return self.request.get(
            f'{self.base_url}/{self.endpoint}/findByStatus?status={status}')

    def update(self, body):
        return self.request.put(
            f'{self.base_url}/{self.endpoint}', body, self.headers)

    def delete(self, pet_id):
        return self.request.delete(f'{self.base_url}/{self.endpoint}/{pet_id}')
