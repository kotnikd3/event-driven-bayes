from unittest import TestCase

from api.infrastructure.controllers import FlaskController
from tests.conftest import FakePublisher


class TestFlaskController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        publisher = FakePublisher()
        cls.controller = FlaskController(publisher=publisher)

    def setUp(self) -> None:
        self.client = self.controller.app.test_client(self)

    def test_model_updated(self):
        with self.client:
            response = self.client.get('/update_model/w')

        self.assertEqual(201, response.status_code)
        self.assertEqual('Model updated', response.text)

        with self.client:
            response = self.client.get('/update_model/l')

        self.assertEqual(201, response.status_code)
        self.assertEqual('Model updated', response.text)

    def test_model_now_updated(self):
        with self.client:
            response = self.client.get('/update_model/WRONG')

        self.assertEqual(404, response.status_code)
        self.assertEqual('Not found', response.text)
