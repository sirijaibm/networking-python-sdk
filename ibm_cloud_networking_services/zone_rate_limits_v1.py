# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.114.0-a902401e-20260427-192904

"""
Zone Rate Limits

API Version: 1.0.1
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class ZoneRateLimitsV1(BaseService):
    """The Zone Rate Limits V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'zone_rate_limits'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'ZoneRateLimitsV1':
        """
        Return a new client for the Zone Rate Limits service using the specified
               parameters and external configuration.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_identifier,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        crn: str,
        zone_identifier: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Zone Rate Limits service.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier

    #########################
    # Zone Rate Limits
    #########################

    def list_all_zone_rate_limits(
        self,
        *,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all rate limits.

        The details of Rate Limit for a given zone under a given service instance.

        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of rate limits per page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRatelimitResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_all_zone_rate_limits',
        )
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rate_limits'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_zone_rate_limits(
        self,
        *,
        threshold: Optional[int] = None,
        period: Optional[int] = None,
        action: Optional['RatelimitInputAction'] = None,
        match: Optional['RatelimitInputMatch'] = None,
        disabled: Optional[bool] = None,
        description: Optional[str] = None,
        bypass: Optional[List['RatelimitInputBypassItem']] = None,
        correlate: Optional['RatelimitInputCorrelate'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create rate limit.

        Create a new rate limit for a given zone under a service instance.

        :param int threshold: (optional) The threshold that triggers the rate limit
               mitigations, combine with period. i.e. threshold per period.
        :param int period: (optional) The time in seconds to count matching
               traffic. If the count exceeds threshold within this period the action will
               be performed.
        :param RatelimitInputAction action: (optional) action.
        :param RatelimitInputMatch match: (optional) Determines which traffic the
               rate limit counts towards the threshold. Needs to be one of "request" or
               "response" objects.
        :param bool disabled: (optional) Whether this ratelimit is currently
               disabled.
        :param str description: (optional) A note that you can use to describe the
               reason for a rate limit.
        :param List[RatelimitInputBypassItem] bypass: (optional) Criteria that
               would allow the rate limit to be bypassed, for example to express that you
               shouldn't apply a rate limit to a given set of URLs.
        :param RatelimitInputCorrelate correlate: (optional) Enable NAT based rate
               limits.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitResp` object
        """

        if action is not None:
            action = convert_model(action)
        if match is not None:
            match = convert_model(match)
        if bypass is not None:
            bypass = [convert_model(x) for x in bypass]
        if correlate is not None:
            correlate = convert_model(correlate)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_zone_rate_limits',
        )
        headers.update(sdk_headers)

        data = {
            'threshold': threshold,
            'period': period,
            'action': action,
            'match': match,
            'disabled': disabled,
            'description': description,
            'bypass': bypass,
            'correlate': correlate,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rate_limits'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_zone_rate_limit(
        self,
        rate_limit_identifier: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete rate limit.

        Delete a rate limit given its id.

        :param str rate_limit_identifier: Identifier of the rate limit to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteRateLimitResp` object
        """

        if not rate_limit_identifier:
            raise ValueError('rate_limit_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_zone_rate_limit',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'rate_limit_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rate_limits/{rate_limit_identifier}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_rate_limit(
        self,
        rate_limit_identifier: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a rate limit.

        Get the details of a rate limit for a given zone under a given service instance.

        :param str rate_limit_identifier: Identifier of rate limit for the given
               zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitResp` object
        """

        if not rate_limit_identifier:
            raise ValueError('rate_limit_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_rate_limit',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'rate_limit_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rate_limits/{rate_limit_identifier}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_rate_limit(
        self,
        rate_limit_identifier: str,
        *,
        threshold: Optional[int] = None,
        period: Optional[int] = None,
        action: Optional['RatelimitInputAction'] = None,
        match: Optional['RatelimitInputMatch'] = None,
        disabled: Optional[bool] = None,
        description: Optional[str] = None,
        bypass: Optional[List['RatelimitInputBypassItem']] = None,
        correlate: Optional['RatelimitInputCorrelate'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update rate limit.

        Update an existing rate limit for a given zone under a service instance.

        :param str rate_limit_identifier: Identifier of rate limit.
        :param int threshold: (optional) The threshold that triggers the rate limit
               mitigations, combine with period. i.e. threshold per period.
        :param int period: (optional) The time in seconds to count matching
               traffic. If the count exceeds threshold within this period the action will
               be performed.
        :param RatelimitInputAction action: (optional) action.
        :param RatelimitInputMatch match: (optional) Determines which traffic the
               rate limit counts towards the threshold. Needs to be one of "request" or
               "response" objects.
        :param bool disabled: (optional) Whether this ratelimit is currently
               disabled.
        :param str description: (optional) A note that you can use to describe the
               reason for a rate limit.
        :param List[RatelimitInputBypassItem] bypass: (optional) Criteria that
               would allow the rate limit to be bypassed, for example to express that you
               shouldn't apply a rate limit to a given set of URLs.
        :param RatelimitInputCorrelate correlate: (optional) Enable NAT based rate
               limits.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitResp` object
        """

        if not rate_limit_identifier:
            raise ValueError('rate_limit_identifier must be provided')
        if action is not None:
            action = convert_model(action)
        if match is not None:
            match = convert_model(match)
        if bypass is not None:
            bypass = [convert_model(x) for x in bypass]
        if correlate is not None:
            correlate = convert_model(correlate)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_rate_limit',
        )
        headers.update(sdk_headers)

        data = {
            'threshold': threshold,
            'period': period,
            'action': action,
            'match': match,
            'disabled': disabled,
            'description': description,
            'bypass': bypass,
            'correlate': correlate,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'rate_limit_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rate_limits/{rate_limit_identifier}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_rate_limit_analytics(
        self,
        since: datetime,
        until: datetime,
        time_delta: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get rate limit analytics for a zone.

        Get rate limit analytics for a zone.

        :param datetime since: The beginning of the requested time frame.
        :param datetime until: The end of the requested time frame.
        :param int time_delta: The time interval (seconds) of each analytic's
               record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitAnalyticsResp` object
        """

        if since is None:
            raise ValueError('since must be provided')
        if until is None:
            raise ValueError('until must be provided')
        if time_delta is None:
            raise ValueError('time_delta must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_rate_limit_analytics',
        )
        headers.update(sdk_headers)

        params = {
            'since': since,
            'until': until,
            'time_delta': time_delta,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rate_limit_analytics'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class DeleteRateLimitRespResult:
    """
    Container for response information.

    :param str id: ID.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a DeleteRateLimitRespResult object.

        :param str id: ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteRateLimitRespResult':
        """Initialize a DeleteRateLimitRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DeleteRateLimitRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteRateLimitRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteRateLimitRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteRateLimitRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteRateLimitRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListRatelimitRespResultInfo:
    """
    Statistics of results.

    :param int page: Page number.
    :param int per_page: Number of results per page.
    :param int count: Number of results.
    :param int total_count: Total number of results.
    """

    def __init__(
        self,
        page: int,
        per_page: int,
        count: int,
        total_count: int,
    ) -> None:
        """
        Initialize a ListRatelimitRespResultInfo object.

        :param int page: Page number.
        :param int per_page: Number of results per page.
        :param int count: Number of results.
        :param int total_count: Total number of results.
        """
        self.page = page
        self.per_page = per_page
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRatelimitRespResultInfo':
        """Initialize a ListRatelimitRespResultInfo object from a json dictionary."""
        args = {}
        if (page := _dict.get('page')) is not None:
            args['page'] = page
        else:
            raise ValueError('Required property \'page\' not present in ListRatelimitRespResultInfo JSON')
        if (per_page := _dict.get('per_page')) is not None:
            args['per_page'] = per_page
        else:
            raise ValueError('Required property \'per_page\' not present in ListRatelimitRespResultInfo JSON')
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        else:
            raise ValueError('Required property \'count\' not present in ListRatelimitRespResultInfo JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ListRatelimitRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRatelimitRespResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'page') and self.page is not None:
            _dict['page'] = self.page
        if hasattr(self, 'per_page') and self.per_page is not None:
            _dict['per_page'] = self.per_page
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListRatelimitRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRatelimitRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRatelimitRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitAnalyticsRespTimeseriesItem:
    """
    RatelimitAnalyticsRespTimeseriesItem.

    :param datetime since: The beginning time of the analytics record.
    :param datetime until: The end time of the analytics record.
    :param dict rules: rate limit rules.
    """

    def __init__(
        self,
        since: datetime,
        until: datetime,
        rules: dict,
    ) -> None:
        """
        Initialize a RatelimitAnalyticsRespTimeseriesItem object.

        :param datetime since: The beginning time of the analytics record.
        :param datetime until: The end time of the analytics record.
        :param dict rules: rate limit rules.
        """
        self.since = since
        self.until = until
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitAnalyticsRespTimeseriesItem':
        """Initialize a RatelimitAnalyticsRespTimeseriesItem object from a json dictionary."""
        args = {}
        if (since := _dict.get('since')) is not None:
            args['since'] = string_to_datetime(since)
        else:
            raise ValueError('Required property \'since\' not present in RatelimitAnalyticsRespTimeseriesItem JSON')
        if (until := _dict.get('until')) is not None:
            args['until'] = string_to_datetime(until)
        else:
            raise ValueError('Required property \'until\' not present in RatelimitAnalyticsRespTimeseriesItem JSON')
        if (rules := _dict.get('rules')) is not None:
            args['rules'] = rules
        else:
            raise ValueError('Required property \'rules\' not present in RatelimitAnalyticsRespTimeseriesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitAnalyticsRespTimeseriesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'since') and self.since is not None:
            _dict['since'] = datetime_to_string(self.since)
        if hasattr(self, 'until') and self.until is not None:
            _dict['until'] = datetime_to_string(self.until)
        if hasattr(self, 'rules') and self.rules is not None:
            _dict['rules'] = self.rules
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitAnalyticsRespTimeseriesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitAnalyticsRespTimeseriesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitAnalyticsRespTimeseriesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitInputAction:
    """
    action.

    :param str mode: The type of action to perform.
    :param int timeout: (optional) The time in seconds as an integer to perform the
          mitigation action. Must be the same or greater than the period. This field is
          valid only when mode is "simulate" or "ban".
    :param RatelimitInputActionResponse response: (optional) Custom content-type and
          body to return, this overrides the custom error for the zone. This field is not
          required. Omission will result in default HTML error page.This field is valid
          only when mode is "simulate" or "ban".
    """

    def __init__(
        self,
        mode: str,
        *,
        timeout: Optional[int] = None,
        response: Optional['RatelimitInputActionResponse'] = None,
    ) -> None:
        """
        Initialize a RatelimitInputAction object.

        :param str mode: The type of action to perform.
        :param int timeout: (optional) The time in seconds as an integer to perform
               the mitigation action. Must be the same or greater than the period. This
               field is valid only when mode is "simulate" or "ban".
        :param RatelimitInputActionResponse response: (optional) Custom
               content-type and body to return, this overrides the custom error for the
               zone. This field is not required. Omission will result in default HTML
               error page.This field is valid only when mode is "simulate" or "ban".
        """
        self.mode = mode
        self.timeout = timeout
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputAction':
        """Initialize a RatelimitInputAction object from a json dictionary."""
        args = {}
        if (mode := _dict.get('mode')) is not None:
            args['mode'] = mode
        else:
            raise ValueError('Required property \'mode\' not present in RatelimitInputAction JSON')
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
        if (response := _dict.get('response')) is not None:
            args['response'] = RatelimitInputActionResponse.from_dict(response)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        The type of action to perform.
        """

        SIMULATE = 'simulate'
        BAN = 'ban'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'



class RatelimitInputActionResponse:
    """
    Custom content-type and body to return, this overrides the custom error for the zone.
    This field is not required. Omission will result in default HTML error page.This field
    is valid only when mode is "simulate" or "ban".

    :param str content_type: (optional) The content type of the body.
    :param str body: (optional) The body to return, the content here should conform
          to the content_type.
    """

    def __init__(
        self,
        *,
        content_type: Optional[str] = None,
        body: Optional[str] = None,
    ) -> None:
        """
        Initialize a RatelimitInputActionResponse object.

        :param str content_type: (optional) The content type of the body.
        :param str body: (optional) The body to return, the content here should
               conform to the content_type.
        """
        self.content_type = content_type
        self.body = body

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputActionResponse':
        """Initialize a RatelimitInputActionResponse object from a json dictionary."""
        args = {}
        if (content_type := _dict.get('content_type')) is not None:
            args['content_type'] = content_type
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputActionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputActionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputActionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputActionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ContentTypeEnum(str, Enum):
        """
        The content type of the body.
        """

        TEXT_PLAIN = 'text/plain'
        TEXT_XML = 'text/xml'
        APPLICATION_JSON = 'application/json'



class RatelimitInputBypassItem:
    """
    RatelimitInputBypassItem.

    :param str name: Rate limit name.
    :param str value: The url to bypass.
    """

    def __init__(
        self,
        name: str,
        value: str,
    ) -> None:
        """
        Initialize a RatelimitInputBypassItem object.

        :param str name: Rate limit name.
        :param str value: The url to bypass.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputBypassItem':
        """Initialize a RatelimitInputBypassItem object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in RatelimitInputBypassItem JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in RatelimitInputBypassItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputBypassItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputBypassItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputBypassItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputBypassItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        Rate limit name.
        """

        URL = 'url'



class RatelimitInputCorrelate:
    """
    Enable NAT based rate limits.

    :param str by: NAT rate limits by.
    """

    def __init__(
        self,
        by: str,
    ) -> None:
        """
        Initialize a RatelimitInputCorrelate object.

        :param str by: NAT rate limits by.
        """
        self.by = by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputCorrelate':
        """Initialize a RatelimitInputCorrelate object from a json dictionary."""
        args = {}
        if (by := _dict.get('by')) is not None:
            args['by'] = by
        else:
            raise ValueError('Required property \'by\' not present in RatelimitInputCorrelate JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputCorrelate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'by') and self.by is not None:
            _dict['by'] = self.by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputCorrelate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputCorrelate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputCorrelate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ByEnum(str, Enum):
        """
        NAT rate limits by.
        """

        NAT = 'nat'



class RatelimitInputMatch:
    """
    Determines which traffic the rate limit counts towards the threshold. Needs to be one
    of "request" or "response" objects.

    :param RatelimitInputMatchRequest request: (optional) request.
    :param RatelimitInputMatchResponse response: (optional) response.
    """

    def __init__(
        self,
        *,
        request: Optional['RatelimitInputMatchRequest'] = None,
        response: Optional['RatelimitInputMatchResponse'] = None,
    ) -> None:
        """
        Initialize a RatelimitInputMatch object.

        :param RatelimitInputMatchRequest request: (optional) request.
        :param RatelimitInputMatchResponse response: (optional) response.
        """
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatch':
        """Initialize a RatelimitInputMatch object from a json dictionary."""
        args = {}
        if (request := _dict.get('request')) is not None:
            args['request'] = RatelimitInputMatchRequest.from_dict(request)
        if (response := _dict.get('response')) is not None:
            args['response'] = RatelimitInputMatchResponse.from_dict(response)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request') and self.request is not None:
            if isinstance(self.request, dict):
                _dict['request'] = self.request
            else:
                _dict['request'] = self.request.to_dict()
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitInputMatchRequest:
    """
    request.

    :param List[str] methods: (optional) A subset of the list HTTP methods, or
          ["_ALL_"] for selecting all methods.
    :param List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
          selecting all schemes.
    :param str url: The URL pattern to match comprised of the host and path, i.e.
          example.org/path. Wildcard are expanded to match applicable traffic, query
          strings are not matched. Use * for all traffic to your zone.
    """

    def __init__(
        self,
        url: str,
        *,
        methods: Optional[List[str]] = None,
        schemes: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a RatelimitInputMatchRequest object.

        :param str url: The URL pattern to match comprised of the host and path,
               i.e. example.org/path. Wildcard are expanded to match applicable traffic,
               query strings are not matched. Use * for all traffic to your zone.
        :param List[str] methods: (optional) A subset of the list HTTP methods, or
               ["_ALL_"] for selecting all methods.
        :param List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
               selecting all schemes.
        """
        self.methods = methods
        self.schemes = schemes
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatchRequest':
        """Initialize a RatelimitInputMatchRequest object from a json dictionary."""
        args = {}
        if (methods := _dict.get('methods')) is not None:
            args['methods'] = methods
        if (schemes := _dict.get('schemes')) is not None:
            args['schemes'] = schemes
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in RatelimitInputMatchRequest JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatchRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'methods') and self.methods is not None:
            _dict['methods'] = self.methods
        if hasattr(self, 'schemes') and self.schemes is not None:
            _dict['schemes'] = self.schemes
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatchRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatchRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatchRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodsEnum(str, Enum):
        """
        methods.
        """

        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        DELETE = 'DELETE'
        PATCH = 'PATCH'
        HEAD = 'HEAD'
        ALL = '_ALL_'


    class SchemesEnum(str, Enum):
        """
        schemes.
        """

        HTTP = 'HTTP'
        HTTPS = 'HTTPS'
        ALL = '_ALL_'



class RatelimitInputMatchResponse:
    """
    response.

    :param List[int] status: (optional) HTTP Status codes, can be one [403], many
          [401,403] or indicate all by not providing this value. This field is not
          required.
    :param List[RatelimitInputMatchResponseHeadersItem] headers_: (optional) Array
          of response headers to match. If a response does not meet the header criteria
          then the request will not be counted towards the rate limit.
    :param bool origin_traffic: (optional) Deprecated, please use response headers
          instead and also provide "origin_traffic:false" to avoid legacy behaviour
          interacting with the response.headers property.
    """

    def __init__(
        self,
        *,
        status: Optional[List[int]] = None,
        headers_: Optional[List['RatelimitInputMatchResponseHeadersItem']] = None,
        origin_traffic: Optional[bool] = None,
    ) -> None:
        """
        Initialize a RatelimitInputMatchResponse object.

        :param List[int] status: (optional) HTTP Status codes, can be one [403],
               many [401,403] or indicate all by not providing this value. This field is
               not required.
        :param List[RatelimitInputMatchResponseHeadersItem] headers_: (optional)
               Array of response headers to match. If a response does not meet the header
               criteria then the request will not be counted towards the rate limit.
        :param bool origin_traffic: (optional) Deprecated, please use response
               headers instead and also provide "origin_traffic:false" to avoid legacy
               behaviour interacting with the response.headers property.
        """
        self.status = status
        self.headers_ = headers_
        self.origin_traffic = origin_traffic

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatchResponse':
        """Initialize a RatelimitInputMatchResponse object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (headers_ := _dict.get('headers')) is not None:
            args['headers_'] = [RatelimitInputMatchResponseHeadersItem.from_dict(v) for v in headers_]
        if (origin_traffic := _dict.get('origin_traffic')) is not None:
            args['origin_traffic'] = origin_traffic
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatchResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'headers_') and self.headers_ is not None:
            headers_list = []
            for v in self.headers_:
                if isinstance(v, dict):
                    headers_list.append(v)
                else:
                    headers_list.append(v.to_dict())
            _dict['headers'] = headers_list
        if hasattr(self, 'origin_traffic') and self.origin_traffic is not None:
            _dict['origin_traffic'] = self.origin_traffic
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatchResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatchResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatchResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitInputMatchResponseHeadersItem:
    """
    RatelimitInputMatchResponseHeadersItem.

    :param str name: The name of the response header to match.
    :param str op: The operator when matchin, eq means equals, ne means not equals.
    :param str value: The value of the header, which will be exactly matched.
    """

    def __init__(
        self,
        name: str,
        op: str,
        value: str,
    ) -> None:
        """
        Initialize a RatelimitInputMatchResponseHeadersItem object.

        :param str name: The name of the response header to match.
        :param str op: The operator when matchin, eq means equals, ne means not
               equals.
        :param str value: The value of the header, which will be exactly matched.
        """
        self.name = name
        self.op = op
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatchResponseHeadersItem':
        """Initialize a RatelimitInputMatchResponseHeadersItem object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in RatelimitInputMatchResponseHeadersItem JSON')
        if (op := _dict.get('op')) is not None:
            args['op'] = op
        else:
            raise ValueError('Required property \'op\' not present in RatelimitInputMatchResponseHeadersItem JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in RatelimitInputMatchResponseHeadersItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatchResponseHeadersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'op') and self.op is not None:
            _dict['op'] = self.op
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatchResponseHeadersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OpEnum(str, Enum):
        """
        The operator when matchin, eq means equals, ne means not equals.
        """

        EQ = 'eq'
        NE = 'ne'


    class ValueEnum(str, Enum):
        """
        The value of the header, which will be exactly matched.
        """

        HIT = 'HIT'



class RatelimitObjectAction:
    """
    action.

    :param str mode: The type of action to perform.
    :param int timeout: (optional) The time in seconds as an integer to perform the
          mitigation action. Must be the same or greater than the period. This field is
          valid only when mode is "simulate" or "ban".
    :param RatelimitObjectActionResponse response: (optional) Custom content-type
          and body to return, this overrides the custom error for the zone. This field is
          not required. Omission will result in default HTML error page.This field is
          valid only when mode is "simulate" or "ban".
    """

    def __init__(
        self,
        mode: str,
        *,
        timeout: Optional[int] = None,
        response: Optional['RatelimitObjectActionResponse'] = None,
    ) -> None:
        """
        Initialize a RatelimitObjectAction object.

        :param str mode: The type of action to perform.
        :param int timeout: (optional) The time in seconds as an integer to perform
               the mitigation action. Must be the same or greater than the period. This
               field is valid only when mode is "simulate" or "ban".
        :param RatelimitObjectActionResponse response: (optional) Custom
               content-type and body to return, this overrides the custom error for the
               zone. This field is not required. Omission will result in default HTML
               error page.This field is valid only when mode is "simulate" or "ban".
        """
        self.mode = mode
        self.timeout = timeout
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectAction':
        """Initialize a RatelimitObjectAction object from a json dictionary."""
        args = {}
        if (mode := _dict.get('mode')) is not None:
            args['mode'] = mode
        else:
            raise ValueError('Required property \'mode\' not present in RatelimitObjectAction JSON')
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
        if (response := _dict.get('response')) is not None:
            args['response'] = RatelimitObjectActionResponse.from_dict(response)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        The type of action to perform.
        """

        SIMULATE = 'simulate'
        BAN = 'ban'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'



class RatelimitObjectActionResponse:
    """
    Custom content-type and body to return, this overrides the custom error for the zone.
    This field is not required. Omission will result in default HTML error page.This field
    is valid only when mode is "simulate" or "ban".

    :param str content_type: The content type of the body.
    :param str body: The body to return, the content here should conform to the
          content_type.
    """

    def __init__(
        self,
        content_type: str,
        body: str,
    ) -> None:
        """
        Initialize a RatelimitObjectActionResponse object.

        :param str content_type: The content type of the body.
        :param str body: The body to return, the content here should conform to the
               content_type.
        """
        self.content_type = content_type
        self.body = body

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectActionResponse':
        """Initialize a RatelimitObjectActionResponse object from a json dictionary."""
        args = {}
        if (content_type := _dict.get('content_type')) is not None:
            args['content_type'] = content_type
        else:
            raise ValueError('Required property \'content_type\' not present in RatelimitObjectActionResponse JSON')
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        else:
            raise ValueError('Required property \'body\' not present in RatelimitObjectActionResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectActionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectActionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectActionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectActionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ContentTypeEnum(str, Enum):
        """
        The content type of the body.
        """

        TEXT_PLAIN = 'text/plain'
        TEXT_XML = 'text/xml'
        APPLICATION_JSON = 'application/json'



class RatelimitObjectBypassItem:
    """
    RatelimitObjectBypassItem.

    :param str name: rate limit name.
    :param str value: The url to bypass.
    """

    def __init__(
        self,
        name: str,
        value: str,
    ) -> None:
        """
        Initialize a RatelimitObjectBypassItem object.

        :param str name: rate limit name.
        :param str value: The url to bypass.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectBypassItem':
        """Initialize a RatelimitObjectBypassItem object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in RatelimitObjectBypassItem JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in RatelimitObjectBypassItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectBypassItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectBypassItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectBypassItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectBypassItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        rate limit name.
        """

        URL = 'url'



class RatelimitObjectCorrelate:
    """
    Enable NAT based rate limits.

    :param str by: rate limit enabled by.
    """

    def __init__(
        self,
        by: str,
    ) -> None:
        """
        Initialize a RatelimitObjectCorrelate object.

        :param str by: rate limit enabled by.
        """
        self.by = by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectCorrelate':
        """Initialize a RatelimitObjectCorrelate object from a json dictionary."""
        args = {}
        if (by := _dict.get('by')) is not None:
            args['by'] = by
        else:
            raise ValueError('Required property \'by\' not present in RatelimitObjectCorrelate JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectCorrelate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'by') and self.by is not None:
            _dict['by'] = self.by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectCorrelate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectCorrelate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectCorrelate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ByEnum(str, Enum):
        """
        rate limit enabled by.
        """

        NAT = 'nat'



class RatelimitObjectMatch:
    """
    Determines which traffic the rate limit counts towards the threshold. Needs to be one
    of "request" or "response" objects.

    :param RatelimitObjectMatchRequest request: (optional) request.
    :param RatelimitObjectMatchResponse response: (optional) response.
    """

    def __init__(
        self,
        *,
        request: Optional['RatelimitObjectMatchRequest'] = None,
        response: Optional['RatelimitObjectMatchResponse'] = None,
    ) -> None:
        """
        Initialize a RatelimitObjectMatch object.

        :param RatelimitObjectMatchRequest request: (optional) request.
        :param RatelimitObjectMatchResponse response: (optional) response.
        """
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatch':
        """Initialize a RatelimitObjectMatch object from a json dictionary."""
        args = {}
        if (request := _dict.get('request')) is not None:
            args['request'] = RatelimitObjectMatchRequest.from_dict(request)
        if (response := _dict.get('response')) is not None:
            args['response'] = RatelimitObjectMatchResponse.from_dict(response)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request') and self.request is not None:
            if isinstance(self.request, dict):
                _dict['request'] = self.request
            else:
                _dict['request'] = self.request.to_dict()
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitObjectMatchRequest:
    """
    request.

    :param List[str] methods: (optional) A subset of the list HTTP methods, or
          ["_ALL_"] for selecting all methods.
    :param List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
          selecting all schemes.
    :param str url: The URL pattern to match comprised of the host and path, i.e.
          example.org/path. Wildcard are expanded to match applicable traffic, query
          strings are not matched. Use * for all traffic to your zone.
    """

    def __init__(
        self,
        url: str,
        *,
        methods: Optional[List[str]] = None,
        schemes: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a RatelimitObjectMatchRequest object.

        :param str url: The URL pattern to match comprised of the host and path,
               i.e. example.org/path. Wildcard are expanded to match applicable traffic,
               query strings are not matched. Use * for all traffic to your zone.
        :param List[str] methods: (optional) A subset of the list HTTP methods, or
               ["_ALL_"] for selecting all methods.
        :param List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
               selecting all schemes.
        """
        self.methods = methods
        self.schemes = schemes
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatchRequest':
        """Initialize a RatelimitObjectMatchRequest object from a json dictionary."""
        args = {}
        if (methods := _dict.get('methods')) is not None:
            args['methods'] = methods
        if (schemes := _dict.get('schemes')) is not None:
            args['schemes'] = schemes
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in RatelimitObjectMatchRequest JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatchRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'methods') and self.methods is not None:
            _dict['methods'] = self.methods
        if hasattr(self, 'schemes') and self.schemes is not None:
            _dict['schemes'] = self.schemes
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatchRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatchRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatchRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodsEnum(str, Enum):
        """
        methods.
        """

        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        DELETE = 'DELETE'
        PATCH = 'PATCH'
        HEAD = 'HEAD'
        ALL = '_ALL_'


    class SchemesEnum(str, Enum):
        """
        schemes.
        """

        HTTP = 'HTTP'
        HTTPS = 'HTTPS'
        ALL = '_ALL_'



class RatelimitObjectMatchResponse:
    """
    response.

    :param List[int] status: (optional) HTTP Status codes, can be one [403], many
          [401,403] or indicate all by not providing this value. This field is not
          required.
    :param List[RatelimitObjectMatchResponseHeadersItem] headers_: (optional) Array
          of response headers to match. If a response does not meet the header criteria
          then the request will not be counted towards the rate limit.
    :param bool origin_traffic: (optional) Deprecated, please use response headers
          instead and also provide "origin_traffic:false" to avoid legacy behaviour
          interacting with the response.headers property.
    """

    def __init__(
        self,
        *,
        status: Optional[List[int]] = None,
        headers_: Optional[List['RatelimitObjectMatchResponseHeadersItem']] = None,
        origin_traffic: Optional[bool] = None,
    ) -> None:
        """
        Initialize a RatelimitObjectMatchResponse object.

        :param List[int] status: (optional) HTTP Status codes, can be one [403],
               many [401,403] or indicate all by not providing this value. This field is
               not required.
        :param List[RatelimitObjectMatchResponseHeadersItem] headers_: (optional)
               Array of response headers to match. If a response does not meet the header
               criteria then the request will not be counted towards the rate limit.
        :param bool origin_traffic: (optional) Deprecated, please use response
               headers instead and also provide "origin_traffic:false" to avoid legacy
               behaviour interacting with the response.headers property.
        """
        self.status = status
        self.headers_ = headers_
        self.origin_traffic = origin_traffic

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatchResponse':
        """Initialize a RatelimitObjectMatchResponse object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (headers_ := _dict.get('headers')) is not None:
            args['headers_'] = [RatelimitObjectMatchResponseHeadersItem.from_dict(v) for v in headers_]
        if (origin_traffic := _dict.get('origin_traffic')) is not None:
            args['origin_traffic'] = origin_traffic
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatchResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'headers_') and self.headers_ is not None:
            headers_list = []
            for v in self.headers_:
                if isinstance(v, dict):
                    headers_list.append(v)
                else:
                    headers_list.append(v.to_dict())
            _dict['headers'] = headers_list
        if hasattr(self, 'origin_traffic') and self.origin_traffic is not None:
            _dict['origin_traffic'] = self.origin_traffic
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatchResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatchResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatchResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitObjectMatchResponseHeadersItem:
    """
    RatelimitObjectMatchResponseHeadersItem.

    :param str name: The name of the response header to match.
    :param str op: The operator when matchin, eq means equals, ne means not equals.
    :param str value: The value of the header, which will be exactly matched.
    """

    def __init__(
        self,
        name: str,
        op: str,
        value: str,
    ) -> None:
        """
        Initialize a RatelimitObjectMatchResponseHeadersItem object.

        :param str name: The name of the response header to match.
        :param str op: The operator when matchin, eq means equals, ne means not
               equals.
        :param str value: The value of the header, which will be exactly matched.
        """
        self.name = name
        self.op = op
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatchResponseHeadersItem':
        """Initialize a RatelimitObjectMatchResponseHeadersItem object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in RatelimitObjectMatchResponseHeadersItem JSON')
        if (op := _dict.get('op')) is not None:
            args['op'] = op
        else:
            raise ValueError('Required property \'op\' not present in RatelimitObjectMatchResponseHeadersItem JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in RatelimitObjectMatchResponseHeadersItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatchResponseHeadersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'op') and self.op is not None:
            _dict['op'] = self.op
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatchResponseHeadersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OpEnum(str, Enum):
        """
        The operator when matchin, eq means equals, ne means not equals.
        """

        EQ = 'eq'
        NE = 'ne'


    class ValueEnum(str, Enum):
        """
        The value of the header, which will be exactly matched.
        """

        HIT = 'HIT'



class DeleteRateLimitResp:
    """
    rate limit delete response.

    :param bool success: Operation success flag.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param DeleteRateLimitRespResult result: Container for response information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'DeleteRateLimitRespResult',
    ) -> None:
        """
        Initialize a DeleteRateLimitResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param DeleteRateLimitRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteRateLimitResp':
        """Initialize a DeleteRateLimitResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DeleteRateLimitResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DeleteRateLimitResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DeleteRateLimitResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = DeleteRateLimitRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in DeleteRateLimitResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteRateLimitResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteRateLimitResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteRateLimitResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteRateLimitResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListRatelimitResp:
    """
    rate limit list response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[RatelimitObject] result: Container for response information.
    :param ListRatelimitRespResultInfo result_info: Statistics of results.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['RatelimitObject'],
        result_info: 'ListRatelimitRespResultInfo',
    ) -> None:
        """
        Initialize a ListRatelimitResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[RatelimitObject] result: Container for response information.
        :param ListRatelimitRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRatelimitResp':
        """Initialize a ListRatelimitResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListRatelimitResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListRatelimitResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListRatelimitResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [RatelimitObject.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ListRatelimitResp JSON')
        if (result_info := _dict.get('result_info')) is not None:
            args['result_info'] = ListRatelimitRespResultInfo.from_dict(result_info)
        else:
            raise ValueError('Required property \'result_info\' not present in ListRatelimitResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRatelimitResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        if hasattr(self, 'result_info') and self.result_info is not None:
            if isinstance(self.result_info, dict):
                _dict['result_info'] = self.result_info
            else:
                _dict['result_info'] = self.result_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListRatelimitResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRatelimitResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRatelimitResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitAnalyticsResp:
    """
    Rate limit analytics.

    :param datetime since: The beginning time of analytics.
    :param datetime until: The end time of analytics.
    :param int time_delta: The time interval of analytics' record.
    :param bool golden_record: Whether the analytics' record is golden record.
    :param dict labels: Labels.
    :param List[RatelimitAnalyticsRespTimeseriesItem] timeseries: The analytics'
          records in the time frame.
    """

    def __init__(
        self,
        since: datetime,
        until: datetime,
        time_delta: int,
        golden_record: bool,
        labels: dict,
        timeseries: List['RatelimitAnalyticsRespTimeseriesItem'],
    ) -> None:
        """
        Initialize a RatelimitAnalyticsResp object.

        :param datetime since: The beginning time of analytics.
        :param datetime until: The end time of analytics.
        :param int time_delta: The time interval of analytics' record.
        :param bool golden_record: Whether the analytics' record is golden record.
        :param dict labels: Labels.
        :param List[RatelimitAnalyticsRespTimeseriesItem] timeseries: The
               analytics' records in the time frame.
        """
        self.since = since
        self.until = until
        self.time_delta = time_delta
        self.golden_record = golden_record
        self.labels = labels
        self.timeseries = timeseries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitAnalyticsResp':
        """Initialize a RatelimitAnalyticsResp object from a json dictionary."""
        args = {}
        if (since := _dict.get('since')) is not None:
            args['since'] = string_to_datetime(since)
        else:
            raise ValueError('Required property \'since\' not present in RatelimitAnalyticsResp JSON')
        if (until := _dict.get('until')) is not None:
            args['until'] = string_to_datetime(until)
        else:
            raise ValueError('Required property \'until\' not present in RatelimitAnalyticsResp JSON')
        if (time_delta := _dict.get('time_delta')) is not None:
            args['time_delta'] = time_delta
        else:
            raise ValueError('Required property \'time_delta\' not present in RatelimitAnalyticsResp JSON')
        if (golden_record := _dict.get('golden_record')) is not None:
            args['golden_record'] = golden_record
        else:
            raise ValueError('Required property \'golden_record\' not present in RatelimitAnalyticsResp JSON')
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
        else:
            raise ValueError('Required property \'labels\' not present in RatelimitAnalyticsResp JSON')
        if (timeseries := _dict.get('timeseries')) is not None:
            args['timeseries'] = [RatelimitAnalyticsRespTimeseriesItem.from_dict(v) for v in timeseries]
        else:
            raise ValueError('Required property \'timeseries\' not present in RatelimitAnalyticsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitAnalyticsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'since') and self.since is not None:
            _dict['since'] = datetime_to_string(self.since)
        if hasattr(self, 'until') and self.until is not None:
            _dict['until'] = datetime_to_string(self.until)
        if hasattr(self, 'time_delta') and self.time_delta is not None:
            _dict['time_delta'] = self.time_delta
        if hasattr(self, 'golden_record') and self.golden_record is not None:
            _dict['golden_record'] = self.golden_record
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'timeseries') and self.timeseries is not None:
            timeseries_list = []
            for v in self.timeseries:
                if isinstance(v, dict):
                    timeseries_list.append(v)
                else:
                    timeseries_list.append(v.to_dict())
            _dict['timeseries'] = timeseries_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitAnalyticsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitAnalyticsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitAnalyticsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitObject:
    """
    rate limit object.

    :param str id: Identifier of the rate limit.
    :param bool disabled: Whether this ratelimit is currently disabled.
    :param str description: A note that you can use to describe the reason for a
          rate limit.
    :param List[RatelimitObjectBypassItem] bypass: Criteria that would allow the
          rate limit to be bypassed, for example to express that you shouldn't apply a
          rate limit to a given set of URLs.
    :param int threshold: The threshold that triggers the rate limit mitigations,
          combine with period. i.e. threshold per period.
    :param int period: The time in seconds to count matching traffic. If the count
          exceeds threshold within this period the action will be performed.
    :param RatelimitObjectCorrelate correlate: (optional) Enable NAT based rate
          limits.
    :param RatelimitObjectAction action: action.
    :param RatelimitObjectMatch match: Determines which traffic the rate limit
          counts towards the threshold. Needs to be one of "request" or "response"
          objects.
    """

    def __init__(
        self,
        id: str,
        disabled: bool,
        description: str,
        bypass: List['RatelimitObjectBypassItem'],
        threshold: int,
        period: int,
        action: 'RatelimitObjectAction',
        match: 'RatelimitObjectMatch',
        *,
        correlate: Optional['RatelimitObjectCorrelate'] = None,
    ) -> None:
        """
        Initialize a RatelimitObject object.

        :param str id: Identifier of the rate limit.
        :param bool disabled: Whether this ratelimit is currently disabled.
        :param str description: A note that you can use to describe the reason for
               a rate limit.
        :param List[RatelimitObjectBypassItem] bypass: Criteria that would allow
               the rate limit to be bypassed, for example to express that you shouldn't
               apply a rate limit to a given set of URLs.
        :param int threshold: The threshold that triggers the rate limit
               mitigations, combine with period. i.e. threshold per period.
        :param int period: The time in seconds to count matching traffic. If the
               count exceeds threshold within this period the action will be performed.
        :param RatelimitObjectAction action: action.
        :param RatelimitObjectMatch match: Determines which traffic the rate limit
               counts towards the threshold. Needs to be one of "request" or "response"
               objects.
        :param RatelimitObjectCorrelate correlate: (optional) Enable NAT based rate
               limits.
        """
        self.id = id
        self.disabled = disabled
        self.description = description
        self.bypass = bypass
        self.threshold = threshold
        self.period = period
        self.correlate = correlate
        self.action = action
        self.match = match

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObject':
        """Initialize a RatelimitObject object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in RatelimitObject JSON')
        if (disabled := _dict.get('disabled')) is not None:
            args['disabled'] = disabled
        else:
            raise ValueError('Required property \'disabled\' not present in RatelimitObject JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in RatelimitObject JSON')
        if (bypass := _dict.get('bypass')) is not None:
            args['bypass'] = [RatelimitObjectBypassItem.from_dict(v) for v in bypass]
        else:
            raise ValueError('Required property \'bypass\' not present in RatelimitObject JSON')
        if (threshold := _dict.get('threshold')) is not None:
            args['threshold'] = threshold
        else:
            raise ValueError('Required property \'threshold\' not present in RatelimitObject JSON')
        if (period := _dict.get('period')) is not None:
            args['period'] = period
        else:
            raise ValueError('Required property \'period\' not present in RatelimitObject JSON')
        if (correlate := _dict.get('correlate')) is not None:
            args['correlate'] = RatelimitObjectCorrelate.from_dict(correlate)
        if (action := _dict.get('action')) is not None:
            args['action'] = RatelimitObjectAction.from_dict(action)
        else:
            raise ValueError('Required property \'action\' not present in RatelimitObject JSON')
        if (match := _dict.get('match')) is not None:
            args['match'] = RatelimitObjectMatch.from_dict(match)
        else:
            raise ValueError('Required property \'match\' not present in RatelimitObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'bypass') and self.bypass is not None:
            bypass_list = []
            for v in self.bypass:
                if isinstance(v, dict):
                    bypass_list.append(v)
                else:
                    bypass_list.append(v.to_dict())
            _dict['bypass'] = bypass_list
        if hasattr(self, 'threshold') and self.threshold is not None:
            _dict['threshold'] = self.threshold
        if hasattr(self, 'period') and self.period is not None:
            _dict['period'] = self.period
        if hasattr(self, 'correlate') and self.correlate is not None:
            if isinstance(self.correlate, dict):
                _dict['correlate'] = self.correlate
            else:
                _dict['correlate'] = self.correlate.to_dict()
        if hasattr(self, 'action') and self.action is not None:
            if isinstance(self.action, dict):
                _dict['action'] = self.action
            else:
                _dict['action'] = self.action.to_dict()
        if hasattr(self, 'match') and self.match is not None:
            if isinstance(self.match, dict):
                _dict['match'] = self.match
            else:
                _dict['match'] = self.match.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RatelimitResp:
    """
    rate limit response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param RatelimitObject result: rate limit object.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'RatelimitObject',
    ) -> None:
        """
        Initialize a RatelimitResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param RatelimitObject result: rate limit object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitResp':
        """Initialize a RatelimitResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in RatelimitResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in RatelimitResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in RatelimitResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = RatelimitObject.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in RatelimitResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
