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
Bot Management

API Version: 1.0.1
"""

from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class BotManagementV1(BaseService):
    """The Bot Management V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'bot_management'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'BotManagementV1':
        """
        Return a new client for the Bot Management service using the specified
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
        Construct a new client for the Bot Management service.

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
    # botManagementSettings
    #########################

    def get_bot_management(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Bot management setting.

        Get Bot management setting for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BotMgtResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_bot_management',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/bot_management'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_bot_management(
        self,
        *,
        fight_mode: Optional[bool] = None,
        session_score: Optional[bool] = None,
        enable_js: Optional[bool] = None,
        auth_id_logging: Optional[bool] = None,
        use_latest_model: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update Bot management setting.

        Update Bot management setting for given zone.

        :param bool fight_mode: (optional)
        :param bool session_score: (optional)
        :param bool enable_js: (optional)
        :param bool auth_id_logging: (optional)
        :param bool use_latest_model: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BotMgtResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_bot_management',
        )
        headers.update(sdk_headers)

        data = {
            'fight_mode': fight_mode,
            'session_score': session_score,
            'enable_js': enable_js,
            'auth_id_logging': auth_id_logging,
            'use_latest_model': use_latest_model,
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
        url = '/v1/{crn}/zones/{zone_identifier}/bot_management'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class BotMgtRespResult:
    """
    Container for response information.

    :param bool fight_mode: (optional)
    :param bool session_score: (optional)
    :param bool enable_js: (optional)
    :param bool auth_id_logging: (optional)
    :param bool use_latest_model: (optional)
    """

    def __init__(
        self,
        *,
        fight_mode: Optional[bool] = None,
        session_score: Optional[bool] = None,
        enable_js: Optional[bool] = None,
        auth_id_logging: Optional[bool] = None,
        use_latest_model: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BotMgtRespResult object.

        :param bool fight_mode: (optional)
        :param bool session_score: (optional)
        :param bool enable_js: (optional)
        :param bool auth_id_logging: (optional)
        :param bool use_latest_model: (optional)
        """
        self.fight_mode = fight_mode
        self.session_score = session_score
        self.enable_js = enable_js
        self.auth_id_logging = auth_id_logging
        self.use_latest_model = use_latest_model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotMgtRespResult':
        """Initialize a BotMgtRespResult object from a json dictionary."""
        args = {}
        if (fight_mode := _dict.get('fight_mode')) is not None:
            args['fight_mode'] = fight_mode
        if (session_score := _dict.get('session_score')) is not None:
            args['session_score'] = session_score
        if (enable_js := _dict.get('enable_js')) is not None:
            args['enable_js'] = enable_js
        if (auth_id_logging := _dict.get('auth_id_logging')) is not None:
            args['auth_id_logging'] = auth_id_logging
        if (use_latest_model := _dict.get('use_latest_model')) is not None:
            args['use_latest_model'] = use_latest_model
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotMgtRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fight_mode') and self.fight_mode is not None:
            _dict['fight_mode'] = self.fight_mode
        if hasattr(self, 'session_score') and self.session_score is not None:
            _dict['session_score'] = self.session_score
        if hasattr(self, 'enable_js') and self.enable_js is not None:
            _dict['enable_js'] = self.enable_js
        if hasattr(self, 'auth_id_logging') and self.auth_id_logging is not None:
            _dict['auth_id_logging'] = self.auth_id_logging
        if hasattr(self, 'use_latest_model') and self.use_latest_model is not None:
            _dict['use_latest_model'] = self.use_latest_model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BotMgtRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotMgtRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotMgtRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BotMgtResp:
    """
    Bot Management Response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Array of errors encountered.
    :param List[List[str]] messages: Array of messages returned.
    :param BotMgtRespResult result: Container for response information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'BotMgtRespResult',
    ) -> None:
        """
        Initialize a BotMgtResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param BotMgtRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BotMgtResp':
        """Initialize a BotMgtResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in BotMgtResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in BotMgtResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in BotMgtResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = BotMgtRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in BotMgtResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BotMgtResp object from a json dictionary."""
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
        """Return a `str` version of this BotMgtResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BotMgtResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BotMgtResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
