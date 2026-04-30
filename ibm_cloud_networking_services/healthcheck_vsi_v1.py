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
GLB Health Event API for Healthcheck VSI

API Version: 1.0.0
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


class HealthcheckVsiV1(BaseService):
    """The Healthcheck VSI V1 service."""

    DEFAULT_SERVICE_URL = 'https://admin.dns-svcs.cloud.ibm.com/internal/v1'
    DEFAULT_SERVICE_NAME = 'healthcheck_vsi'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'HealthcheckVsiV1':
        """
        Return a new client for the Healthcheck VSI service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Healthcheck VSI service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Healthcheck VSI
    #########################

    def edit_healtcheck_vsi(
        self,
        vsi_doc_id: str,
        *,
        vsi_id: Optional[str] = None,
        state: Optional[str] = None,
        management_address: Optional[str] = None,
        management_subnet: Optional[str] = None,
        name: Optional[str] = None,
        login_credentials: Optional[str] = None,
        region: Optional[str] = None,
        az: Optional[str] = None,
        customer_networks: Optional[List['CustomNetwork']] = None,
        performance_profile: Optional[str] = None,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Edit Healthcheck VSI.

        Edit healthcheck VSI document in cloudant.

        :param str vsi_doc_id: The healthcheck VSI document ID.
        :param str vsi_id: (optional) RIAS VSI instance ID.
        :param str state: (optional) State of the Healthcheck VSI.
        :param str management_address: (optional) Management address of the
               healthcheck VSI.
        :param str management_subnet: (optional) RIAS subnet ID for the management
               address.
        :param str name: (optional) RIAS VSI name.
        :param str login_credentials: (optional) Login credential.
        :param str region: (optional) VPC region.
        :param str az: (optional) VPC availability zone.
        :param List[CustomNetwork] customer_networks: (optional) List of customer
               networks attached to the Healthcheck VSI.
        :param str performance_profile: (optional) The performance profile name of
               VSI.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HealthcheckVsi` object
        """

        if not vsi_doc_id:
            raise ValueError('vsi_doc_id must be provided')
        if customer_networks is not None:
            customer_networks = [convert_model(x) for x in customer_networks]
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='edit_healtcheck_vsi',
        )
        headers.update(sdk_headers)

        data = {
            'vsi_id': vsi_id,
            'state': state,
            'management_address': management_address,
            'management_subnet': management_subnet,
            'name': name,
            'login_credentials': login_credentials,
            'region': region,
            'az': az,
            'customer_networks': customer_networks,
            'performance_profile': performance_profile,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['vsi_doc_id']
        path_param_values = self.encode_path_vars(vsi_doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/healthcheck/vsi/{vsi_doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Origin Healthcheck Status
    #########################

    def update_origin_status(
        self,
        vsi_doc_id: str,
        origin_doc_id: str,
        *,
        status: Optional[str] = None,
        health_failure_reason: Optional[str] = None,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update healthcheck status of an origin.

        Update healthcheck status of an origin.

        :param str vsi_doc_id: The healthcheck VSI document ID.
        :param str origin_doc_id: Origin document ID.
        :param str status: (optional) healthcheck status.
        :param str health_failure_reason: (optional) healthcheck failure reason
               code (TODO - may add other codes in future), 'SUCCESS' is the only reason
               code applicable to status 'UP'.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HealthcheckOrigin` object
        """

        if not vsi_doc_id:
            raise ValueError('vsi_doc_id must be provided')
        if not origin_doc_id:
            raise ValueError('origin_doc_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_origin_status',
        )
        headers.update(sdk_headers)

        data = {
            'status': status,
            'health_failure_reason': health_failure_reason,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['vsi_doc_id', 'origin_doc_id']
        path_param_values = self.encode_path_vars(vsi_doc_id, origin_doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/healthcheck/vsi/{vsi_doc_id}/origins/{origin_doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Application Status
    #########################

    def update_app_status(
        self,
        vsi_doc_id: str,
        *,
        application: Optional[str] = None,
        health: Optional[bool] = None,
        subnet_crn: Optional[str] = None,
        x_correlation_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update status of an application.

        Update status of an application.

        :param str vsi_doc_id: The healthcheck VSI document ID.
        :param str application: (optional) The type of the application.
        :param bool health: (optional) Whether the application is healthy.
        :param str subnet_crn: (optional) The customer subnet CRN of the VSI that
               the application resides in.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AppStatus` object
        """

        if not vsi_doc_id:
            raise ValueError('vsi_doc_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_app_status',
        )
        headers.update(sdk_headers)

        data = {
            'application': application,
            'health': health,
            'subnet_crn': subnet_crn,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['vsi_doc_id']
        path_param_values = self.encode_path_vars(vsi_doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/healthcheck/vsi/{vsi_doc_id}/application'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AppStatus:
    """
    Application status.

    :param str application: The type of the application.
    :param bool health: Whether the application is healthy.
    :param str subnet_crn: The customer subnet CRN of the VSI that the application
          resides in.
    """

    def __init__(
        self,
        application: str,
        health: bool,
        subnet_crn: str,
    ) -> None:
        """
        Initialize a AppStatus object.

        :param str application: The type of the application.
        :param bool health: Whether the application is healthy.
        :param str subnet_crn: The customer subnet CRN of the VSI that the
               application resides in.
        """
        self.application = application
        self.health = health
        self.subnet_crn = subnet_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppStatus':
        """Initialize a AppStatus object from a json dictionary."""
        args = {}
        if (application := _dict.get('application')) is not None:
            args['application'] = application
        else:
            raise ValueError('Required property \'application\' not present in AppStatus JSON')
        if (health := _dict.get('health')) is not None:
            args['health'] = health
        else:
            raise ValueError('Required property \'health\' not present in AppStatus JSON')
        if (subnet_crn := _dict.get('subnet_crn')) is not None:
            args['subnet_crn'] = subnet_crn
        else:
            raise ValueError('Required property \'subnet_crn\' not present in AppStatus JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application') and self.application is not None:
            _dict['application'] = self.application
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'subnet_crn') and self.subnet_crn is not None:
            _dict['subnet_crn'] = self.subnet_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ApplicationEnum(str, Enum):
        """
        The type of the application.
        """

        CUSTOM_RESOLVER = 'custom-resolver'



class CustomNetwork:
    """
    Customer network attached to a a healthcheck VSI.

    :param str vpc: (optional) The VPC CRN that the customer network resides in.
    :param str id: (optional) RIAS subnet ID of the customer network.
    :param str ipv4_cidr_block: (optional) IPv4 CIDR block allocated to the customer
          network.
    :param str ipv4_address: (optional) The interface address attached to
          healthcheck VSI in the customer network.
    """

    def __init__(
        self,
        *,
        vpc: Optional[str] = None,
        id: Optional[str] = None,
        ipv4_cidr_block: Optional[str] = None,
        ipv4_address: Optional[str] = None,
    ) -> None:
        """
        Initialize a CustomNetwork object.

        :param str vpc: (optional) The VPC CRN that the customer network resides
               in.
        :param str id: (optional) RIAS subnet ID of the customer network.
        :param str ipv4_cidr_block: (optional) IPv4 CIDR block allocated to the
               customer network.
        :param str ipv4_address: (optional) The interface address attached to
               healthcheck VSI in the customer network.
        """
        self.vpc = vpc
        self.id = id
        self.ipv4_cidr_block = ipv4_cidr_block
        self.ipv4_address = ipv4_address

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomNetwork':
        """Initialize a CustomNetwork object from a json dictionary."""
        args = {}
        if (vpc := _dict.get('vpc')) is not None:
            args['vpc'] = vpc
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (ipv4_cidr_block := _dict.get('ipv4_cidr_block')) is not None:
            args['ipv4_cidr_block'] = ipv4_cidr_block
        if (ipv4_address := _dict.get('ipv4_address')) is not None:
            args['ipv4_address'] = ipv4_address
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomNetwork object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'vpc') and self.vpc is not None:
            _dict['vpc'] = self.vpc
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'ipv4_cidr_block') and self.ipv4_cidr_block is not None:
            _dict['ipv4_cidr_block'] = self.ipv4_cidr_block
        if hasattr(self, 'ipv4_address') and self.ipv4_address is not None:
            _dict['ipv4_address'] = self.ipv4_address
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomNetwork object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomNetwork') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomNetwork') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HealthcheckOrigin:
    """
    Origin healthy status.

    :param str status: healthcheck status.
    :param str health_failure_reason: healthcheck failure reason code (TODO - may
          add other codes in future), 'SUCCESS' is the only reason code applicable to
          status 'UP'.
    """

    def __init__(
        self,
        status: str,
        health_failure_reason: str,
    ) -> None:
        """
        Initialize a HealthcheckOrigin object.

        :param str status: healthcheck status.
        :param str health_failure_reason: healthcheck failure reason code (TODO -
               may add other codes in future), 'SUCCESS' is the only reason code
               applicable to status 'UP'.
        """
        self.status = status
        self.health_failure_reason = health_failure_reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthcheckOrigin':
        """Initialize a HealthcheckOrigin object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in HealthcheckOrigin JSON')
        if (health_failure_reason := _dict.get('health_failure_reason')) is not None:
            args['health_failure_reason'] = health_failure_reason
        else:
            raise ValueError('Required property \'health_failure_reason\' not present in HealthcheckOrigin JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthcheckOrigin object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'health_failure_reason') and self.health_failure_reason is not None:
            _dict['health_failure_reason'] = self.health_failure_reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthcheckOrigin object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthcheckOrigin') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthcheckOrigin') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        healthcheck status.
        """

        UP = 'UP'
        DOWN = 'DOWN'


    class HealthFailureReasonEnum(str, Enum):
        """
        healthcheck failure reason code (TODO - may add other codes in future), 'SUCCESS'
        is the only reason code applicable to status 'UP'.
        """

        SUCCESS = 'SUCCESS'
        L3_UNREACHABLE = 'L3_UNREACHABLE'
        TCP_CONNECTION_TIMEOUT = 'TCP_CONNECTION_TIMEOUT'
        TCP_CONNECTION_RESET = 'TCP_CONNECTION_RESET'
        HTTP_RESPONSE_CODE_MISMATCH = 'HTTP_RESPONSE_CODE_MISMATCH'
        HTTP_RESPONSE_BODY_UNEXPECTED = 'HTTP_RESPONSE_BODY_UNEXPECTED'
        HTTP_REDIRECTION_FAILURE = 'HTTP_REDIRECTION_FAILURE'
        HTTP_REQUEST_TIMEOUT = 'HTTP_REQUEST_TIMEOUT'
        HTTPS_INSECURE_SSL = 'HTTPS_INSECURE_SSL'



class HealthcheckVsi:
    """
    Healthcheck VSI details.

    :param str id: (optional) Unique identifier of a healthcheck VSI document in
          cloudant.
    :param datetime created_on: (optional) the time when a DNS zone is created.
    :param datetime modified_on: (optional) the recent time when a DNS zone is
          modified.
    :param str vsi_id: (optional) RIAS VSI instance ID.
    :param str state: (optional) State of the Healthcheck VSI.
    :param str management_address: (optional) Management address of the healthcheck
          VSI.
    :param str management_subnet: (optional) RIAS subnet ID for the management
          address.
    :param str name: (optional) RIAS VSI name.
    :param str login_credentials: (optional) Login credential.
    :param str region: (optional) VPC region.
    :param str az: (optional) VPC availability zone.
    :param List[CustomNetwork] customer_networks: (optional) List of customer
          networks attached to the Healthcheck VSI.
    :param str performance_profile: (optional) The performance profile name of VSI.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        created_on: Optional[datetime] = None,
        modified_on: Optional[datetime] = None,
        vsi_id: Optional[str] = None,
        state: Optional[str] = None,
        management_address: Optional[str] = None,
        management_subnet: Optional[str] = None,
        name: Optional[str] = None,
        login_credentials: Optional[str] = None,
        region: Optional[str] = None,
        az: Optional[str] = None,
        customer_networks: Optional[List['CustomNetwork']] = None,
        performance_profile: Optional[str] = None,
    ) -> None:
        """
        Initialize a HealthcheckVsi object.

        :param str id: (optional) Unique identifier of a healthcheck VSI document
               in cloudant.
        :param datetime created_on: (optional) the time when a DNS zone is created.
        :param datetime modified_on: (optional) the recent time when a DNS zone is
               modified.
        :param str vsi_id: (optional) RIAS VSI instance ID.
        :param str state: (optional) State of the Healthcheck VSI.
        :param str management_address: (optional) Management address of the
               healthcheck VSI.
        :param str management_subnet: (optional) RIAS subnet ID for the management
               address.
        :param str name: (optional) RIAS VSI name.
        :param str login_credentials: (optional) Login credential.
        :param str region: (optional) VPC region.
        :param str az: (optional) VPC availability zone.
        :param List[CustomNetwork] customer_networks: (optional) List of customer
               networks attached to the Healthcheck VSI.
        :param str performance_profile: (optional) The performance profile name of
               VSI.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.vsi_id = vsi_id
        self.state = state
        self.management_address = management_address
        self.management_subnet = management_subnet
        self.name = name
        self.login_credentials = login_credentials
        self.region = region
        self.az = az
        self.customer_networks = customer_networks
        self.performance_profile = performance_profile

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthcheckVsi':
        """Initialize a HealthcheckVsi object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = string_to_datetime(modified_on)
        if (vsi_id := _dict.get('vsi_id')) is not None:
            args['vsi_id'] = vsi_id
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (management_address := _dict.get('management_address')) is not None:
            args['management_address'] = management_address
        if (management_subnet := _dict.get('management_subnet')) is not None:
            args['management_subnet'] = management_subnet
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (login_credentials := _dict.get('login_credentials')) is not None:
            args['login_credentials'] = login_credentials
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (az := _dict.get('az')) is not None:
            args['az'] = az
        if (customer_networks := _dict.get('customer_networks')) is not None:
            args['customer_networks'] = [CustomNetwork.from_dict(v) for v in customer_networks]
        if (performance_profile := _dict.get('performance_profile')) is not None:
            args['performance_profile'] = performance_profile
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthcheckVsi object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        if hasattr(self, 'vsi_id') and self.vsi_id is not None:
            _dict['vsi_id'] = self.vsi_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'management_address') and self.management_address is not None:
            _dict['management_address'] = self.management_address
        if hasattr(self, 'management_subnet') and self.management_subnet is not None:
            _dict['management_subnet'] = self.management_subnet
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'login_credentials') and self.login_credentials is not None:
            _dict['login_credentials'] = self.login_credentials
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'az') and self.az is not None:
            _dict['az'] = self.az
        if hasattr(self, 'customer_networks') and self.customer_networks is not None:
            customer_networks_list = []
            for v in self.customer_networks:
                if isinstance(v, dict):
                    customer_networks_list.append(v)
                else:
                    customer_networks_list.append(v.to_dict())
            _dict['customer_networks'] = customer_networks_list
        if hasattr(self, 'performance_profile') and self.performance_profile is not None:
            _dict['performance_profile'] = self.performance_profile
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthcheckVsi object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthcheckVsi') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthcheckVsi') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Healthcheck VSI.
        """

        UP = 'UP'
        DOWN = 'DOWN'
        PROVISIONING = 'PROVISIONING'
        DEPROVISIONING = 'DEPROVISIONING'
        INIT = 'INIT'
        DELETED = 'DELETED'


    class PerformanceProfileEnum(str, Enum):
        """
        The performance profile name of VSI.
        """

        BX2_2X8 = 'bx2-2x8'
        BX2_8X32 = 'bx2-8x32'
        BX2_16X64 = 'bx2-16x64'

