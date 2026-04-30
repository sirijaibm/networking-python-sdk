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
Unit Tests for BotAnalyticsV1
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
from ibm_cloud_networking_services.bot_analytics_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = BotAnalyticsV1(
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
# Start of Service: BotAnalyticsScoreSource
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

        service = BotAnalyticsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, BotAnalyticsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = BotAnalyticsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = BotAnalyticsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided must be provided'):
            service = BotAnalyticsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetBotScore:
    """
    Test Class for get_bot_score
    """

    @responses.activate
    def test_get_bot_score_all_params(self):
        """
        get_bot_score()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_analytics/score_source')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"botScore": [{"avg": {"sampleInterval": 15}, "count": 5, "dimensions": {"botScoreSrcName": "bot_score_src_name"}}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        since = string_to_datetime('2021-06-10T00:00:00Z')
        until = string_to_datetime('2021-06-11T00:00:00Z')

        # Invoke method
        response = _service.get_bot_score(
            since,
            until,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)

    def test_get_bot_score_all_params_with_retries(self):
        # Enable retries and run test_get_bot_score_all_params.
        _service.enable_retries()
        self.test_get_bot_score_all_params()

        # Disable retries and run test_get_bot_score_all_params.
        _service.disable_retries()
        self.test_get_bot_score_all_params()

    @responses.activate
    def test_get_bot_score_value_error(self):
        """
        test_get_bot_score_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_analytics/score_source')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"botScore": [{"avg": {"sampleInterval": 15}, "count": 5, "dimensions": {"botScoreSrcName": "bot_score_src_name"}}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        since = string_to_datetime('2021-06-10T00:00:00Z')
        until = string_to_datetime('2021-06-11T00:00:00Z')

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "since": since,
            "until": until,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_bot_score(**req_copy)

    def test_get_bot_score_value_error_with_retries(self):
        # Enable retries and run test_get_bot_score_value_error.
        _service.enable_retries()
        self.test_get_bot_score_value_error()

        # Disable retries and run test_get_bot_score_value_error.
        _service.disable_retries()
        self.test_get_bot_score_value_error()


# endregion
##############################################################################
# End of Service: BotAnalyticsScoreSource
##############################################################################

##############################################################################
# Start of Service: BotAnalyticsTimeseries
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

        service = BotAnalyticsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, BotAnalyticsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = BotAnalyticsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = BotAnalyticsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided must be provided'):
            service = BotAnalyticsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetBotTimeseries:
    """
    Test Class for get_bot_timeseries
    """

    @responses.activate
    def test_get_bot_timeseries_all_params(self):
        """
        get_bot_timeseries()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_analytics/timeseries')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"botScore": [{"anyKey": "anyValue"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        since = string_to_datetime('2021-06-10T00:00:00Z')
        until = string_to_datetime('2021-06-11T00:00:00Z')

        # Invoke method
        response = _service.get_bot_timeseries(
            since,
            until,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)

    def test_get_bot_timeseries_all_params_with_retries(self):
        # Enable retries and run test_get_bot_timeseries_all_params.
        _service.enable_retries()
        self.test_get_bot_timeseries_all_params()

        # Disable retries and run test_get_bot_timeseries_all_params.
        _service.disable_retries()
        self.test_get_bot_timeseries_all_params()

    @responses.activate
    def test_get_bot_timeseries_value_error(self):
        """
        test_get_bot_timeseries_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_analytics/timeseries')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"botScore": [{"anyKey": "anyValue"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        since = string_to_datetime('2021-06-10T00:00:00Z')
        until = string_to_datetime('2021-06-11T00:00:00Z')

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "since": since,
            "until": until,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_bot_timeseries(**req_copy)

    def test_get_bot_timeseries_value_error_with_retries(self):
        # Enable retries and run test_get_bot_timeseries_value_error.
        _service.enable_retries()
        self.test_get_bot_timeseries_value_error()

        # Disable retries and run test_get_bot_timeseries_value_error.
        _service.disable_retries()
        self.test_get_bot_timeseries_value_error()


# endregion
##############################################################################
# End of Service: BotAnalyticsTimeseries
##############################################################################

##############################################################################
# Start of Service: BotAnalyticsTopNs
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

        service = BotAnalyticsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, BotAnalyticsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = BotAnalyticsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = BotAnalyticsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = BotAnalyticsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetBotTopns:
    """
    Test Class for get_bot_topns
    """

    @responses.activate
    def test_get_bot_topns_all_params(self):
        """
        get_bot_topns()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_analytics/top_ns')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"anyKey": "anyValue"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        since = string_to_datetime('2021-06-10T00:00:00Z')
        until = string_to_datetime('2021-06-11T00:00:00Z')

        # Invoke method
        response = _service.get_bot_topns(
            since,
            until,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)

    def test_get_bot_topns_all_params_with_retries(self):
        # Enable retries and run test_get_bot_topns_all_params.
        _service.enable_retries()
        self.test_get_bot_topns_all_params()

        # Disable retries and run test_get_bot_topns_all_params.
        _service.disable_retries()
        self.test_get_bot_topns_all_params()

    @responses.activate
    def test_get_bot_topns_value_error(self):
        """
        test_get_bot_topns_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_analytics/top_ns')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"anyKey": "anyValue"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        since = string_to_datetime('2021-06-10T00:00:00Z')
        until = string_to_datetime('2021-06-11T00:00:00Z')

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "since": since,
            "until": until,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_bot_topns(**req_copy)

    def test_get_bot_topns_value_error_with_retries(self):
        # Enable retries and run test_get_bot_topns_value_error.
        _service.enable_retries()
        self.test_get_bot_topns_value_error()

        # Disable retries and run test_get_bot_topns_value_error.
        _service.disable_retries()
        self.test_get_bot_topns_value_error()


# endregion
##############################################################################
# End of Service: BotAnalyticsTopNs
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_BotScoreRespResultItem:
    """
    Test Class for BotScoreRespResultItem
    """

    def test_bot_score_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for BotScoreRespResultItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bot_score_resp_result_item_bot_score_item_avg_model = {}  # BotScoreRespResultItemBotScoreItemAvg
        bot_score_resp_result_item_bot_score_item_avg_model['sampleInterval'] = 72.5

        bot_score_resp_result_item_bot_score_item_dimensions_model = {}  # BotScoreRespResultItemBotScoreItemDimensions
        bot_score_resp_result_item_bot_score_item_dimensions_model['botScoreSrcName'] = 'testString'

        bot_score_resp_result_item_bot_score_item_model = {}  # BotScoreRespResultItemBotScoreItem
        bot_score_resp_result_item_bot_score_item_model['avg'] = bot_score_resp_result_item_bot_score_item_avg_model
        bot_score_resp_result_item_bot_score_item_model['count'] = 72.5
        bot_score_resp_result_item_bot_score_item_model['dimensions'] = bot_score_resp_result_item_bot_score_item_dimensions_model

        # Construct a json representation of a BotScoreRespResultItem model
        bot_score_resp_result_item_model_json = {}
        bot_score_resp_result_item_model_json['botScore'] = [bot_score_resp_result_item_bot_score_item_model]

        # Construct a model instance of BotScoreRespResultItem by calling from_dict on the json representation
        bot_score_resp_result_item_model = BotScoreRespResultItem.from_dict(bot_score_resp_result_item_model_json)
        assert bot_score_resp_result_item_model != False

        # Construct a model instance of BotScoreRespResultItem by calling from_dict on the json representation
        bot_score_resp_result_item_model_dict = BotScoreRespResultItem.from_dict(bot_score_resp_result_item_model_json).__dict__
        bot_score_resp_result_item_model2 = BotScoreRespResultItem(**bot_score_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert bot_score_resp_result_item_model == bot_score_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        bot_score_resp_result_item_model_json2 = bot_score_resp_result_item_model.to_dict()
        assert bot_score_resp_result_item_model_json2 == bot_score_resp_result_item_model_json


class TestModel_BotScoreRespResultItemBotScoreItem:
    """
    Test Class for BotScoreRespResultItemBotScoreItem
    """

    def test_bot_score_resp_result_item_bot_score_item_serialization(self):
        """
        Test serialization/deserialization for BotScoreRespResultItemBotScoreItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bot_score_resp_result_item_bot_score_item_avg_model = {}  # BotScoreRespResultItemBotScoreItemAvg
        bot_score_resp_result_item_bot_score_item_avg_model['sampleInterval'] = 72.5

        bot_score_resp_result_item_bot_score_item_dimensions_model = {}  # BotScoreRespResultItemBotScoreItemDimensions
        bot_score_resp_result_item_bot_score_item_dimensions_model['botScoreSrcName'] = 'testString'

        # Construct a json representation of a BotScoreRespResultItemBotScoreItem model
        bot_score_resp_result_item_bot_score_item_model_json = {}
        bot_score_resp_result_item_bot_score_item_model_json['avg'] = bot_score_resp_result_item_bot_score_item_avg_model
        bot_score_resp_result_item_bot_score_item_model_json['count'] = 72.5
        bot_score_resp_result_item_bot_score_item_model_json['dimensions'] = bot_score_resp_result_item_bot_score_item_dimensions_model

        # Construct a model instance of BotScoreRespResultItemBotScoreItem by calling from_dict on the json representation
        bot_score_resp_result_item_bot_score_item_model = BotScoreRespResultItemBotScoreItem.from_dict(bot_score_resp_result_item_bot_score_item_model_json)
        assert bot_score_resp_result_item_bot_score_item_model != False

        # Construct a model instance of BotScoreRespResultItemBotScoreItem by calling from_dict on the json representation
        bot_score_resp_result_item_bot_score_item_model_dict = BotScoreRespResultItemBotScoreItem.from_dict(bot_score_resp_result_item_bot_score_item_model_json).__dict__
        bot_score_resp_result_item_bot_score_item_model2 = BotScoreRespResultItemBotScoreItem(**bot_score_resp_result_item_bot_score_item_model_dict)

        # Verify the model instances are equivalent
        assert bot_score_resp_result_item_bot_score_item_model == bot_score_resp_result_item_bot_score_item_model2

        # Convert model instance back to dict and verify no loss of data
        bot_score_resp_result_item_bot_score_item_model_json2 = bot_score_resp_result_item_bot_score_item_model.to_dict()
        assert bot_score_resp_result_item_bot_score_item_model_json2 == bot_score_resp_result_item_bot_score_item_model_json


class TestModel_BotScoreRespResultItemBotScoreItemAvg:
    """
    Test Class for BotScoreRespResultItemBotScoreItemAvg
    """

    def test_bot_score_resp_result_item_bot_score_item_avg_serialization(self):
        """
        Test serialization/deserialization for BotScoreRespResultItemBotScoreItemAvg
        """

        # Construct a json representation of a BotScoreRespResultItemBotScoreItemAvg model
        bot_score_resp_result_item_bot_score_item_avg_model_json = {}
        bot_score_resp_result_item_bot_score_item_avg_model_json['sampleInterval'] = 72.5

        # Construct a model instance of BotScoreRespResultItemBotScoreItemAvg by calling from_dict on the json representation
        bot_score_resp_result_item_bot_score_item_avg_model = BotScoreRespResultItemBotScoreItemAvg.from_dict(bot_score_resp_result_item_bot_score_item_avg_model_json)
        assert bot_score_resp_result_item_bot_score_item_avg_model != False

        # Construct a model instance of BotScoreRespResultItemBotScoreItemAvg by calling from_dict on the json representation
        bot_score_resp_result_item_bot_score_item_avg_model_dict = BotScoreRespResultItemBotScoreItemAvg.from_dict(bot_score_resp_result_item_bot_score_item_avg_model_json).__dict__
        bot_score_resp_result_item_bot_score_item_avg_model2 = BotScoreRespResultItemBotScoreItemAvg(**bot_score_resp_result_item_bot_score_item_avg_model_dict)

        # Verify the model instances are equivalent
        assert bot_score_resp_result_item_bot_score_item_avg_model == bot_score_resp_result_item_bot_score_item_avg_model2

        # Convert model instance back to dict and verify no loss of data
        bot_score_resp_result_item_bot_score_item_avg_model_json2 = bot_score_resp_result_item_bot_score_item_avg_model.to_dict()
        assert bot_score_resp_result_item_bot_score_item_avg_model_json2 == bot_score_resp_result_item_bot_score_item_avg_model_json


class TestModel_BotScoreRespResultItemBotScoreItemDimensions:
    """
    Test Class for BotScoreRespResultItemBotScoreItemDimensions
    """

    def test_bot_score_resp_result_item_bot_score_item_dimensions_serialization(self):
        """
        Test serialization/deserialization for BotScoreRespResultItemBotScoreItemDimensions
        """

        # Construct a json representation of a BotScoreRespResultItemBotScoreItemDimensions model
        bot_score_resp_result_item_bot_score_item_dimensions_model_json = {}
        bot_score_resp_result_item_bot_score_item_dimensions_model_json['botScoreSrcName'] = 'testString'

        # Construct a model instance of BotScoreRespResultItemBotScoreItemDimensions by calling from_dict on the json representation
        bot_score_resp_result_item_bot_score_item_dimensions_model = BotScoreRespResultItemBotScoreItemDimensions.from_dict(bot_score_resp_result_item_bot_score_item_dimensions_model_json)
        assert bot_score_resp_result_item_bot_score_item_dimensions_model != False

        # Construct a model instance of BotScoreRespResultItemBotScoreItemDimensions by calling from_dict on the json representation
        bot_score_resp_result_item_bot_score_item_dimensions_model_dict = BotScoreRespResultItemBotScoreItemDimensions.from_dict(bot_score_resp_result_item_bot_score_item_dimensions_model_json).__dict__
        bot_score_resp_result_item_bot_score_item_dimensions_model2 = BotScoreRespResultItemBotScoreItemDimensions(**bot_score_resp_result_item_bot_score_item_dimensions_model_dict)

        # Verify the model instances are equivalent
        assert bot_score_resp_result_item_bot_score_item_dimensions_model == bot_score_resp_result_item_bot_score_item_dimensions_model2

        # Convert model instance back to dict and verify no loss of data
        bot_score_resp_result_item_bot_score_item_dimensions_model_json2 = bot_score_resp_result_item_bot_score_item_dimensions_model.to_dict()
        assert bot_score_resp_result_item_bot_score_item_dimensions_model_json2 == bot_score_resp_result_item_bot_score_item_dimensions_model_json


class TestModel_BotTimeseriesRespResultItem:
    """
    Test Class for BotTimeseriesRespResultItem
    """

    def test_bot_timeseries_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for BotTimeseriesRespResultItem
        """

        # Construct a json representation of a BotTimeseriesRespResultItem model
        bot_timeseries_resp_result_item_model_json = {}
        bot_timeseries_resp_result_item_model_json['botScore'] = [{'anyKey': 'anyValue'}]

        # Construct a model instance of BotTimeseriesRespResultItem by calling from_dict on the json representation
        bot_timeseries_resp_result_item_model = BotTimeseriesRespResultItem.from_dict(bot_timeseries_resp_result_item_model_json)
        assert bot_timeseries_resp_result_item_model != False

        # Construct a model instance of BotTimeseriesRespResultItem by calling from_dict on the json representation
        bot_timeseries_resp_result_item_model_dict = BotTimeseriesRespResultItem.from_dict(bot_timeseries_resp_result_item_model_json).__dict__
        bot_timeseries_resp_result_item_model2 = BotTimeseriesRespResultItem(**bot_timeseries_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert bot_timeseries_resp_result_item_model == bot_timeseries_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        bot_timeseries_resp_result_item_model_json2 = bot_timeseries_resp_result_item_model.to_dict()
        assert bot_timeseries_resp_result_item_model_json2 == bot_timeseries_resp_result_item_model_json


class TestModel_BotScoreResp:
    """
    Test Class for BotScoreResp
    """

    def test_bot_score_resp_serialization(self):
        """
        Test serialization/deserialization for BotScoreResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bot_score_resp_result_item_bot_score_item_avg_model = {}  # BotScoreRespResultItemBotScoreItemAvg
        bot_score_resp_result_item_bot_score_item_avg_model['sampleInterval'] = 72.5

        bot_score_resp_result_item_bot_score_item_dimensions_model = {}  # BotScoreRespResultItemBotScoreItemDimensions
        bot_score_resp_result_item_bot_score_item_dimensions_model['botScoreSrcName'] = 'testString'

        bot_score_resp_result_item_bot_score_item_model = {}  # BotScoreRespResultItemBotScoreItem
        bot_score_resp_result_item_bot_score_item_model['avg'] = bot_score_resp_result_item_bot_score_item_avg_model
        bot_score_resp_result_item_bot_score_item_model['count'] = 72.5
        bot_score_resp_result_item_bot_score_item_model['dimensions'] = bot_score_resp_result_item_bot_score_item_dimensions_model

        bot_score_resp_result_item_model = {}  # BotScoreRespResultItem
        bot_score_resp_result_item_model['botScore'] = [bot_score_resp_result_item_bot_score_item_model]

        # Construct a json representation of a BotScoreResp model
        bot_score_resp_model_json = {}
        bot_score_resp_model_json['success'] = True
        bot_score_resp_model_json['errors'] = [['testString']]
        bot_score_resp_model_json['messages'] = [['testString']]
        bot_score_resp_model_json['result'] = [bot_score_resp_result_item_model]

        # Construct a model instance of BotScoreResp by calling from_dict on the json representation
        bot_score_resp_model = BotScoreResp.from_dict(bot_score_resp_model_json)
        assert bot_score_resp_model != False

        # Construct a model instance of BotScoreResp by calling from_dict on the json representation
        bot_score_resp_model_dict = BotScoreResp.from_dict(bot_score_resp_model_json).__dict__
        bot_score_resp_model2 = BotScoreResp(**bot_score_resp_model_dict)

        # Verify the model instances are equivalent
        assert bot_score_resp_model == bot_score_resp_model2

        # Convert model instance back to dict and verify no loss of data
        bot_score_resp_model_json2 = bot_score_resp_model.to_dict()
        assert bot_score_resp_model_json2 == bot_score_resp_model_json


class TestModel_BotTimeseriesResp:
    """
    Test Class for BotTimeseriesResp
    """

    def test_bot_timeseries_resp_serialization(self):
        """
        Test serialization/deserialization for BotTimeseriesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bot_timeseries_resp_result_item_model = {}  # BotTimeseriesRespResultItem
        bot_timeseries_resp_result_item_model['botScore'] = [{'anyKey': 'anyValue'}]

        # Construct a json representation of a BotTimeseriesResp model
        bot_timeseries_resp_model_json = {}
        bot_timeseries_resp_model_json['success'] = True
        bot_timeseries_resp_model_json['errors'] = [['testString']]
        bot_timeseries_resp_model_json['messages'] = [['testString']]
        bot_timeseries_resp_model_json['result'] = [bot_timeseries_resp_result_item_model]

        # Construct a model instance of BotTimeseriesResp by calling from_dict on the json representation
        bot_timeseries_resp_model = BotTimeseriesResp.from_dict(bot_timeseries_resp_model_json)
        assert bot_timeseries_resp_model != False

        # Construct a model instance of BotTimeseriesResp by calling from_dict on the json representation
        bot_timeseries_resp_model_dict = BotTimeseriesResp.from_dict(bot_timeseries_resp_model_json).__dict__
        bot_timeseries_resp_model2 = BotTimeseriesResp(**bot_timeseries_resp_model_dict)

        # Verify the model instances are equivalent
        assert bot_timeseries_resp_model == bot_timeseries_resp_model2

        # Convert model instance back to dict and verify no loss of data
        bot_timeseries_resp_model_json2 = bot_timeseries_resp_model.to_dict()
        assert bot_timeseries_resp_model_json2 == bot_timeseries_resp_model_json


class TestModel_BotTopnsResp:
    """
    Test Class for BotTopnsResp
    """

    def test_bot_topns_resp_serialization(self):
        """
        Test serialization/deserialization for BotTopnsResp
        """

        # Construct a json representation of a BotTopnsResp model
        bot_topns_resp_model_json = {}
        bot_topns_resp_model_json['success'] = True
        bot_topns_resp_model_json['errors'] = [['testString']]
        bot_topns_resp_model_json['messages'] = [['testString']]
        bot_topns_resp_model_json['result'] = [{'anyKey': 'anyValue'}]

        # Construct a model instance of BotTopnsResp by calling from_dict on the json representation
        bot_topns_resp_model = BotTopnsResp.from_dict(bot_topns_resp_model_json)
        assert bot_topns_resp_model != False

        # Construct a model instance of BotTopnsResp by calling from_dict on the json representation
        bot_topns_resp_model_dict = BotTopnsResp.from_dict(bot_topns_resp_model_json).__dict__
        bot_topns_resp_model2 = BotTopnsResp(**bot_topns_resp_model_dict)

        # Verify the model instances are equivalent
        assert bot_topns_resp_model == bot_topns_resp_model2

        # Convert model instance back to dict and verify no loss of data
        bot_topns_resp_model_json2 = bot_topns_resp_model.to_dict()
        assert bot_topns_resp_model_json2 == bot_topns_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
