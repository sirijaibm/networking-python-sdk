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
Bot Analytics

API Version: 1.0.1
"""

from datetime import datetime
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class BotAnalyticsV1(BaseService):
    """The Bot Analytics V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'bot_analytics'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'BotAnalyticsV1':
        """
        Return a new client for the Bot Analytics service using the specified
               parameters and external configuration.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: Zone identifier to identifiy the zone.
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
        Construct a new client for the Bot Analytics service.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: Zone identifier to identifiy the zone.

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
    # botAnalyticsScoreSource
    #########################

    def get_bot_score(
        self,
        since: datetime,
        until: datetime,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Bot Analytics score source.

        Get Bot Analytics score source for a given zone. Use this to identify the most
        common detection engines used to score your traffic.

        :param datetime since: UTC datetime for start of query.
        :param datetime until: UTC datetime for end of query.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BotScoreResp` object
        """

        if since is None:
            raise ValueError('since must be provided')
        if until is None:
            raise ValueError('until must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_bot_score',
        )
        headers.update(sdk_headers)

        params = {
            'since': since,
            'until': until,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/bot_analytics/score_source'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # botAnalyticsTimeseries
    #########################

    def get_bot_timeseries(
        self,
        since: datetime,
        until: datetime,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Bot Analytics timeseries.

        Get Bot Analytics timeseries for a given zone.

        :param datetime since: UTC datetime for start of query.
        :param datetime until: UTC datetime for end of query.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BotTimeseriesResp` object
        """

        if since is None:
            raise ValueError('since must be provided')
        if until is None:
            raise ValueError('until must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_bot_timeseries',
        )
        headers.update(sdk_headers)

        params = {
            'since': since,
            'until': until,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/bot_analytics/timeseries'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # botAnalyticsTopNs
    #########################

    def get_bot_topns(
        self,
        since: datetime,
        until: datetime,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Bot Analytics top attributes.

        Get Bot Analytics top attributes for a given zone. Use this to view more detailed
        information on specific IP addresses and other characteristics.

        :param datetime since: UTC datetime for start of query.
        :param datetime until: UTC datetime for end of query.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BotTopnsResp` object
        """

        if since is None:
            raise ValueError('since must be provided')
        if until is None:
            raise ValueError('until must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_bot_topns',
        )
        headers.update(sdk_headers)

        params = {
            'since': since,
            'until': until,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/bot_analytics/top_ns'.format(**path_param_dict)
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


class BotScoreRespResultItem:
    """
    BotScoreRespResultItem.

    :param List[BotScoreRespResultItemBotScoreItem] bot_score: (optional)
    """

    def __init__(
        self,
        *,
        bot_score: Optional[List['BotScoreRespResultItemBotScoreItem']] = None,
    ) -> None:
        """
        Initialize a BotScoreRespResultItem object.

        :param List[BotScoreRespResultItemBotScoreItem] bot_score: (optional)
        """
        self.bot_score = bot_score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotScoreRespResultItem':
        """Initialize a BotScoreRespResultItem object from a json dictionary."""
        args = {}
        if (bot_score := _dict.get('botScore')) is not None:
            args['bot_score'] = [BotScoreRespResultItemBotScoreItem.from_dict(v) for v in bot_score]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotScoreRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bot_score') and self.bot_score is not None:
            botScore_list = []
            for v in self.bot_score:
                if isinstance(v, dict):
                    botScore_list.append(v)
                else:
                    botScore_list.append(v.to_dict())
            _dict['botScore'] = botScore_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotScoreRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotScoreRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotScoreRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotScoreRespResultItemBotScoreItem:
    """
    BotScoreRespResultItemBotScoreItem.

    :param BotScoreRespResultItemBotScoreItemAvg avg: (optional)
    :param float count: (optional)
    :param BotScoreRespResultItemBotScoreItemDimensions dimensions: (optional)
    """

    def __init__(
        self,
        *,
        avg: Optional['BotScoreRespResultItemBotScoreItemAvg'] = None,
        count: Optional[float] = None,
        dimensions: Optional['BotScoreRespResultItemBotScoreItemDimensions'] = None,
    ) -> None:
        """
        Initialize a BotScoreRespResultItemBotScoreItem object.

        :param BotScoreRespResultItemBotScoreItemAvg avg: (optional)
        :param float count: (optional)
        :param BotScoreRespResultItemBotScoreItemDimensions dimensions: (optional)
        """
        self.avg = avg
        self.count = count
        self.dimensions = dimensions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotScoreRespResultItemBotScoreItem':
        """Initialize a BotScoreRespResultItemBotScoreItem object from a json dictionary."""
        args = {}
        if (avg := _dict.get('avg')) is not None:
            args['avg'] = BotScoreRespResultItemBotScoreItemAvg.from_dict(avg)
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (dimensions := _dict.get('dimensions')) is not None:
            args['dimensions'] = BotScoreRespResultItemBotScoreItemDimensions.from_dict(dimensions)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotScoreRespResultItemBotScoreItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'avg') and self.avg is not None:
            if isinstance(self.avg, dict):
                _dict['avg'] = self.avg
            else:
                _dict['avg'] = self.avg.to_dict()
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'dimensions') and self.dimensions is not None:
            if isinstance(self.dimensions, dict):
                _dict['dimensions'] = self.dimensions
            else:
                _dict['dimensions'] = self.dimensions.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotScoreRespResultItemBotScoreItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotScoreRespResultItemBotScoreItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotScoreRespResultItemBotScoreItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotScoreRespResultItemBotScoreItemAvg:
    """
    BotScoreRespResultItemBotScoreItemAvg.

    :param float sample_interval: (optional)
    """

    def __init__(
        self,
        *,
        sample_interval: Optional[float] = None,
    ) -> None:
        """
        Initialize a BotScoreRespResultItemBotScoreItemAvg object.

        :param float sample_interval: (optional)
        """
        self.sample_interval = sample_interval

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotScoreRespResultItemBotScoreItemAvg':
        """Initialize a BotScoreRespResultItemBotScoreItemAvg object from a json dictionary."""
        args = {}
        if (sample_interval := _dict.get('sampleInterval')) is not None:
            args['sample_interval'] = sample_interval
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotScoreRespResultItemBotScoreItemAvg object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sample_interval') and self.sample_interval is not None:
            _dict['sampleInterval'] = self.sample_interval
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotScoreRespResultItemBotScoreItemAvg object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotScoreRespResultItemBotScoreItemAvg') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotScoreRespResultItemBotScoreItemAvg') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotScoreRespResultItemBotScoreItemDimensions:
    """
    BotScoreRespResultItemBotScoreItemDimensions.

    :param str bot_score_src_name: (optional)
    """

    def __init__(
        self,
        *,
        bot_score_src_name: Optional[str] = None,
    ) -> None:
        """
        Initialize a BotScoreRespResultItemBotScoreItemDimensions object.

        :param str bot_score_src_name: (optional)
        """
        self.bot_score_src_name = bot_score_src_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotScoreRespResultItemBotScoreItemDimensions':
        """Initialize a BotScoreRespResultItemBotScoreItemDimensions object from a json dictionary."""
        args = {}
        if (bot_score_src_name := _dict.get('botScoreSrcName')) is not None:
            args['bot_score_src_name'] = bot_score_src_name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotScoreRespResultItemBotScoreItemDimensions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bot_score_src_name') and self.bot_score_src_name is not None:
            _dict['botScoreSrcName'] = self.bot_score_src_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotScoreRespResultItemBotScoreItemDimensions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotScoreRespResultItemBotScoreItemDimensions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotScoreRespResultItemBotScoreItemDimensions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotTimeseriesRespResultItem:
    """
    BotTimeseriesRespResultItem.

    :param List[dict] bot_score: (optional)
    """

    def __init__(
        self,
        *,
        bot_score: Optional[List[dict]] = None,
    ) -> None:
        """
        Initialize a BotTimeseriesRespResultItem object.

        :param List[dict] bot_score: (optional)
        """
        self.bot_score = bot_score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotTimeseriesRespResultItem':
        """Initialize a BotTimeseriesRespResultItem object from a json dictionary."""
        args = {}
        if (bot_score := _dict.get('botScore')) is not None:
            args['bot_score'] = bot_score
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotTimeseriesRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bot_score') and self.bot_score is not None:
            _dict['botScore'] = self.bot_score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotTimeseriesRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotTimeseriesRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotTimeseriesRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotScoreResp:
    """
    Bot Score Source Response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[BotScoreRespResultItem] result: Container for response information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['BotScoreRespResultItem'],
    ) -> None:
        """
        Initialize a BotScoreResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[BotScoreRespResultItem] result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotScoreResp':
        """Initialize a BotScoreResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in BotScoreResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in BotScoreResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in BotScoreResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [BotScoreRespResultItem.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in BotScoreResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotScoreResp object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotScoreResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotScoreResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotScoreResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotTimeseriesResp:
    """
    Bot Timeseries Response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[BotTimeseriesRespResultItem] result: Container for response
          information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['BotTimeseriesRespResultItem'],
    ) -> None:
        """
        Initialize a BotTimeseriesResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[BotTimeseriesRespResultItem] result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotTimeseriesResp':
        """Initialize a BotTimeseriesResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in BotTimeseriesResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in BotTimeseriesResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in BotTimeseriesResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [BotTimeseriesRespResultItem.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in BotTimeseriesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotTimeseriesResp object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotTimeseriesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotTimeseriesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotTimeseriesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotTopnsResp:
    """
    Bot top attributes response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param List[dict] result: Container for response information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List[dict],
    ) -> None:
        """
        Initialize a BotTopnsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[dict] result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotTopnsResp':
        """Initialize a BotTopnsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in BotTopnsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in BotTopnsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in BotTopnsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = result
        else:
            raise ValueError('Required property \'result\' not present in BotTopnsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotTopnsResp object from a json dictionary."""
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
            _dict['result'] = self.result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotTopnsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotTopnsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotTopnsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
