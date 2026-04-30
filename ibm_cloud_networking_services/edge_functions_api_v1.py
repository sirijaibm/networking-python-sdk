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
Edge Functions

API Version: 1.0.0
"""

from datetime import datetime
from typing import Dict, List, Optional, TextIO, Union
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class EdgeFunctionsApiV1(BaseService):
    """The Edge Functions API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'edge_functions_api'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'EdgeFunctionsApiV1':
        """
        Return a new client for the Edge Functions API service using the specified
               parameters and external configuration.

        :param str crn: cloud resource name.

        :param str zone_identifier: zone identifier.
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
        Construct a new client for the Edge Functions API service.

        :param str crn: cloud resource name.

        :param str zone_identifier: zone identifier.

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
    # Edge Functions Actions
    #########################

    def list_edge_functions_actions(
        self,
        *,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all edge functions scripts for a given instance.

        Get all edge functions scripts for a given instance.

        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListEdgeFunctionsActionsResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_edge_functions_actions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/workers/scripts'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_edge_functions_action(
        self,
        script_name: str,
        *,
        edge_functions_action: Optional[Union[str, TextIO]] = None,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Upload or replace an edge functions action for a given instance.

        Upload or replace an exitsing edge functions action for a given instance.

        :param str script_name: the edge function action name.
        :param str edge_functions_action: (optional) upload or replace an edge
               functions action.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetEdgeFunctionsActionResp` object
        """

        if not script_name:
            raise ValueError('script_name must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_edge_functions_action',
        )
        headers.update(sdk_headers)

        data = edge_functions_action
        headers['content-type'] = 'application/javascript'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'script_name']
        path_param_values = self.encode_path_vars(self.crn, script_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/workers/scripts/{script_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_edge_functions_action(
        self,
        script_name: str,
        *,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Download a edge functions action for a given instance.

        Fetch raw script content for your worker. Note this is the original script
        content, not JSON encoded.

        :param str script_name: the edge function action name.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not script_name:
            raise ValueError('script_name must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_edge_functions_action',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/javascript'

        path_param_keys = ['crn', 'script_name']
        path_param_values = self.encode_path_vars(self.crn, script_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/workers/scripts/{script_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_edge_functions_action(
        self,
        script_name: str,
        *,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a edge functions action for a given instance.

        Delete an edge functions action for a given instance.

        :param str script_name: the edge function action name.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteEdgeFunctionsActionResp` object
        """

        if not script_name:
            raise ValueError('script_name must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_edge_functions_action',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'script_name']
        path_param_values = self.encode_path_vars(self.crn, script_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/workers/scripts/{script_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Edge Functions Triggers
    #########################

    def create_edge_functions_trigger(
        self,
        *,
        pattern: Optional[str] = None,
        script: Optional[str] = None,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an edge functions trigger on a given zone.

        Create an edge functions trigger on a given zone.

        :param str pattern: (optional) a string pattern.
        :param str script: (optional) Name of the script to apply when the route is
               matched. The route is skipped when this is blank/missing.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateEdgeFunctionsTriggerResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_edge_functions_trigger',
        )
        headers.update(sdk_headers)

        data = {
            'pattern': pattern,
            'script': script,
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
        url = '/v1/{crn}/zones/{zone_identifier}/workers/routes'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_edge_functions_triggers(
        self,
        *,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all edge functions triggers on a given zone.

        List all edge functions triggers on a given zone.

        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListEdgeFunctionsTriggersResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_edge_functions_triggers',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/workers/routes'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_edge_functions_trigger(
        self,
        route_id: str,
        *,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an edge functions trigger on a given zone.

        Get an edge functions trigger on a given zone.

        :param str route_id: trigger identifier.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetEdgeFunctionsTriggerResp` object
        """

        if not route_id:
            raise ValueError('route_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_edge_functions_trigger',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'route_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, route_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/workers/routes/{route_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_edge_functions_trigger(
        self,
        route_id: str,
        *,
        pattern: Optional[str] = None,
        script: Optional[str] = None,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an edge functions trigger on a given zone.

        Update an edge functions trigger on a given zone.

        :param str route_id: trigger identifier.
        :param str pattern: (optional) a string pattern.
        :param str script: (optional) Name of the script to apply when the route is
               matched. The route is skipped when this is blank/missing.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetEdgeFunctionsTriggerResp` object
        """

        if not route_id:
            raise ValueError('route_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_edge_functions_trigger',
        )
        headers.update(sdk_headers)

        data = {
            'pattern': pattern,
            'script': script,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'route_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, route_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/workers/routes/{route_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_edge_functions_trigger(
        self,
        route_id: str,
        *,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an edge functions trigger on a given zone.

        Delete an edge functions trigger on a given zone.

        :param str route_id: trigger identifier.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateEdgeFunctionsTriggerResp` object
        """

        if not route_id:
            raise ValueError('route_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_edge_functions_trigger',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'route_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, route_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/workers/routes/{route_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class CreateEdgeFunctionsTriggerResp:
    """
    create an edge funtions trigger response.

    :param EdgeFunctionsTriggerId result: (optional) edge function trigger id.
    :param bool success: (optional) success.
    :param List[str] errors: (optional) An array with errors.
    :param List[str] messages: (optional) An array with messages.
    """

    def __init__(
        self,
        *,
        result: Optional['EdgeFunctionsTriggerId'] = None,
        success: Optional[bool] = None,
        errors: Optional[List[str]] = None,
        messages: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a CreateEdgeFunctionsTriggerResp object.

        :param EdgeFunctionsTriggerId result: (optional) edge function trigger id.
        :param bool success: (optional) success.
        :param List[str] errors: (optional) An array with errors.
        :param List[str] messages: (optional) An array with messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateEdgeFunctionsTriggerResp':
        """Initialize a CreateEdgeFunctionsTriggerResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = EdgeFunctionsTriggerId.from_dict(result)
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateEdgeFunctionsTriggerResp object from a json dictionary."""
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
        """Return a `str` version of this CreateEdgeFunctionsTriggerResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateEdgeFunctionsTriggerResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateEdgeFunctionsTriggerResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteEdgeFunctionsActionResp:
    """
    create an edge funtions trigger response.

    :param EdgeFunctionsActionId result: (optional) edge function action id.
    :param bool success: (optional) success.
    :param List[str] errors: (optional) An array with errors.
    :param List[str] messages: (optional) An array with messages.
    """

    def __init__(
        self,
        *,
        result: Optional['EdgeFunctionsActionId'] = None,
        success: Optional[bool] = None,
        errors: Optional[List[str]] = None,
        messages: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a DeleteEdgeFunctionsActionResp object.

        :param EdgeFunctionsActionId result: (optional) edge function action id.
        :param bool success: (optional) success.
        :param List[str] errors: (optional) An array with errors.
        :param List[str] messages: (optional) An array with messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteEdgeFunctionsActionResp':
        """Initialize a DeleteEdgeFunctionsActionResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = EdgeFunctionsActionId.from_dict(result)
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteEdgeFunctionsActionResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteEdgeFunctionsActionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteEdgeFunctionsActionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteEdgeFunctionsActionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EdgeFunctionsActionId:
    """
    edge function action id.

    :param str id: (optional) edge functions action identifier tag.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a EdgeFunctionsActionId object.

        :param str id: (optional) edge functions action identifier tag.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EdgeFunctionsActionId':
        """Initialize a EdgeFunctionsActionId object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EdgeFunctionsActionId object from a json dictionary."""
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
        """Return a `str` version of this EdgeFunctionsActionId object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EdgeFunctionsActionId') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EdgeFunctionsActionId') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EdgeFunctionsActionResp:
    """
    edge function script.

    :param str script: (optional) Raw script content, as a string.
    :param str etag: (optional) Hashed script content, can be used in a
          If-None-Match header when updating.
    :param List[str] handlers: (optional) handlers.
    :param datetime modified_on: (optional) The time when the script was last
          modified.
    :param datetime created_on: (optional) The time when the script was last
          created.
    :param List[EdgeFunctionsTriggerResp] routes: (optional) An array with items in
          the list response.
    """

    def __init__(
        self,
        *,
        script: Optional[str] = None,
        etag: Optional[str] = None,
        handlers: Optional[List[str]] = None,
        modified_on: Optional[datetime] = None,
        created_on: Optional[datetime] = None,
        routes: Optional[List['EdgeFunctionsTriggerResp']] = None,
    ) -> None:
        """
        Initialize a EdgeFunctionsActionResp object.

        :param str script: (optional) Raw script content, as a string.
        :param str etag: (optional) Hashed script content, can be used in a
               If-None-Match header when updating.
        :param List[str] handlers: (optional) handlers.
        :param datetime modified_on: (optional) The time when the script was last
               modified.
        :param datetime created_on: (optional) The time when the script was last
               created.
        :param List[EdgeFunctionsTriggerResp] routes: (optional) An array with
               items in the list response.
        """
        self.script = script
        self.etag = etag
        self.handlers = handlers
        self.modified_on = modified_on
        self.created_on = created_on
        self.routes = routes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EdgeFunctionsActionResp':
        """Initialize a EdgeFunctionsActionResp object from a json dictionary."""
        args = {}
        if (script := _dict.get('script')) is not None:
            args['script'] = script
        if (etag := _dict.get('etag')) is not None:
            args['etag'] = etag
        if (handlers := _dict.get('handlers')) is not None:
            args['handlers'] = handlers
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = string_to_datetime(modified_on)
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (routes := _dict.get('routes')) is not None:
            args['routes'] = [EdgeFunctionsTriggerResp.from_dict(v) for v in routes]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EdgeFunctionsActionResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'script') and self.script is not None:
            _dict['script'] = self.script
        if hasattr(self, 'etag') and self.etag is not None:
            _dict['etag'] = self.etag
        if hasattr(self, 'handlers') and self.handlers is not None:
            _dict['handlers'] = self.handlers
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'routes') and self.routes is not None:
            routes_list = []
            for v in self.routes:
                if isinstance(v, dict):
                    routes_list.append(v)
                else:
                    routes_list.append(v.to_dict())
            _dict['routes'] = routes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EdgeFunctionsActionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EdgeFunctionsActionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EdgeFunctionsActionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EdgeFunctionsTriggerId:
    """
    edge function trigger id.

    :param str id: (optional) edge functions trigger identifier tag.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a EdgeFunctionsTriggerId object.

        :param str id: (optional) edge functions trigger identifier tag.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EdgeFunctionsTriggerId':
        """Initialize a EdgeFunctionsTriggerId object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EdgeFunctionsTriggerId object from a json dictionary."""
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
        """Return a `str` version of this EdgeFunctionsTriggerId object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EdgeFunctionsTriggerId') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EdgeFunctionsTriggerId') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EdgeFunctionsTriggerResp:
    """
    edge function trigger id.

    :param str id: (optional) edge functions trigger identifier tag.
    :param str pattern: (optional) a string pattern.
    :param str script: (optional) Name of the script to apply when the route is
          matched. The route is skipped when this is blank/missing.
    :param bool request_limit_fail_open: (optional) request limit fail open or not.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        pattern: Optional[str] = None,
        script: Optional[str] = None,
        request_limit_fail_open: Optional[bool] = None,
    ) -> None:
        """
        Initialize a EdgeFunctionsTriggerResp object.

        :param str id: (optional) edge functions trigger identifier tag.
        :param str pattern: (optional) a string pattern.
        :param str script: (optional) Name of the script to apply when the route is
               matched. The route is skipped when this is blank/missing.
        :param bool request_limit_fail_open: (optional) request limit fail open or
               not.
        """
        self.id = id
        self.pattern = pattern
        self.script = script
        self.request_limit_fail_open = request_limit_fail_open

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EdgeFunctionsTriggerResp':
        """Initialize a EdgeFunctionsTriggerResp object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (pattern := _dict.get('pattern')) is not None:
            args['pattern'] = pattern
        if (script := _dict.get('script')) is not None:
            args['script'] = script
        if (request_limit_fail_open := _dict.get('request_limit_fail_open')) is not None:
            args['request_limit_fail_open'] = request_limit_fail_open
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EdgeFunctionsTriggerResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'pattern') and self.pattern is not None:
            _dict['pattern'] = self.pattern
        if hasattr(self, 'script') and self.script is not None:
            _dict['script'] = self.script
        if hasattr(self, 'request_limit_fail_open') and self.request_limit_fail_open is not None:
            _dict['request_limit_fail_open'] = self.request_limit_fail_open
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EdgeFunctionsTriggerResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EdgeFunctionsTriggerResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EdgeFunctionsTriggerResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetEdgeFunctionsActionResp:
    """
    edge funtions action response.

    :param EdgeFunctionsActionResp result: (optional) edge function script.
    :param bool success: (optional) success.
    :param List[str] errors: (optional) An array with errors.
    :param List[str] messages: (optional) An array with messages.
    """

    def __init__(
        self,
        *,
        result: Optional['EdgeFunctionsActionResp'] = None,
        success: Optional[bool] = None,
        errors: Optional[List[str]] = None,
        messages: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a GetEdgeFunctionsActionResp object.

        :param EdgeFunctionsActionResp result: (optional) edge function script.
        :param bool success: (optional) success.
        :param List[str] errors: (optional) An array with errors.
        :param List[str] messages: (optional) An array with messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetEdgeFunctionsActionResp':
        """Initialize a GetEdgeFunctionsActionResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = EdgeFunctionsActionResp.from_dict(result)
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetEdgeFunctionsActionResp object from a json dictionary."""
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
        """Return a `str` version of this GetEdgeFunctionsActionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetEdgeFunctionsActionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetEdgeFunctionsActionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetEdgeFunctionsTriggerResp:
    """
    edge funtions trigger response.

    :param EdgeFunctionsTriggerResp result: (optional) edge function trigger id.
    :param bool success: (optional) success.
    :param List[str] errors: (optional) An array with errors.
    :param List[str] messages: (optional) An array with messages.
    """

    def __init__(
        self,
        *,
        result: Optional['EdgeFunctionsTriggerResp'] = None,
        success: Optional[bool] = None,
        errors: Optional[List[str]] = None,
        messages: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a GetEdgeFunctionsTriggerResp object.

        :param EdgeFunctionsTriggerResp result: (optional) edge function trigger
               id.
        :param bool success: (optional) success.
        :param List[str] errors: (optional) An array with errors.
        :param List[str] messages: (optional) An array with messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetEdgeFunctionsTriggerResp':
        """Initialize a GetEdgeFunctionsTriggerResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = EdgeFunctionsTriggerResp.from_dict(result)
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetEdgeFunctionsTriggerResp object from a json dictionary."""
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
        """Return a `str` version of this GetEdgeFunctionsTriggerResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetEdgeFunctionsTriggerResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetEdgeFunctionsTriggerResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListEdgeFunctionsActionsResp:
    """
    edge funtions actions response.

    :param List[EdgeFunctionsActionResp] result: (optional) An array with items in
          the list response.
    :param bool success: (optional) success.
    :param List[str] errors: (optional) An array with errors.
    :param List[str] messages: (optional) An array with messages.
    """

    def __init__(
        self,
        *,
        result: Optional[List['EdgeFunctionsActionResp']] = None,
        success: Optional[bool] = None,
        errors: Optional[List[str]] = None,
        messages: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ListEdgeFunctionsActionsResp object.

        :param List[EdgeFunctionsActionResp] result: (optional) An array with items
               in the list response.
        :param bool success: (optional) success.
        :param List[str] errors: (optional) An array with errors.
        :param List[str] messages: (optional) An array with messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEdgeFunctionsActionsResp':
        """Initialize a ListEdgeFunctionsActionsResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = [EdgeFunctionsActionResp.from_dict(v) for v in result]
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEdgeFunctionsActionsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
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
        """Return a `str` version of this ListEdgeFunctionsActionsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEdgeFunctionsActionsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEdgeFunctionsActionsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListEdgeFunctionsTriggersResp:
    """
    edge funtions triggers response.

    :param List[EdgeFunctionsTriggerResp] result: (optional) An array with items in
          the list response.
    :param bool success: (optional) success.
    :param List[str] errors: (optional) An array with errors.
    :param List[str] messages: (optional) An array with messages.
    """

    def __init__(
        self,
        *,
        result: Optional[List['EdgeFunctionsTriggerResp']] = None,
        success: Optional[bool] = None,
        errors: Optional[List[str]] = None,
        messages: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ListEdgeFunctionsTriggersResp object.

        :param List[EdgeFunctionsTriggerResp] result: (optional) An array with
               items in the list response.
        :param bool success: (optional) success.
        :param List[str] errors: (optional) An array with errors.
        :param List[str] messages: (optional) An array with messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEdgeFunctionsTriggersResp':
        """Initialize a ListEdgeFunctionsTriggersResp object from a json dictionary."""
        args = {}
        if (result := _dict.get('result')) is not None:
            args['result'] = [EdgeFunctionsTriggerResp.from_dict(v) for v in result]
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEdgeFunctionsTriggersResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
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
        """Return a `str` version of this ListEdgeFunctionsTriggersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEdgeFunctionsTriggersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEdgeFunctionsTriggersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
