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
MTLS

API Version: 1.0.0
"""

from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class MtlsV1(BaseService):
    """The MTLS V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'mtls'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'MtlsV1':
        """
        Return a new client for the MTLS service using the specified parameters and
               external configuration.

        :param str crn: Cloud resource name.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        crn: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the MTLS service.

        :param str crn: Cloud resource name.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn

    #########################
    # Mutual TLS
    #########################

    def list_access_certificates(
        self,
        zone_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List access certificates.

        List access certificates.

        :param str zone_id: Zone ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListAccessCertsResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_access_certificates',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_access_certificate(
        self,
        zone_id: str,
        *,
        name: Optional[str] = None,
        certificate: Optional[str] = None,
        associated_hostnames: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create access certificate.

        Create access certificate.

        :param str zone_id: Zone ID.
        :param str name: (optional) Access certificate name.
        :param str certificate: (optional) Access certificate.
        :param List[str] associated_hostnames: (optional) The hostnames that are
               prompted for this certificate.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessCertResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_access_certificate',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'certificate': certificate,
            'associated_hostnames': associated_hostnames,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_access_certificate(
        self,
        zone_id: str,
        cert_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get access certificate.

        Get access certificate.

        :param str zone_id: Zone ID.
        :param str cert_id: Access certificate ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessCertResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not cert_id:
            raise ValueError('cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_access_certificate',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'cert_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, cert_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates/{cert_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_access_certificate(
        self,
        zone_id: str,
        cert_id: str,
        *,
        name: Optional[str] = None,
        associated_hostnames: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update access certificate.

        Update access certificate.

        :param str zone_id: Zone ID.
        :param str cert_id: Access certificate ID.
        :param str name: (optional) Access certificate name.
        :param List[str] associated_hostnames: (optional) The hostnames that are
               prompted for this certificate.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessCertResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not cert_id:
            raise ValueError('cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_access_certificate',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'associated_hostnames': associated_hostnames,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'cert_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, cert_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates/{cert_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_access_certificate(
        self,
        zone_id: str,
        cert_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete access certificate.

        Delete access certificate.

        :param str zone_id: Zone ID.
        :param str cert_id: Access certificate ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteAccessCertResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not cert_id:
            raise ValueError('cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_access_certificate',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'cert_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, cert_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates/{cert_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_access_applications(
        self,
        zone_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List access applications.

        List access applications.

        :param str zone_id: Zone ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListAccessAppsResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_access_applications',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_access_application(
        self,
        zone_id: str,
        *,
        name: Optional[str] = None,
        domain: Optional[str] = None,
        session_duration: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create access application.

        Create access application.

        :param str zone_id: Zone ID.
        :param str name: (optional) Application name.
        :param str domain: (optional) The domain and path that Access blocks.
        :param str session_duration: (optional) The amount of time that the tokens
               issued for this application are valid.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateAccessAppResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_access_application',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'domain': domain,
            'session_duration': session_duration,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_access_application(
        self,
        zone_id: str,
        app_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get access application.

        Get access application.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessAppResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_access_application',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_access_application(
        self,
        zone_id: str,
        app_id: str,
        *,
        name: Optional[str] = None,
        domain: Optional[str] = None,
        session_duration: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update access application.

        Update access application.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param str name: (optional) Application name.
        :param str domain: (optional) The domain and path that Access blocks.
        :param str session_duration: (optional) The amount of time that the tokens
               issued for this application are valid.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessAppResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_access_application',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'domain': domain,
            'session_duration': session_duration,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_access_application(
        self,
        zone_id: str,
        app_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete access application.

        Delete access application.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteAccessAppResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_access_application',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_access_policies(
        self,
        zone_id: str,
        app_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List access policies.

        List access policies.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListAccessPoliciesResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_access_policies',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}/policies'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_access_policy(
        self,
        zone_id: str,
        app_id: str,
        *,
        name: Optional[str] = None,
        decision: Optional[str] = None,
        include: Optional[List['PolicyRule']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create access policy.

        Create access policy.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param str name: (optional) Policy name.
        :param str decision: (optional) Defines the action Access takes if the
               policy matches the user.
        :param List[PolicyRule] include: (optional) The include policy works like
               an OR logical operator. The user must satisfy one of the rules in includes.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessPolicyResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        if include is not None:
            include = [convert_model(x) for x in include]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_access_policy',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'decision': decision,
            'include': include,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}/policies'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_access_policy(
        self,
        zone_id: str,
        app_id: str,
        policy_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get access policy.

        Get access policy.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param str policy_id: Access policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessPolicyResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_access_policy',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id', 'policy_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_access_policy(
        self,
        zone_id: str,
        app_id: str,
        policy_id: str,
        *,
        name: Optional[str] = None,
        decision: Optional[str] = None,
        include: Optional[List['PolicyRule']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update access policy.

        Update access policy.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param str policy_id: Access policy ID.
        :param str name: (optional) Policy name.
        :param str decision: (optional) Defines the action Access takes if the
               policy matches the user.
        :param List[PolicyRule] include: (optional) The include policy works like
               an OR logical operator. The user must satisfy one of the rules in includes.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessPolicyResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        if not policy_id:
            raise ValueError('policy_id must be provided')
        if include is not None:
            include = [convert_model(x) for x in include]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_access_policy',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'decision': decision,
            'include': include,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id', 'policy_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_access_policy(
        self,
        zone_id: str,
        app_id: str,
        policy_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete access policy.

        Delete access policy.

        :param str zone_id: Zone ID.
        :param str app_id: Access application ID.
        :param str policy_id: Access policy ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteAccessPolicyResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if not app_id:
            raise ValueError('app_id must be provided')
        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_access_policy',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id', 'app_id', 'policy_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id, app_id, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/apps/{app_id}/policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_access_cert_settings(
        self,
        zone_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get access certificates settings.

        Get access certificates settings.

        :param str zone_id: Zone ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessCertSettingsResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_access_cert_settings',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates/settings'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_access_cert_settings(
        self,
        zone_id: str,
        *,
        settings: Optional[List['AccessCertSettingsInputArray']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update access certificates settings.

        Update access certificates settings.

        :param str zone_id: Zone ID.
        :param List[AccessCertSettingsInputArray] settings: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessCertSettingsResp` object
        """

        if not zone_id:
            raise ValueError('zone_id must be provided')
        if settings is not None:
            settings = [convert_model(x) for x in settings]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_access_cert_settings',
        )
        headers.update(sdk_headers)

        data = {
            'settings': settings,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_id']
        path_param_values = self.encode_path_vars(self.crn, zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_id}/access/certificates/settings'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_access_organization(
        self,
        *,
        name: Optional[str] = None,
        auth_domain: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create access organization.

        Create access organization.

        :param str name: (optional) Name of the access organization.
        :param str auth_domain: (optional) The domain that you are redirected to on
               Access login attempts.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessOrgResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_access_organization',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'auth_domain': auth_domain,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/access/organizations'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AccessOrgRespResult:
    """
    AccessOrgRespResult.

    :param str auth_domain: (optional)
    :param str name: (optional)
    :param dict login_design: (optional)
    :param str created_at: (optional)
    :param str updated_at: (optional)
    """

    def __init__(
        self,
        *,
        auth_domain: Optional[str] = None,
        name: Optional[str] = None,
        login_design: Optional[dict] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> None:
        """
        Initialize a AccessOrgRespResult object.

        :param str auth_domain: (optional)
        :param str name: (optional)
        :param dict login_design: (optional)
        :param str created_at: (optional)
        :param str updated_at: (optional)
        """
        self.auth_domain = auth_domain
        self.name = name
        self.login_design = login_design
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessOrgRespResult':
        """Initialize a AccessOrgRespResult object from a json dictionary."""
        args = {}
        if (auth_domain := _dict.get('auth_domain')) is not None:
            args['auth_domain'] = auth_domain
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (login_design := _dict.get('login_design')) is not None:
            args['login_design'] = login_design
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = updated_at
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessOrgRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'auth_domain') and self.auth_domain is not None:
            _dict['auth_domain'] = self.auth_domain
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'login_design') and self.login_design is not None:
            _dict['login_design'] = self.login_design
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccessOrgRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessOrgRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessOrgRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateAccessAppRespResult:
    """
    Access application details.

    :param str id: (optional)
    :param str name: (optional)
    :param str domain: (optional)
    :param str aud: (optional)
    :param List[dict] policies: (optional)
    :param List[str] allowed_idps: (optional)
    :param bool auto_redirect_to_identity: (optional)
    :param str session_duration: (optional)
    :param str type: (optional)
    :param str uid: (optional)
    :param str created_at: (optional)
    :param str updated_at: (optional)
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        domain: Optional[str] = None,
        aud: Optional[str] = None,
        policies: Optional[List[dict]] = None,
        allowed_idps: Optional[List[str]] = None,
        auto_redirect_to_identity: Optional[bool] = None,
        session_duration: Optional[str] = None,
        type: Optional[str] = None,
        uid: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateAccessAppRespResult object.

        :param str id: (optional)
        :param str name: (optional)
        :param str domain: (optional)
        :param str aud: (optional)
        :param List[dict] policies: (optional)
        :param List[str] allowed_idps: (optional)
        :param bool auto_redirect_to_identity: (optional)
        :param str session_duration: (optional)
        :param str type: (optional)
        :param str uid: (optional)
        :param str created_at: (optional)
        :param str updated_at: (optional)
        """
        self.id = id
        self.name = name
        self.domain = domain
        self.aud = aud
        self.policies = policies
        self.allowed_idps = allowed_idps
        self.auto_redirect_to_identity = auto_redirect_to_identity
        self.session_duration = session_duration
        self.type = type
        self.uid = uid
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAccessAppRespResult':
        """Initialize a CreateAccessAppRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = domain
        if (aud := _dict.get('aud')) is not None:
            args['aud'] = aud
        if (policies := _dict.get('policies')) is not None:
            args['policies'] = policies
        if (allowed_idps := _dict.get('allowed_idps')) is not None:
            args['allowed_idps'] = allowed_idps
        if (auto_redirect_to_identity := _dict.get('auto_redirect_to_identity')) is not None:
            args['auto_redirect_to_identity'] = auto_redirect_to_identity
        if (session_duration := _dict.get('session_duration')) is not None:
            args['session_duration'] = session_duration
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (uid := _dict.get('uid')) is not None:
            args['uid'] = uid
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = updated_at
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAccessAppRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'domain') and self.domain is not None:
            _dict['domain'] = self.domain
        if hasattr(self, 'aud') and self.aud is not None:
            _dict['aud'] = self.aud
        if hasattr(self, 'policies') and self.policies is not None:
            _dict['policies'] = self.policies
        if hasattr(self, 'allowed_idps') and self.allowed_idps is not None:
            _dict['allowed_idps'] = self.allowed_idps
        if hasattr(self, 'auto_redirect_to_identity') and self.auto_redirect_to_identity is not None:
            _dict['auto_redirect_to_identity'] = self.auto_redirect_to_identity
        if hasattr(self, 'session_duration') and self.session_duration is not None:
            _dict['session_duration'] = self.session_duration
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateAccessAppRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAccessAppRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAccessAppRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAccessAppRespResult:
    """
    DeleteAccessAppRespResult.

    :param str id: (optional) Application ID.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeleteAccessAppRespResult object.

        :param str id: (optional) Application ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccessAppRespResult':
        """Initialize a DeleteAccessAppRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccessAppRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccessAppRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccessAppRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccessAppRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAccessCertRespResult:
    """
    DeleteAccessCertRespResult.

    :param str id: (optional) Certificate ID.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeleteAccessCertRespResult object.

        :param str id: (optional) Certificate ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccessCertRespResult':
        """Initialize a DeleteAccessCertRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccessCertRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccessCertRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccessCertRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccessCertRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAccessPolicyRespResult:
    """
    DeleteAccessPolicyRespResult.

    :param str id: (optional) Policy ID.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeleteAccessPolicyRespResult object.

        :param str id: (optional) Policy ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccessPolicyRespResult':
        """Initialize a DeleteAccessPolicyRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccessPolicyRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccessPolicyRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccessPolicyRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccessPolicyRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyCnRuleCommonName:
    """
    PolicyCnRuleCommonName.

    :param str common_name: Common name of client certificate.
    """

    def __init__(
        self,
        common_name: str,
    ) -> None:
        """
        Initialize a PolicyCnRuleCommonName object.

        :param str common_name: Common name of client certificate.
        """
        self.common_name = common_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyCnRuleCommonName':
        """Initialize a PolicyCnRuleCommonName object from a json dictionary."""
        args = {}
        if (common_name := _dict.get('common_name')) is not None:
            args['common_name'] = common_name
        else:
            raise ValueError('Required property \'common_name\' not present in PolicyCnRuleCommonName JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyCnRuleCommonName object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'common_name') and self.common_name is not None:
            _dict['common_name'] = self.common_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyCnRuleCommonName object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyCnRuleCommonName') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyCnRuleCommonName') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccessAppResp:
    """
    Access application response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param AppResult result: (optional) Access application details.
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['AppResult'] = None,
    ) -> None:
        """
        Initialize a AccessAppResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param AppResult result: (optional) Access application details.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessAppResp':
        """Initialize a AccessAppResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = AppResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessAppResp object from a json dictionary."""
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
        """Return a `str` version of this AccessAppResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessAppResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessAppResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccessCertResp:
    """
    Access certificate response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param CertResult result: (optional) Access certificate details.
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['CertResult'] = None,
    ) -> None:
        """
        Initialize a AccessCertResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param CertResult result: (optional) Access certificate details.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessCertResp':
        """Initialize a AccessCertResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = CertResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessCertResp object from a json dictionary."""
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
        """Return a `str` version of this AccessCertResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessCertResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessCertResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccessCertSettingsInputArray:
    """
    AccessCertSettingsInputArray.

    :param str hostname:
    :param bool client_certificate_forwarding: Whether to forward the client
          certificate.
    """

    def __init__(
        self,
        hostname: str,
        client_certificate_forwarding: bool,
    ) -> None:
        """
        Initialize a AccessCertSettingsInputArray object.

        :param str hostname:
        :param bool client_certificate_forwarding: Whether to forward the client
               certificate.
        """
        self.hostname = hostname
        self.client_certificate_forwarding = client_certificate_forwarding

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessCertSettingsInputArray':
        """Initialize a AccessCertSettingsInputArray object from a json dictionary."""
        args = {}
        if (hostname := _dict.get('hostname')) is not None:
            args['hostname'] = hostname
        else:
            raise ValueError('Required property \'hostname\' not present in AccessCertSettingsInputArray JSON')
        if (client_certificate_forwarding := _dict.get('client_certificate_forwarding')) is not None:
            args['client_certificate_forwarding'] = client_certificate_forwarding
        else:
            raise ValueError('Required property \'client_certificate_forwarding\' not present in AccessCertSettingsInputArray JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessCertSettingsInputArray object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'client_certificate_forwarding') and self.client_certificate_forwarding is not None:
            _dict['client_certificate_forwarding'] = self.client_certificate_forwarding
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccessCertSettingsInputArray object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessCertSettingsInputArray') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessCertSettingsInputArray') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccessCertSettingsResp:
    """
    Access certificates settings response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param List[CertSettingsResult] result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional[List['CertSettingsResult']] = None,
    ) -> None:
        """
        Initialize a AccessCertSettingsResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param List[CertSettingsResult] result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessCertSettingsResp':
        """Initialize a AccessCertSettingsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = [CertSettingsResult.from_dict(v) for v in result]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessCertSettingsResp object from a json dictionary."""
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
        """Return a `str` version of this AccessCertSettingsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessCertSettingsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessCertSettingsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccessOrgResp:
    """
    Access organization response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param AccessOrgRespResult result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['AccessOrgRespResult'] = None,
    ) -> None:
        """
        Initialize a AccessOrgResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param AccessOrgRespResult result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessOrgResp':
        """Initialize a AccessOrgResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = AccessOrgRespResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessOrgResp object from a json dictionary."""
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
        """Return a `str` version of this AccessOrgResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessOrgResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessOrgResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AccessPolicyResp:
    """
    Access policy response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param PolicyResult result: (optional) Access policies information.
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['PolicyResult'] = None,
    ) -> None:
        """
        Initialize a AccessPolicyResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param PolicyResult result: (optional) Access policies information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessPolicyResp':
        """Initialize a AccessPolicyResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = PolicyResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessPolicyResp object from a json dictionary."""
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
        """Return a `str` version of this AccessPolicyResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessPolicyResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessPolicyResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AppResult:
    """
    Access application details.

    :param str id: (optional) Application ID.
    :param str name: (optional) Application name.
    :param str domain: (optional) The domain and path that Access blocks.
    :param str aud: (optional)
    :param List[PolicyResult] policies: (optional) Policies of the application.
    :param List[str] allowed_idps: (optional) The identity providers selected for
          application.
    :param bool auto_redirect_to_identity: (optional) Option to skip identity
          provider selection if only one is configured in allowed_idps.
    :param str session_duration: (optional) The amount of time that the tokens
          issued for this application are valid.
    :param str type: (optional) Application type.
    :param str uid: (optional) UUID, same as ID.
    :param str created_at: (optional) Created time of the application.
    :param str updated_at: (optional) Updated time of the application.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        domain: Optional[str] = None,
        aud: Optional[str] = None,
        policies: Optional[List['PolicyResult']] = None,
        allowed_idps: Optional[List[str]] = None,
        auto_redirect_to_identity: Optional[bool] = None,
        session_duration: Optional[str] = None,
        type: Optional[str] = None,
        uid: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> None:
        """
        Initialize a AppResult object.

        :param str id: (optional) Application ID.
        :param str name: (optional) Application name.
        :param str domain: (optional) The domain and path that Access blocks.
        :param str aud: (optional)
        :param List[PolicyResult] policies: (optional) Policies of the application.
        :param List[str] allowed_idps: (optional) The identity providers selected
               for application.
        :param bool auto_redirect_to_identity: (optional) Option to skip identity
               provider selection if only one is configured in allowed_idps.
        :param str session_duration: (optional) The amount of time that the tokens
               issued for this application are valid.
        :param str type: (optional) Application type.
        :param str uid: (optional) UUID, same as ID.
        :param str created_at: (optional) Created time of the application.
        :param str updated_at: (optional) Updated time of the application.
        """
        self.id = id
        self.name = name
        self.domain = domain
        self.aud = aud
        self.policies = policies
        self.allowed_idps = allowed_idps
        self.auto_redirect_to_identity = auto_redirect_to_identity
        self.session_duration = session_duration
        self.type = type
        self.uid = uid
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppResult':
        """Initialize a AppResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = domain
        if (aud := _dict.get('aud')) is not None:
            args['aud'] = aud
        if (policies := _dict.get('policies')) is not None:
            args['policies'] = [PolicyResult.from_dict(v) for v in policies]
        if (allowed_idps := _dict.get('allowed_idps')) is not None:
            args['allowed_idps'] = allowed_idps
        if (auto_redirect_to_identity := _dict.get('auto_redirect_to_identity')) is not None:
            args['auto_redirect_to_identity'] = auto_redirect_to_identity
        if (session_duration := _dict.get('session_duration')) is not None:
            args['session_duration'] = session_duration
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (uid := _dict.get('uid')) is not None:
            args['uid'] = uid
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = updated_at
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'domain') and self.domain is not None:
            _dict['domain'] = self.domain
        if hasattr(self, 'aud') and self.aud is not None:
            _dict['aud'] = self.aud
        if hasattr(self, 'policies') and self.policies is not None:
            policies_list = []
            for v in self.policies:
                if isinstance(v, dict):
                    policies_list.append(v)
                else:
                    policies_list.append(v.to_dict())
            _dict['policies'] = policies_list
        if hasattr(self, 'allowed_idps') and self.allowed_idps is not None:
            _dict['allowed_idps'] = self.allowed_idps
        if hasattr(self, 'auto_redirect_to_identity') and self.auto_redirect_to_identity is not None:
            _dict['auto_redirect_to_identity'] = self.auto_redirect_to_identity
        if hasattr(self, 'session_duration') and self.session_duration is not None:
            _dict['session_duration'] = self.session_duration
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CertResult:
    """
    Access certificate details.

    :param str id: (optional) Access certificate ID.
    :param str name: (optional) access certificate name.
    :param str fingerprint: (optional) Fingerprint of the certificate.
    :param List[str] associated_hostnames: (optional) The hostnames that are
          prompted for this certificate.
    :param str created_at: (optional) Created time of the access certificate.
    :param str updated_at: (optional) Updated time of the access certificate.
    :param str expires_on: (optional) Expire time of the access certificate.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        fingerprint: Optional[str] = None,
        associated_hostnames: Optional[List[str]] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        expires_on: Optional[str] = None,
    ) -> None:
        """
        Initialize a CertResult object.

        :param str id: (optional) Access certificate ID.
        :param str name: (optional) access certificate name.
        :param str fingerprint: (optional) Fingerprint of the certificate.
        :param List[str] associated_hostnames: (optional) The hostnames that are
               prompted for this certificate.
        :param str created_at: (optional) Created time of the access certificate.
        :param str updated_at: (optional) Updated time of the access certificate.
        :param str expires_on: (optional) Expire time of the access certificate.
        """
        self.id = id
        self.name = name
        self.fingerprint = fingerprint
        self.associated_hostnames = associated_hostnames
        self.created_at = created_at
        self.updated_at = updated_at
        self.expires_on = expires_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CertResult':
        """Initialize a CertResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (fingerprint := _dict.get('fingerprint')) is not None:
            args['fingerprint'] = fingerprint
        if (associated_hostnames := _dict.get('associated_hostnames')) is not None:
            args['associated_hostnames'] = associated_hostnames
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = updated_at
        if (expires_on := _dict.get('expires_on')) is not None:
            args['expires_on'] = expires_on
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CertResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'fingerprint') and self.fingerprint is not None:
            _dict['fingerprint'] = self.fingerprint
        if hasattr(self, 'associated_hostnames') and self.associated_hostnames is not None:
            _dict['associated_hostnames'] = self.associated_hostnames
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        if hasattr(self, 'expires_on') and self.expires_on is not None:
            _dict['expires_on'] = self.expires_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CertResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CertResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CertResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CertSettingsResult:
    """
    CertSettingsResult.

    :param str hostname: (optional)
    :param bool china_network: (optional)
    :param bool client_certificate_forwarding: (optional)
    """

    def __init__(
        self,
        *,
        hostname: Optional[str] = None,
        china_network: Optional[bool] = None,
        client_certificate_forwarding: Optional[bool] = None,
    ) -> None:
        """
        Initialize a CertSettingsResult object.

        :param str hostname: (optional)
        :param bool china_network: (optional)
        :param bool client_certificate_forwarding: (optional)
        """
        self.hostname = hostname
        self.china_network = china_network
        self.client_certificate_forwarding = client_certificate_forwarding

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CertSettingsResult':
        """Initialize a CertSettingsResult object from a json dictionary."""
        args = {}
        if (hostname := _dict.get('hostname')) is not None:
            args['hostname'] = hostname
        if (china_network := _dict.get('china_network')) is not None:
            args['china_network'] = china_network
        if (client_certificate_forwarding := _dict.get('client_certificate_forwarding')) is not None:
            args['client_certificate_forwarding'] = client_certificate_forwarding
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CertSettingsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'china_network') and self.china_network is not None:
            _dict['china_network'] = self.china_network
        if hasattr(self, 'client_certificate_forwarding') and self.client_certificate_forwarding is not None:
            _dict['client_certificate_forwarding'] = self.client_certificate_forwarding
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CertSettingsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CertSettingsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CertSettingsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateAccessAppResp:
    """
    Create access application response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param CreateAccessAppRespResult result: (optional) Access application details.
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['CreateAccessAppRespResult'] = None,
    ) -> None:
        """
        Initialize a CreateAccessAppResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param CreateAccessAppRespResult result: (optional) Access application
               details.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAccessAppResp':
        """Initialize a CreateAccessAppResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = CreateAccessAppRespResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAccessAppResp object from a json dictionary."""
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
        """Return a `str` version of this CreateAccessAppResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAccessAppResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAccessAppResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAccessAppResp:
    """
    Delete access application response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param DeleteAccessAppRespResult result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['DeleteAccessAppRespResult'] = None,
    ) -> None:
        """
        Initialize a DeleteAccessAppResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param DeleteAccessAppRespResult result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccessAppResp':
        """Initialize a DeleteAccessAppResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = DeleteAccessAppRespResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccessAppResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccessAppResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccessAppResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccessAppResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAccessCertResp:
    """
    Delete access certificate response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param DeleteAccessCertRespResult result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['DeleteAccessCertRespResult'] = None,
    ) -> None:
        """
        Initialize a DeleteAccessCertResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param DeleteAccessCertRespResult result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccessCertResp':
        """Initialize a DeleteAccessCertResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = DeleteAccessCertRespResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccessCertResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccessCertResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccessCertResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccessCertResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAccessPolicyResp:
    """
    Delete access policy response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param DeleteAccessPolicyRespResult result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional['DeleteAccessPolicyRespResult'] = None,
    ) -> None:
        """
        Initialize a DeleteAccessPolicyResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param DeleteAccessPolicyRespResult result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccessPolicyResp':
        """Initialize a DeleteAccessPolicyResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = DeleteAccessPolicyRespResult.from_dict(result)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccessPolicyResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccessPolicyResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccessPolicyResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccessPolicyResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListAccessAppsResp:
    """
    List access applications response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param List[AppResult] result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional[List['AppResult']] = None,
    ) -> None:
        """
        Initialize a ListAccessAppsResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param List[AppResult] result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAccessAppsResp':
        """Initialize a ListAccessAppsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = [AppResult.from_dict(v) for v in result]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAccessAppsResp object from a json dictionary."""
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
        """Return a `str` version of this ListAccessAppsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAccessAppsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAccessAppsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListAccessCertsResp:
    """
    List access certificate response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param List[CertResult] result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional[List['CertResult']] = None,
    ) -> None:
        """
        Initialize a ListAccessCertsResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param List[CertResult] result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAccessCertsResp':
        """Initialize a ListAccessCertsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = [CertResult.from_dict(v) for v in result]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAccessCertsResp object from a json dictionary."""
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
        """Return a `str` version of this ListAccessCertsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAccessCertsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAccessCertsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListAccessPoliciesResp:
    """
    List access policies response.

    :param bool success: (optional) Was operation successful.
    :param List[List[str]] errors: (optional) Array of errors encountered.
    :param List[List[str]] messages: (optional) Array of messages returned.
    :param List[PolicyResult] result: (optional)
    """

    def __init__(
        self,
        *,
        success: Optional[bool] = None,
        errors: Optional[List[List[str]]] = None,
        messages: Optional[List[List[str]]] = None,
        result: Optional[List['PolicyResult']] = None,
    ) -> None:
        """
        Initialize a ListAccessPoliciesResp object.

        :param bool success: (optional) Was operation successful.
        :param List[List[str]] errors: (optional) Array of errors encountered.
        :param List[List[str]] messages: (optional) Array of messages returned.
        :param List[PolicyResult] result: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAccessPoliciesResp':
        """Initialize a ListAccessPoliciesResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        if (result := _dict.get('result')) is not None:
            args['result'] = [PolicyResult.from_dict(v) for v in result]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAccessPoliciesResp object from a json dictionary."""
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
        """Return a `str` version of this ListAccessPoliciesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAccessPoliciesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAccessPoliciesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyResult:
    """
    Access policies information.

    :param str id: (optional) Policy ID.
    :param str name: (optional) Policy name.
    :param str decision: (optional) The action Access takes if the policy matches
          the user.
    :param List[PolicyRule] include: (optional) The include policy works like an OR
          logical operator.
    :param List[PolicyRule] exclude: (optional) The exclude policy works like a NOT
          logical operator.
    :param int precedence: (optional) The unique precedence for policies on a single
          application.
    :param List[PolicyRule] require: (optional) The require policy works like a AND
          logical operator.
    :param str uid: (optional) UUID, same as ID.
    :param str created_at: (optional) Created time of the policy.
    :param str updated_at: (optional) Updated time of the policy.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        decision: Optional[str] = None,
        include: Optional[List['PolicyRule']] = None,
        exclude: Optional[List['PolicyRule']] = None,
        precedence: Optional[int] = None,
        require: Optional[List['PolicyRule']] = None,
        uid: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> None:
        """
        Initialize a PolicyResult object.

        :param str id: (optional) Policy ID.
        :param str name: (optional) Policy name.
        :param str decision: (optional) The action Access takes if the policy
               matches the user.
        :param List[PolicyRule] include: (optional) The include policy works like
               an OR logical operator.
        :param List[PolicyRule] exclude: (optional) The exclude policy works like a
               NOT logical operator.
        :param int precedence: (optional) The unique precedence for policies on a
               single application.
        :param List[PolicyRule] require: (optional) The require policy works like a
               AND logical operator.
        :param str uid: (optional) UUID, same as ID.
        :param str created_at: (optional) Created time of the policy.
        :param str updated_at: (optional) Updated time of the policy.
        """
        self.id = id
        self.name = name
        self.decision = decision
        self.include = include
        self.exclude = exclude
        self.precedence = precedence
        self.require = require
        self.uid = uid
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyResult':
        """Initialize a PolicyResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (decision := _dict.get('decision')) is not None:
            args['decision'] = decision
        if (include := _dict.get('include')) is not None:
            args['include'] = include
        if (exclude := _dict.get('exclude')) is not None:
            args['exclude'] = exclude
        if (precedence := _dict.get('precedence')) is not None:
            args['precedence'] = precedence
        if (require := _dict.get('require')) is not None:
            args['require'] = require
        if (uid := _dict.get('uid')) is not None:
            args['uid'] = uid
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = updated_at
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'decision') and self.decision is not None:
            _dict['decision'] = self.decision
        if hasattr(self, 'include') and self.include is not None:
            include_list = []
            for v in self.include:
                if isinstance(v, dict):
                    include_list.append(v)
                else:
                    include_list.append(v.to_dict())
            _dict['include'] = include_list
        if hasattr(self, 'exclude') and self.exclude is not None:
            exclude_list = []
            for v in self.exclude:
                if isinstance(v, dict):
                    exclude_list.append(v)
                else:
                    exclude_list.append(v.to_dict())
            _dict['exclude'] = exclude_list
        if hasattr(self, 'precedence') and self.precedence is not None:
            _dict['precedence'] = self.precedence
        if hasattr(self, 'require') and self.require is not None:
            require_list = []
            for v in self.require:
                if isinstance(v, dict):
                    require_list.append(v)
                else:
                    require_list.append(v.to_dict())
            _dict['require'] = require_list
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyRule:
    """
    Policy rule.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a PolicyRule object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['PolicyRulePolicyCertRule', 'PolicyRulePolicyCnRule'])
        )
        raise Exception(msg)


class PolicyRulePolicyCertRule(PolicyRule):
    """
    Policy rule of certificate.

    :param dict certificate: (optional)
    """

    def __init__(
        self,
        *,
        certificate: Optional[dict] = None,
    ) -> None:
        """
        Initialize a PolicyRulePolicyCertRule object.

        :param dict certificate: (optional)
        """
        # pylint: disable=super-init-not-called
        self.certificate = certificate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRulePolicyCertRule':
        """Initialize a PolicyRulePolicyCertRule object from a json dictionary."""
        args = {}
        if (certificate := _dict.get('certificate')) is not None:
            args['certificate'] = certificate
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRulePolicyCertRule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyRulePolicyCertRule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRulePolicyCertRule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRulePolicyCertRule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PolicyRulePolicyCnRule(PolicyRule):
    """
    Policy rule of common name.

    :param PolicyCnRuleCommonName common_name:
    """

    def __init__(
        self,
        common_name: 'PolicyCnRuleCommonName',
    ) -> None:
        """
        Initialize a PolicyRulePolicyCnRule object.

        :param PolicyCnRuleCommonName common_name:
        """
        # pylint: disable=super-init-not-called
        self.common_name = common_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PolicyRulePolicyCnRule':
        """Initialize a PolicyRulePolicyCnRule object from a json dictionary."""
        args = {}
        if (common_name := _dict.get('common_name')) is not None:
            args['common_name'] = PolicyCnRuleCommonName.from_dict(common_name)
        else:
            raise ValueError('Required property \'common_name\' not present in PolicyRulePolicyCnRule JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PolicyRulePolicyCnRule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'common_name') and self.common_name is not None:
            if isinstance(self.common_name, dict):
                _dict['common_name'] = self.common_name
            else:
                _dict['common_name'] = self.common_name.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PolicyRulePolicyCnRule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PolicyRulePolicyCnRule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PolicyRulePolicyCnRule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
