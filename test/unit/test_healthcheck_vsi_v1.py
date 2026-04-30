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
Unit Tests for HealthcheckVsiV1
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
from ibm_cloud_networking_services.healthcheck_vsi_v1 import *


_service = HealthcheckVsiV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://admin.dns-svcs.cloud.ibm.com/internal/v1'
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
# Start of Service: HealthcheckVSI
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

        service = HealthcheckVsiV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, HealthcheckVsiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = HealthcheckVsiV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestEditHealtcheckVsi:
    """
    Test Class for edit_healtcheck_vsi
    """

    @responses.activate
    def test_edit_healtcheck_vsi_all_params(self):
        """
        edit_healtcheck_vsi()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z", "vsi_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "state": "PROVISIONING", "management_address": "10.10.1.1", "management_subnet": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "healthcheck-vsi-us-south-0001", "login_credentials": "credential", "region": "us-south", "az": "us-south-1", "customer_networks": [{"vpc": "crn:v1:bluemix:public:is:us-south:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:r0006-6e6cc326-04d1-4c99-a289-efb3ae4193d6", "id": "6e6cc326-04d1-4c99-a289-efb3ae4193d6", "ipv4_cidr_block": "10.10.1.1/24", "ipv4_address": "10.10.1.1"}], "performance_profile": "bx2-2x8"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a CustomNetwork model
        custom_network_model = {}
        custom_network_model['vpc'] = 'crn:v1:bluemix:public:is:us-south:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:r0006-6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        custom_network_model['id'] = '6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        custom_network_model['ipv4_cidr_block'] = '10.10.1.1/24'
        custom_network_model['ipv4_address'] = '10.10.1.1'

        # Set up parameter values
        vsi_doc_id = 'testString'
        vsi_id = '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        state = 'PROVISIONING'
        management_address = '10.10.1.1'
        management_subnet = '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        name = 'healthcheck-vsi-us-south-0001'
        login_credentials = 'credential'
        region = 'us-south'
        az = 'us-south-1'
        customer_networks = [custom_network_model]
        performance_profile = 'bx2-2x8'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.edit_healtcheck_vsi(
            vsi_doc_id,
            vsi_id=vsi_id,
            state=state,
            management_address=management_address,
            management_subnet=management_subnet,
            name=name,
            login_credentials=login_credentials,
            region=region,
            az=az,
            customer_networks=customer_networks,
            performance_profile=performance_profile,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['vsi_id'] == '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        assert req_body['state'] == 'PROVISIONING'
        assert req_body['management_address'] == '10.10.1.1'
        assert req_body['management_subnet'] == '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        assert req_body['name'] == 'healthcheck-vsi-us-south-0001'
        assert req_body['login_credentials'] == 'credential'
        assert req_body['region'] == 'us-south'
        assert req_body['az'] == 'us-south-1'
        assert req_body['customer_networks'] == [custom_network_model]
        assert req_body['performance_profile'] == 'bx2-2x8'

    def test_edit_healtcheck_vsi_all_params_with_retries(self):
        # Enable retries and run test_edit_healtcheck_vsi_all_params.
        _service.enable_retries()
        self.test_edit_healtcheck_vsi_all_params()

        # Disable retries and run test_edit_healtcheck_vsi_all_params.
        _service.disable_retries()
        self.test_edit_healtcheck_vsi_all_params()

    @responses.activate
    def test_edit_healtcheck_vsi_required_params(self):
        """
        test_edit_healtcheck_vsi_required_params()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z", "vsi_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "state": "PROVISIONING", "management_address": "10.10.1.1", "management_subnet": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "healthcheck-vsi-us-south-0001", "login_credentials": "credential", "region": "us-south", "az": "us-south-1", "customer_networks": [{"vpc": "crn:v1:bluemix:public:is:us-south:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:r0006-6e6cc326-04d1-4c99-a289-efb3ae4193d6", "id": "6e6cc326-04d1-4c99-a289-efb3ae4193d6", "ipv4_cidr_block": "10.10.1.1/24", "ipv4_address": "10.10.1.1"}], "performance_profile": "bx2-2x8"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'

        # Invoke method
        response = _service.edit_healtcheck_vsi(
            vsi_doc_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_edit_healtcheck_vsi_required_params_with_retries(self):
        # Enable retries and run test_edit_healtcheck_vsi_required_params.
        _service.enable_retries()
        self.test_edit_healtcheck_vsi_required_params()

        # Disable retries and run test_edit_healtcheck_vsi_required_params.
        _service.disable_retries()
        self.test_edit_healtcheck_vsi_required_params()

    @responses.activate
    def test_edit_healtcheck_vsi_value_error(self):
        """
        test_edit_healtcheck_vsi_value_error()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z", "vsi_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "state": "PROVISIONING", "management_address": "10.10.1.1", "management_subnet": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "healthcheck-vsi-us-south-0001", "login_credentials": "credential", "region": "us-south", "az": "us-south-1", "customer_networks": [{"vpc": "crn:v1:bluemix:public:is:us-south:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:r0006-6e6cc326-04d1-4c99-a289-efb3ae4193d6", "id": "6e6cc326-04d1-4c99-a289-efb3ae4193d6", "ipv4_cidr_block": "10.10.1.1/24", "ipv4_address": "10.10.1.1"}], "performance_profile": "bx2-2x8"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "vsi_doc_id": vsi_doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.edit_healtcheck_vsi(**req_copy)

    def test_edit_healtcheck_vsi_value_error_with_retries(self):
        # Enable retries and run test_edit_healtcheck_vsi_value_error.
        _service.enable_retries()
        self.test_edit_healtcheck_vsi_value_error()

        # Disable retries and run test_edit_healtcheck_vsi_value_error.
        _service.disable_retries()
        self.test_edit_healtcheck_vsi_value_error()


# endregion
##############################################################################
# End of Service: HealthcheckVSI
##############################################################################

##############################################################################
# Start of Service: OriginHealthcheckStatus
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

        service = HealthcheckVsiV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, HealthcheckVsiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = HealthcheckVsiV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestUpdateOriginStatus:
    """
    Test Class for update_origin_status
    """

    @responses.activate
    def test_update_origin_status_all_params(self):
        """
        update_origin_status()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString/origins/testString')
        mock_response = '{"status": "UP", "health_failure_reason": "SUCCESS"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'
        origin_doc_id = 'testString'
        status = 'UP'
        health_failure_reason = 'SUCCESS'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_origin_status(
            vsi_doc_id,
            origin_doc_id,
            status=status,
            health_failure_reason=health_failure_reason,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['status'] == 'UP'
        assert req_body['health_failure_reason'] == 'SUCCESS'

    def test_update_origin_status_all_params_with_retries(self):
        # Enable retries and run test_update_origin_status_all_params.
        _service.enable_retries()
        self.test_update_origin_status_all_params()

        # Disable retries and run test_update_origin_status_all_params.
        _service.disable_retries()
        self.test_update_origin_status_all_params()

    @responses.activate
    def test_update_origin_status_required_params(self):
        """
        test_update_origin_status_required_params()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString/origins/testString')
        mock_response = '{"status": "UP", "health_failure_reason": "SUCCESS"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'
        origin_doc_id = 'testString'

        # Invoke method
        response = _service.update_origin_status(
            vsi_doc_id,
            origin_doc_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_origin_status_required_params_with_retries(self):
        # Enable retries and run test_update_origin_status_required_params.
        _service.enable_retries()
        self.test_update_origin_status_required_params()

        # Disable retries and run test_update_origin_status_required_params.
        _service.disable_retries()
        self.test_update_origin_status_required_params()

    @responses.activate
    def test_update_origin_status_value_error(self):
        """
        test_update_origin_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString/origins/testString')
        mock_response = '{"status": "UP", "health_failure_reason": "SUCCESS"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'
        origin_doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "vsi_doc_id": vsi_doc_id,
            "origin_doc_id": origin_doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_origin_status(**req_copy)

    def test_update_origin_status_value_error_with_retries(self):
        # Enable retries and run test_update_origin_status_value_error.
        _service.enable_retries()
        self.test_update_origin_status_value_error()

        # Disable retries and run test_update_origin_status_value_error.
        _service.disable_retries()
        self.test_update_origin_status_value_error()


# endregion
##############################################################################
# End of Service: OriginHealthcheckStatus
##############################################################################

##############################################################################
# Start of Service: ApplicationStatus
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

        service = HealthcheckVsiV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, HealthcheckVsiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = HealthcheckVsiV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestUpdateAppStatus:
    """
    Test Class for update_app_status
    """

    @responses.activate
    def test_update_app_status_all_params(self):
        """
        update_app_status()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString/application')
        mock_response = '{"application": "custom-resolver", "health": true, "subnet_crn": "crn:v1:staging:public:is:us-south-3:a/bcf1865e99742d38d2d5fc3fb80a5496::subnet:0736-a700f01d-179d-4cfe-be26-56b4ff64f0f5"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'
        application = 'custom-resolver'
        health = True
        subnet_crn = 'crn:v1:staging:public:is:us-south-3:a/bcf1865e99742d38d2d5fc3fb80a5496::subnet:0736-a700f01d-179d-4cfe-be26-56b4ff64f0f5'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_app_status(
            vsi_doc_id,
            application=application,
            health=health,
            subnet_crn=subnet_crn,
            x_correlation_id=x_correlation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['application'] == 'custom-resolver'
        assert req_body['health'] == True
        assert req_body['subnet_crn'] == 'crn:v1:staging:public:is:us-south-3:a/bcf1865e99742d38d2d5fc3fb80a5496::subnet:0736-a700f01d-179d-4cfe-be26-56b4ff64f0f5'

    def test_update_app_status_all_params_with_retries(self):
        # Enable retries and run test_update_app_status_all_params.
        _service.enable_retries()
        self.test_update_app_status_all_params()

        # Disable retries and run test_update_app_status_all_params.
        _service.disable_retries()
        self.test_update_app_status_all_params()

    @responses.activate
    def test_update_app_status_required_params(self):
        """
        test_update_app_status_required_params()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString/application')
        mock_response = '{"application": "custom-resolver", "health": true, "subnet_crn": "crn:v1:staging:public:is:us-south-3:a/bcf1865e99742d38d2d5fc3fb80a5496::subnet:0736-a700f01d-179d-4cfe-be26-56b4ff64f0f5"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'

        # Invoke method
        response = _service.update_app_status(
            vsi_doc_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_app_status_required_params_with_retries(self):
        # Enable retries and run test_update_app_status_required_params.
        _service.enable_retries()
        self.test_update_app_status_required_params()

        # Disable retries and run test_update_app_status_required_params.
        _service.disable_retries()
        self.test_update_app_status_required_params()

    @responses.activate
    def test_update_app_status_value_error(self):
        """
        test_update_app_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/healthcheck/vsi/testString/application')
        mock_response = '{"application": "custom-resolver", "health": true, "subnet_crn": "crn:v1:staging:public:is:us-south-3:a/bcf1865e99742d38d2d5fc3fb80a5496::subnet:0736-a700f01d-179d-4cfe-be26-56b4ff64f0f5"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        vsi_doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "vsi_doc_id": vsi_doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_app_status(**req_copy)

    def test_update_app_status_value_error_with_retries(self):
        # Enable retries and run test_update_app_status_value_error.
        _service.enable_retries()
        self.test_update_app_status_value_error()

        # Disable retries and run test_update_app_status_value_error.
        _service.disable_retries()
        self.test_update_app_status_value_error()


# endregion
##############################################################################
# End of Service: ApplicationStatus
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AppStatus:
    """
    Test Class for AppStatus
    """

    def test_app_status_serialization(self):
        """
        Test serialization/deserialization for AppStatus
        """

        # Construct a json representation of a AppStatus model
        app_status_model_json = {}
        app_status_model_json['application'] = 'custom-resolver'
        app_status_model_json['health'] = True
        app_status_model_json['subnet_crn'] = 'crn:v1:staging:public:is:us-south-3:a/bcf1865e99742d38d2d5fc3fb80a5496::subnet:0736-a700f01d-179d-4cfe-be26-56b4ff64f0f5'

        # Construct a model instance of AppStatus by calling from_dict on the json representation
        app_status_model = AppStatus.from_dict(app_status_model_json)
        assert app_status_model != False

        # Construct a model instance of AppStatus by calling from_dict on the json representation
        app_status_model_dict = AppStatus.from_dict(app_status_model_json).__dict__
        app_status_model2 = AppStatus(**app_status_model_dict)

        # Verify the model instances are equivalent
        assert app_status_model == app_status_model2

        # Convert model instance back to dict and verify no loss of data
        app_status_model_json2 = app_status_model.to_dict()
        assert app_status_model_json2 == app_status_model_json


class TestModel_CustomNetwork:
    """
    Test Class for CustomNetwork
    """

    def test_custom_network_serialization(self):
        """
        Test serialization/deserialization for CustomNetwork
        """

        # Construct a json representation of a CustomNetwork model
        custom_network_model_json = {}
        custom_network_model_json['vpc'] = 'crn:v1:bluemix:public:is:us-south:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:r0006-6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        custom_network_model_json['id'] = '6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        custom_network_model_json['ipv4_cidr_block'] = '10.10.1.1/24'
        custom_network_model_json['ipv4_address'] = '10.10.1.1'

        # Construct a model instance of CustomNetwork by calling from_dict on the json representation
        custom_network_model = CustomNetwork.from_dict(custom_network_model_json)
        assert custom_network_model != False

        # Construct a model instance of CustomNetwork by calling from_dict on the json representation
        custom_network_model_dict = CustomNetwork.from_dict(custom_network_model_json).__dict__
        custom_network_model2 = CustomNetwork(**custom_network_model_dict)

        # Verify the model instances are equivalent
        assert custom_network_model == custom_network_model2

        # Convert model instance back to dict and verify no loss of data
        custom_network_model_json2 = custom_network_model.to_dict()
        assert custom_network_model_json2 == custom_network_model_json


class TestModel_HealthcheckOrigin:
    """
    Test Class for HealthcheckOrigin
    """

    def test_healthcheck_origin_serialization(self):
        """
        Test serialization/deserialization for HealthcheckOrigin
        """

        # Construct a json representation of a HealthcheckOrigin model
        healthcheck_origin_model_json = {}
        healthcheck_origin_model_json['status'] = 'UP'
        healthcheck_origin_model_json['health_failure_reason'] = 'SUCCESS'

        # Construct a model instance of HealthcheckOrigin by calling from_dict on the json representation
        healthcheck_origin_model = HealthcheckOrigin.from_dict(healthcheck_origin_model_json)
        assert healthcheck_origin_model != False

        # Construct a model instance of HealthcheckOrigin by calling from_dict on the json representation
        healthcheck_origin_model_dict = HealthcheckOrigin.from_dict(healthcheck_origin_model_json).__dict__
        healthcheck_origin_model2 = HealthcheckOrigin(**healthcheck_origin_model_dict)

        # Verify the model instances are equivalent
        assert healthcheck_origin_model == healthcheck_origin_model2

        # Convert model instance back to dict and verify no loss of data
        healthcheck_origin_model_json2 = healthcheck_origin_model.to_dict()
        assert healthcheck_origin_model_json2 == healthcheck_origin_model_json


class TestModel_HealthcheckVsi:
    """
    Test Class for HealthcheckVsi
    """

    def test_healthcheck_vsi_serialization(self):
        """
        Test serialization/deserialization for HealthcheckVsi
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_network_model = {}  # CustomNetwork
        custom_network_model['vpc'] = 'crn:v1:bluemix:public:is:us-south:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:r0006-6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        custom_network_model['id'] = '6e6cc326-04d1-4c99-a289-efb3ae4193d6'
        custom_network_model['ipv4_cidr_block'] = '10.10.1.1/24'
        custom_network_model['ipv4_address'] = '10.10.1.1'

        # Construct a json representation of a HealthcheckVsi model
        healthcheck_vsi_model_json = {}
        healthcheck_vsi_model_json['id'] = '2d0f862b-67cc-41f3-b6a2-59860d0aa90e'
        healthcheck_vsi_model_json['created_on'] = '2019-01-01T05:20:00.123000Z'
        healthcheck_vsi_model_json['modified_on'] = '2019-01-01T05:20:00.123000Z'
        healthcheck_vsi_model_json['vsi_id'] = '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        healthcheck_vsi_model_json['state'] = 'PROVISIONING'
        healthcheck_vsi_model_json['management_address'] = '10.10.1.1'
        healthcheck_vsi_model_json['management_subnet'] = '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        healthcheck_vsi_model_json['name'] = 'healthcheck-vsi-us-south-0001'
        healthcheck_vsi_model_json['login_credentials'] = 'credential'
        healthcheck_vsi_model_json['region'] = 'us-south'
        healthcheck_vsi_model_json['az'] = 'us-south-1'
        healthcheck_vsi_model_json['customer_networks'] = [custom_network_model]
        healthcheck_vsi_model_json['performance_profile'] = 'bx2-2x8'

        # Construct a model instance of HealthcheckVsi by calling from_dict on the json representation
        healthcheck_vsi_model = HealthcheckVsi.from_dict(healthcheck_vsi_model_json)
        assert healthcheck_vsi_model != False

        # Construct a model instance of HealthcheckVsi by calling from_dict on the json representation
        healthcheck_vsi_model_dict = HealthcheckVsi.from_dict(healthcheck_vsi_model_json).__dict__
        healthcheck_vsi_model2 = HealthcheckVsi(**healthcheck_vsi_model_dict)

        # Verify the model instances are equivalent
        assert healthcheck_vsi_model == healthcheck_vsi_model2

        # Convert model instance back to dict and verify no loss of data
        healthcheck_vsi_model_json2 = healthcheck_vsi_model.to_dict()
        assert healthcheck_vsi_model_json2 == healthcheck_vsi_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
