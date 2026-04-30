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
Unit Tests for BotManagementV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.bot_management_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = BotManagementV1(
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
# Start of Service: BotManagementSettings
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

        service = BotManagementV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, BotManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = BotManagementV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = BotManagementV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = BotManagementV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetBotManagement:
    """
    Test Class for get_bot_management
    """

    @responses.activate
    def test_get_bot_management_all_params(self):
        """
        get_bot_management()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"fight_mode": false, "session_score": false, "enable_js": false, "auth_id_logging": false, "use_latest_model": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_bot_management()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_bot_management_all_params_with_retries(self):
        # Enable retries and run test_get_bot_management_all_params.
        _service.enable_retries()
        self.test_get_bot_management_all_params()

        # Disable retries and run test_get_bot_management_all_params.
        _service.disable_retries()
        self.test_get_bot_management_all_params()

    @responses.activate
    def test_get_bot_management_value_error(self):
        """
        test_get_bot_management_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"fight_mode": false, "session_score": false, "enable_js": false, "auth_id_logging": false, "use_latest_model": false}}'
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
                _service.get_bot_management(**req_copy)

    def test_get_bot_management_value_error_with_retries(self):
        # Enable retries and run test_get_bot_management_value_error.
        _service.enable_retries()
        self.test_get_bot_management_value_error()

        # Disable retries and run test_get_bot_management_value_error.
        _service.disable_retries()
        self.test_get_bot_management_value_error()


class TestUpdateBotManagement:
    """
    Test Class for update_bot_management
    """

    @responses.activate
    def test_update_bot_management_all_params(self):
        """
        update_bot_management()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"fight_mode": false, "session_score": false, "enable_js": false, "auth_id_logging": false, "use_latest_model": false}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        fight_mode = False
        session_score = False
        enable_js = False
        auth_id_logging = False
        use_latest_model = False

        # Invoke method
        response = _service.update_bot_management(
            fight_mode=fight_mode,
            session_score=session_score,
            enable_js=enable_js,
            auth_id_logging=auth_id_logging,
            use_latest_model=use_latest_model,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['fight_mode'] == False
        assert req_body['session_score'] == False
        assert req_body['enable_js'] == False
        assert req_body['auth_id_logging'] == False
        assert req_body['use_latest_model'] == False

    def test_update_bot_management_all_params_with_retries(self):
        # Enable retries and run test_update_bot_management_all_params.
        _service.enable_retries()
        self.test_update_bot_management_all_params()

        # Disable retries and run test_update_bot_management_all_params.
        _service.disable_retries()
        self.test_update_bot_management_all_params()

    @responses.activate
    def test_update_bot_management_required_params(self):
        """
        test_update_bot_management_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"fight_mode": false, "session_score": false, "enable_js": false, "auth_id_logging": false, "use_latest_model": false}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_bot_management()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_bot_management_required_params_with_retries(self):
        # Enable retries and run test_update_bot_management_required_params.
        _service.enable_retries()
        self.test_update_bot_management_required_params()

        # Disable retries and run test_update_bot_management_required_params.
        _service.disable_retries()
        self.test_update_bot_management_required_params()

    @responses.activate
    def test_update_bot_management_value_error(self):
        """
        test_update_bot_management_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"fight_mode": false, "session_score": false, "enable_js": false, "auth_id_logging": false, "use_latest_model": false}}'
        responses.add(
            responses.PUT,
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
                _service.update_bot_management(**req_copy)

    def test_update_bot_management_value_error_with_retries(self):
        # Enable retries and run test_update_bot_management_value_error.
        _service.enable_retries()
        self.test_update_bot_management_value_error()

        # Disable retries and run test_update_bot_management_value_error.
        _service.disable_retries()
        self.test_update_bot_management_value_error()


# endregion
##############################################################################
# End of Service: BotManagementSettings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_BotMgtRespResult:
    """
    Test Class for BotMgtRespResult
    """

    def test_bot_mgt_resp_result_serialization(self):
        """
        Test serialization/deserialization for BotMgtRespResult
        """

        # Construct a json representation of a BotMgtRespResult model
        bot_mgt_resp_result_model_json = {}
        bot_mgt_resp_result_model_json['fight_mode'] = False
        bot_mgt_resp_result_model_json['session_score'] = False
        bot_mgt_resp_result_model_json['enable_js'] = False
        bot_mgt_resp_result_model_json['auth_id_logging'] = False
        bot_mgt_resp_result_model_json['use_latest_model'] = False

        # Construct a model instance of BotMgtRespResult by calling from_dict on the json representation
        bot_mgt_resp_result_model = BotMgtRespResult.from_dict(bot_mgt_resp_result_model_json)
        assert bot_mgt_resp_result_model != False

        # Construct a model instance of BotMgtRespResult by calling from_dict on the json representation
        bot_mgt_resp_result_model_dict = BotMgtRespResult.from_dict(bot_mgt_resp_result_model_json).__dict__
        bot_mgt_resp_result_model2 = BotMgtRespResult(**bot_mgt_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert bot_mgt_resp_result_model == bot_mgt_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        bot_mgt_resp_result_model_json2 = bot_mgt_resp_result_model.to_dict()
        assert bot_mgt_resp_result_model_json2 == bot_mgt_resp_result_model_json


class TestModel_BotMgtResp:
    """
    Test Class for BotMgtResp
    """

    def test_bot_mgt_resp_serialization(self):
        """
        Test serialization/deserialization for BotMgtResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bot_mgt_resp_result_model = {}  # BotMgtRespResult
        bot_mgt_resp_result_model['fight_mode'] = False
        bot_mgt_resp_result_model['session_score'] = False
        bot_mgt_resp_result_model['enable_js'] = False
        bot_mgt_resp_result_model['auth_id_logging'] = False
        bot_mgt_resp_result_model['use_latest_model'] = False

        # Construct a json representation of a BotMgtResp model
        bot_mgt_resp_model_json = {}
        bot_mgt_resp_model_json['success'] = True
        bot_mgt_resp_model_json['errors'] = [['testString']]
        bot_mgt_resp_model_json['messages'] = [['testString']]
        bot_mgt_resp_model_json['result'] = bot_mgt_resp_result_model

        # Construct a model instance of BotMgtResp by calling from_dict on the json representation
        bot_mgt_resp_model = BotMgtResp.from_dict(bot_mgt_resp_model_json)
        assert bot_mgt_resp_model != False

        # Construct a model instance of BotMgtResp by calling from_dict on the json representation
        bot_mgt_resp_model_dict = BotMgtResp.from_dict(bot_mgt_resp_model_json).__dict__
        bot_mgt_resp_model2 = BotMgtResp(**bot_mgt_resp_model_dict)

        # Verify the model instances are equivalent
        assert bot_mgt_resp_model == bot_mgt_resp_model2

        # Convert model instance back to dict and verify no loss of data
        bot_mgt_resp_model_json2 = bot_mgt_resp_model.to_dict()
        assert bot_mgt_resp_model_json2 == bot_mgt_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
