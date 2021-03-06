import json
import allure 
import pytest 

from antiphishme.src.config import (
    BASE_PATH
)
from antiphishme.tests.test_helpers import (
    data_to_json, 
    info, 
    assert_equal, 
    assert_dict_contains_key
)

from os import getenv

@allure.epic("Verify")
@allure.parent_suite("Functional")
@allure.suite("Verify")
@allure.sub_suite("Safebrowsing")
class Tests:

    @allure.description("""
    Test endpoint "/verify/by_sfbrowsing"

    Send correct data.
    """)
    def test_verify_by_sfbrowsing(self, client_with_db):
        client = client_with_db[0]
        endpoint = '/verify/by_sfbrowsing'
        data = {
            'url': 'example.com'
        }
        headers = {
            'Content-Type': "application/json"
        }
        info("POST {}".format(endpoint))
        response = client.post(BASE_PATH + endpoint, data=json.dumps(data), headers=headers)
        assert_equal(response.status_code, 200, "Check status code")
        j = data_to_json(response.data)
        field = "status"
        expected_value = "good"
        assert_dict_contains_key(j, field, "Check if dict contains given key - \"{}\"".format(field))
        assert_equal(j[field], expected_value, "Check if item \"{}\" is equal to \"{}\"".format(field, expected_value))

    @pytest.mark.skipif(getenv('SAFEBROWSING_API_KEY', None) is  None, reason="SAFEBROWSING_API_KEY env variable must be set")
    @allure.description_html("""
    Test endpoint "/verify/by_sfbrowsing"

    Send correct malicious data.

    <h2> Fail if env. variable not set</h2>
    """)
    def test_verify_by_sfbrowsing_malicious(self, client_with_db):
        client = client_with_db[0]
        endpoint = '/verify/by_sfbrowsing'
        data = {
            'url': 'http://malware.testing.google.test/testing/malware/'
        }
        headers = {
            'Content-Type': "application/json"
        }
        info("POST {}".format(endpoint))
        response = client.post(BASE_PATH + endpoint, data=json.dumps(data), headers=headers)
        assert_equal(response.status_code, 200, "Check status code")
        j = data_to_json(response.data)
        field = "status"
        expected_value = "malicious"
        assert_dict_contains_key(j, field, "Check if dict contains given key - \"{}\"".format(field))
        assert_equal(j[field], expected_value, "Check if item \"{}\" is equal to \"{}\"".format(field, expected_value))

    @allure.description("""
    Test endpoint "/verify/by_sfbrowsing"

    Send wrong data and expect error.
    """)
    def test_verify_by_sfbrowsing_wrong_data(self, client_with_db):
        client = client_with_db[0]
        endpoint = '/verify/by_sfbrowsing'
        data = {
            'temp': 'example.com'
        }
        headers = {
            'Content-Type': "application/json"
        }
        info("POST {}".format(endpoint))
        response = client.post(BASE_PATH + endpoint, data=json.dumps(data), headers=headers)
        j = data_to_json(response.data)
        assert_equal(response.status_code, 400, "Check status code")
        field = "detail"
        expected_value = "'url' is a required property"
        assert_dict_contains_key(j, field, "Check if dict contains given key - \"{}\"".format(field))
        assert_equal(j[field], expected_value, "Check if item \"{}\" is equal to \"{}\"".format(field, expected_value))
        field = "title"
        expected_value = "Bad Request"
        assert_dict_contains_key(j, field, "Check if dict contains given key - \"{}\"".format(field))
        assert_equal(j[field], expected_value, "Check if item \"{}\" is equal to \"{}\"".format(field, expected_value))