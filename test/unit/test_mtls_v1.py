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
Unit Tests for MtlsV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.mtls_v1 import *

crn = 'testString'

_service = MtlsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
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
# Start of Service: MutualTLS
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

        service = MtlsV1.new_instance(
            crn=crn,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, MtlsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = MtlsV1.new_instance(
                crn=crn,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = MtlsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = MtlsV1.new_instance(
                crn=None,
            )


class TestListAccessCertificates:
    """
    Test Class for list_access_certificates
    """

    @responses.activate
    def test_list_access_certificates_all_params(self):
        """
        list_access_certificates()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.list_access_certificates(
            zone_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_access_certificates_all_params_with_retries(self):
        # Enable retries and run test_list_access_certificates_all_params.
        _service.enable_retries()
        self.test_list_access_certificates_all_params()

        # Disable retries and run test_list_access_certificates_all_params.
        _service.disable_retries()
        self.test_list_access_certificates_all_params()

    @responses.activate
    def test_list_access_certificates_value_error(self):
        """
        test_list_access_certificates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_certificates(**req_copy)

    def test_list_access_certificates_value_error_with_retries(self):
        # Enable retries and run test_list_access_certificates_value_error.
        _service.enable_retries()
        self.test_list_access_certificates_value_error()

        # Disable retries and run test_list_access_certificates_value_error.
        _service.disable_retries()
        self.test_list_access_certificates_value_error()


class TestCreateAccessCertificate:
    """
    Test Class for create_access_certificate
    """

    @responses.activate
    def test_create_access_certificate_all_params(self):
        """
        create_access_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        name = 'test-cert'
        certificate = '-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----'
        associated_hostnames = ['test.example.com']

        # Invoke method
        response = _service.create_access_certificate(
            zone_id,
            name=name,
            certificate=certificate,
            associated_hostnames=associated_hostnames,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test-cert'
        assert req_body['certificate'] == '-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----'
        assert req_body['associated_hostnames'] == ['test.example.com']

    def test_create_access_certificate_all_params_with_retries(self):
        # Enable retries and run test_create_access_certificate_all_params.
        _service.enable_retries()
        self.test_create_access_certificate_all_params()

        # Disable retries and run test_create_access_certificate_all_params.
        _service.disable_retries()
        self.test_create_access_certificate_all_params()

    @responses.activate
    def test_create_access_certificate_required_params(self):
        """
        test_create_access_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.create_access_certificate(
            zone_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_access_certificate_required_params_with_retries(self):
        # Enable retries and run test_create_access_certificate_required_params.
        _service.enable_retries()
        self.test_create_access_certificate_required_params()

        # Disable retries and run test_create_access_certificate_required_params.
        _service.disable_retries()
        self.test_create_access_certificate_required_params()

    @responses.activate
    def test_create_access_certificate_value_error(self):
        """
        test_create_access_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_access_certificate(**req_copy)

    def test_create_access_certificate_value_error_with_retries(self):
        # Enable retries and run test_create_access_certificate_value_error.
        _service.enable_retries()
        self.test_create_access_certificate_value_error()

        # Disable retries and run test_create_access_certificate_value_error.
        _service.disable_retries()
        self.test_create_access_certificate_value_error()


class TestGetAccessCertificate:
    """
    Test Class for get_access_certificate
    """

    @responses.activate
    def test_get_access_certificate_all_params(self):
        """
        get_access_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'

        # Invoke method
        response = _service.get_access_certificate(
            zone_id,
            cert_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_certificate_all_params_with_retries(self):
        # Enable retries and run test_get_access_certificate_all_params.
        _service.enable_retries()
        self.test_get_access_certificate_all_params()

        # Disable retries and run test_get_access_certificate_all_params.
        _service.disable_retries()
        self.test_get_access_certificate_all_params()

    @responses.activate
    def test_get_access_certificate_value_error(self):
        """
        test_get_access_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "cert_id": cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_certificate(**req_copy)

    def test_get_access_certificate_value_error_with_retries(self):
        # Enable retries and run test_get_access_certificate_value_error.
        _service.enable_retries()
        self.test_get_access_certificate_value_error()

        # Disable retries and run test_get_access_certificate_value_error.
        _service.disable_retries()
        self.test_get_access_certificate_value_error()


class TestUpdateAccessCertificate:
    """
    Test Class for update_access_certificate
    """

    @responses.activate
    def test_update_access_certificate_all_params(self):
        """
        update_access_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'
        name = 'test-cert'
        associated_hostnames = ['test.example.com']

        # Invoke method
        response = _service.update_access_certificate(
            zone_id,
            cert_id,
            name=name,
            associated_hostnames=associated_hostnames,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test-cert'
        assert req_body['associated_hostnames'] == ['test.example.com']

    def test_update_access_certificate_all_params_with_retries(self):
        # Enable retries and run test_update_access_certificate_all_params.
        _service.enable_retries()
        self.test_update_access_certificate_all_params()

        # Disable retries and run test_update_access_certificate_all_params.
        _service.disable_retries()
        self.test_update_access_certificate_all_params()

    @responses.activate
    def test_update_access_certificate_required_params(self):
        """
        test_update_access_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'

        # Invoke method
        response = _service.update_access_certificate(
            zone_id,
            cert_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_access_certificate_required_params_with_retries(self):
        # Enable retries and run test_update_access_certificate_required_params.
        _service.enable_retries()
        self.test_update_access_certificate_required_params()

        # Disable retries and run test_update_access_certificate_required_params.
        _service.disable_retries()
        self.test_update_access_certificate_required_params()

    @responses.activate
    def test_update_access_certificate_value_error(self):
        """
        test_update_access_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f", "name": "test-cert", "fingerprint": "MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F", "associated_hostnames": ["test.example.com"], "created_at": "2021-04-19T11:09:11Z", "updated_at": "2021-04-19T11:09:11Z", "expires_on": "2026-04-18T06:26:00Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "cert_id": cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_access_certificate(**req_copy)

    def test_update_access_certificate_value_error_with_retries(self):
        # Enable retries and run test_update_access_certificate_value_error.
        _service.enable_retries()
        self.test_update_access_certificate_value_error()

        # Disable retries and run test_update_access_certificate_value_error.
        _service.disable_retries()
        self.test_update_access_certificate_value_error()


class TestDeleteAccessCertificate:
    """
    Test Class for delete_access_certificate
    """

    @responses.activate
    def test_delete_access_certificate_all_params(self):
        """
        delete_access_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'

        # Invoke method
        response = _service.delete_access_certificate(
            zone_id,
            cert_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_access_certificate_all_params_with_retries(self):
        # Enable retries and run test_delete_access_certificate_all_params.
        _service.enable_retries()
        self.test_delete_access_certificate_all_params()

        # Disable retries and run test_delete_access_certificate_all_params.
        _service.disable_retries()
        self.test_delete_access_certificate_all_params()

    @responses.activate
    def test_delete_access_certificate_value_error(self):
        """
        test_delete_access_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "21a41336-9001-42c4-8440-c79e0cb86e1f"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        cert_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "cert_id": cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_access_certificate(**req_copy)

    def test_delete_access_certificate_value_error_with_retries(self):
        # Enable retries and run test_delete_access_certificate_value_error.
        _service.enable_retries()
        self.test_delete_access_certificate_value_error()

        # Disable retries and run test_delete_access_certificate_value_error.
        _service.disable_retries()
        self.test_delete_access_certificate_value_error()


class TestListAccessApplications:
    """
    Test Class for list_access_applications
    """

    @responses.activate
    def test_list_access_applications_all_params(self):
        """
        list_access_applications()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.list_access_applications(
            zone_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_access_applications_all_params_with_retries(self):
        # Enable retries and run test_list_access_applications_all_params.
        _service.enable_retries()
        self.test_list_access_applications_all_params()

        # Disable retries and run test_list_access_applications_all_params.
        _service.disable_retries()
        self.test_list_access_applications_all_params()

    @responses.activate
    def test_list_access_applications_value_error(self):
        """
        test_list_access_applications_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_applications(**req_copy)

    def test_list_access_applications_value_error_with_retries(self):
        # Enable retries and run test_list_access_applications_value_error.
        _service.enable_retries()
        self.test_list_access_applications_value_error()

        # Disable retries and run test_list_access_applications_value_error.
        _service.disable_retries()
        self.test_list_access_applications_value_error()


class TestCreateAccessApplication:
    """
    Test Class for create_access_application
    """

    @responses.activate
    def test_create_access_application_all_params(self):
        """
        create_access_application()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"anyKey": "anyValue"}], "allowed_idps": ["allowed_idps"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        name = 'mtls-test-app'
        domain = 'test.example.com'
        session_duration = '24h'

        # Invoke method
        response = _service.create_access_application(
            zone_id,
            name=name,
            domain=domain,
            session_duration=session_duration,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'mtls-test-app'
        assert req_body['domain'] == 'test.example.com'
        assert req_body['session_duration'] == '24h'

    def test_create_access_application_all_params_with_retries(self):
        # Enable retries and run test_create_access_application_all_params.
        _service.enable_retries()
        self.test_create_access_application_all_params()

        # Disable retries and run test_create_access_application_all_params.
        _service.disable_retries()
        self.test_create_access_application_all_params()

    @responses.activate
    def test_create_access_application_required_params(self):
        """
        test_create_access_application_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"anyKey": "anyValue"}], "allowed_idps": ["allowed_idps"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.create_access_application(
            zone_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_access_application_required_params_with_retries(self):
        # Enable retries and run test_create_access_application_required_params.
        _service.enable_retries()
        self.test_create_access_application_required_params()

        # Disable retries and run test_create_access_application_required_params.
        _service.disable_retries()
        self.test_create_access_application_required_params()

    @responses.activate
    def test_create_access_application_value_error(self):
        """
        test_create_access_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"anyKey": "anyValue"}], "allowed_idps": ["allowed_idps"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_access_application(**req_copy)

    def test_create_access_application_value_error_with_retries(self):
        # Enable retries and run test_create_access_application_value_error.
        _service.enable_retries()
        self.test_create_access_application_value_error()

        # Disable retries and run test_create_access_application_value_error.
        _service.disable_retries()
        self.test_create_access_application_value_error()


class TestGetAccessApplication:
    """
    Test Class for get_access_application
    """

    @responses.activate
    def test_get_access_application_all_params(self):
        """
        get_access_application()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Invoke method
        response = _service.get_access_application(
            zone_id,
            app_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_application_all_params_with_retries(self):
        # Enable retries and run test_get_access_application_all_params.
        _service.enable_retries()
        self.test_get_access_application_all_params()

        # Disable retries and run test_get_access_application_all_params.
        _service.disable_retries()
        self.test_get_access_application_all_params()

    @responses.activate
    def test_get_access_application_value_error(self):
        """
        test_get_access_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_application(**req_copy)

    def test_get_access_application_value_error_with_retries(self):
        # Enable retries and run test_get_access_application_value_error.
        _service.enable_retries()
        self.test_get_access_application_value_error()

        # Disable retries and run test_get_access_application_value_error.
        _service.disable_retries()
        self.test_get_access_application_value_error()


class TestUpdateAccessApplication:
    """
    Test Class for update_access_application
    """

    @responses.activate
    def test_update_access_application_all_params(self):
        """
        update_access_application()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        name = 'mtls-test-app'
        domain = 'test.example.com'
        session_duration = '24h'

        # Invoke method
        response = _service.update_access_application(
            zone_id,
            app_id,
            name=name,
            domain=domain,
            session_duration=session_duration,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'mtls-test-app'
        assert req_body['domain'] == 'test.example.com'
        assert req_body['session_duration'] == '24h'

    def test_update_access_application_all_params_with_retries(self):
        # Enable retries and run test_update_access_application_all_params.
        _service.enable_retries()
        self.test_update_access_application_all_params()

        # Disable retries and run test_update_access_application_all_params.
        _service.disable_retries()
        self.test_update_access_application_all_params()

    @responses.activate
    def test_update_access_application_required_params(self):
        """
        test_update_access_application_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Invoke method
        response = _service.update_access_application(
            zone_id,
            app_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_access_application_required_params_with_retries(self):
        # Enable retries and run test_update_access_application_required_params.
        _service.enable_retries()
        self.test_update_access_application_required_params()

        # Disable retries and run test_update_access_application_required_params.
        _service.disable_retries()
        self.test_update_access_application_required_params()

    @responses.activate
    def test_update_access_application_value_error(self):
        """
        test_update_access_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8", "name": "mtls-test-app", "domain": "test.example.com", "aud": "f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008", "policies": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}], "allowed_idps": ["699d98642c564d2e855e9661899b7252"], "auto_redirect_to_identity": false, "session_duration": "24h", "type": "self_hosted", "uid": "de4526d6-d125-4f95-906f-1757510a9cd8", "created_at": "2021-04-19T07:59:49Z", "updated_at": "2021-04-19T07:59:49Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_access_application(**req_copy)

    def test_update_access_application_value_error_with_retries(self):
        # Enable retries and run test_update_access_application_value_error.
        _service.enable_retries()
        self.test_update_access_application_value_error()

        # Disable retries and run test_update_access_application_value_error.
        _service.disable_retries()
        self.test_update_access_application_value_error()


class TestDeleteAccessApplication:
    """
    Test Class for delete_access_application
    """

    @responses.activate
    def test_delete_access_application_all_params(self):
        """
        delete_access_application()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Invoke method
        response = _service.delete_access_application(
            zone_id,
            app_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_access_application_all_params_with_retries(self):
        # Enable retries and run test_delete_access_application_all_params.
        _service.enable_retries()
        self.test_delete_access_application_all_params()

        # Disable retries and run test_delete_access_application_all_params.
        _service.disable_retries()
        self.test_delete_access_application_all_params()

    @responses.activate
    def test_delete_access_application_value_error(self):
        """
        test_delete_access_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "de4526d6-d125-4f95-906f-1757510a9cd8"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_access_application(**req_copy)

    def test_delete_access_application_value_error_with_retries(self):
        # Enable retries and run test_delete_access_application_value_error.
        _service.enable_retries()
        self.test_delete_access_application_value_error()

        # Disable retries and run test_delete_access_application_value_error.
        _service.disable_retries()
        self.test_delete_access_application_value_error()


class TestListAccessPolicies:
    """
    Test Class for list_access_policies
    """

    @responses.activate
    def test_list_access_policies_all_params(self):
        """
        list_access_policies()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Invoke method
        response = _service.list_access_policies(
            zone_id,
            app_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_access_policies_all_params_with_retries(self):
        # Enable retries and run test_list_access_policies_all_params.
        _service.enable_retries()
        self.test_list_access_policies_all_params()

        # Disable retries and run test_list_access_policies_all_params.
        _service.disable_retries()
        self.test_list_access_policies_all_params()

    @responses.activate
    def test_list_access_policies_value_error(self):
        """
        test_list_access_policies_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_access_policies(**req_copy)

    def test_list_access_policies_value_error_with_retries(self):
        # Enable retries and run test_list_access_policies_value_error.
        _service.enable_retries()
        self.test_list_access_policies_value_error()

        # Disable retries and run test_list_access_policies_value_error.
        _service.disable_retries()
        self.test_list_access_policies_value_error()


class TestCreateAccessPolicy:
    """
    Test Class for create_access_policy
    """

    @responses.activate
    def test_create_access_policy_all_params(self):
        """
        create_access_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PolicyRulePolicyCertRule model
        policy_rule_model = {}
        policy_rule_model['certificate'] = {}

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        name = 'mtls-test-policy'
        decision = 'non_identity'
        include = [policy_rule_model]

        # Invoke method
        response = _service.create_access_policy(
            zone_id,
            app_id,
            name=name,
            decision=decision,
            include=include,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'mtls-test-policy'
        assert req_body['decision'] == 'non_identity'
        assert req_body['include'] == [policy_rule_model]

    def test_create_access_policy_all_params_with_retries(self):
        # Enable retries and run test_create_access_policy_all_params.
        _service.enable_retries()
        self.test_create_access_policy_all_params()

        # Disable retries and run test_create_access_policy_all_params.
        _service.disable_retries()
        self.test_create_access_policy_all_params()

    @responses.activate
    def test_create_access_policy_required_params(self):
        """
        test_create_access_policy_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Invoke method
        response = _service.create_access_policy(
            zone_id,
            app_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_access_policy_required_params_with_retries(self):
        # Enable retries and run test_create_access_policy_required_params.
        _service.enable_retries()
        self.test_create_access_policy_required_params()

        # Disable retries and run test_create_access_policy_required_params.
        _service.disable_retries()
        self.test_create_access_policy_required_params()

    @responses.activate
    def test_create_access_policy_value_error(self):
        """
        test_create_access_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_access_policy(**req_copy)

    def test_create_access_policy_value_error_with_retries(self):
        # Enable retries and run test_create_access_policy_value_error.
        _service.enable_retries()
        self.test_create_access_policy_value_error()

        # Disable retries and run test_create_access_policy_value_error.
        _service.disable_retries()
        self.test_create_access_policy_value_error()


class TestGetAccessPolicy:
    """
    Test Class for get_access_policy
    """

    @responses.activate
    def test_get_access_policy_all_params(self):
        """
        get_access_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'

        # Invoke method
        response = _service.get_access_policy(
            zone_id,
            app_id,
            policy_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_policy_all_params_with_retries(self):
        # Enable retries and run test_get_access_policy_all_params.
        _service.enable_retries()
        self.test_get_access_policy_all_params()

        # Disable retries and run test_get_access_policy_all_params.
        _service.disable_retries()
        self.test_get_access_policy_all_params()

    @responses.activate
    def test_get_access_policy_value_error(self):
        """
        test_get_access_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_policy(**req_copy)

    def test_get_access_policy_value_error_with_retries(self):
        # Enable retries and run test_get_access_policy_value_error.
        _service.enable_retries()
        self.test_get_access_policy_value_error()

        # Disable retries and run test_get_access_policy_value_error.
        _service.disable_retries()
        self.test_get_access_policy_value_error()


class TestUpdateAccessPolicy:
    """
    Test Class for update_access_policy
    """

    @responses.activate
    def test_update_access_policy_all_params(self):
        """
        update_access_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PolicyRulePolicyCertRule model
        policy_rule_model = {}
        policy_rule_model['certificate'] = {}

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'
        name = 'mtls-test-policy'
        decision = 'non_identity'
        include = [policy_rule_model]

        # Invoke method
        response = _service.update_access_policy(
            zone_id,
            app_id,
            policy_id,
            name=name,
            decision=decision,
            include=include,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'mtls-test-policy'
        assert req_body['decision'] == 'non_identity'
        assert req_body['include'] == [policy_rule_model]

    def test_update_access_policy_all_params_with_retries(self):
        # Enable retries and run test_update_access_policy_all_params.
        _service.enable_retries()
        self.test_update_access_policy_all_params()

        # Disable retries and run test_update_access_policy_all_params.
        _service.disable_retries()
        self.test_update_access_policy_all_params()

    @responses.activate
    def test_update_access_policy_required_params(self):
        """
        test_update_access_policy_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'

        # Invoke method
        response = _service.update_access_policy(
            zone_id,
            app_id,
            policy_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_access_policy_required_params_with_retries(self):
        # Enable retries and run test_update_access_policy_required_params.
        _service.enable_retries()
        self.test_update_access_policy_required_params()

        # Disable retries and run test_update_access_policy_required_params.
        _service.disable_retries()
        self.test_update_access_policy_required_params()

    @responses.activate
    def test_update_access_policy_value_error(self):
        """
        test_update_access_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "name": "mtls-test-policy", "decision": "non_identity", "include": [{"certificate": {"anyKey": "anyValue"}}], "exclude": [{"certificate": {"anyKey": "anyValue"}}], "precedence": 1, "require": [{"certificate": {"anyKey": "anyValue"}}], "uid": "acabcdb1-afb3-4f61-9dae-d1a353a93661", "created_at": "2021-04-19T08:01:21Z", "updated_at": "2021-04-19T08:01:21Z"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_access_policy(**req_copy)

    def test_update_access_policy_value_error_with_retries(self):
        # Enable retries and run test_update_access_policy_value_error.
        _service.enable_retries()
        self.test_update_access_policy_value_error()

        # Disable retries and run test_update_access_policy_value_error.
        _service.disable_retries()
        self.test_update_access_policy_value_error()


class TestDeleteAccessPolicy:
    """
    Test Class for delete_access_policy
    """

    @responses.activate
    def test_delete_access_policy_all_params(self):
        """
        delete_access_policy()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'

        # Invoke method
        response = _service.delete_access_policy(
            zone_id,
            app_id,
            policy_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_access_policy_all_params_with_retries(self):
        # Enable retries and run test_delete_access_policy_all_params.
        _service.enable_retries()
        self.test_delete_access_policy_all_params()

        # Disable retries and run test_delete_access_policy_all_params.
        _service.disable_retries()
        self.test_delete_access_policy_all_params()

    @responses.activate
    def test_delete_access_policy_value_error(self):
        """
        test_delete_access_policy_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/apps/testString/policies/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "acabcdb1-afb3-4f61-9dae-d1a353a93661"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'
        app_id = 'testString'
        policy_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
            "app_id": app_id,
            "policy_id": policy_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_access_policy(**req_copy)

    def test_delete_access_policy_value_error_with_retries(self):
        # Enable retries and run test_delete_access_policy_value_error.
        _service.enable_retries()
        self.test_delete_access_policy_value_error()

        # Disable retries and run test_delete_access_policy_value_error.
        _service.disable_retries()
        self.test_delete_access_policy_value_error()


class TestGetAccessCertSettings:
    """
    Test Class for get_access_cert_settings
    """

    @responses.activate
    def test_get_access_cert_settings_all_params(self):
        """
        get_access_cert_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"hostname": "test.example.com", "china_network": false, "client_certificate_forwarding": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.get_access_cert_settings(
            zone_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_access_cert_settings_all_params_with_retries(self):
        # Enable retries and run test_get_access_cert_settings_all_params.
        _service.enable_retries()
        self.test_get_access_cert_settings_all_params()

        # Disable retries and run test_get_access_cert_settings_all_params.
        _service.disable_retries()
        self.test_get_access_cert_settings_all_params()

    @responses.activate
    def test_get_access_cert_settings_value_error(self):
        """
        test_get_access_cert_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"hostname": "test.example.com", "china_network": false, "client_certificate_forwarding": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_access_cert_settings(**req_copy)

    def test_get_access_cert_settings_value_error_with_retries(self):
        # Enable retries and run test_get_access_cert_settings_value_error.
        _service.enable_retries()
        self.test_get_access_cert_settings_value_error()

        # Disable retries and run test_get_access_cert_settings_value_error.
        _service.disable_retries()
        self.test_get_access_cert_settings_value_error()


class TestUpdateAccessCertSettings:
    """
    Test Class for update_access_cert_settings
    """

    @responses.activate
    def test_update_access_cert_settings_all_params(self):
        """
        update_access_cert_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"hostname": "test.example.com", "china_network": false, "client_certificate_forwarding": true}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AccessCertSettingsInputArray model
        access_cert_settings_input_array_model = {}
        access_cert_settings_input_array_model['hostname'] = 'test.example.com'
        access_cert_settings_input_array_model['client_certificate_forwarding'] = True

        # Set up parameter values
        zone_id = 'testString'
        settings = [access_cert_settings_input_array_model]

        # Invoke method
        response = _service.update_access_cert_settings(
            zone_id,
            settings=settings,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['settings'] == [access_cert_settings_input_array_model]

    def test_update_access_cert_settings_all_params_with_retries(self):
        # Enable retries and run test_update_access_cert_settings_all_params.
        _service.enable_retries()
        self.test_update_access_cert_settings_all_params()

        # Disable retries and run test_update_access_cert_settings_all_params.
        _service.disable_retries()
        self.test_update_access_cert_settings_all_params()

    @responses.activate
    def test_update_access_cert_settings_required_params(self):
        """
        test_update_access_cert_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"hostname": "test.example.com", "china_network": false, "client_certificate_forwarding": true}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Invoke method
        response = _service.update_access_cert_settings(
            zone_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_access_cert_settings_required_params_with_retries(self):
        # Enable retries and run test_update_access_cert_settings_required_params.
        _service.enable_retries()
        self.test_update_access_cert_settings_required_params()

        # Disable retries and run test_update_access_cert_settings_required_params.
        _service.disable_retries()
        self.test_update_access_cert_settings_required_params()

    @responses.activate
    def test_update_access_cert_settings_value_error(self):
        """
        test_update_access_cert_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/access/certificates/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"hostname": "test.example.com", "china_network": false, "client_certificate_forwarding": true}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_id": zone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_access_cert_settings(**req_copy)

    def test_update_access_cert_settings_value_error_with_retries(self):
        # Enable retries and run test_update_access_cert_settings_value_error.
        _service.enable_retries()
        self.test_update_access_cert_settings_value_error()

        # Disable retries and run test_update_access_cert_settings_value_error.
        _service.disable_retries()
        self.test_update_access_cert_settings_value_error()


class TestCreateAccessOrganization:
    """
    Test Class for create_access_organization
    """

    @responses.activate
    def test_create_access_organization_all_params(self):
        """
        create_access_organization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/access/organizations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"auth_domain": "01652b251c3ae2787110a995d8db0135.cloudflareaccess.com", "name": "MTLS enabled", "login_design": {"anyKey": "anyValue"}, "created_at": "2019-08-13T16:31:42Z", "updated_at": "2019-08-13T16:31:42Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        name = 'MTLS enabled'
        auth_domain = '01652b251c3ae2787110a995d8db0135.cloudflareaccess.com'

        # Invoke method
        response = _service.create_access_organization(
            name=name,
            auth_domain=auth_domain,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'MTLS enabled'
        assert req_body['auth_domain'] == '01652b251c3ae2787110a995d8db0135.cloudflareaccess.com'

    def test_create_access_organization_all_params_with_retries(self):
        # Enable retries and run test_create_access_organization_all_params.
        _service.enable_retries()
        self.test_create_access_organization_all_params()

        # Disable retries and run test_create_access_organization_all_params.
        _service.disable_retries()
        self.test_create_access_organization_all_params()

    @responses.activate
    def test_create_access_organization_required_params(self):
        """
        test_create_access_organization_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/access/organizations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"auth_domain": "01652b251c3ae2787110a995d8db0135.cloudflareaccess.com", "name": "MTLS enabled", "login_design": {"anyKey": "anyValue"}, "created_at": "2019-08-13T16:31:42Z", "updated_at": "2019-08-13T16:31:42Z"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_access_organization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_access_organization_required_params_with_retries(self):
        # Enable retries and run test_create_access_organization_required_params.
        _service.enable_retries()
        self.test_create_access_organization_required_params()

        # Disable retries and run test_create_access_organization_required_params.
        _service.disable_retries()
        self.test_create_access_organization_required_params()

    @responses.activate
    def test_create_access_organization_value_error(self):
        """
        test_create_access_organization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/access/organizations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"auth_domain": "01652b251c3ae2787110a995d8db0135.cloudflareaccess.com", "name": "MTLS enabled", "login_design": {"anyKey": "anyValue"}, "created_at": "2019-08-13T16:31:42Z", "updated_at": "2019-08-13T16:31:42Z"}}'
        responses.add(
            responses.POST,
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
                _service.create_access_organization(**req_copy)

    def test_create_access_organization_value_error_with_retries(self):
        # Enable retries and run test_create_access_organization_value_error.
        _service.enable_retries()
        self.test_create_access_organization_value_error()

        # Disable retries and run test_create_access_organization_value_error.
        _service.disable_retries()
        self.test_create_access_organization_value_error()


# endregion
##############################################################################
# End of Service: MutualTLS
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AccessOrgRespResult:
    """
    Test Class for AccessOrgRespResult
    """

    def test_access_org_resp_result_serialization(self):
        """
        Test serialization/deserialization for AccessOrgRespResult
        """

        # Construct a json representation of a AccessOrgRespResult model
        access_org_resp_result_model_json = {}
        access_org_resp_result_model_json['auth_domain'] = '01652b251c3ae2787110a995d8db0135.cloudflareaccess.com'
        access_org_resp_result_model_json['name'] = 'MTLS enabled'
        access_org_resp_result_model_json['login_design'] = {}
        access_org_resp_result_model_json['created_at'] = '2019-08-13T16:31:42Z'
        access_org_resp_result_model_json['updated_at'] = '2019-08-13T16:31:42Z'

        # Construct a model instance of AccessOrgRespResult by calling from_dict on the json representation
        access_org_resp_result_model = AccessOrgRespResult.from_dict(access_org_resp_result_model_json)
        assert access_org_resp_result_model != False

        # Construct a model instance of AccessOrgRespResult by calling from_dict on the json representation
        access_org_resp_result_model_dict = AccessOrgRespResult.from_dict(access_org_resp_result_model_json).__dict__
        access_org_resp_result_model2 = AccessOrgRespResult(**access_org_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert access_org_resp_result_model == access_org_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        access_org_resp_result_model_json2 = access_org_resp_result_model.to_dict()
        assert access_org_resp_result_model_json2 == access_org_resp_result_model_json


class TestModel_CreateAccessAppRespResult:
    """
    Test Class for CreateAccessAppRespResult
    """

    def test_create_access_app_resp_result_serialization(self):
        """
        Test serialization/deserialization for CreateAccessAppRespResult
        """

        # Construct a json representation of a CreateAccessAppRespResult model
        create_access_app_resp_result_model_json = {}
        create_access_app_resp_result_model_json['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        create_access_app_resp_result_model_json['name'] = 'mtls-test-app'
        create_access_app_resp_result_model_json['domain'] = 'test.example.com'
        create_access_app_resp_result_model_json['aud'] = 'f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008'
        create_access_app_resp_result_model_json['policies'] = []
        create_access_app_resp_result_model_json['allowed_idps'] = []
        create_access_app_resp_result_model_json['auto_redirect_to_identity'] = False
        create_access_app_resp_result_model_json['session_duration'] = '24h'
        create_access_app_resp_result_model_json['type'] = 'self_hosted'
        create_access_app_resp_result_model_json['uid'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        create_access_app_resp_result_model_json['created_at'] = '2021-04-19T07:59:49Z'
        create_access_app_resp_result_model_json['updated_at'] = '2021-04-19T07:59:49Z'

        # Construct a model instance of CreateAccessAppRespResult by calling from_dict on the json representation
        create_access_app_resp_result_model = CreateAccessAppRespResult.from_dict(create_access_app_resp_result_model_json)
        assert create_access_app_resp_result_model != False

        # Construct a model instance of CreateAccessAppRespResult by calling from_dict on the json representation
        create_access_app_resp_result_model_dict = CreateAccessAppRespResult.from_dict(create_access_app_resp_result_model_json).__dict__
        create_access_app_resp_result_model2 = CreateAccessAppRespResult(**create_access_app_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert create_access_app_resp_result_model == create_access_app_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        create_access_app_resp_result_model_json2 = create_access_app_resp_result_model.to_dict()
        assert create_access_app_resp_result_model_json2 == create_access_app_resp_result_model_json


class TestModel_DeleteAccessAppRespResult:
    """
    Test Class for DeleteAccessAppRespResult
    """

    def test_delete_access_app_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteAccessAppRespResult
        """

        # Construct a json representation of a DeleteAccessAppRespResult model
        delete_access_app_resp_result_model_json = {}
        delete_access_app_resp_result_model_json['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'

        # Construct a model instance of DeleteAccessAppRespResult by calling from_dict on the json representation
        delete_access_app_resp_result_model = DeleteAccessAppRespResult.from_dict(delete_access_app_resp_result_model_json)
        assert delete_access_app_resp_result_model != False

        # Construct a model instance of DeleteAccessAppRespResult by calling from_dict on the json representation
        delete_access_app_resp_result_model_dict = DeleteAccessAppRespResult.from_dict(delete_access_app_resp_result_model_json).__dict__
        delete_access_app_resp_result_model2 = DeleteAccessAppRespResult(**delete_access_app_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_access_app_resp_result_model == delete_access_app_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_access_app_resp_result_model_json2 = delete_access_app_resp_result_model.to_dict()
        assert delete_access_app_resp_result_model_json2 == delete_access_app_resp_result_model_json


class TestModel_DeleteAccessCertRespResult:
    """
    Test Class for DeleteAccessCertRespResult
    """

    def test_delete_access_cert_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteAccessCertRespResult
        """

        # Construct a json representation of a DeleteAccessCertRespResult model
        delete_access_cert_resp_result_model_json = {}
        delete_access_cert_resp_result_model_json['id'] = '21a41336-9001-42c4-8440-c79e0cb86e1f'

        # Construct a model instance of DeleteAccessCertRespResult by calling from_dict on the json representation
        delete_access_cert_resp_result_model = DeleteAccessCertRespResult.from_dict(delete_access_cert_resp_result_model_json)
        assert delete_access_cert_resp_result_model != False

        # Construct a model instance of DeleteAccessCertRespResult by calling from_dict on the json representation
        delete_access_cert_resp_result_model_dict = DeleteAccessCertRespResult.from_dict(delete_access_cert_resp_result_model_json).__dict__
        delete_access_cert_resp_result_model2 = DeleteAccessCertRespResult(**delete_access_cert_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_access_cert_resp_result_model == delete_access_cert_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_access_cert_resp_result_model_json2 = delete_access_cert_resp_result_model.to_dict()
        assert delete_access_cert_resp_result_model_json2 == delete_access_cert_resp_result_model_json


class TestModel_DeleteAccessPolicyRespResult:
    """
    Test Class for DeleteAccessPolicyRespResult
    """

    def test_delete_access_policy_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteAccessPolicyRespResult
        """

        # Construct a json representation of a DeleteAccessPolicyRespResult model
        delete_access_policy_resp_result_model_json = {}
        delete_access_policy_resp_result_model_json['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'

        # Construct a model instance of DeleteAccessPolicyRespResult by calling from_dict on the json representation
        delete_access_policy_resp_result_model = DeleteAccessPolicyRespResult.from_dict(delete_access_policy_resp_result_model_json)
        assert delete_access_policy_resp_result_model != False

        # Construct a model instance of DeleteAccessPolicyRespResult by calling from_dict on the json representation
        delete_access_policy_resp_result_model_dict = DeleteAccessPolicyRespResult.from_dict(delete_access_policy_resp_result_model_json).__dict__
        delete_access_policy_resp_result_model2 = DeleteAccessPolicyRespResult(**delete_access_policy_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_access_policy_resp_result_model == delete_access_policy_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_access_policy_resp_result_model_json2 = delete_access_policy_resp_result_model.to_dict()
        assert delete_access_policy_resp_result_model_json2 == delete_access_policy_resp_result_model_json


class TestModel_PolicyCnRuleCommonName:
    """
    Test Class for PolicyCnRuleCommonName
    """

    def test_policy_cn_rule_common_name_serialization(self):
        """
        Test serialization/deserialization for PolicyCnRuleCommonName
        """

        # Construct a json representation of a PolicyCnRuleCommonName model
        policy_cn_rule_common_name_model_json = {}
        policy_cn_rule_common_name_model_json['common_name'] = 'Access Testing CA'

        # Construct a model instance of PolicyCnRuleCommonName by calling from_dict on the json representation
        policy_cn_rule_common_name_model = PolicyCnRuleCommonName.from_dict(policy_cn_rule_common_name_model_json)
        assert policy_cn_rule_common_name_model != False

        # Construct a model instance of PolicyCnRuleCommonName by calling from_dict on the json representation
        policy_cn_rule_common_name_model_dict = PolicyCnRuleCommonName.from_dict(policy_cn_rule_common_name_model_json).__dict__
        policy_cn_rule_common_name_model2 = PolicyCnRuleCommonName(**policy_cn_rule_common_name_model_dict)

        # Verify the model instances are equivalent
        assert policy_cn_rule_common_name_model == policy_cn_rule_common_name_model2

        # Convert model instance back to dict and verify no loss of data
        policy_cn_rule_common_name_model_json2 = policy_cn_rule_common_name_model.to_dict()
        assert policy_cn_rule_common_name_model_json2 == policy_cn_rule_common_name_model_json


class TestModel_AccessAppResp:
    """
    Test Class for AccessAppResp
    """

    def test_access_app_resp_serialization(self):
        """
        Test serialization/deserialization for AccessAppResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_rule_model = {}  # PolicyRulePolicyCertRule
        policy_rule_model['certificate'] = {}

        policy_result_model = {}  # PolicyResult
        policy_result_model['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['name'] = 'mtls-test-policy'
        policy_result_model['decision'] = 'non_identity'
        policy_result_model['include'] = [policy_rule_model]
        policy_result_model['exclude'] = [policy_rule_model]
        policy_result_model['precedence'] = 1
        policy_result_model['require'] = [policy_rule_model]
        policy_result_model['uid'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['created_at'] = '2021-04-19T08:01:21Z'
        policy_result_model['updated_at'] = '2021-04-19T08:01:21Z'

        app_result_model = {}  # AppResult
        app_result_model['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        app_result_model['name'] = 'mtls-test-app'
        app_result_model['domain'] = 'test.example.com'
        app_result_model['aud'] = 'f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008'
        app_result_model['policies'] = [policy_result_model]
        app_result_model['allowed_idps'] = ['699d98642c564d2e855e9661899b7252']
        app_result_model['auto_redirect_to_identity'] = False
        app_result_model['session_duration'] = '24h'
        app_result_model['type'] = 'self_hosted'
        app_result_model['uid'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        app_result_model['created_at'] = '2021-04-19T07:59:49Z'
        app_result_model['updated_at'] = '2021-04-19T07:59:49Z'

        # Construct a json representation of a AccessAppResp model
        access_app_resp_model_json = {}
        access_app_resp_model_json['success'] = True
        access_app_resp_model_json['errors'] = []
        access_app_resp_model_json['messages'] = []
        access_app_resp_model_json['result'] = app_result_model

        # Construct a model instance of AccessAppResp by calling from_dict on the json representation
        access_app_resp_model = AccessAppResp.from_dict(access_app_resp_model_json)
        assert access_app_resp_model != False

        # Construct a model instance of AccessAppResp by calling from_dict on the json representation
        access_app_resp_model_dict = AccessAppResp.from_dict(access_app_resp_model_json).__dict__
        access_app_resp_model2 = AccessAppResp(**access_app_resp_model_dict)

        # Verify the model instances are equivalent
        assert access_app_resp_model == access_app_resp_model2

        # Convert model instance back to dict and verify no loss of data
        access_app_resp_model_json2 = access_app_resp_model.to_dict()
        assert access_app_resp_model_json2 == access_app_resp_model_json


class TestModel_AccessCertResp:
    """
    Test Class for AccessCertResp
    """

    def test_access_cert_resp_serialization(self):
        """
        Test serialization/deserialization for AccessCertResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cert_result_model = {}  # CertResult
        cert_result_model['id'] = '21a41336-9001-42c4-8440-c79e0cb86e1f'
        cert_result_model['name'] = 'test-cert'
        cert_result_model['fingerprint'] = 'MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F'
        cert_result_model['associated_hostnames'] = ['test.example.com']
        cert_result_model['created_at'] = '2021-04-19T11:09:11Z'
        cert_result_model['updated_at'] = '2021-04-19T11:09:11Z'
        cert_result_model['expires_on'] = '2026-04-18T06:26:00Z'

        # Construct a json representation of a AccessCertResp model
        access_cert_resp_model_json = {}
        access_cert_resp_model_json['success'] = True
        access_cert_resp_model_json['errors'] = []
        access_cert_resp_model_json['messages'] = []
        access_cert_resp_model_json['result'] = cert_result_model

        # Construct a model instance of AccessCertResp by calling from_dict on the json representation
        access_cert_resp_model = AccessCertResp.from_dict(access_cert_resp_model_json)
        assert access_cert_resp_model != False

        # Construct a model instance of AccessCertResp by calling from_dict on the json representation
        access_cert_resp_model_dict = AccessCertResp.from_dict(access_cert_resp_model_json).__dict__
        access_cert_resp_model2 = AccessCertResp(**access_cert_resp_model_dict)

        # Verify the model instances are equivalent
        assert access_cert_resp_model == access_cert_resp_model2

        # Convert model instance back to dict and verify no loss of data
        access_cert_resp_model_json2 = access_cert_resp_model.to_dict()
        assert access_cert_resp_model_json2 == access_cert_resp_model_json


class TestModel_AccessCertSettingsInputArray:
    """
    Test Class for AccessCertSettingsInputArray
    """

    def test_access_cert_settings_input_array_serialization(self):
        """
        Test serialization/deserialization for AccessCertSettingsInputArray
        """

        # Construct a json representation of a AccessCertSettingsInputArray model
        access_cert_settings_input_array_model_json = {}
        access_cert_settings_input_array_model_json['hostname'] = 'test.example.com'
        access_cert_settings_input_array_model_json['client_certificate_forwarding'] = True

        # Construct a model instance of AccessCertSettingsInputArray by calling from_dict on the json representation
        access_cert_settings_input_array_model = AccessCertSettingsInputArray.from_dict(access_cert_settings_input_array_model_json)
        assert access_cert_settings_input_array_model != False

        # Construct a model instance of AccessCertSettingsInputArray by calling from_dict on the json representation
        access_cert_settings_input_array_model_dict = AccessCertSettingsInputArray.from_dict(access_cert_settings_input_array_model_json).__dict__
        access_cert_settings_input_array_model2 = AccessCertSettingsInputArray(**access_cert_settings_input_array_model_dict)

        # Verify the model instances are equivalent
        assert access_cert_settings_input_array_model == access_cert_settings_input_array_model2

        # Convert model instance back to dict and verify no loss of data
        access_cert_settings_input_array_model_json2 = access_cert_settings_input_array_model.to_dict()
        assert access_cert_settings_input_array_model_json2 == access_cert_settings_input_array_model_json


class TestModel_AccessCertSettingsResp:
    """
    Test Class for AccessCertSettingsResp
    """

    def test_access_cert_settings_resp_serialization(self):
        """
        Test serialization/deserialization for AccessCertSettingsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cert_settings_result_model = {}  # CertSettingsResult
        cert_settings_result_model['hostname'] = 'test.example.com'
        cert_settings_result_model['china_network'] = False
        cert_settings_result_model['client_certificate_forwarding'] = True

        # Construct a json representation of a AccessCertSettingsResp model
        access_cert_settings_resp_model_json = {}
        access_cert_settings_resp_model_json['success'] = True
        access_cert_settings_resp_model_json['errors'] = []
        access_cert_settings_resp_model_json['messages'] = []
        access_cert_settings_resp_model_json['result'] = [cert_settings_result_model]

        # Construct a model instance of AccessCertSettingsResp by calling from_dict on the json representation
        access_cert_settings_resp_model = AccessCertSettingsResp.from_dict(access_cert_settings_resp_model_json)
        assert access_cert_settings_resp_model != False

        # Construct a model instance of AccessCertSettingsResp by calling from_dict on the json representation
        access_cert_settings_resp_model_dict = AccessCertSettingsResp.from_dict(access_cert_settings_resp_model_json).__dict__
        access_cert_settings_resp_model2 = AccessCertSettingsResp(**access_cert_settings_resp_model_dict)

        # Verify the model instances are equivalent
        assert access_cert_settings_resp_model == access_cert_settings_resp_model2

        # Convert model instance back to dict and verify no loss of data
        access_cert_settings_resp_model_json2 = access_cert_settings_resp_model.to_dict()
        assert access_cert_settings_resp_model_json2 == access_cert_settings_resp_model_json


class TestModel_AccessOrgResp:
    """
    Test Class for AccessOrgResp
    """

    def test_access_org_resp_serialization(self):
        """
        Test serialization/deserialization for AccessOrgResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        access_org_resp_result_model = {}  # AccessOrgRespResult
        access_org_resp_result_model['auth_domain'] = '01652b251c3ae2787110a995d8db0135.cloudflareaccess.com'
        access_org_resp_result_model['name'] = 'MTLS enabled'
        access_org_resp_result_model['login_design'] = {}
        access_org_resp_result_model['created_at'] = '2019-08-13T16:31:42Z'
        access_org_resp_result_model['updated_at'] = '2019-08-13T16:31:42Z'

        # Construct a json representation of a AccessOrgResp model
        access_org_resp_model_json = {}
        access_org_resp_model_json['success'] = True
        access_org_resp_model_json['errors'] = []
        access_org_resp_model_json['messages'] = []
        access_org_resp_model_json['result'] = access_org_resp_result_model

        # Construct a model instance of AccessOrgResp by calling from_dict on the json representation
        access_org_resp_model = AccessOrgResp.from_dict(access_org_resp_model_json)
        assert access_org_resp_model != False

        # Construct a model instance of AccessOrgResp by calling from_dict on the json representation
        access_org_resp_model_dict = AccessOrgResp.from_dict(access_org_resp_model_json).__dict__
        access_org_resp_model2 = AccessOrgResp(**access_org_resp_model_dict)

        # Verify the model instances are equivalent
        assert access_org_resp_model == access_org_resp_model2

        # Convert model instance back to dict and verify no loss of data
        access_org_resp_model_json2 = access_org_resp_model.to_dict()
        assert access_org_resp_model_json2 == access_org_resp_model_json


class TestModel_AccessPolicyResp:
    """
    Test Class for AccessPolicyResp
    """

    def test_access_policy_resp_serialization(self):
        """
        Test serialization/deserialization for AccessPolicyResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_rule_model = {}  # PolicyRulePolicyCertRule
        policy_rule_model['certificate'] = {}

        policy_result_model = {}  # PolicyResult
        policy_result_model['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['name'] = 'mtls-test-policy'
        policy_result_model['decision'] = 'non_identity'
        policy_result_model['include'] = [policy_rule_model]
        policy_result_model['exclude'] = [policy_rule_model]
        policy_result_model['precedence'] = 1
        policy_result_model['require'] = [policy_rule_model]
        policy_result_model['uid'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['created_at'] = '2021-04-19T08:01:21Z'
        policy_result_model['updated_at'] = '2021-04-19T08:01:21Z'

        # Construct a json representation of a AccessPolicyResp model
        access_policy_resp_model_json = {}
        access_policy_resp_model_json['success'] = True
        access_policy_resp_model_json['errors'] = []
        access_policy_resp_model_json['messages'] = []
        access_policy_resp_model_json['result'] = policy_result_model

        # Construct a model instance of AccessPolicyResp by calling from_dict on the json representation
        access_policy_resp_model = AccessPolicyResp.from_dict(access_policy_resp_model_json)
        assert access_policy_resp_model != False

        # Construct a model instance of AccessPolicyResp by calling from_dict on the json representation
        access_policy_resp_model_dict = AccessPolicyResp.from_dict(access_policy_resp_model_json).__dict__
        access_policy_resp_model2 = AccessPolicyResp(**access_policy_resp_model_dict)

        # Verify the model instances are equivalent
        assert access_policy_resp_model == access_policy_resp_model2

        # Convert model instance back to dict and verify no loss of data
        access_policy_resp_model_json2 = access_policy_resp_model.to_dict()
        assert access_policy_resp_model_json2 == access_policy_resp_model_json


class TestModel_AppResult:
    """
    Test Class for AppResult
    """

    def test_app_result_serialization(self):
        """
        Test serialization/deserialization for AppResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_rule_model = {}  # PolicyRulePolicyCertRule
        policy_rule_model['certificate'] = {}

        policy_result_model = {}  # PolicyResult
        policy_result_model['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['name'] = 'mtls-test-policy'
        policy_result_model['decision'] = 'non_identity'
        policy_result_model['include'] = [policy_rule_model]
        policy_result_model['exclude'] = [policy_rule_model]
        policy_result_model['precedence'] = 1
        policy_result_model['require'] = [policy_rule_model]
        policy_result_model['uid'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['created_at'] = '2021-04-19T08:01:21Z'
        policy_result_model['updated_at'] = '2021-04-19T08:01:21Z'

        # Construct a json representation of a AppResult model
        app_result_model_json = {}
        app_result_model_json['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        app_result_model_json['name'] = 'mtls-test-app'
        app_result_model_json['domain'] = 'test.example.com'
        app_result_model_json['aud'] = 'f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008'
        app_result_model_json['policies'] = [policy_result_model]
        app_result_model_json['allowed_idps'] = ['699d98642c564d2e855e9661899b7252']
        app_result_model_json['auto_redirect_to_identity'] = False
        app_result_model_json['session_duration'] = '24h'
        app_result_model_json['type'] = 'self_hosted'
        app_result_model_json['uid'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        app_result_model_json['created_at'] = '2021-04-19T07:59:49Z'
        app_result_model_json['updated_at'] = '2021-04-19T07:59:49Z'

        # Construct a model instance of AppResult by calling from_dict on the json representation
        app_result_model = AppResult.from_dict(app_result_model_json)
        assert app_result_model != False

        # Construct a model instance of AppResult by calling from_dict on the json representation
        app_result_model_dict = AppResult.from_dict(app_result_model_json).__dict__
        app_result_model2 = AppResult(**app_result_model_dict)

        # Verify the model instances are equivalent
        assert app_result_model == app_result_model2

        # Convert model instance back to dict and verify no loss of data
        app_result_model_json2 = app_result_model.to_dict()
        assert app_result_model_json2 == app_result_model_json


class TestModel_CertResult:
    """
    Test Class for CertResult
    """

    def test_cert_result_serialization(self):
        """
        Test serialization/deserialization for CertResult
        """

        # Construct a json representation of a CertResult model
        cert_result_model_json = {}
        cert_result_model_json['id'] = '21a41336-9001-42c4-8440-c79e0cb86e1f'
        cert_result_model_json['name'] = 'test-cert'
        cert_result_model_json['fingerprint'] = 'MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F'
        cert_result_model_json['associated_hostnames'] = ['test.example.com']
        cert_result_model_json['created_at'] = '2021-04-19T11:09:11Z'
        cert_result_model_json['updated_at'] = '2021-04-19T11:09:11Z'
        cert_result_model_json['expires_on'] = '2026-04-18T06:26:00Z'

        # Construct a model instance of CertResult by calling from_dict on the json representation
        cert_result_model = CertResult.from_dict(cert_result_model_json)
        assert cert_result_model != False

        # Construct a model instance of CertResult by calling from_dict on the json representation
        cert_result_model_dict = CertResult.from_dict(cert_result_model_json).__dict__
        cert_result_model2 = CertResult(**cert_result_model_dict)

        # Verify the model instances are equivalent
        assert cert_result_model == cert_result_model2

        # Convert model instance back to dict and verify no loss of data
        cert_result_model_json2 = cert_result_model.to_dict()
        assert cert_result_model_json2 == cert_result_model_json


class TestModel_CertSettingsResult:
    """
    Test Class for CertSettingsResult
    """

    def test_cert_settings_result_serialization(self):
        """
        Test serialization/deserialization for CertSettingsResult
        """

        # Construct a json representation of a CertSettingsResult model
        cert_settings_result_model_json = {}
        cert_settings_result_model_json['hostname'] = 'test.example.com'
        cert_settings_result_model_json['china_network'] = False
        cert_settings_result_model_json['client_certificate_forwarding'] = True

        # Construct a model instance of CertSettingsResult by calling from_dict on the json representation
        cert_settings_result_model = CertSettingsResult.from_dict(cert_settings_result_model_json)
        assert cert_settings_result_model != False

        # Construct a model instance of CertSettingsResult by calling from_dict on the json representation
        cert_settings_result_model_dict = CertSettingsResult.from_dict(cert_settings_result_model_json).__dict__
        cert_settings_result_model2 = CertSettingsResult(**cert_settings_result_model_dict)

        # Verify the model instances are equivalent
        assert cert_settings_result_model == cert_settings_result_model2

        # Convert model instance back to dict and verify no loss of data
        cert_settings_result_model_json2 = cert_settings_result_model.to_dict()
        assert cert_settings_result_model_json2 == cert_settings_result_model_json


class TestModel_CreateAccessAppResp:
    """
    Test Class for CreateAccessAppResp
    """

    def test_create_access_app_resp_serialization(self):
        """
        Test serialization/deserialization for CreateAccessAppResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        create_access_app_resp_result_model = {}  # CreateAccessAppRespResult
        create_access_app_resp_result_model['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        create_access_app_resp_result_model['name'] = 'mtls-test-app'
        create_access_app_resp_result_model['domain'] = 'test.example.com'
        create_access_app_resp_result_model['aud'] = 'f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008'
        create_access_app_resp_result_model['policies'] = []
        create_access_app_resp_result_model['allowed_idps'] = []
        create_access_app_resp_result_model['auto_redirect_to_identity'] = False
        create_access_app_resp_result_model['session_duration'] = '24h'
        create_access_app_resp_result_model['type'] = 'self_hosted'
        create_access_app_resp_result_model['uid'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        create_access_app_resp_result_model['created_at'] = '2021-04-19T07:59:49Z'
        create_access_app_resp_result_model['updated_at'] = '2021-04-19T07:59:49Z'

        # Construct a json representation of a CreateAccessAppResp model
        create_access_app_resp_model_json = {}
        create_access_app_resp_model_json['success'] = True
        create_access_app_resp_model_json['errors'] = []
        create_access_app_resp_model_json['messages'] = []
        create_access_app_resp_model_json['result'] = create_access_app_resp_result_model

        # Construct a model instance of CreateAccessAppResp by calling from_dict on the json representation
        create_access_app_resp_model = CreateAccessAppResp.from_dict(create_access_app_resp_model_json)
        assert create_access_app_resp_model != False

        # Construct a model instance of CreateAccessAppResp by calling from_dict on the json representation
        create_access_app_resp_model_dict = CreateAccessAppResp.from_dict(create_access_app_resp_model_json).__dict__
        create_access_app_resp_model2 = CreateAccessAppResp(**create_access_app_resp_model_dict)

        # Verify the model instances are equivalent
        assert create_access_app_resp_model == create_access_app_resp_model2

        # Convert model instance back to dict and verify no loss of data
        create_access_app_resp_model_json2 = create_access_app_resp_model.to_dict()
        assert create_access_app_resp_model_json2 == create_access_app_resp_model_json


class TestModel_DeleteAccessAppResp:
    """
    Test Class for DeleteAccessAppResp
    """

    def test_delete_access_app_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteAccessAppResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_access_app_resp_result_model = {}  # DeleteAccessAppRespResult
        delete_access_app_resp_result_model['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'

        # Construct a json representation of a DeleteAccessAppResp model
        delete_access_app_resp_model_json = {}
        delete_access_app_resp_model_json['success'] = True
        delete_access_app_resp_model_json['errors'] = []
        delete_access_app_resp_model_json['messages'] = []
        delete_access_app_resp_model_json['result'] = delete_access_app_resp_result_model

        # Construct a model instance of DeleteAccessAppResp by calling from_dict on the json representation
        delete_access_app_resp_model = DeleteAccessAppResp.from_dict(delete_access_app_resp_model_json)
        assert delete_access_app_resp_model != False

        # Construct a model instance of DeleteAccessAppResp by calling from_dict on the json representation
        delete_access_app_resp_model_dict = DeleteAccessAppResp.from_dict(delete_access_app_resp_model_json).__dict__
        delete_access_app_resp_model2 = DeleteAccessAppResp(**delete_access_app_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_access_app_resp_model == delete_access_app_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_access_app_resp_model_json2 = delete_access_app_resp_model.to_dict()
        assert delete_access_app_resp_model_json2 == delete_access_app_resp_model_json


class TestModel_DeleteAccessCertResp:
    """
    Test Class for DeleteAccessCertResp
    """

    def test_delete_access_cert_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteAccessCertResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_access_cert_resp_result_model = {}  # DeleteAccessCertRespResult
        delete_access_cert_resp_result_model['id'] = '21a41336-9001-42c4-8440-c79e0cb86e1f'

        # Construct a json representation of a DeleteAccessCertResp model
        delete_access_cert_resp_model_json = {}
        delete_access_cert_resp_model_json['success'] = True
        delete_access_cert_resp_model_json['errors'] = []
        delete_access_cert_resp_model_json['messages'] = []
        delete_access_cert_resp_model_json['result'] = delete_access_cert_resp_result_model

        # Construct a model instance of DeleteAccessCertResp by calling from_dict on the json representation
        delete_access_cert_resp_model = DeleteAccessCertResp.from_dict(delete_access_cert_resp_model_json)
        assert delete_access_cert_resp_model != False

        # Construct a model instance of DeleteAccessCertResp by calling from_dict on the json representation
        delete_access_cert_resp_model_dict = DeleteAccessCertResp.from_dict(delete_access_cert_resp_model_json).__dict__
        delete_access_cert_resp_model2 = DeleteAccessCertResp(**delete_access_cert_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_access_cert_resp_model == delete_access_cert_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_access_cert_resp_model_json2 = delete_access_cert_resp_model.to_dict()
        assert delete_access_cert_resp_model_json2 == delete_access_cert_resp_model_json


class TestModel_DeleteAccessPolicyResp:
    """
    Test Class for DeleteAccessPolicyResp
    """

    def test_delete_access_policy_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteAccessPolicyResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_access_policy_resp_result_model = {}  # DeleteAccessPolicyRespResult
        delete_access_policy_resp_result_model['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'

        # Construct a json representation of a DeleteAccessPolicyResp model
        delete_access_policy_resp_model_json = {}
        delete_access_policy_resp_model_json['success'] = True
        delete_access_policy_resp_model_json['errors'] = []
        delete_access_policy_resp_model_json['messages'] = []
        delete_access_policy_resp_model_json['result'] = delete_access_policy_resp_result_model

        # Construct a model instance of DeleteAccessPolicyResp by calling from_dict on the json representation
        delete_access_policy_resp_model = DeleteAccessPolicyResp.from_dict(delete_access_policy_resp_model_json)
        assert delete_access_policy_resp_model != False

        # Construct a model instance of DeleteAccessPolicyResp by calling from_dict on the json representation
        delete_access_policy_resp_model_dict = DeleteAccessPolicyResp.from_dict(delete_access_policy_resp_model_json).__dict__
        delete_access_policy_resp_model2 = DeleteAccessPolicyResp(**delete_access_policy_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_access_policy_resp_model == delete_access_policy_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_access_policy_resp_model_json2 = delete_access_policy_resp_model.to_dict()
        assert delete_access_policy_resp_model_json2 == delete_access_policy_resp_model_json


class TestModel_ListAccessAppsResp:
    """
    Test Class for ListAccessAppsResp
    """

    def test_list_access_apps_resp_serialization(self):
        """
        Test serialization/deserialization for ListAccessAppsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_rule_model = {}  # PolicyRulePolicyCertRule
        policy_rule_model['certificate'] = {}

        policy_result_model = {}  # PolicyResult
        policy_result_model['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['name'] = 'mtls-test-policy'
        policy_result_model['decision'] = 'non_identity'
        policy_result_model['include'] = [policy_rule_model]
        policy_result_model['exclude'] = [policy_rule_model]
        policy_result_model['precedence'] = 1
        policy_result_model['require'] = [policy_rule_model]
        policy_result_model['uid'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['created_at'] = '2021-04-19T08:01:21Z'
        policy_result_model['updated_at'] = '2021-04-19T08:01:21Z'

        app_result_model = {}  # AppResult
        app_result_model['id'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        app_result_model['name'] = 'mtls-test-app'
        app_result_model['domain'] = 'test.example.com'
        app_result_model['aud'] = 'f8e1744453ea3679d919fdc6db58cff648f2b14b33a729f780fc02e75a42a008'
        app_result_model['policies'] = [policy_result_model]
        app_result_model['allowed_idps'] = ['699d98642c564d2e855e9661899b7252']
        app_result_model['auto_redirect_to_identity'] = False
        app_result_model['session_duration'] = '24h'
        app_result_model['type'] = 'self_hosted'
        app_result_model['uid'] = 'de4526d6-d125-4f95-906f-1757510a9cd8'
        app_result_model['created_at'] = '2021-04-19T07:59:49Z'
        app_result_model['updated_at'] = '2021-04-19T07:59:49Z'

        # Construct a json representation of a ListAccessAppsResp model
        list_access_apps_resp_model_json = {}
        list_access_apps_resp_model_json['success'] = True
        list_access_apps_resp_model_json['errors'] = []
        list_access_apps_resp_model_json['messages'] = []
        list_access_apps_resp_model_json['result'] = [app_result_model]

        # Construct a model instance of ListAccessAppsResp by calling from_dict on the json representation
        list_access_apps_resp_model = ListAccessAppsResp.from_dict(list_access_apps_resp_model_json)
        assert list_access_apps_resp_model != False

        # Construct a model instance of ListAccessAppsResp by calling from_dict on the json representation
        list_access_apps_resp_model_dict = ListAccessAppsResp.from_dict(list_access_apps_resp_model_json).__dict__
        list_access_apps_resp_model2 = ListAccessAppsResp(**list_access_apps_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_access_apps_resp_model == list_access_apps_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_access_apps_resp_model_json2 = list_access_apps_resp_model.to_dict()
        assert list_access_apps_resp_model_json2 == list_access_apps_resp_model_json


class TestModel_ListAccessCertsResp:
    """
    Test Class for ListAccessCertsResp
    """

    def test_list_access_certs_resp_serialization(self):
        """
        Test serialization/deserialization for ListAccessCertsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cert_result_model = {}  # CertResult
        cert_result_model['id'] = '21a41336-9001-42c4-8440-c79e0cb86e1f'
        cert_result_model['name'] = 'test-cert'
        cert_result_model['fingerprint'] = 'MD5 Fingerprint=38:38:B4:FB:3C:33:CE:2C:8E:8E:D1:1B:94:70:C1:5F'
        cert_result_model['associated_hostnames'] = ['test.example.com']
        cert_result_model['created_at'] = '2021-04-19T11:09:11Z'
        cert_result_model['updated_at'] = '2021-04-19T11:09:11Z'
        cert_result_model['expires_on'] = '2026-04-18T06:26:00Z'

        # Construct a json representation of a ListAccessCertsResp model
        list_access_certs_resp_model_json = {}
        list_access_certs_resp_model_json['success'] = True
        list_access_certs_resp_model_json['errors'] = []
        list_access_certs_resp_model_json['messages'] = []
        list_access_certs_resp_model_json['result'] = [cert_result_model]

        # Construct a model instance of ListAccessCertsResp by calling from_dict on the json representation
        list_access_certs_resp_model = ListAccessCertsResp.from_dict(list_access_certs_resp_model_json)
        assert list_access_certs_resp_model != False

        # Construct a model instance of ListAccessCertsResp by calling from_dict on the json representation
        list_access_certs_resp_model_dict = ListAccessCertsResp.from_dict(list_access_certs_resp_model_json).__dict__
        list_access_certs_resp_model2 = ListAccessCertsResp(**list_access_certs_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_access_certs_resp_model == list_access_certs_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_access_certs_resp_model_json2 = list_access_certs_resp_model.to_dict()
        assert list_access_certs_resp_model_json2 == list_access_certs_resp_model_json


class TestModel_ListAccessPoliciesResp:
    """
    Test Class for ListAccessPoliciesResp
    """

    def test_list_access_policies_resp_serialization(self):
        """
        Test serialization/deserialization for ListAccessPoliciesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_rule_model = {}  # PolicyRulePolicyCertRule
        policy_rule_model['certificate'] = {}

        policy_result_model = {}  # PolicyResult
        policy_result_model['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['name'] = 'mtls-test-policy'
        policy_result_model['decision'] = 'non_identity'
        policy_result_model['include'] = [policy_rule_model]
        policy_result_model['exclude'] = [policy_rule_model]
        policy_result_model['precedence'] = 1
        policy_result_model['require'] = [policy_rule_model]
        policy_result_model['uid'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model['created_at'] = '2021-04-19T08:01:21Z'
        policy_result_model['updated_at'] = '2021-04-19T08:01:21Z'

        # Construct a json representation of a ListAccessPoliciesResp model
        list_access_policies_resp_model_json = {}
        list_access_policies_resp_model_json['success'] = True
        list_access_policies_resp_model_json['errors'] = []
        list_access_policies_resp_model_json['messages'] = []
        list_access_policies_resp_model_json['result'] = [policy_result_model]

        # Construct a model instance of ListAccessPoliciesResp by calling from_dict on the json representation
        list_access_policies_resp_model = ListAccessPoliciesResp.from_dict(list_access_policies_resp_model_json)
        assert list_access_policies_resp_model != False

        # Construct a model instance of ListAccessPoliciesResp by calling from_dict on the json representation
        list_access_policies_resp_model_dict = ListAccessPoliciesResp.from_dict(list_access_policies_resp_model_json).__dict__
        list_access_policies_resp_model2 = ListAccessPoliciesResp(**list_access_policies_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_access_policies_resp_model == list_access_policies_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_access_policies_resp_model_json2 = list_access_policies_resp_model.to_dict()
        assert list_access_policies_resp_model_json2 == list_access_policies_resp_model_json


class TestModel_PolicyResult:
    """
    Test Class for PolicyResult
    """

    def test_policy_result_serialization(self):
        """
        Test serialization/deserialization for PolicyResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_rule_model = {}  # PolicyRulePolicyCertRule
        policy_rule_model['certificate'] = {}

        # Construct a json representation of a PolicyResult model
        policy_result_model_json = {}
        policy_result_model_json['id'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model_json['name'] = 'mtls-test-policy'
        policy_result_model_json['decision'] = 'non_identity'
        policy_result_model_json['include'] = [policy_rule_model]
        policy_result_model_json['exclude'] = [policy_rule_model]
        policy_result_model_json['precedence'] = 1
        policy_result_model_json['require'] = [policy_rule_model]
        policy_result_model_json['uid'] = 'acabcdb1-afb3-4f61-9dae-d1a353a93661'
        policy_result_model_json['created_at'] = '2021-04-19T08:01:21Z'
        policy_result_model_json['updated_at'] = '2021-04-19T08:01:21Z'

        # Construct a model instance of PolicyResult by calling from_dict on the json representation
        policy_result_model = PolicyResult.from_dict(policy_result_model_json)
        assert policy_result_model != False

        # Construct a model instance of PolicyResult by calling from_dict on the json representation
        policy_result_model_dict = PolicyResult.from_dict(policy_result_model_json).__dict__
        policy_result_model2 = PolicyResult(**policy_result_model_dict)

        # Verify the model instances are equivalent
        assert policy_result_model == policy_result_model2

        # Convert model instance back to dict and verify no loss of data
        policy_result_model_json2 = policy_result_model.to_dict()
        assert policy_result_model_json2 == policy_result_model_json


class TestModel_PolicyRulePolicyCertRule:
    """
    Test Class for PolicyRulePolicyCertRule
    """

    def test_policy_rule_policy_cert_rule_serialization(self):
        """
        Test serialization/deserialization for PolicyRulePolicyCertRule
        """

        # Construct a json representation of a PolicyRulePolicyCertRule model
        policy_rule_policy_cert_rule_model_json = {}
        policy_rule_policy_cert_rule_model_json['certificate'] = {}

        # Construct a model instance of PolicyRulePolicyCertRule by calling from_dict on the json representation
        policy_rule_policy_cert_rule_model = PolicyRulePolicyCertRule.from_dict(policy_rule_policy_cert_rule_model_json)
        assert policy_rule_policy_cert_rule_model != False

        # Construct a model instance of PolicyRulePolicyCertRule by calling from_dict on the json representation
        policy_rule_policy_cert_rule_model_dict = PolicyRulePolicyCertRule.from_dict(policy_rule_policy_cert_rule_model_json).__dict__
        policy_rule_policy_cert_rule_model2 = PolicyRulePolicyCertRule(**policy_rule_policy_cert_rule_model_dict)

        # Verify the model instances are equivalent
        assert policy_rule_policy_cert_rule_model == policy_rule_policy_cert_rule_model2

        # Convert model instance back to dict and verify no loss of data
        policy_rule_policy_cert_rule_model_json2 = policy_rule_policy_cert_rule_model.to_dict()
        assert policy_rule_policy_cert_rule_model_json2 == policy_rule_policy_cert_rule_model_json


class TestModel_PolicyRulePolicyCnRule:
    """
    Test Class for PolicyRulePolicyCnRule
    """

    def test_policy_rule_policy_cn_rule_serialization(self):
        """
        Test serialization/deserialization for PolicyRulePolicyCnRule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        policy_cn_rule_common_name_model = {}  # PolicyCnRuleCommonName
        policy_cn_rule_common_name_model['common_name'] = 'Access Testing CA'

        # Construct a json representation of a PolicyRulePolicyCnRule model
        policy_rule_policy_cn_rule_model_json = {}
        policy_rule_policy_cn_rule_model_json['common_name'] = policy_cn_rule_common_name_model

        # Construct a model instance of PolicyRulePolicyCnRule by calling from_dict on the json representation
        policy_rule_policy_cn_rule_model = PolicyRulePolicyCnRule.from_dict(policy_rule_policy_cn_rule_model_json)
        assert policy_rule_policy_cn_rule_model != False

        # Construct a model instance of PolicyRulePolicyCnRule by calling from_dict on the json representation
        policy_rule_policy_cn_rule_model_dict = PolicyRulePolicyCnRule.from_dict(policy_rule_policy_cn_rule_model_json).__dict__
        policy_rule_policy_cn_rule_model2 = PolicyRulePolicyCnRule(**policy_rule_policy_cn_rule_model_dict)

        # Verify the model instances are equivalent
        assert policy_rule_policy_cn_rule_model == policy_rule_policy_cn_rule_model2

        # Convert model instance back to dict and verify no loss of data
        policy_rule_policy_cn_rule_model_json2 = policy_rule_policy_cn_rule_model.to_dict()
        assert policy_rule_policy_cn_rule_model_json2 == policy_rule_policy_cn_rule_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
