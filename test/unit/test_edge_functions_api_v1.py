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
Unit Tests for EdgeFunctionsApiV1
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
from ibm_cloud_networking_services.edge_functions_api_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = EdgeFunctionsApiV1(
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
# Start of Service: EdgeFunctionsActions
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

        service = EdgeFunctionsApiV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EdgeFunctionsApiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EdgeFunctionsApiV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = EdgeFunctionsApiV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided must be provided'):
            service = EdgeFunctionsApiV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestListEdgeFunctionsActions:
    """
    Test Class for list_edge_functions_actions
    """

    @responses.activate
    def test_list_edge_functions_actions_all_params(self):
        """
        list_edge_functions_actions()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts')
        mock_response = '{"result": [{"script": "addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })", "etag": "ea95132c15732412d22c1476fa83f27a", "handlers": ["fetch"], "modified_on": "2100-01-01T05:20:00.000Z", "created_on": "2100-01-01T05:20:00.000Z", "routes": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}]}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_edge_functions_actions(
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_edge_functions_actions_all_params_with_retries(self):
        # Enable retries and run test_list_edge_functions_actions_all_params.
        _service.enable_retries()
        self.test_list_edge_functions_actions_all_params()

        # Disable retries and run test_list_edge_functions_actions_all_params.
        _service.disable_retries()
        self.test_list_edge_functions_actions_all_params()

    @responses.activate
    def test_list_edge_functions_actions_required_params(self):
        """
        test_list_edge_functions_actions_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts')
        mock_response = '{"result": [{"script": "addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })", "etag": "ea95132c15732412d22c1476fa83f27a", "handlers": ["fetch"], "modified_on": "2100-01-01T05:20:00.000Z", "created_on": "2100-01-01T05:20:00.000Z", "routes": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}]}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_edge_functions_actions()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_edge_functions_actions_required_params_with_retries(self):
        # Enable retries and run test_list_edge_functions_actions_required_params.
        _service.enable_retries()
        self.test_list_edge_functions_actions_required_params()

        # Disable retries and run test_list_edge_functions_actions_required_params.
        _service.disable_retries()
        self.test_list_edge_functions_actions_required_params()

    @responses.activate
    def test_list_edge_functions_actions_value_error(self):
        """
        test_list_edge_functions_actions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts')
        mock_response = '{"result": [{"script": "addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })", "etag": "ea95132c15732412d22c1476fa83f27a", "handlers": ["fetch"], "modified_on": "2100-01-01T05:20:00.000Z", "created_on": "2100-01-01T05:20:00.000Z", "routes": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}]}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
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
                _service.list_edge_functions_actions(**req_copy)

    def test_list_edge_functions_actions_value_error_with_retries(self):
        # Enable retries and run test_list_edge_functions_actions_value_error.
        _service.enable_retries()
        self.test_list_edge_functions_actions_value_error()

        # Disable retries and run test_list_edge_functions_actions_value_error.
        _service.disable_retries()
        self.test_list_edge_functions_actions_value_error()


class TestUpdateEdgeFunctionsAction:
    """
    Test Class for update_edge_functions_action
    """

    @responses.activate
    def test_update_edge_functions_action_all_params(self):
        """
        update_edge_functions_action()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = '{"result": {"script": "addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })", "etag": "ea95132c15732412d22c1476fa83f27a", "handlers": ["fetch"], "modified_on": "2100-01-01T05:20:00.000Z", "created_on": "2100-01-01T05:20:00.000Z", "routes": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}]}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'
        edge_functions_action = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_edge_functions_action(
            script_name,
            edge_functions_action=edge_functions_action,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        assert str(responses.calls[0].request.body, 'utf-8') == edge_functions_action

    def test_update_edge_functions_action_all_params_with_retries(self):
        # Enable retries and run test_update_edge_functions_action_all_params.
        _service.enable_retries()
        self.test_update_edge_functions_action_all_params()

        # Disable retries and run test_update_edge_functions_action_all_params.
        _service.disable_retries()
        self.test_update_edge_functions_action_all_params()

    @responses.activate
    def test_update_edge_functions_action_required_params(self):
        """
        test_update_edge_functions_action_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = '{"result": {"script": "addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })", "etag": "ea95132c15732412d22c1476fa83f27a", "handlers": ["fetch"], "modified_on": "2100-01-01T05:20:00.000Z", "created_on": "2100-01-01T05:20:00.000Z", "routes": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}]}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'

        # Invoke method
        response = _service.update_edge_functions_action(
            script_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_edge_functions_action_required_params_with_retries(self):
        # Enable retries and run test_update_edge_functions_action_required_params.
        _service.enable_retries()
        self.test_update_edge_functions_action_required_params()

        # Disable retries and run test_update_edge_functions_action_required_params.
        _service.disable_retries()
        self.test_update_edge_functions_action_required_params()

    @responses.activate
    def test_update_edge_functions_action_value_error(self):
        """
        test_update_edge_functions_action_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = '{"result": {"script": "addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })", "etag": "ea95132c15732412d22c1476fa83f27a", "handlers": ["fetch"], "modified_on": "2100-01-01T05:20:00.000Z", "created_on": "2100-01-01T05:20:00.000Z", "routes": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}]}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "script_name": script_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_edge_functions_action(**req_copy)

    def test_update_edge_functions_action_value_error_with_retries(self):
        # Enable retries and run test_update_edge_functions_action_value_error.
        _service.enable_retries()
        self.test_update_edge_functions_action_value_error()

        # Disable retries and run test_update_edge_functions_action_value_error.
        _service.disable_retries()
        self.test_update_edge_functions_action_value_error()


class TestGetEdgeFunctionsAction:
    """
    Test Class for get_edge_functions_action
    """

    @responses.activate
    def test_get_edge_functions_action_all_params(self):
        """
        get_edge_functions_action()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/javascript',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_edge_functions_action(
            script_name,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_edge_functions_action_all_params_with_retries(self):
        # Enable retries and run test_get_edge_functions_action_all_params.
        _service.enable_retries()
        self.test_get_edge_functions_action_all_params()

        # Disable retries and run test_get_edge_functions_action_all_params.
        _service.disable_retries()
        self.test_get_edge_functions_action_all_params()

    @responses.activate
    def test_get_edge_functions_action_required_params(self):
        """
        test_get_edge_functions_action_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/javascript',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'

        # Invoke method
        response = _service.get_edge_functions_action(
            script_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_edge_functions_action_required_params_with_retries(self):
        # Enable retries and run test_get_edge_functions_action_required_params.
        _service.enable_retries()
        self.test_get_edge_functions_action_required_params()

        # Disable retries and run test_get_edge_functions_action_required_params.
        _service.disable_retries()
        self.test_get_edge_functions_action_required_params()

    @responses.activate
    def test_get_edge_functions_action_value_error(self):
        """
        test_get_edge_functions_action_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/javascript',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "script_name": script_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_edge_functions_action(**req_copy)

    def test_get_edge_functions_action_value_error_with_retries(self):
        # Enable retries and run test_get_edge_functions_action_value_error.
        _service.enable_retries()
        self.test_get_edge_functions_action_value_error()

        # Disable retries and run test_get_edge_functions_action_value_error.
        _service.disable_retries()
        self.test_get_edge_functions_action_value_error()


class TestDeleteEdgeFunctionsAction:
    """
    Test Class for delete_edge_functions_action
    """

    @responses.activate
    def test_delete_edge_functions_action_all_params(self):
        """
        delete_edge_functions_action()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_edge_functions_action(
            script_name,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_edge_functions_action_all_params_with_retries(self):
        # Enable retries and run test_delete_edge_functions_action_all_params.
        _service.enable_retries()
        self.test_delete_edge_functions_action_all_params()

        # Disable retries and run test_delete_edge_functions_action_all_params.
        _service.disable_retries()
        self.test_delete_edge_functions_action_all_params()

    @responses.activate
    def test_delete_edge_functions_action_required_params(self):
        """
        test_delete_edge_functions_action_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'

        # Invoke method
        response = _service.delete_edge_functions_action(
            script_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_edge_functions_action_required_params_with_retries(self):
        # Enable retries and run test_delete_edge_functions_action_required_params.
        _service.enable_retries()
        self.test_delete_edge_functions_action_required_params()

        # Disable retries and run test_delete_edge_functions_action_required_params.
        _service.disable_retries()
        self.test_delete_edge_functions_action_required_params()

    @responses.activate
    def test_delete_edge_functions_action_value_error(self):
        """
        test_delete_edge_functions_action_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/workers/scripts/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        script_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "script_name": script_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_edge_functions_action(**req_copy)

    def test_delete_edge_functions_action_value_error_with_retries(self):
        # Enable retries and run test_delete_edge_functions_action_value_error.
        _service.enable_retries()
        self.test_delete_edge_functions_action_value_error()

        # Disable retries and run test_delete_edge_functions_action_value_error.
        _service.disable_retries()
        self.test_delete_edge_functions_action_value_error()


# endregion
##############################################################################
# End of Service: EdgeFunctionsActions
##############################################################################

##############################################################################
# Start of Service: EdgeFunctionsTriggers
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

        service = EdgeFunctionsApiV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EdgeFunctionsApiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EdgeFunctionsApiV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = EdgeFunctionsApiV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = EdgeFunctionsApiV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestCreateEdgeFunctionsTrigger:
    """
    Test Class for create_edge_functions_trigger
    """

    @responses.activate
    def test_create_edge_functions_trigger_all_params(self):
        """
        create_edge_functions_trigger()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pattern = 'example.net/*'
        script = 'this-is_my_script-01'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_edge_functions_trigger(
            pattern=pattern,
            script=script,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pattern'] == 'example.net/*'
        assert req_body['script'] == 'this-is_my_script-01'

    def test_create_edge_functions_trigger_all_params_with_retries(self):
        # Enable retries and run test_create_edge_functions_trigger_all_params.
        _service.enable_retries()
        self.test_create_edge_functions_trigger_all_params()

        # Disable retries and run test_create_edge_functions_trigger_all_params.
        _service.disable_retries()
        self.test_create_edge_functions_trigger_all_params()

    @responses.activate
    def test_create_edge_functions_trigger_required_params(self):
        """
        test_create_edge_functions_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_edge_functions_trigger()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_edge_functions_trigger_required_params_with_retries(self):
        # Enable retries and run test_create_edge_functions_trigger_required_params.
        _service.enable_retries()
        self.test_create_edge_functions_trigger_required_params()

        # Disable retries and run test_create_edge_functions_trigger_required_params.
        _service.disable_retries()
        self.test_create_edge_functions_trigger_required_params()

    @responses.activate
    def test_create_edge_functions_trigger_value_error(self):
        """
        test_create_edge_functions_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.POST,
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
                _service.create_edge_functions_trigger(**req_copy)

    def test_create_edge_functions_trigger_value_error_with_retries(self):
        # Enable retries and run test_create_edge_functions_trigger_value_error.
        _service.enable_retries()
        self.test_create_edge_functions_trigger_value_error()

        # Disable retries and run test_create_edge_functions_trigger_value_error.
        _service.disable_retries()
        self.test_create_edge_functions_trigger_value_error()


class TestListEdgeFunctionsTriggers:
    """
    Test Class for list_edge_functions_triggers
    """

    @responses.activate
    def test_list_edge_functions_triggers_all_params(self):
        """
        list_edge_functions_triggers()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes')
        mock_response = '{"result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_edge_functions_triggers(
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_edge_functions_triggers_all_params_with_retries(self):
        # Enable retries and run test_list_edge_functions_triggers_all_params.
        _service.enable_retries()
        self.test_list_edge_functions_triggers_all_params()

        # Disable retries and run test_list_edge_functions_triggers_all_params.
        _service.disable_retries()
        self.test_list_edge_functions_triggers_all_params()

    @responses.activate
    def test_list_edge_functions_triggers_required_params(self):
        """
        test_list_edge_functions_triggers_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes')
        mock_response = '{"result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_edge_functions_triggers()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_edge_functions_triggers_required_params_with_retries(self):
        # Enable retries and run test_list_edge_functions_triggers_required_params.
        _service.enable_retries()
        self.test_list_edge_functions_triggers_required_params()

        # Disable retries and run test_list_edge_functions_triggers_required_params.
        _service.disable_retries()
        self.test_list_edge_functions_triggers_required_params()

    @responses.activate
    def test_list_edge_functions_triggers_value_error(self):
        """
        test_list_edge_functions_triggers_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes')
        mock_response = '{"result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
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
                _service.list_edge_functions_triggers(**req_copy)

    def test_list_edge_functions_triggers_value_error_with_retries(self):
        # Enable retries and run test_list_edge_functions_triggers_value_error.
        _service.enable_retries()
        self.test_list_edge_functions_triggers_value_error()

        # Disable retries and run test_list_edge_functions_triggers_value_error.
        _service.disable_retries()
        self.test_list_edge_functions_triggers_value_error()


class TestGetEdgeFunctionsTrigger:
    """
    Test Class for get_edge_functions_trigger
    """

    @responses.activate
    def test_get_edge_functions_trigger_all_params(self):
        """
        get_edge_functions_trigger()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_edge_functions_trigger(
            route_id,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_edge_functions_trigger_all_params_with_retries(self):
        # Enable retries and run test_get_edge_functions_trigger_all_params.
        _service.enable_retries()
        self.test_get_edge_functions_trigger_all_params()

        # Disable retries and run test_get_edge_functions_trigger_all_params.
        _service.disable_retries()
        self.test_get_edge_functions_trigger_all_params()

    @responses.activate
    def test_get_edge_functions_trigger_required_params(self):
        """
        test_get_edge_functions_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'

        # Invoke method
        response = _service.get_edge_functions_trigger(
            route_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_edge_functions_trigger_required_params_with_retries(self):
        # Enable retries and run test_get_edge_functions_trigger_required_params.
        _service.enable_retries()
        self.test_get_edge_functions_trigger_required_params()

        # Disable retries and run test_get_edge_functions_trigger_required_params.
        _service.disable_retries()
        self.test_get_edge_functions_trigger_required_params()

    @responses.activate
    def test_get_edge_functions_trigger_value_error(self):
        """
        test_get_edge_functions_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "route_id": route_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_edge_functions_trigger(**req_copy)

    def test_get_edge_functions_trigger_value_error_with_retries(self):
        # Enable retries and run test_get_edge_functions_trigger_value_error.
        _service.enable_retries()
        self.test_get_edge_functions_trigger_value_error()

        # Disable retries and run test_get_edge_functions_trigger_value_error.
        _service.disable_retries()
        self.test_get_edge_functions_trigger_value_error()


class TestUpdateEdgeFunctionsTrigger:
    """
    Test Class for update_edge_functions_trigger
    """

    @responses.activate
    def test_update_edge_functions_trigger_all_params(self):
        """
        update_edge_functions_trigger()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'
        pattern = 'example.net/*'
        script = 'this-is_my_script-01'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_edge_functions_trigger(
            route_id,
            pattern=pattern,
            script=script,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pattern'] == 'example.net/*'
        assert req_body['script'] == 'this-is_my_script-01'

    def test_update_edge_functions_trigger_all_params_with_retries(self):
        # Enable retries and run test_update_edge_functions_trigger_all_params.
        _service.enable_retries()
        self.test_update_edge_functions_trigger_all_params()

        # Disable retries and run test_update_edge_functions_trigger_all_params.
        _service.disable_retries()
        self.test_update_edge_functions_trigger_all_params()

    @responses.activate
    def test_update_edge_functions_trigger_required_params(self):
        """
        test_update_edge_functions_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'

        # Invoke method
        response = _service.update_edge_functions_trigger(
            route_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_edge_functions_trigger_required_params_with_retries(self):
        # Enable retries and run test_update_edge_functions_trigger_required_params.
        _service.enable_retries()
        self.test_update_edge_functions_trigger_required_params()

        # Disable retries and run test_update_edge_functions_trigger_required_params.
        _service.disable_retries()
        self.test_update_edge_functions_trigger_required_params()

    @responses.activate
    def test_update_edge_functions_trigger_value_error(self):
        """
        test_update_edge_functions_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac", "pattern": "example.net/*", "script": "this-is_my_script-01", "request_limit_fail_open": false}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "route_id": route_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_edge_functions_trigger(**req_copy)

    def test_update_edge_functions_trigger_value_error_with_retries(self):
        # Enable retries and run test_update_edge_functions_trigger_value_error.
        _service.enable_retries()
        self.test_update_edge_functions_trigger_value_error()

        # Disable retries and run test_update_edge_functions_trigger_value_error.
        _service.disable_retries()
        self.test_update_edge_functions_trigger_value_error()


class TestDeleteEdgeFunctionsTrigger:
    """
    Test Class for delete_edge_functions_trigger
    """

    @responses.activate
    def test_delete_edge_functions_trigger_all_params(self):
        """
        delete_edge_functions_trigger()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_edge_functions_trigger(
            route_id,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_edge_functions_trigger_all_params_with_retries(self):
        # Enable retries and run test_delete_edge_functions_trigger_all_params.
        _service.enable_retries()
        self.test_delete_edge_functions_trigger_all_params()

        # Disable retries and run test_delete_edge_functions_trigger_all_params.
        _service.disable_retries()
        self.test_delete_edge_functions_trigger_all_params()

    @responses.activate
    def test_delete_edge_functions_trigger_required_params(self):
        """
        test_delete_edge_functions_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'

        # Invoke method
        response = _service.delete_edge_functions_trigger(
            route_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_edge_functions_trigger_required_params_with_retries(self):
        # Enable retries and run test_delete_edge_functions_trigger_required_params.
        _service.enable_retries()
        self.test_delete_edge_functions_trigger_required_params()

        # Disable retries and run test_delete_edge_functions_trigger_required_params.
        _service.disable_retries()
        self.test_delete_edge_functions_trigger_required_params()

    @responses.activate
    def test_delete_edge_functions_trigger_value_error(self):
        """
        test_delete_edge_functions_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/workers/routes/testString')
        mock_response = '{"result": {"id": "9a7806061c88ada191ed06f989cc3dac"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        route_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "route_id": route_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_edge_functions_trigger(**req_copy)

    def test_delete_edge_functions_trigger_value_error_with_retries(self):
        # Enable retries and run test_delete_edge_functions_trigger_value_error.
        _service.enable_retries()
        self.test_delete_edge_functions_trigger_value_error()

        # Disable retries and run test_delete_edge_functions_trigger_value_error.
        _service.disable_retries()
        self.test_delete_edge_functions_trigger_value_error()


# endregion
##############################################################################
# End of Service: EdgeFunctionsTriggers
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_CreateEdgeFunctionsTriggerResp:
    """
    Test Class for CreateEdgeFunctionsTriggerResp
    """

    def test_create_edge_functions_trigger_resp_serialization(self):
        """
        Test serialization/deserialization for CreateEdgeFunctionsTriggerResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_trigger_id_model = {}  # EdgeFunctionsTriggerId
        edge_functions_trigger_id_model['id'] = '9a7806061c88ada191ed06f989cc3dac'

        # Construct a json representation of a CreateEdgeFunctionsTriggerResp model
        create_edge_functions_trigger_resp_model_json = {}
        create_edge_functions_trigger_resp_model_json['result'] = edge_functions_trigger_id_model
        create_edge_functions_trigger_resp_model_json['success'] = True
        create_edge_functions_trigger_resp_model_json['errors'] = ['testString']
        create_edge_functions_trigger_resp_model_json['messages'] = ['testString']

        # Construct a model instance of CreateEdgeFunctionsTriggerResp by calling from_dict on the json representation
        create_edge_functions_trigger_resp_model = CreateEdgeFunctionsTriggerResp.from_dict(create_edge_functions_trigger_resp_model_json)
        assert create_edge_functions_trigger_resp_model != False

        # Construct a model instance of CreateEdgeFunctionsTriggerResp by calling from_dict on the json representation
        create_edge_functions_trigger_resp_model_dict = CreateEdgeFunctionsTriggerResp.from_dict(create_edge_functions_trigger_resp_model_json).__dict__
        create_edge_functions_trigger_resp_model2 = CreateEdgeFunctionsTriggerResp(**create_edge_functions_trigger_resp_model_dict)

        # Verify the model instances are equivalent
        assert create_edge_functions_trigger_resp_model == create_edge_functions_trigger_resp_model2

        # Convert model instance back to dict and verify no loss of data
        create_edge_functions_trigger_resp_model_json2 = create_edge_functions_trigger_resp_model.to_dict()
        assert create_edge_functions_trigger_resp_model_json2 == create_edge_functions_trigger_resp_model_json


class TestModel_DeleteEdgeFunctionsActionResp:
    """
    Test Class for DeleteEdgeFunctionsActionResp
    """

    def test_delete_edge_functions_action_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteEdgeFunctionsActionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_action_id_model = {}  # EdgeFunctionsActionId
        edge_functions_action_id_model['id'] = '9a7806061c88ada191ed06f989cc3dac'

        # Construct a json representation of a DeleteEdgeFunctionsActionResp model
        delete_edge_functions_action_resp_model_json = {}
        delete_edge_functions_action_resp_model_json['result'] = edge_functions_action_id_model
        delete_edge_functions_action_resp_model_json['success'] = True
        delete_edge_functions_action_resp_model_json['errors'] = ['testString']
        delete_edge_functions_action_resp_model_json['messages'] = ['testString']

        # Construct a model instance of DeleteEdgeFunctionsActionResp by calling from_dict on the json representation
        delete_edge_functions_action_resp_model = DeleteEdgeFunctionsActionResp.from_dict(delete_edge_functions_action_resp_model_json)
        assert delete_edge_functions_action_resp_model != False

        # Construct a model instance of DeleteEdgeFunctionsActionResp by calling from_dict on the json representation
        delete_edge_functions_action_resp_model_dict = DeleteEdgeFunctionsActionResp.from_dict(delete_edge_functions_action_resp_model_json).__dict__
        delete_edge_functions_action_resp_model2 = DeleteEdgeFunctionsActionResp(**delete_edge_functions_action_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_edge_functions_action_resp_model == delete_edge_functions_action_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_edge_functions_action_resp_model_json2 = delete_edge_functions_action_resp_model.to_dict()
        assert delete_edge_functions_action_resp_model_json2 == delete_edge_functions_action_resp_model_json


class TestModel_EdgeFunctionsActionId:
    """
    Test Class for EdgeFunctionsActionId
    """

    def test_edge_functions_action_id_serialization(self):
        """
        Test serialization/deserialization for EdgeFunctionsActionId
        """

        # Construct a json representation of a EdgeFunctionsActionId model
        edge_functions_action_id_model_json = {}
        edge_functions_action_id_model_json['id'] = '9a7806061c88ada191ed06f989cc3dac'

        # Construct a model instance of EdgeFunctionsActionId by calling from_dict on the json representation
        edge_functions_action_id_model = EdgeFunctionsActionId.from_dict(edge_functions_action_id_model_json)
        assert edge_functions_action_id_model != False

        # Construct a model instance of EdgeFunctionsActionId by calling from_dict on the json representation
        edge_functions_action_id_model_dict = EdgeFunctionsActionId.from_dict(edge_functions_action_id_model_json).__dict__
        edge_functions_action_id_model2 = EdgeFunctionsActionId(**edge_functions_action_id_model_dict)

        # Verify the model instances are equivalent
        assert edge_functions_action_id_model == edge_functions_action_id_model2

        # Convert model instance back to dict and verify no loss of data
        edge_functions_action_id_model_json2 = edge_functions_action_id_model.to_dict()
        assert edge_functions_action_id_model_json2 == edge_functions_action_id_model_json


class TestModel_EdgeFunctionsActionResp:
    """
    Test Class for EdgeFunctionsActionResp
    """

    def test_edge_functions_action_resp_serialization(self):
        """
        Test serialization/deserialization for EdgeFunctionsActionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_trigger_resp_model = {}  # EdgeFunctionsTriggerResp
        edge_functions_trigger_resp_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        edge_functions_trigger_resp_model['pattern'] = 'example.net/*'
        edge_functions_trigger_resp_model['script'] = 'this-is_my_script-01'
        edge_functions_trigger_resp_model['request_limit_fail_open'] = False

        # Construct a json representation of a EdgeFunctionsActionResp model
        edge_functions_action_resp_model_json = {}
        edge_functions_action_resp_model_json['script'] = 'addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })'
        edge_functions_action_resp_model_json['etag'] = 'ea95132c15732412d22c1476fa83f27a'
        edge_functions_action_resp_model_json['handlers'] = ['fetch']
        edge_functions_action_resp_model_json['modified_on'] = '2100-01-01T05:20:00Z'
        edge_functions_action_resp_model_json['created_on'] = '2100-01-01T05:20:00Z'
        edge_functions_action_resp_model_json['routes'] = [edge_functions_trigger_resp_model]

        # Construct a model instance of EdgeFunctionsActionResp by calling from_dict on the json representation
        edge_functions_action_resp_model = EdgeFunctionsActionResp.from_dict(edge_functions_action_resp_model_json)
        assert edge_functions_action_resp_model != False

        # Construct a model instance of EdgeFunctionsActionResp by calling from_dict on the json representation
        edge_functions_action_resp_model_dict = EdgeFunctionsActionResp.from_dict(edge_functions_action_resp_model_json).__dict__
        edge_functions_action_resp_model2 = EdgeFunctionsActionResp(**edge_functions_action_resp_model_dict)

        # Verify the model instances are equivalent
        assert edge_functions_action_resp_model == edge_functions_action_resp_model2

        # Convert model instance back to dict and verify no loss of data
        edge_functions_action_resp_model_json2 = edge_functions_action_resp_model.to_dict()
        assert edge_functions_action_resp_model_json2 == edge_functions_action_resp_model_json


class TestModel_EdgeFunctionsTriggerId:
    """
    Test Class for EdgeFunctionsTriggerId
    """

    def test_edge_functions_trigger_id_serialization(self):
        """
        Test serialization/deserialization for EdgeFunctionsTriggerId
        """

        # Construct a json representation of a EdgeFunctionsTriggerId model
        edge_functions_trigger_id_model_json = {}
        edge_functions_trigger_id_model_json['id'] = '9a7806061c88ada191ed06f989cc3dac'

        # Construct a model instance of EdgeFunctionsTriggerId by calling from_dict on the json representation
        edge_functions_trigger_id_model = EdgeFunctionsTriggerId.from_dict(edge_functions_trigger_id_model_json)
        assert edge_functions_trigger_id_model != False

        # Construct a model instance of EdgeFunctionsTriggerId by calling from_dict on the json representation
        edge_functions_trigger_id_model_dict = EdgeFunctionsTriggerId.from_dict(edge_functions_trigger_id_model_json).__dict__
        edge_functions_trigger_id_model2 = EdgeFunctionsTriggerId(**edge_functions_trigger_id_model_dict)

        # Verify the model instances are equivalent
        assert edge_functions_trigger_id_model == edge_functions_trigger_id_model2

        # Convert model instance back to dict and verify no loss of data
        edge_functions_trigger_id_model_json2 = edge_functions_trigger_id_model.to_dict()
        assert edge_functions_trigger_id_model_json2 == edge_functions_trigger_id_model_json


class TestModel_EdgeFunctionsTriggerResp:
    """
    Test Class for EdgeFunctionsTriggerResp
    """

    def test_edge_functions_trigger_resp_serialization(self):
        """
        Test serialization/deserialization for EdgeFunctionsTriggerResp
        """

        # Construct a json representation of a EdgeFunctionsTriggerResp model
        edge_functions_trigger_resp_model_json = {}
        edge_functions_trigger_resp_model_json['id'] = '9a7806061c88ada191ed06f989cc3dac'
        edge_functions_trigger_resp_model_json['pattern'] = 'example.net/*'
        edge_functions_trigger_resp_model_json['script'] = 'this-is_my_script-01'
        edge_functions_trigger_resp_model_json['request_limit_fail_open'] = False

        # Construct a model instance of EdgeFunctionsTriggerResp by calling from_dict on the json representation
        edge_functions_trigger_resp_model = EdgeFunctionsTriggerResp.from_dict(edge_functions_trigger_resp_model_json)
        assert edge_functions_trigger_resp_model != False

        # Construct a model instance of EdgeFunctionsTriggerResp by calling from_dict on the json representation
        edge_functions_trigger_resp_model_dict = EdgeFunctionsTriggerResp.from_dict(edge_functions_trigger_resp_model_json).__dict__
        edge_functions_trigger_resp_model2 = EdgeFunctionsTriggerResp(**edge_functions_trigger_resp_model_dict)

        # Verify the model instances are equivalent
        assert edge_functions_trigger_resp_model == edge_functions_trigger_resp_model2

        # Convert model instance back to dict and verify no loss of data
        edge_functions_trigger_resp_model_json2 = edge_functions_trigger_resp_model.to_dict()
        assert edge_functions_trigger_resp_model_json2 == edge_functions_trigger_resp_model_json


class TestModel_GetEdgeFunctionsActionResp:
    """
    Test Class for GetEdgeFunctionsActionResp
    """

    def test_get_edge_functions_action_resp_serialization(self):
        """
        Test serialization/deserialization for GetEdgeFunctionsActionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_trigger_resp_model = {}  # EdgeFunctionsTriggerResp
        edge_functions_trigger_resp_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        edge_functions_trigger_resp_model['pattern'] = 'example.net/*'
        edge_functions_trigger_resp_model['script'] = 'this-is_my_script-01'
        edge_functions_trigger_resp_model['request_limit_fail_open'] = False

        edge_functions_action_resp_model = {}  # EdgeFunctionsActionResp
        edge_functions_action_resp_model['script'] = 'addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })'
        edge_functions_action_resp_model['etag'] = 'ea95132c15732412d22c1476fa83f27a'
        edge_functions_action_resp_model['handlers'] = ['fetch']
        edge_functions_action_resp_model['modified_on'] = '2100-01-01T05:20:00Z'
        edge_functions_action_resp_model['created_on'] = '2100-01-01T05:20:00Z'
        edge_functions_action_resp_model['routes'] = [edge_functions_trigger_resp_model]

        # Construct a json representation of a GetEdgeFunctionsActionResp model
        get_edge_functions_action_resp_model_json = {}
        get_edge_functions_action_resp_model_json['result'] = edge_functions_action_resp_model
        get_edge_functions_action_resp_model_json['success'] = True
        get_edge_functions_action_resp_model_json['errors'] = ['testString']
        get_edge_functions_action_resp_model_json['messages'] = ['testString']

        # Construct a model instance of GetEdgeFunctionsActionResp by calling from_dict on the json representation
        get_edge_functions_action_resp_model = GetEdgeFunctionsActionResp.from_dict(get_edge_functions_action_resp_model_json)
        assert get_edge_functions_action_resp_model != False

        # Construct a model instance of GetEdgeFunctionsActionResp by calling from_dict on the json representation
        get_edge_functions_action_resp_model_dict = GetEdgeFunctionsActionResp.from_dict(get_edge_functions_action_resp_model_json).__dict__
        get_edge_functions_action_resp_model2 = GetEdgeFunctionsActionResp(**get_edge_functions_action_resp_model_dict)

        # Verify the model instances are equivalent
        assert get_edge_functions_action_resp_model == get_edge_functions_action_resp_model2

        # Convert model instance back to dict and verify no loss of data
        get_edge_functions_action_resp_model_json2 = get_edge_functions_action_resp_model.to_dict()
        assert get_edge_functions_action_resp_model_json2 == get_edge_functions_action_resp_model_json


class TestModel_GetEdgeFunctionsTriggerResp:
    """
    Test Class for GetEdgeFunctionsTriggerResp
    """

    def test_get_edge_functions_trigger_resp_serialization(self):
        """
        Test serialization/deserialization for GetEdgeFunctionsTriggerResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_trigger_resp_model = {}  # EdgeFunctionsTriggerResp
        edge_functions_trigger_resp_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        edge_functions_trigger_resp_model['pattern'] = 'example.net/*'
        edge_functions_trigger_resp_model['script'] = 'this-is_my_script-01'
        edge_functions_trigger_resp_model['request_limit_fail_open'] = False

        # Construct a json representation of a GetEdgeFunctionsTriggerResp model
        get_edge_functions_trigger_resp_model_json = {}
        get_edge_functions_trigger_resp_model_json['result'] = edge_functions_trigger_resp_model
        get_edge_functions_trigger_resp_model_json['success'] = True
        get_edge_functions_trigger_resp_model_json['errors'] = ['testString']
        get_edge_functions_trigger_resp_model_json['messages'] = ['testString']

        # Construct a model instance of GetEdgeFunctionsTriggerResp by calling from_dict on the json representation
        get_edge_functions_trigger_resp_model = GetEdgeFunctionsTriggerResp.from_dict(get_edge_functions_trigger_resp_model_json)
        assert get_edge_functions_trigger_resp_model != False

        # Construct a model instance of GetEdgeFunctionsTriggerResp by calling from_dict on the json representation
        get_edge_functions_trigger_resp_model_dict = GetEdgeFunctionsTriggerResp.from_dict(get_edge_functions_trigger_resp_model_json).__dict__
        get_edge_functions_trigger_resp_model2 = GetEdgeFunctionsTriggerResp(**get_edge_functions_trigger_resp_model_dict)

        # Verify the model instances are equivalent
        assert get_edge_functions_trigger_resp_model == get_edge_functions_trigger_resp_model2

        # Convert model instance back to dict and verify no loss of data
        get_edge_functions_trigger_resp_model_json2 = get_edge_functions_trigger_resp_model.to_dict()
        assert get_edge_functions_trigger_resp_model_json2 == get_edge_functions_trigger_resp_model_json


class TestModel_ListEdgeFunctionsActionsResp:
    """
    Test Class for ListEdgeFunctionsActionsResp
    """

    def test_list_edge_functions_actions_resp_serialization(self):
        """
        Test serialization/deserialization for ListEdgeFunctionsActionsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_trigger_resp_model = {}  # EdgeFunctionsTriggerResp
        edge_functions_trigger_resp_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        edge_functions_trigger_resp_model['pattern'] = 'example.net/*'
        edge_functions_trigger_resp_model['script'] = 'this-is_my_script-01'
        edge_functions_trigger_resp_model['request_limit_fail_open'] = False

        edge_functions_action_resp_model = {}  # EdgeFunctionsActionResp
        edge_functions_action_resp_model['script'] = 'addEventListener(\'fetch\', event => { event.respondWith(fetch(event.request)) })'
        edge_functions_action_resp_model['etag'] = 'ea95132c15732412d22c1476fa83f27a'
        edge_functions_action_resp_model['handlers'] = ['fetch']
        edge_functions_action_resp_model['modified_on'] = '2100-01-01T05:20:00Z'
        edge_functions_action_resp_model['created_on'] = '2100-01-01T05:20:00Z'
        edge_functions_action_resp_model['routes'] = [edge_functions_trigger_resp_model]

        # Construct a json representation of a ListEdgeFunctionsActionsResp model
        list_edge_functions_actions_resp_model_json = {}
        list_edge_functions_actions_resp_model_json['result'] = [edge_functions_action_resp_model]
        list_edge_functions_actions_resp_model_json['success'] = True
        list_edge_functions_actions_resp_model_json['errors'] = ['testString']
        list_edge_functions_actions_resp_model_json['messages'] = ['testString']

        # Construct a model instance of ListEdgeFunctionsActionsResp by calling from_dict on the json representation
        list_edge_functions_actions_resp_model = ListEdgeFunctionsActionsResp.from_dict(list_edge_functions_actions_resp_model_json)
        assert list_edge_functions_actions_resp_model != False

        # Construct a model instance of ListEdgeFunctionsActionsResp by calling from_dict on the json representation
        list_edge_functions_actions_resp_model_dict = ListEdgeFunctionsActionsResp.from_dict(list_edge_functions_actions_resp_model_json).__dict__
        list_edge_functions_actions_resp_model2 = ListEdgeFunctionsActionsResp(**list_edge_functions_actions_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_edge_functions_actions_resp_model == list_edge_functions_actions_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_edge_functions_actions_resp_model_json2 = list_edge_functions_actions_resp_model.to_dict()
        assert list_edge_functions_actions_resp_model_json2 == list_edge_functions_actions_resp_model_json


class TestModel_ListEdgeFunctionsTriggersResp:
    """
    Test Class for ListEdgeFunctionsTriggersResp
    """

    def test_list_edge_functions_triggers_resp_serialization(self):
        """
        Test serialization/deserialization for ListEdgeFunctionsTriggersResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        edge_functions_trigger_resp_model = {}  # EdgeFunctionsTriggerResp
        edge_functions_trigger_resp_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        edge_functions_trigger_resp_model['pattern'] = 'example.net/*'
        edge_functions_trigger_resp_model['script'] = 'this-is_my_script-01'
        edge_functions_trigger_resp_model['request_limit_fail_open'] = False

        # Construct a json representation of a ListEdgeFunctionsTriggersResp model
        list_edge_functions_triggers_resp_model_json = {}
        list_edge_functions_triggers_resp_model_json['result'] = [edge_functions_trigger_resp_model]
        list_edge_functions_triggers_resp_model_json['success'] = True
        list_edge_functions_triggers_resp_model_json['errors'] = ['testString']
        list_edge_functions_triggers_resp_model_json['messages'] = ['testString']

        # Construct a model instance of ListEdgeFunctionsTriggersResp by calling from_dict on the json representation
        list_edge_functions_triggers_resp_model = ListEdgeFunctionsTriggersResp.from_dict(list_edge_functions_triggers_resp_model_json)
        assert list_edge_functions_triggers_resp_model != False

        # Construct a model instance of ListEdgeFunctionsTriggersResp by calling from_dict on the json representation
        list_edge_functions_triggers_resp_model_dict = ListEdgeFunctionsTriggersResp.from_dict(list_edge_functions_triggers_resp_model_json).__dict__
        list_edge_functions_triggers_resp_model2 = ListEdgeFunctionsTriggersResp(**list_edge_functions_triggers_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_edge_functions_triggers_resp_model == list_edge_functions_triggers_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_edge_functions_triggers_resp_model_json2 = list_edge_functions_triggers_resp_model.to_dict()
        assert list_edge_functions_triggers_resp_model_json2 == list_edge_functions_triggers_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
