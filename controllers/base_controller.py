from config import BASE_URL
from utils.request import Request


class BaseController:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = BASE_URL
        self.request = Request()
