from controllers.base_controller import BaseController


class User(BaseController):

    endpoint = 'user'

    def add_new(self, body):
        return self.request.post(f'{self.base_url}/{self.endpoint}', body)

    def find_by_id(self, pet_id):
        return self.request.get(f'{self.base_url}/{self.endpoint}/{pet_id}')

    def update(self, body):
        return self.request.put(f'{self.base_url}/{self.endpoint}', body)

    def delete(self, pet_id):
        return self.request.delete(f'{self.base_url}/{self.endpoint}/{pet_id}')
