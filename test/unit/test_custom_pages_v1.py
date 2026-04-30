# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for CustomPagesV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.custom_pages_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = CustomPagesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier,
)

_base_url = 'https://api.cis.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: CustomPages
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CustomPagesV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CustomPagesV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CustomPagesV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = CustomPagesV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = CustomPagesV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestListInstanceCustomPages:
    """
    Test Class for list_instance_custom_pages
    """

    @responses.activate
    def test_list_instance_custom_pages_all_params(self):
        """
        list_instance_custom_pages()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_instance_custom_pages()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_custom_pages_all_params_with_retries(self):
        # Enable retries and run test_list_instance_custom_pages_all_params.
        _service.enable_retries()
        self.test_list_instance_custom_pages_all_params()

        # Disable retries and run test_list_instance_custom_pages_all_params.
        _service.disable_retries()
        self.test_list_instance_custom_pages_all_params()

    @responses.activate
    def test_list_instance_custom_pages_value_error(self):
        """
        test_list_instance_custom_pages_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_custom_pages(**req_copy)

    def test_list_instance_custom_pages_value_error_with_retries(self):
        # Enable retries and run test_list_instance_custom_pages_value_error.
        _service.enable_retries()
        self.test_list_instance_custom_pages_value_error()

        # Disable retries and run test_list_instance_custom_pages_value_error.
        _service.disable_retries()
        self.test_list_instance_custom_pages_value_error()


class TestGetInstanceCustomPage:
    """
    Test Class for get_instance_custom_page
    """

    @responses.activate
    def test_get_instance_custom_page_all_params(self):
        """
        get_instance_custom_page()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = _service.get_instance_custom_page(
            page_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_custom_page_all_params_with_retries(self):
        # Enable retries and run test_get_instance_custom_page_all_params.
        _service.enable_retries()
        self.test_get_instance_custom_page_all_params()

        # Disable retries and run test_get_instance_custom_page_all_params.
        _service.disable_retries()
        self.test_get_instance_custom_page_all_params()

    @responses.activate
    def test_get_instance_custom_page_value_error(self):
        """
        test_get_instance_custom_page_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "page_identifier": page_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_custom_page(**req_copy)

    def test_get_instance_custom_page_value_error_with_retries(self):
        # Enable retries and run test_get_instance_custom_page_value_error.
        _service.enable_retries()
        self.test_get_instance_custom_page_value_error()

        # Disable retries and run test_get_instance_custom_page_value_error.
        _service.disable_retries()
        self.test_get_instance_custom_page_value_error()


