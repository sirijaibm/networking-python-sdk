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
Routing

API Version: 1.0.1
"""

from datetime import datetime
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class RoutingV1(BaseService):
    """The Routing V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'routing'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'RoutingV1':
        """
        Return a new client for the Routing service using the specified parameters
               and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier.
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
        Construct a new client for the Routing service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier.

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
    # Routing
    #########################

    def get_smart_routing(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Routing feature smart routing setting.

        Get Routing feature smart routing setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SmartRoutingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_smart_routing',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/routing/smart_routing'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_smart_routing(
        self,
        *,
        value: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update Routing feature smart route setting.

        Update Routing feature smart route setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SmartRoutingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_smart_routing',
        )
        headers.update(sdk_headers)

        data = {
            'value': value,
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
        url = '/v1/{crn}/zones/{zone_identifier}/routing/smart_routing'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_routing_tiered_caching(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get routing tiered cache setting.

        Get routing tiered cache setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoutingTieredCachingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_routing_tiered_caching',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/routing/tiered_caching'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_routing_tiered_caching(
        self,
        *,
        value: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update routing tiered cache setting.

        Update routing tiered cache setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoutingTieredCachingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_routing_tiered_caching',
        )
        headers.update(sdk_headers)

        data = {
            'value': value,
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
        url = '/v1/{crn}/zones/{zone_identifier}/routing/tiered_caching'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_routing_latency(
        self,
        *,
        bins: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Routing Latency Analytics.

        Get Routing Latency Analytics for a given zone.

        :param int bins: (optional) the number of bins.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoutingLatencyResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_routing_latency',
        )
        headers.update(sdk_headers)

        params = {
            'bins': bins,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/routing/latency'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_routing_latency_colos(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Routing Latency Colos Analytics.

        Get Routing Latency Colos Analytics for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RoutingLatencyColosResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_routing_latency_colos',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/routing/latency/colos'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class RoutingLatencyColosRespResult:
    """
    Container for response information.

    :param str type: type.
    :param List[RoutingLatencyColosRespResultFeaturesItem] features: features.
    """

    def __init__(
        self,
        type: str,
        features: List['RoutingLatencyColosRespResultFeaturesItem'],
    ) -> None:
        """
        Initialize a RoutingLatencyColosRespResult object.

        :param str type: type.
        :param List[RoutingLatencyColosRespResultFeaturesItem] features: features.
        """
        self.type = type
        self.features = features

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyColosRespResult':
        """Initialize a RoutingLatencyColosRespResult object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in RoutingLatencyColosRespResult JSON')
        if (features := _dict.get('features')) is not None:
            args['features'] = [RoutingLatencyColosRespResultFeaturesItem.from_dict(v) for v in features]
        else:
            raise ValueError('Required property \'features\' not present in RoutingLatencyColosRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyColosRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'features') and self.features is not None:
            features_list = []
            for v in self.features:
                if isinstance(v, dict):
                    features_list.append(v)
                else:
                    features_list.append(v.to_dict())
            _dict['features'] = features_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyColosRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyColosRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyColosRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyColosRespResultFeaturesItem:
    """
    RoutingLatencyColosRespResultFeaturesItem.

    :param str code: (optional) code.
    :param int smart_routing_req_count: (optional) routing request count.
    :param float pct_avg_change: (optional) pct avg change.
    :param float no_smart_routing_avg: (optional) no smart routing avg.
    :param float smart_routing_avg: (optional) no smart routing avg.
    :param RoutingLatencyColosRespResultFeaturesItemGeometry geometry: (optional)
          geometry.
    """

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        smart_routing_req_count: Optional[int] = None,
        pct_avg_change: Optional[float] = None,
        no_smart_routing_avg: Optional[float] = None,
        smart_routing_avg: Optional[float] = None,
        geometry: Optional['RoutingLatencyColosRespResultFeaturesItemGeometry'] = None,
    ) -> None:
        """
        Initialize a RoutingLatencyColosRespResultFeaturesItem object.

        :param str code: (optional) code.
        :param int smart_routing_req_count: (optional) routing request count.
        :param float pct_avg_change: (optional) pct avg change.
        :param float no_smart_routing_avg: (optional) no smart routing avg.
        :param float smart_routing_avg: (optional) no smart routing avg.
        :param RoutingLatencyColosRespResultFeaturesItemGeometry geometry:
               (optional) geometry.
        """
        self.code = code
        self.smart_routing_req_count = smart_routing_req_count
        self.pct_avg_change = pct_avg_change
        self.no_smart_routing_avg = no_smart_routing_avg
        self.smart_routing_avg = smart_routing_avg
        self.geometry = geometry

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyColosRespResultFeaturesItem':
        """Initialize a RoutingLatencyColosRespResultFeaturesItem object from a json dictionary."""
        args = {}
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        if (smart_routing_req_count := _dict.get('smart_routing_req_count')) is not None:
            args['smart_routing_req_count'] = smart_routing_req_count
        if (pct_avg_change := _dict.get('pct_avg_change')) is not None:
            args['pct_avg_change'] = pct_avg_change
        if (no_smart_routing_avg := _dict.get('no_smart_routing_avg')) is not None:
            args['no_smart_routing_avg'] = no_smart_routing_avg
        if (smart_routing_avg := _dict.get('smart_routing_avg')) is not None:
            args['smart_routing_avg'] = smart_routing_avg
        if (geometry := _dict.get('geometry')) is not None:
            args['geometry'] = RoutingLatencyColosRespResultFeaturesItemGeometry.from_dict(geometry)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyColosRespResultFeaturesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'smart_routing_req_count') and self.smart_routing_req_count is not None:
            _dict['smart_routing_req_count'] = self.smart_routing_req_count
        if hasattr(self, 'pct_avg_change') and self.pct_avg_change is not None:
            _dict['pct_avg_change'] = self.pct_avg_change
        if hasattr(self, 'no_smart_routing_avg') and self.no_smart_routing_avg is not None:
            _dict['no_smart_routing_avg'] = self.no_smart_routing_avg
        if hasattr(self, 'smart_routing_avg') and self.smart_routing_avg is not None:
            _dict['smart_routing_avg'] = self.smart_routing_avg
        if hasattr(self, 'geometry') and self.geometry is not None:
            if isinstance(self.geometry, dict):
                _dict['geometry'] = self.geometry
            else:
                _dict['geometry'] = self.geometry.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyColosRespResultFeaturesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyColosRespResultFeaturesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyColosRespResultFeaturesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyColosRespResultFeaturesItemGeometry:
    """
    geometry.

    :param List[float] coordinates: (optional) coordinates.
    :param str type: (optional) type.
    """

    def __init__(
        self,
        *,
        coordinates: Optional[List[float]] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a RoutingLatencyColosRespResultFeaturesItemGeometry object.

        :param List[float] coordinates: (optional) coordinates.
        :param str type: (optional) type.
        """
        self.coordinates = coordinates
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyColosRespResultFeaturesItemGeometry':
        """Initialize a RoutingLatencyColosRespResultFeaturesItemGeometry object from a json dictionary."""
        args = {}
        if (coordinates := _dict.get('coordinates')) is not None:
            args['coordinates'] = coordinates
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyColosRespResultFeaturesItemGeometry object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'coordinates') and self.coordinates is not None:
            _dict['coordinates'] = self.coordinates
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyColosRespResultFeaturesItemGeometry object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyColosRespResultFeaturesItemGeometry') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyColosRespResultFeaturesItemGeometry') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyRespResult:
    """
    Container for response information.

    :param float percent_smart_routed: percent smart routed.
    :param int bins: the number of bin.
    :param RoutingLatencyRespResultRange range: range.
    :param RoutingLatencyRespResultTimeRange time_range: time range.
    :param RoutingLatencyRespResultData data: date.
    """

    def __init__(
        self,
        percent_smart_routed: float,
        bins: int,
        range: 'RoutingLatencyRespResultRange',
        time_range: 'RoutingLatencyRespResultTimeRange',
        data: 'RoutingLatencyRespResultData',
    ) -> None:
        """
        Initialize a RoutingLatencyRespResult object.

        :param float percent_smart_routed: percent smart routed.
        :param int bins: the number of bin.
        :param RoutingLatencyRespResultRange range: range.
        :param RoutingLatencyRespResultTimeRange time_range: time range.
        :param RoutingLatencyRespResultData data: date.
        """
        self.percent_smart_routed = percent_smart_routed
        self.bins = bins
        self.range = range
        self.time_range = time_range
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyRespResult':
        """Initialize a RoutingLatencyRespResult object from a json dictionary."""
        args = {}
        if (percent_smart_routed := _dict.get('percent_smart_routed')) is not None:
            args['percent_smart_routed'] = percent_smart_routed
        else:
            raise ValueError('Required property \'percent_smart_routed\' not present in RoutingLatencyRespResult JSON')
        if (bins := _dict.get('bins')) is not None:
            args['bins'] = bins
        else:
            raise ValueError('Required property \'bins\' not present in RoutingLatencyRespResult JSON')
        if (range := _dict.get('range')) is not None:
            args['range'] = RoutingLatencyRespResultRange.from_dict(range)
        else:
            raise ValueError('Required property \'range\' not present in RoutingLatencyRespResult JSON')
        if (time_range := _dict.get('time_range')) is not None:
            args['time_range'] = RoutingLatencyRespResultTimeRange.from_dict(time_range)
        else:
            raise ValueError('Required property \'time_range\' not present in RoutingLatencyRespResult JSON')
        if (data := _dict.get('data')) is not None:
            args['data'] = RoutingLatencyRespResultData.from_dict(data)
        else:
            raise ValueError('Required property \'data\' not present in RoutingLatencyRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'percent_smart_routed') and self.percent_smart_routed is not None:
            _dict['percent_smart_routed'] = self.percent_smart_routed
        if hasattr(self, 'bins') and self.bins is not None:
            _dict['bins'] = self.bins
        if hasattr(self, 'range') and self.range is not None:
            if isinstance(self.range, dict):
                _dict['range'] = self.range
            else:
                _dict['range'] = self.range.to_dict()
        if hasattr(self, 'time_range') and self.time_range is not None:
            if isinstance(self.time_range, dict):
                _dict['time_range'] = self.time_range
            else:
                _dict['time_range'] = self.time_range.to_dict()
        if hasattr(self, 'data') and self.data is not None:
            if isinstance(self.data, dict):
                _dict['data'] = self.data
            else:
                _dict['data'] = self.data.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyRespResultData:
    """
    date.

    :param List[str] lable: (optional) lable.
    :param List[int] counts: (optional) counts.
    :param List[int] averages: (optional) averages.
    """

    def __init__(
        self,
        *,
        lable: Optional[List[str]] = None,
        counts: Optional[List[int]] = None,
        averages: Optional[List[int]] = None,
    ) -> None:
        """
        Initialize a RoutingLatencyRespResultData object.

        :param List[str] lable: (optional) lable.
        :param List[int] counts: (optional) counts.
        :param List[int] averages: (optional) averages.
        """
        self.lable = lable
        self.counts = counts
        self.averages = averages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyRespResultData':
        """Initialize a RoutingLatencyRespResultData object from a json dictionary."""
        args = {}
        if (lable := _dict.get('lable')) is not None:
            args['lable'] = lable
        if (counts := _dict.get('counts')) is not None:
            args['counts'] = counts
        if (averages := _dict.get('averages')) is not None:
            args['averages'] = averages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyRespResultData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'lable') and self.lable is not None:
            _dict['lable'] = self.lable
        if hasattr(self, 'counts') and self.counts is not None:
            _dict['counts'] = self.counts
        if hasattr(self, 'averages') and self.averages is not None:
            _dict['averages'] = self.averages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyRespResultData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyRespResultData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyRespResultData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyRespResultRange:
    """
    range.

    :param int min: (optional) min time.
    :param int max: (optional) max time.
    """

    def __init__(
        self,
        *,
        min: Optional[int] = None,
        max: Optional[int] = None,
    ) -> None:
        """
        Initialize a RoutingLatencyRespResultRange object.

        :param int min: (optional) min time.
        :param int max: (optional) max time.
        """
        self.min = min
        self.max = max

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyRespResultRange':
        """Initialize a RoutingLatencyRespResultRange object from a json dictionary."""
        args = {}
        if (min := _dict.get('min')) is not None:
            args['min'] = min
        if (max := _dict.get('max')) is not None:
            args['max'] = max
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyRespResultRange object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'min') and self.min is not None:
            _dict['min'] = self.min
        if hasattr(self, 'max') and self.max is not None:
            _dict['max'] = self.max
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyRespResultRange object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyRespResultRange') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyRespResultRange') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyRespResultTimeRange:
    """
    time range.

    :param datetime min: (optional) min time.
    :param datetime max: (optional) max time.
    """

    def __init__(
        self,
        *,
        min: Optional[datetime] = None,
        max: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a RoutingLatencyRespResultTimeRange object.

        :param datetime min: (optional) min time.
        :param datetime max: (optional) max time.
        """
        self.min = min
        self.max = max

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyRespResultTimeRange':
        """Initialize a RoutingLatencyRespResultTimeRange object from a json dictionary."""
        args = {}
        if (min := _dict.get('min')) is not None:
            args['min'] = string_to_datetime(min)
        if (max := _dict.get('max')) is not None:
            args['max'] = string_to_datetime(max)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyRespResultTimeRange object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'min') and self.min is not None:
            _dict['min'] = datetime_to_string(self.min)
        if hasattr(self, 'max') and self.max is not None:
            _dict['max'] = datetime_to_string(self.max)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyRespResultTimeRange object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyRespResultTimeRange') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyRespResultTimeRange') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingTieredCachingRespResult:
    """
    Container for response information.

    :param str id: ID.
    :param str value: Value.
    :param bool editable: Editable.
    :param datetime modified_on: Modified date.
    """

    def __init__(
        self,
        id: str,
        value: str,
        editable: bool,
        modified_on: datetime,
    ) -> None:
        """
        Initialize a RoutingTieredCachingRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingTieredCachingRespResult':
        """Initialize a RoutingTieredCachingRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in RoutingTieredCachingRespResult JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in RoutingTieredCachingRespResult JSON')
        if (editable := _dict.get('editable')) is not None:
            args['editable'] = editable
        else:
            raise ValueError('Required property \'editable\' not present in RoutingTieredCachingRespResult JSON')
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = string_to_datetime(modified_on)
        else:
            raise ValueError('Required property \'modified_on\' not present in RoutingTieredCachingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingTieredCachingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingTieredCachingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingTieredCachingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingTieredCachingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SmartRoutingRespResult:
    """
    Container for response information.

    :param str id: ID.
    :param str value: Value.
    :param bool editable: Editable.
    :param datetime modified_on: Modified date.
    """

    def __init__(
        self,
        id: str,
        value: str,
        editable: bool,
        modified_on: datetime,
    ) -> None:
        """
        Initialize a SmartRoutingRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SmartRoutingRespResult':
        """Initialize a SmartRoutingRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in SmartRoutingRespResult JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in SmartRoutingRespResult JSON')
        if (editable := _dict.get('editable')) is not None:
            args['editable'] = editable
        else:
            raise ValueError('Required property \'editable\' not present in SmartRoutingRespResult JSON')
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = string_to_datetime(modified_on)
        else:
            raise ValueError('Required property \'modified_on\' not present in SmartRoutingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SmartRoutingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SmartRoutingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SmartRoutingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SmartRoutingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyColosResp:
    """
    routing latency colos response.

    :param RoutingLatencyColosRespResult result: Container for response information.
    :param bool success: Was the get successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    """

    def __init__(
        self,
        result: 'RoutingLatencyColosRespResult',
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
    ) -> None:
        """
        Initialize a RoutingLatencyColosResp object.

        :param RoutingLatencyColosRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyColosResp':
        """Initialize a RoutingLatencyColosResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = RoutingLatencyColosRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in RoutingLatencyColosResp JSON')
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in RoutingLatencyColosResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in RoutingLatencyColosResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in RoutingLatencyColosResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyColosResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyColosResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyColosResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyColosResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingLatencyResp:
    """
    routing latency response.

    :param RoutingLatencyRespResult result: Container for response information.
    :param bool success: Was the get successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    """

    def __init__(
        self,
        result: 'RoutingLatencyRespResult',
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
    ) -> None:
        """
        Initialize a RoutingLatencyResp object.

        :param RoutingLatencyRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingLatencyResp':
        """Initialize a RoutingLatencyResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = RoutingLatencyRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in RoutingLatencyResp JSON')
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in RoutingLatencyResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in RoutingLatencyResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in RoutingLatencyResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingLatencyResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingLatencyResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingLatencyResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingLatencyResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoutingTieredCachingResp:
    """
    tiered routing cache response.

    :param RoutingTieredCachingRespResult result: Container for response
          information.
    :param bool success: Was the get successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    """

    def __init__(
        self,
        result: 'RoutingTieredCachingRespResult',
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
    ) -> None:
        """
        Initialize a RoutingTieredCachingResp object.

        :param RoutingTieredCachingRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoutingTieredCachingResp':
        """Initialize a RoutingTieredCachingResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = RoutingTieredCachingRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in RoutingTieredCachingResp JSON')
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in RoutingTieredCachingResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in RoutingTieredCachingResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in RoutingTieredCachingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoutingTieredCachingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoutingTieredCachingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoutingTieredCachingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoutingTieredCachingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SmartRoutingResp:
    """
    smart routing response.

    :param SmartRoutingRespResult result: Container for response information.
    :param bool success: Was the get successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    """

    def __init__(
        self,
        result: 'SmartRoutingRespResult',
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
    ) -> None:
        """
        Initialize a SmartRoutingResp object.

        :param SmartRoutingRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SmartRoutingResp':
        """Initialize a SmartRoutingResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = SmartRoutingRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in SmartRoutingResp JSON')
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in SmartRoutingResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in SmartRoutingResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in SmartRoutingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SmartRoutingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SmartRoutingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SmartRoutingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SmartRoutingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
