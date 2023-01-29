from controllers.base_controller import BaseController


class Store(BaseController):

    endpoint = 'store'

    def place_order(self, body):
        return self.request.post(
            f'{self.base_url}/{self.endpoint}/order', body)

    def find_by_id(self, order_id):
        return self.request.get(
            f'{self.base_url}/{self.endpoint}/order/{order_id}')

    def update(self, body):
        return self.request.put(f'{self.base_url}/{self.endpoint}', body)

    def delete(self, order_id):
        return self.request.delete(
            f'{self.base_url}/{self.endpoint}/order/{order_id}')
