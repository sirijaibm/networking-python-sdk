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
Unit Tests for RoutingV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_networking_services.routing_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = RoutingV1(
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
# Start of Service: Routing
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

        service = RoutingV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, RoutingV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = RoutingV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = RoutingV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = RoutingV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetSmartRouting:
    """
    Test Class for get_smart_routing
    """

    @responses.activate
    def test_get_smart_routing_all_params(self):
        """
        get_smart_routing()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_smart_routing()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_smart_routing_all_params_with_retries(self):
        # Enable retries and run test_get_smart_routing_all_params.
        _service.enable_retries()
        self.test_get_smart_routing_all_params()

        # Disable retries and run test_get_smart_routing_all_params.
        _service.disable_retries()
        self.test_get_smart_routing_all_params()

    @responses.activate
    def test_get_smart_routing_value_error(self):
        """
        test_get_smart_routing_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_smart_routing(**req_copy)

    def test_get_smart_routing_value_error_with_retries(self):
        # Enable retries and run test_get_smart_routing_value_error.
        _service.enable_retries()
        self.test_get_smart_routing_value_error()

        # Disable retries and run test_get_smart_routing_value_error.
        _service.disable_retries()
        self.test_get_smart_routing_value_error()


class TestUpdateSmartRouting:
    """
    Test Class for update_smart_routing
    """

    @responses.activate
    def test_update_smart_routing_all_params(self):
        """
        update_smart_routing()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = _service.update_smart_routing(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'

    def test_update_smart_routing_all_params_with_retries(self):
        # Enable retries and run test_update_smart_routing_all_params.
        _service.enable_retries()
        self.test_update_smart_routing_all_params()

        # Disable retries and run test_update_smart_routing_all_params.
        _service.disable_retries()
        self.test_update_smart_routing_all_params()

    @responses.activate
    def test_update_smart_routing_required_params(self):
        """
        test_update_smart_routing_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_smart_routing()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_smart_routing_required_params_with_retries(self):
        # Enable retries and run test_update_smart_routing_required_params.
        _service.enable_retries()
        self.test_update_smart_routing_required_params()

        # Disable retries and run test_update_smart_routing_required_params.
        _service.disable_retries()
        self.test_update_smart_routing_required_params()

    @responses.activate
    def test_update_smart_routing_value_error(self):
        """
        test_update_smart_routing_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
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
                _service.update_smart_routing(**req_copy)

    def test_update_smart_routing_value_error_with_retries(self):
        # Enable retries and run test_update_smart_routing_value_error.
        _service.enable_retries()
        self.test_update_smart_routing_value_error()

        # Disable retries and run test_update_smart_routing_value_error.
        _service.disable_retries()
        self.test_update_smart_routing_value_error()


class TestGetRoutingTieredCaching:
    """
    Test Class for get_routing_tiered_caching
    """

    @responses.activate
    def test_get_routing_tiered_caching_all_params(self):
        """
        get_routing_tiered_caching()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/tiered_caching')
        mock_response = '{"result": {"id": "tiered_caching", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_routing_tiered_caching()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_routing_tiered_caching_all_params_with_retries(self):
        # Enable retries and run test_get_routing_tiered_caching_all_params.
        _service.enable_retries()
        self.test_get_routing_tiered_caching_all_params()

        # Disable retries and run test_get_routing_tiered_caching_all_params.
        _service.disable_retries()
        self.test_get_routing_tiered_caching_all_params()

    @responses.activate
    def test_get_routing_tiered_caching_value_error(self):
        """
        test_get_routing_tiered_caching_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/tiered_caching')
        mock_response = '{"result": {"id": "tiered_caching", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_routing_tiered_caching(**req_copy)

    def test_get_routing_tiered_caching_value_error_with_retries(self):
        # Enable retries and run test_get_routing_tiered_caching_value_error.
        _service.enable_retries()
        self.test_get_routing_tiered_caching_value_error()

        # Disable retries and run test_get_routing_tiered_caching_value_error.
        _service.disable_retries()
        self.test_get_routing_tiered_caching_value_error()


class TestUpdateRoutingTieredCaching:
    """
    Test Class for update_routing_tiered_caching
    """

    @responses.activate
    def test_update_routing_tiered_caching_all_params(self):
        """
        update_routing_tiered_caching()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/tiered_caching')
        mock_response = '{"result": {"id": "tiered_caching", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_routing_tiered_caching(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_routing_tiered_caching_all_params_with_retries(self):
        # Enable retries and run test_update_routing_tiered_caching_all_params.
        _service.enable_retries()
        self.test_update_routing_tiered_caching_all_params()

        # Disable retries and run test_update_routing_tiered_caching_all_params.
        _service.disable_retries()
        self.test_update_routing_tiered_caching_all_params()

    @responses.activate
    def test_update_routing_tiered_caching_required_params(self):
        """
        test_update_routing_tiered_caching_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/tiered_caching')
        mock_response = '{"result": {"id": "tiered_caching", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_routing_tiered_caching()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_routing_tiered_caching_required_params_with_retries(self):
        # Enable retries and run test_update_routing_tiered_caching_required_params.
        _service.enable_retries()
        self.test_update_routing_tiered_caching_required_params()

        # Disable retries and run test_update_routing_tiered_caching_required_params.
        _service.disable_retries()
        self.test_update_routing_tiered_caching_required_params()

    @responses.activate
    def test_update_routing_tiered_caching_value_error(self):
        """
        test_update_routing_tiered_caching_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/tiered_caching')
        mock_response = '{"result": {"id": "tiered_caching", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00.000Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
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
                _service.update_routing_tiered_caching(**req_copy)

    def test_update_routing_tiered_caching_value_error_with_retries(self):
        # Enable retries and run test_update_routing_tiered_caching_value_error.
        _service.enable_retries()
        self.test_update_routing_tiered_caching_value_error()

        # Disable retries and run test_update_routing_tiered_caching_value_error.
        _service.disable_retries()
        self.test_update_routing_tiered_caching_value_error()


class TestGetRoutingLatency:
    """
    Test Class for get_routing_latency
    """

    @responses.activate
    def test_get_routing_latency_all_params(self):
        """
        get_routing_latency()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/latency')
        mock_response = '{"result": {"percent_smart_routed": 63.4, "bins": 10, "range": {"min": 0, "max": 1500}, "time_range": {"min": "2019-01-01T12:00:00.000Z", "max": "2019-01-01T12:00:00.000Z"}, "data": {"lable": ["lable"], "counts": [6], "averages": [8]}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bins = 50

        # Invoke method
        response = _service.get_routing_latency(
            bins=bins,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'bins={}'.format(bins) in query_string

    def test_get_routing_latency_all_params_with_retries(self):
        # Enable retries and run test_get_routing_latency_all_params.
        _service.enable_retries()
        self.test_get_routing_latency_all_params()

        # Disable retries and run test_get_routing_latency_all_params.
        _service.disable_retries()
        self.test_get_routing_latency_all_params()

    @responses.activate
    def test_get_routing_latency_required_params(self):
        """
        test_get_routing_latency_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/latency')
        mock_response = '{"result": {"percent_smart_routed": 63.4, "bins": 10, "range": {"min": 0, "max": 1500}, "time_range": {"min": "2019-01-01T12:00:00.000Z", "max": "2019-01-01T12:00:00.000Z"}, "data": {"lable": ["lable"], "counts": [6], "averages": [8]}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_routing_latency()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_routing_latency_required_params_with_retries(self):
        # Enable retries and run test_get_routing_latency_required_params.
        _service.enable_retries()
        self.test_get_routing_latency_required_params()

        # Disable retries and run test_get_routing_latency_required_params.
        _service.disable_retries()
        self.test_get_routing_latency_required_params()

    @responses.activate
    def test_get_routing_latency_value_error(self):
        """
        test_get_routing_latency_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/latency')
        mock_response = '{"result": {"percent_smart_routed": 63.4, "bins": 10, "range": {"min": 0, "max": 1500}, "time_range": {"min": "2019-01-01T12:00:00.000Z", "max": "2019-01-01T12:00:00.000Z"}, "data": {"lable": ["lable"], "counts": [6], "averages": [8]}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_routing_latency(**req_copy)

    def test_get_routing_latency_value_error_with_retries(self):
        # Enable retries and run test_get_routing_latency_value_error.
        _service.enable_retries()
        self.test_get_routing_latency_value_error()

        # Disable retries and run test_get_routing_latency_value_error.
        _service.disable_retries()
        self.test_get_routing_latency_value_error()


class TestGetRoutingLatencyColos:
    """
    Test Class for get_routing_latency_colos
    """

    @responses.activate
    def test_get_routing_latency_colos_all_params(self):
        """
        get_routing_latency_colos()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/latency/colos')
        mock_response = '{"result": {"type": "FeatureCollection", "features": [{"code": "EWR", "smart_routing_req_count": 6696990, "pct_avg_change": 0.06003951841343536, "no_smart_routing_avg": 651.7771493198342, "smart_routing_avg": 690.9095354778789, "geometry": {"coordinates": [11], "type": "Point"}}]}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_routing_latency_colos()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_routing_latency_colos_all_params_with_retries(self):
        # Enable retries and run test_get_routing_latency_colos_all_params.
        _service.enable_retries()
        self.test_get_routing_latency_colos_all_params()

        # Disable retries and run test_get_routing_latency_colos_all_params.
        _service.disable_retries()
        self.test_get_routing_latency_colos_all_params()

    @responses.activate
    def test_get_routing_latency_colos_value_error(self):
        """
        test_get_routing_latency_colos_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/routing/latency/colos')
        mock_response = '{"result": {"type": "FeatureCollection", "features": [{"code": "EWR", "smart_routing_req_count": 6696990, "pct_avg_change": 0.06003951841343536, "no_smart_routing_avg": 651.7771493198342, "smart_routing_avg": 690.9095354778789, "geometry": {"coordinates": [11], "type": "Point"}}]}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_routing_latency_colos(**req_copy)

    def test_get_routing_latency_colos_value_error_with_retries(self):
        # Enable retries and run test_get_routing_latency_colos_value_error.
        _service.enable_retries()
        self.test_get_routing_latency_colos_value_error()

        # Disable retries and run test_get_routing_latency_colos_value_error.
        _service.disable_retries()
        self.test_get_routing_latency_colos_value_error()


# endregion
##############################################################################
# End of Service: Routing
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_RoutingLatencyColosRespResult:
    """
    Test Class for RoutingLatencyColosRespResult
    """

    def test_routing_latency_colos_resp_result_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyColosRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        routing_latency_colos_resp_result_features_item_geometry_model = {}  # RoutingLatencyColosRespResultFeaturesItemGeometry
        routing_latency_colos_resp_result_features_item_geometry_model['coordinates'] = [36.0]
        routing_latency_colos_resp_result_features_item_geometry_model['type'] = 'Point'

        routing_latency_colos_resp_result_features_item_model = {}  # RoutingLatencyColosRespResultFeaturesItem
        routing_latency_colos_resp_result_features_item_model['code'] = 'EWR'
        routing_latency_colos_resp_result_features_item_model['smart_routing_req_count'] = 6696990
        routing_latency_colos_resp_result_features_item_model['pct_avg_change'] = 0.06003951841343536
        routing_latency_colos_resp_result_features_item_model['no_smart_routing_avg'] = 651.7771493198342
        routing_latency_colos_resp_result_features_item_model['smart_routing_avg'] = 690.9095354778789
        routing_latency_colos_resp_result_features_item_model['geometry'] = routing_latency_colos_resp_result_features_item_geometry_model

        # Construct a json representation of a RoutingLatencyColosRespResult model
        routing_latency_colos_resp_result_model_json = {}
        routing_latency_colos_resp_result_model_json['type'] = 'FeatureCollection'
        routing_latency_colos_resp_result_model_json['features'] = [routing_latency_colos_resp_result_features_item_model]

        # Construct a model instance of RoutingLatencyColosRespResult by calling from_dict on the json representation
        routing_latency_colos_resp_result_model = RoutingLatencyColosRespResult.from_dict(routing_latency_colos_resp_result_model_json)
        assert routing_latency_colos_resp_result_model != False

        # Construct a model instance of RoutingLatencyColosRespResult by calling from_dict on the json representation
        routing_latency_colos_resp_result_model_dict = RoutingLatencyColosRespResult.from_dict(routing_latency_colos_resp_result_model_json).__dict__
        routing_latency_colos_resp_result_model2 = RoutingLatencyColosRespResult(**routing_latency_colos_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_colos_resp_result_model == routing_latency_colos_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_colos_resp_result_model_json2 = routing_latency_colos_resp_result_model.to_dict()
        assert routing_latency_colos_resp_result_model_json2 == routing_latency_colos_resp_result_model_json


class TestModel_RoutingLatencyColosRespResultFeaturesItem:
    """
    Test Class for RoutingLatencyColosRespResultFeaturesItem
    """

    def test_routing_latency_colos_resp_result_features_item_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyColosRespResultFeaturesItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        routing_latency_colos_resp_result_features_item_geometry_model = {}  # RoutingLatencyColosRespResultFeaturesItemGeometry
        routing_latency_colos_resp_result_features_item_geometry_model['coordinates'] = [36.0]
        routing_latency_colos_resp_result_features_item_geometry_model['type'] = 'Point'

        # Construct a json representation of a RoutingLatencyColosRespResultFeaturesItem model
        routing_latency_colos_resp_result_features_item_model_json = {}
        routing_latency_colos_resp_result_features_item_model_json['code'] = 'EWR'
        routing_latency_colos_resp_result_features_item_model_json['smart_routing_req_count'] = 6696990
        routing_latency_colos_resp_result_features_item_model_json['pct_avg_change'] = 0.06003951841343536
        routing_latency_colos_resp_result_features_item_model_json['no_smart_routing_avg'] = 651.7771493198342
        routing_latency_colos_resp_result_features_item_model_json['smart_routing_avg'] = 690.9095354778789
        routing_latency_colos_resp_result_features_item_model_json['geometry'] = routing_latency_colos_resp_result_features_item_geometry_model

        # Construct a model instance of RoutingLatencyColosRespResultFeaturesItem by calling from_dict on the json representation
        routing_latency_colos_resp_result_features_item_model = RoutingLatencyColosRespResultFeaturesItem.from_dict(routing_latency_colos_resp_result_features_item_model_json)
        assert routing_latency_colos_resp_result_features_item_model != False

        # Construct a model instance of RoutingLatencyColosRespResultFeaturesItem by calling from_dict on the json representation
        routing_latency_colos_resp_result_features_item_model_dict = RoutingLatencyColosRespResultFeaturesItem.from_dict(routing_latency_colos_resp_result_features_item_model_json).__dict__
        routing_latency_colos_resp_result_features_item_model2 = RoutingLatencyColosRespResultFeaturesItem(**routing_latency_colos_resp_result_features_item_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_colos_resp_result_features_item_model == routing_latency_colos_resp_result_features_item_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_colos_resp_result_features_item_model_json2 = routing_latency_colos_resp_result_features_item_model.to_dict()
        assert routing_latency_colos_resp_result_features_item_model_json2 == routing_latency_colos_resp_result_features_item_model_json


class TestModel_RoutingLatencyColosRespResultFeaturesItemGeometry:
    """
    Test Class for RoutingLatencyColosRespResultFeaturesItemGeometry
    """

    def test_routing_latency_colos_resp_result_features_item_geometry_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyColosRespResultFeaturesItemGeometry
        """

        # Construct a json representation of a RoutingLatencyColosRespResultFeaturesItemGeometry model
        routing_latency_colos_resp_result_features_item_geometry_model_json = {}
        routing_latency_colos_resp_result_features_item_geometry_model_json['coordinates'] = [36.0]
        routing_latency_colos_resp_result_features_item_geometry_model_json['type'] = 'Point'

        # Construct a model instance of RoutingLatencyColosRespResultFeaturesItemGeometry by calling from_dict on the json representation
        routing_latency_colos_resp_result_features_item_geometry_model = RoutingLatencyColosRespResultFeaturesItemGeometry.from_dict(routing_latency_colos_resp_result_features_item_geometry_model_json)
        assert routing_latency_colos_resp_result_features_item_geometry_model != False

        # Construct a model instance of RoutingLatencyColosRespResultFeaturesItemGeometry by calling from_dict on the json representation
        routing_latency_colos_resp_result_features_item_geometry_model_dict = RoutingLatencyColosRespResultFeaturesItemGeometry.from_dict(routing_latency_colos_resp_result_features_item_geometry_model_json).__dict__
        routing_latency_colos_resp_result_features_item_geometry_model2 = RoutingLatencyColosRespResultFeaturesItemGeometry(**routing_latency_colos_resp_result_features_item_geometry_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_colos_resp_result_features_item_geometry_model == routing_latency_colos_resp_result_features_item_geometry_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_colos_resp_result_features_item_geometry_model_json2 = routing_latency_colos_resp_result_features_item_geometry_model.to_dict()
        assert routing_latency_colos_resp_result_features_item_geometry_model_json2 == routing_latency_colos_resp_result_features_item_geometry_model_json


class TestModel_RoutingLatencyRespResult:
    """
    Test Class for RoutingLatencyRespResult
    """

    def test_routing_latency_resp_result_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        routing_latency_resp_result_range_model = {}  # RoutingLatencyRespResultRange
        routing_latency_resp_result_range_model['min'] = 0
        routing_latency_resp_result_range_model['max'] = 1500

        routing_latency_resp_result_time_range_model = {}  # RoutingLatencyRespResultTimeRange
        routing_latency_resp_result_time_range_model['min'] = '2019-01-01T12:00:00Z'
        routing_latency_resp_result_time_range_model['max'] = '2019-01-01T12:00:00Z'

        routing_latency_resp_result_data_model = {}  # RoutingLatencyRespResultData
        routing_latency_resp_result_data_model['lable'] = ['testString']
        routing_latency_resp_result_data_model['counts'] = [38]
        routing_latency_resp_result_data_model['averages'] = [38]

        # Construct a json representation of a RoutingLatencyRespResult model
        routing_latency_resp_result_model_json = {}
        routing_latency_resp_result_model_json['percent_smart_routed'] = 63.4
        routing_latency_resp_result_model_json['bins'] = 10
        routing_latency_resp_result_model_json['range'] = routing_latency_resp_result_range_model
        routing_latency_resp_result_model_json['time_range'] = routing_latency_resp_result_time_range_model
        routing_latency_resp_result_model_json['data'] = routing_latency_resp_result_data_model

        # Construct a model instance of RoutingLatencyRespResult by calling from_dict on the json representation
        routing_latency_resp_result_model = RoutingLatencyRespResult.from_dict(routing_latency_resp_result_model_json)
        assert routing_latency_resp_result_model != False

        # Construct a model instance of RoutingLatencyRespResult by calling from_dict on the json representation
        routing_latency_resp_result_model_dict = RoutingLatencyRespResult.from_dict(routing_latency_resp_result_model_json).__dict__
        routing_latency_resp_result_model2 = RoutingLatencyRespResult(**routing_latency_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_resp_result_model == routing_latency_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_resp_result_model_json2 = routing_latency_resp_result_model.to_dict()
        assert routing_latency_resp_result_model_json2 == routing_latency_resp_result_model_json


class TestModel_RoutingLatencyRespResultData:
    """
    Test Class for RoutingLatencyRespResultData
    """

    def test_routing_latency_resp_result_data_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyRespResultData
        """

        # Construct a json representation of a RoutingLatencyRespResultData model
        routing_latency_resp_result_data_model_json = {}
        routing_latency_resp_result_data_model_json['lable'] = ['testString']
        routing_latency_resp_result_data_model_json['counts'] = [38]
        routing_latency_resp_result_data_model_json['averages'] = [38]

        # Construct a model instance of RoutingLatencyRespResultData by calling from_dict on the json representation
        routing_latency_resp_result_data_model = RoutingLatencyRespResultData.from_dict(routing_latency_resp_result_data_model_json)
        assert routing_latency_resp_result_data_model != False

        # Construct a model instance of RoutingLatencyRespResultData by calling from_dict on the json representation
        routing_latency_resp_result_data_model_dict = RoutingLatencyRespResultData.from_dict(routing_latency_resp_result_data_model_json).__dict__
        routing_latency_resp_result_data_model2 = RoutingLatencyRespResultData(**routing_latency_resp_result_data_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_resp_result_data_model == routing_latency_resp_result_data_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_resp_result_data_model_json2 = routing_latency_resp_result_data_model.to_dict()
        assert routing_latency_resp_result_data_model_json2 == routing_latency_resp_result_data_model_json


class TestModel_RoutingLatencyRespResultRange:
    """
    Test Class for RoutingLatencyRespResultRange
    """

    def test_routing_latency_resp_result_range_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyRespResultRange
        """

        # Construct a json representation of a RoutingLatencyRespResultRange model
        routing_latency_resp_result_range_model_json = {}
        routing_latency_resp_result_range_model_json['min'] = 0
        routing_latency_resp_result_range_model_json['max'] = 1500

        # Construct a model instance of RoutingLatencyRespResultRange by calling from_dict on the json representation
        routing_latency_resp_result_range_model = RoutingLatencyRespResultRange.from_dict(routing_latency_resp_result_range_model_json)
        assert routing_latency_resp_result_range_model != False

        # Construct a model instance of RoutingLatencyRespResultRange by calling from_dict on the json representation
        routing_latency_resp_result_range_model_dict = RoutingLatencyRespResultRange.from_dict(routing_latency_resp_result_range_model_json).__dict__
        routing_latency_resp_result_range_model2 = RoutingLatencyRespResultRange(**routing_latency_resp_result_range_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_resp_result_range_model == routing_latency_resp_result_range_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_resp_result_range_model_json2 = routing_latency_resp_result_range_model.to_dict()
        assert routing_latency_resp_result_range_model_json2 == routing_latency_resp_result_range_model_json


class TestModel_RoutingLatencyRespResultTimeRange:
    """
    Test Class for RoutingLatencyRespResultTimeRange
    """

    def test_routing_latency_resp_result_time_range_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyRespResultTimeRange
        """

        # Construct a json representation of a RoutingLatencyRespResultTimeRange model
        routing_latency_resp_result_time_range_model_json = {}
        routing_latency_resp_result_time_range_model_json['min'] = '2019-01-01T12:00:00Z'
        routing_latency_resp_result_time_range_model_json['max'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of RoutingLatencyRespResultTimeRange by calling from_dict on the json representation
        routing_latency_resp_result_time_range_model = RoutingLatencyRespResultTimeRange.from_dict(routing_latency_resp_result_time_range_model_json)
        assert routing_latency_resp_result_time_range_model != False

        # Construct a model instance of RoutingLatencyRespResultTimeRange by calling from_dict on the json representation
        routing_latency_resp_result_time_range_model_dict = RoutingLatencyRespResultTimeRange.from_dict(routing_latency_resp_result_time_range_model_json).__dict__
        routing_latency_resp_result_time_range_model2 = RoutingLatencyRespResultTimeRange(**routing_latency_resp_result_time_range_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_resp_result_time_range_model == routing_latency_resp_result_time_range_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_resp_result_time_range_model_json2 = routing_latency_resp_result_time_range_model.to_dict()
        assert routing_latency_resp_result_time_range_model_json2 == routing_latency_resp_result_time_range_model_json


class TestModel_RoutingTieredCachingRespResult:
    """
    Test Class for RoutingTieredCachingRespResult
    """

    def test_routing_tiered_caching_resp_result_serialization(self):
        """
        Test serialization/deserialization for RoutingTieredCachingRespResult
        """

        # Construct a json representation of a RoutingTieredCachingRespResult model
        routing_tiered_caching_resp_result_model_json = {}
        routing_tiered_caching_resp_result_model_json['id'] = 'tiered_caching'
        routing_tiered_caching_resp_result_model_json['value'] = 'on'
        routing_tiered_caching_resp_result_model_json['editable'] = True
        routing_tiered_caching_resp_result_model_json['modified_on'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of RoutingTieredCachingRespResult by calling from_dict on the json representation
        routing_tiered_caching_resp_result_model = RoutingTieredCachingRespResult.from_dict(routing_tiered_caching_resp_result_model_json)
        assert routing_tiered_caching_resp_result_model != False

        # Construct a model instance of RoutingTieredCachingRespResult by calling from_dict on the json representation
        routing_tiered_caching_resp_result_model_dict = RoutingTieredCachingRespResult.from_dict(routing_tiered_caching_resp_result_model_json).__dict__
        routing_tiered_caching_resp_result_model2 = RoutingTieredCachingRespResult(**routing_tiered_caching_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert routing_tiered_caching_resp_result_model == routing_tiered_caching_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        routing_tiered_caching_resp_result_model_json2 = routing_tiered_caching_resp_result_model.to_dict()
        assert routing_tiered_caching_resp_result_model_json2 == routing_tiered_caching_resp_result_model_json


class TestModel_SmartRoutingRespResult:
    """
    Test Class for SmartRoutingRespResult
    """

    def test_smart_routing_resp_result_serialization(self):
        """
        Test serialization/deserialization for SmartRoutingRespResult
        """

        # Construct a json representation of a SmartRoutingRespResult model
        smart_routing_resp_result_model_json = {}
        smart_routing_resp_result_model_json['id'] = 'smart_routing'
        smart_routing_resp_result_model_json['value'] = 'off'
        smart_routing_resp_result_model_json['editable'] = True
        smart_routing_resp_result_model_json['modified_on'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SmartRoutingRespResult by calling from_dict on the json representation
        smart_routing_resp_result_model = SmartRoutingRespResult.from_dict(smart_routing_resp_result_model_json)
        assert smart_routing_resp_result_model != False

        # Construct a model instance of SmartRoutingRespResult by calling from_dict on the json representation
        smart_routing_resp_result_model_dict = SmartRoutingRespResult.from_dict(smart_routing_resp_result_model_json).__dict__
        smart_routing_resp_result_model2 = SmartRoutingRespResult(**smart_routing_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert smart_routing_resp_result_model == smart_routing_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        smart_routing_resp_result_model_json2 = smart_routing_resp_result_model.to_dict()
        assert smart_routing_resp_result_model_json2 == smart_routing_resp_result_model_json


class TestModel_RoutingLatencyColosResp:
    """
    Test Class for RoutingLatencyColosResp
    """

    def test_routing_latency_colos_resp_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyColosResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        routing_latency_colos_resp_result_features_item_geometry_model = {}  # RoutingLatencyColosRespResultFeaturesItemGeometry
        routing_latency_colos_resp_result_features_item_geometry_model['coordinates'] = [36.0]
        routing_latency_colos_resp_result_features_item_geometry_model['type'] = 'Point'

        routing_latency_colos_resp_result_features_item_model = {}  # RoutingLatencyColosRespResultFeaturesItem
        routing_latency_colos_resp_result_features_item_model['code'] = 'EWR'
        routing_latency_colos_resp_result_features_item_model['smart_routing_req_count'] = 6696990
        routing_latency_colos_resp_result_features_item_model['pct_avg_change'] = 0.06003951841343536
        routing_latency_colos_resp_result_features_item_model['no_smart_routing_avg'] = 651.7771493198342
        routing_latency_colos_resp_result_features_item_model['smart_routing_avg'] = 690.9095354778789
        routing_latency_colos_resp_result_features_item_model['geometry'] = routing_latency_colos_resp_result_features_item_geometry_model

        routing_latency_colos_resp_result_model = {}  # RoutingLatencyColosRespResult
        routing_latency_colos_resp_result_model['type'] = 'FeatureCollection'
        routing_latency_colos_resp_result_model['features'] = [routing_latency_colos_resp_result_features_item_model]

        # Construct a json representation of a RoutingLatencyColosResp model
        routing_latency_colos_resp_model_json = {}
        routing_latency_colos_resp_model_json['result'] = routing_latency_colos_resp_result_model
        routing_latency_colos_resp_model_json['success'] = True
        routing_latency_colos_resp_model_json['errors'] = [['testString']]
        routing_latency_colos_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of RoutingLatencyColosResp by calling from_dict on the json representation
        routing_latency_colos_resp_model = RoutingLatencyColosResp.from_dict(routing_latency_colos_resp_model_json)
        assert routing_latency_colos_resp_model != False

        # Construct a model instance of RoutingLatencyColosResp by calling from_dict on the json representation
        routing_latency_colos_resp_model_dict = RoutingLatencyColosResp.from_dict(routing_latency_colos_resp_model_json).__dict__
        routing_latency_colos_resp_model2 = RoutingLatencyColosResp(**routing_latency_colos_resp_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_colos_resp_model == routing_latency_colos_resp_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_colos_resp_model_json2 = routing_latency_colos_resp_model.to_dict()
        assert routing_latency_colos_resp_model_json2 == routing_latency_colos_resp_model_json


class TestModel_RoutingLatencyResp:
    """
    Test Class for RoutingLatencyResp
    """

    def test_routing_latency_resp_serialization(self):
        """
        Test serialization/deserialization for RoutingLatencyResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        routing_latency_resp_result_range_model = {}  # RoutingLatencyRespResultRange
        routing_latency_resp_result_range_model['min'] = 0
        routing_latency_resp_result_range_model['max'] = 1500

        routing_latency_resp_result_time_range_model = {}  # RoutingLatencyRespResultTimeRange
        routing_latency_resp_result_time_range_model['min'] = '2019-01-01T12:00:00Z'
        routing_latency_resp_result_time_range_model['max'] = '2019-01-01T12:00:00Z'

        routing_latency_resp_result_data_model = {}  # RoutingLatencyRespResultData
        routing_latency_resp_result_data_model['lable'] = ['testString']
        routing_latency_resp_result_data_model['counts'] = [38]
        routing_latency_resp_result_data_model['averages'] = [38]

        routing_latency_resp_result_model = {}  # RoutingLatencyRespResult
        routing_latency_resp_result_model['percent_smart_routed'] = 63.4
        routing_latency_resp_result_model['bins'] = 10
        routing_latency_resp_result_model['range'] = routing_latency_resp_result_range_model
        routing_latency_resp_result_model['time_range'] = routing_latency_resp_result_time_range_model
        routing_latency_resp_result_model['data'] = routing_latency_resp_result_data_model

        # Construct a json representation of a RoutingLatencyResp model
        routing_latency_resp_model_json = {}
        routing_latency_resp_model_json['result'] = routing_latency_resp_result_model
        routing_latency_resp_model_json['success'] = True
        routing_latency_resp_model_json['errors'] = [['testString']]
        routing_latency_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of RoutingLatencyResp by calling from_dict on the json representation
        routing_latency_resp_model = RoutingLatencyResp.from_dict(routing_latency_resp_model_json)
        assert routing_latency_resp_model != False

        # Construct a model instance of RoutingLatencyResp by calling from_dict on the json representation
        routing_latency_resp_model_dict = RoutingLatencyResp.from_dict(routing_latency_resp_model_json).__dict__
        routing_latency_resp_model2 = RoutingLatencyResp(**routing_latency_resp_model_dict)

        # Verify the model instances are equivalent
        assert routing_latency_resp_model == routing_latency_resp_model2

        # Convert model instance back to dict and verify no loss of data
        routing_latency_resp_model_json2 = routing_latency_resp_model.to_dict()
        assert routing_latency_resp_model_json2 == routing_latency_resp_model_json


class TestModel_RoutingTieredCachingResp:
    """
    Test Class for RoutingTieredCachingResp
    """

    def test_routing_tiered_caching_resp_serialization(self):
        """
        Test serialization/deserialization for RoutingTieredCachingResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        routing_tiered_caching_resp_result_model = {}  # RoutingTieredCachingRespResult
        routing_tiered_caching_resp_result_model['id'] = 'tiered_caching'
        routing_tiered_caching_resp_result_model['value'] = 'on'
        routing_tiered_caching_resp_result_model['editable'] = True
        routing_tiered_caching_resp_result_model['modified_on'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a RoutingTieredCachingResp model
        routing_tiered_caching_resp_model_json = {}
        routing_tiered_caching_resp_model_json['result'] = routing_tiered_caching_resp_result_model
        routing_tiered_caching_resp_model_json['success'] = True
        routing_tiered_caching_resp_model_json['errors'] = [['testString']]
        routing_tiered_caching_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of RoutingTieredCachingResp by calling from_dict on the json representation
        routing_tiered_caching_resp_model = RoutingTieredCachingResp.from_dict(routing_tiered_caching_resp_model_json)
        assert routing_tiered_caching_resp_model != False

        # Construct a model instance of RoutingTieredCachingResp by calling from_dict on the json representation
        routing_tiered_caching_resp_model_dict = RoutingTieredCachingResp.from_dict(routing_tiered_caching_resp_model_json).__dict__
        routing_tiered_caching_resp_model2 = RoutingTieredCachingResp(**routing_tiered_caching_resp_model_dict)

        # Verify the model instances are equivalent
        assert routing_tiered_caching_resp_model == routing_tiered_caching_resp_model2

        # Convert model instance back to dict and verify no loss of data
        routing_tiered_caching_resp_model_json2 = routing_tiered_caching_resp_model.to_dict()
        assert routing_tiered_caching_resp_model_json2 == routing_tiered_caching_resp_model_json


class TestModel_SmartRoutingResp:
    """
    Test Class for SmartRoutingResp
    """

    def test_smart_routing_resp_serialization(self):
        """
        Test serialization/deserialization for SmartRoutingResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smart_routing_resp_result_model = {}  # SmartRoutingRespResult
        smart_routing_resp_result_model['id'] = 'smart_routing'
        smart_routing_resp_result_model['value'] = 'off'
        smart_routing_resp_result_model['editable'] = True
        smart_routing_resp_result_model['modified_on'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a SmartRoutingResp model
        smart_routing_resp_model_json = {}
        smart_routing_resp_model_json['result'] = smart_routing_resp_result_model
        smart_routing_resp_model_json['success'] = True
        smart_routing_resp_model_json['errors'] = [['testString']]
        smart_routing_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of SmartRoutingResp by calling from_dict on the json representation
        smart_routing_resp_model = SmartRoutingResp.from_dict(smart_routing_resp_model_json)
        assert smart_routing_resp_model != False

        # Construct a model instance of SmartRoutingResp by calling from_dict on the json representation
        smart_routing_resp_model_dict = SmartRoutingResp.from_dict(smart_routing_resp_model_json).__dict__
        smart_routing_resp_model2 = SmartRoutingResp(**smart_routing_resp_model_dict)

        # Verify the model instances are equivalent
        assert smart_routing_resp_model == smart_routing_resp_model2

        # Convert model instance back to dict and verify no loss of data
        smart_routing_resp_model_json2 = smart_routing_resp_model.to_dict()
        assert smart_routing_resp_model_json2 == smart_routing_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
