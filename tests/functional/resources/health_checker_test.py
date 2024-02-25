from tests.functional.core.base_test import BaseTestCase


class TestHealthCheckerResource(BaseTestCase):

    def test_server_is_up_and_running(self):
        response = self.client.get('/health')
        self.assert200(response)