class TestUpdateInstanceCustomPage:
    """
    Test Class for update_instance_custom_page
    """

    @responses.activate
    def test_update_instance_custom_page_all_params(self):
        """
        update_instance_custom_page()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'
        url = 'https://www.example.com/basic_challenge_error.html'
        state = 'customized'

        # Invoke method
        response = _service.update_instance_custom_page(
            page_identifier,
            url=url,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['url'] == 'https://www.example.com/basic_challenge_error.html'
        assert req_body['state'] == 'customized'

    def test_update_instance_custom_page_all_params_with_retries(self):
        # Enable retries and run test_update_instance_custom_page_all_params.
        _service.enable_retries()
        self.test_update_instance_custom_page_all_params()

        # Disable retries and run test_update_instance_custom_page_all_params.
        _service.disable_retries()
        self.test_update_instance_custom_page_all_params()

    @responses.activate
    def test_update_instance_custom_page_required_params(self):
        """
        test_update_instance_custom_page_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = _service.update_instance_custom_page(
            page_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_instance_custom_page_required_params_with_retries(self):
        # Enable retries and run test_update_instance_custom_page_required_params.
        _service.enable_retries()
        self.test_update_instance_custom_page_required_params()

        # Disable retries and run test_update_instance_custom_page_required_params.
        _service.disable_retries()
        self.test_update_instance_custom_page_required_params()

    @responses.activate
    def test_update_instance_custom_page_value_error(self):
        """
        test_update_instance_custom_page_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "page_identifier": page_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_custom_page(**req_copy)

    def test_update_instance_custom_page_value_error_with_retries(self):
        # Enable retries and run test_update_instance_custom_page_value_error.
        _service.enable_retries()
        self.test_update_instance_custom_page_value_error()

        # Disable retries and run test_update_instance_custom_page_value_error.
        _service.disable_retries()
        self.test_update_instance_custom_page_value_error()


class TestListZoneCustomPages:
    """
    Test Class for list_zone_custom_pages
    """

    @responses.activate
    def test_list_zone_custom_pages_all_params(self):
        """
        list_zone_custom_pages()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_zone_custom_pages()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_zone_custom_pages_all_params_with_retries(self):
        # Enable retries and run test_list_zone_custom_pages_all_params.
        _service.enable_retries()
        self.test_list_zone_custom_pages_all_params()

        # Disable retries and run test_list_zone_custom_pages_all_params.
        _service.disable_retries()
        self.test_list_zone_custom_pages_all_params()

    @responses.activate
    def test_list_zone_custom_pages_value_error(self):
        """
        test_list_zone_custom_pages_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_zone_custom_pages(**req_copy)

    def test_list_zone_custom_pages_value_error_with_retries(self):
        # Enable retries and run test_list_zone_custom_pages_value_error.
        _service.enable_retries()
        self.test_list_zone_custom_pages_value_error()

        # Disable retries and run test_list_zone_custom_pages_value_error.
        _service.disable_retries()
        self.test_list_zone_custom_pages_value_error()


class TestGetZoneCustomPage:
    """
    Test Class for get_zone_custom_page
    """

    @responses.activate
    def test_get_zone_custom_page_all_params(self):
        """
        get_zone_custom_page()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = _service.get_zone_custom_page(
            page_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_custom_page_all_params_with_retries(self):
        # Enable retries and run test_get_zone_custom_page_all_params.
        _service.enable_retries()
        self.test_get_zone_custom_page_all_params()

        # Disable retries and run test_get_zone_custom_page_all_params.
        _service.disable_retries()
        self.test_get_zone_custom_page_all_params()

    @responses.activate
    def test_get_zone_custom_page_value_error(self):
        """
        test_get_zone_custom_page_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "page_identifier": page_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_custom_page(**req_copy)

    def test_get_zone_custom_page_value_error_with_retries(self):
        # Enable retries and run test_get_zone_custom_page_value_error.
        _service.enable_retries()
        self.test_get_zone_custom_page_value_error()

        # Disable retries and run test_get_zone_custom_page_value_error.
        _service.disable_retries()
        self.test_get_zone_custom_page_value_error()


class TestUpdateZoneCustomPage:
    """
    Test Class for update_zone_custom_page
    """

    @responses.activate
    def test_update_zone_custom_page_all_params(self):
        """
        update_zone_custom_page()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'
        url = 'https://www.example.com/basic_challenge_error.html'
        state = 'customized'

        # Invoke method
        response = _service.update_zone_custom_page(
            page_identifier,
            url=url,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['url'] == 'https://www.example.com/basic_challenge_error.html'
        assert req_body['state'] == 'customized'

    def test_update_zone_custom_page_all_params_with_retries(self):
        # Enable retries and run test_update_zone_custom_page_all_params.
        _service.enable_retries()
        self.test_update_zone_custom_page_all_params()

        # Disable retries and run test_update_zone_custom_page_all_params.
        _service.disable_retries()
        self.test_update_zone_custom_page_all_params()

    @responses.activate
    def test_update_zone_custom_page_required_params(self):
        """
        test_update_zone_custom_page_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = _service.update_zone_custom_page(
            page_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_custom_page_required_params_with_retries(self):
        # Enable retries and run test_update_zone_custom_page_required_params.
        _service.enable_retries()
        self.test_update_zone_custom_page_required_params()

        # Disable retries and run test_update_zone_custom_page_required_params.
        _service.disable_retries()
        self.test_update_zone_custom_page_required_params()

    @responses.activate
    def test_update_zone_custom_page_value_error(self):
        """
        test_update_zone_custom_page_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/custom_pages/basic_challenge')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-03-28T02:39:06.656Z", "modified_on": "2019-04-01T07:17:18.358Z", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "page_identifier": page_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_zone_custom_page(**req_copy)

    def test_update_zone_custom_page_value_error_with_retries(self):
        # Enable retries and run test_update_zone_custom_page_value_error.
        _service.enable_retries()
        self.test_update_zone_custom_page_value_error()

        # Disable retries and run test_update_zone_custom_page_value_error.
        _service.disable_retries()
        self.test_update_zone_custom_page_value_error()


# endregion
##############################################################################
# End of Service: CustomPages
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_ListCustomPagesRespResultInfo:
    """
    Test Class for ListCustomPagesRespResultInfo
    """

    def test_list_custom_pages_resp_result_info_serialization(self):
        """
        Test serialization/deserialization for ListCustomPagesRespResultInfo
        """

        # Construct a json representation of a ListCustomPagesRespResultInfo model
        list_custom_pages_resp_result_info_model_json = {}
        list_custom_pages_resp_result_info_model_json['page'] = 1
        list_custom_pages_resp_result_info_model_json['per_page'] = 20
        list_custom_pages_resp_result_info_model_json['total_pages'] = 1
        list_custom_pages_resp_result_info_model_json['count'] = 10
        list_custom_pages_resp_result_info_model_json['total_count'] = 10

        # Construct a model instance of ListCustomPagesRespResultInfo by calling from_dict on the json representation
        list_custom_pages_resp_result_info_model = ListCustomPagesRespResultInfo.from_dict(list_custom_pages_resp_result_info_model_json)
        assert list_custom_pages_resp_result_info_model != False

        # Construct a model instance of ListCustomPagesRespResultInfo by calling from_dict on the json representation
        list_custom_pages_resp_result_info_model_dict = ListCustomPagesRespResultInfo.from_dict(list_custom_pages_resp_result_info_model_json).__dict__
        list_custom_pages_resp_result_info_model2 = ListCustomPagesRespResultInfo(**list_custom_pages_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_custom_pages_resp_result_info_model == list_custom_pages_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_custom_pages_resp_result_info_model_json2 = list_custom_pages_resp_result_info_model.to_dict()
        assert list_custom_pages_resp_result_info_model_json2 == list_custom_pages_resp_result_info_model_json


class TestModel_CustomPageObject:
    """
    Test Class for CustomPageObject
    """

    def test_custom_page_object_serialization(self):
        """
        Test serialization/deserialization for CustomPageObject
        """

        # Construct a json representation of a CustomPageObject model
        custom_page_object_model_json = {}
        custom_page_object_model_json['id'] = 'basic_challenge'
        custom_page_object_model_json['description'] = 'Basic Challenge'
        custom_page_object_model_json['required_tokens'] = ['::CAPTCHA_BOX::']
        custom_page_object_model_json['preview_target'] = 'block:basic-sec-captcha'
        custom_page_object_model_json['created_on'] = '2019-03-28T02:39:06.656000Z'
        custom_page_object_model_json['modified_on'] = '2019-04-01T07:17:18.358000Z'
        custom_page_object_model_json['url'] = 'https://www.example.com/basic_challenge_error.html'
        custom_page_object_model_json['state'] = 'customized'

        # Construct a model instance of CustomPageObject by calling from_dict on the json representation
        custom_page_object_model = CustomPageObject.from_dict(custom_page_object_model_json)
        assert custom_page_object_model != False

        # Construct a model instance of CustomPageObject by calling from_dict on the json representation
        custom_page_object_model_dict = CustomPageObject.from_dict(custom_page_object_model_json).__dict__
        custom_page_object_model2 = CustomPageObject(**custom_page_object_model_dict)

        # Verify the model instances are equivalent
        assert custom_page_object_model == custom_page_object_model2

        # Convert model instance back to dict and verify no loss of data
        custom_page_object_model_json2 = custom_page_object_model.to_dict()
        assert custom_page_object_model_json2 == custom_page_object_model_json


class TestModel_CustomPageSpecificResp:
    """
    Test Class for CustomPageSpecificResp
    """

    def test_custom_page_specific_resp_serialization(self):
        """
        Test serialization/deserialization for CustomPageSpecificResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_page_object_model = {}  # CustomPageObject
        custom_page_object_model['id'] = 'basic_challenge'
        custom_page_object_model['description'] = 'Basic Challenge'
        custom_page_object_model['required_tokens'] = ['::CAPTCHA_BOX::']
        custom_page_object_model['preview_target'] = 'block:basic-sec-captcha'
        custom_page_object_model['created_on'] = '2019-03-28T02:39:06.656000Z'
        custom_page_object_model['modified_on'] = '2019-04-01T07:17:18.358000Z'
        custom_page_object_model['url'] = 'https://www.example.com/basic_challenge_error.html'
        custom_page_object_model['state'] = 'customized'

        # Construct a json representation of a CustomPageSpecificResp model
        custom_page_specific_resp_model_json = {}
        custom_page_specific_resp_model_json['success'] = True
        custom_page_specific_resp_model_json['errors'] = []
        custom_page_specific_resp_model_json['messages'] = []
        custom_page_specific_resp_model_json['result'] = custom_page_object_model

        # Construct a model instance of CustomPageSpecificResp by calling from_dict on the json representation
        custom_page_specific_resp_model = CustomPageSpecificResp.from_dict(custom_page_specific_resp_model_json)
        assert custom_page_specific_resp_model != False

        # Construct a model instance of CustomPageSpecificResp by calling from_dict on the json representation
        custom_page_specific_resp_model_dict = CustomPageSpecificResp.from_dict(custom_page_specific_resp_model_json).__dict__
        custom_page_specific_resp_model2 = CustomPageSpecificResp(**custom_page_specific_resp_model_dict)

        # Verify the model instances are equivalent
        assert custom_page_specific_resp_model == custom_page_specific_resp_model2

        # Convert model instance back to dict and verify no loss of data
        custom_page_specific_resp_model_json2 = custom_page_specific_resp_model.to_dict()
        assert custom_page_specific_resp_model_json2 == custom_page_specific_resp_model_json


class TestModel_ListCustomPagesResp:
    """
    Test Class for ListCustomPagesResp
    """

    def test_list_custom_pages_resp_serialization(self):
        """
        Test serialization/deserialization for ListCustomPagesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_page_object_model = {}  # CustomPageObject
        custom_page_object_model['id'] = 'basic_challenge'
        custom_page_object_model['description'] = 'Basic Challenge'
        custom_page_object_model['required_tokens'] = ['::CAPTCHA_BOX::']
        custom_page_object_model['preview_target'] = 'block:basic-sec-captcha'
        custom_page_object_model['created_on'] = '2019-01-01T00:00:00Z'
        custom_page_object_model['modified_on'] = '2019-01-01T00:00:00Z'
        custom_page_object_model['url'] = 'null'
        custom_page_object_model['state'] = 'default'

        list_custom_pages_resp_result_info_model = {}  # ListCustomPagesRespResultInfo
        list_custom_pages_resp_result_info_model['page'] = 1
        list_custom_pages_resp_result_info_model['per_page'] = 20
        list_custom_pages_resp_result_info_model['total_pages'] = 1
        list_custom_pages_resp_result_info_model['count'] = 10
        list_custom_pages_resp_result_info_model['total_count'] = 10

        # Construct a json representation of a ListCustomPagesResp model
        list_custom_pages_resp_model_json = {}
        list_custom_pages_resp_model_json['success'] = True
        list_custom_pages_resp_model_json['errors'] = []
        list_custom_pages_resp_model_json['messages'] = []
        list_custom_pages_resp_model_json['result'] = [custom_page_object_model]
        list_custom_pages_resp_model_json['result_info'] = list_custom_pages_resp_result_info_model

        # Construct a model instance of ListCustomPagesResp by calling from_dict on the json representation
        list_custom_pages_resp_model = ListCustomPagesResp.from_dict(list_custom_pages_resp_model_json)
        assert list_custom_pages_resp_model != False

        # Construct a model instance of ListCustomPagesResp by calling from_dict on the json representation
        list_custom_pages_resp_model_dict = ListCustomPagesResp.from_dict(list_custom_pages_resp_model_json).__dict__
        list_custom_pages_resp_model2 = ListCustomPagesResp(**list_custom_pages_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_custom_pages_resp_model == list_custom_pages_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_custom_pages_resp_model_json2 = list_custom_pages_resp_model.to_dict()
        assert list_custom_pages_resp_model_json2 == list_custom_pages_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
