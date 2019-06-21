# coding: utf-8
import os
import json
import requests
import unittest

from sqlalchemy import create_engine


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'integration_variables.json')
with open(file_path) as variable_file:
    data = json.load(variable_file)

URL_LOCALHOST = data.get("environment")[0]["localhost"]["url"]

CREDENTIALS_LOCALHOST = \
    data.get("environment")[0]["localhost"]["credentials"][0]

FORBIDDEN_CREDENTIALS_LOCALHOST = \
    data.get("environment")[0]["forbidden_stag"]["credentials"][0]


class TestSetup(unittest.TestCase):
    def setUp(self):

        self.engine = create_engine('sqlite:///data.db', echo=False)

    def setup_cities_localhost(self):
        return requests.post(
            URL_LOCALHOST + "/cities",
            data=CREDENTIALS_LOCALHOST)

    def setup_forbidden_cities_localhost(self):
        return requests.post(
            URL_LOCALHOST + "/cities",
            data=FORBIDDEN_CREDENTIALS_LOCALHOST)

    def test_01_endpoint_cities_localhost(self):
        user = self.setup_cities_localhost()
        forbidden_cities_localhost = self.setup_forbidden_cities_localhost()

        self.assertEqual(200, user.status_code)
        self.assertEqual(403, forbidden_cities_localhost.status_code)
