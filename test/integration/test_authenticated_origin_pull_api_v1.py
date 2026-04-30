# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Authenticated Origin Pull API
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import AuthenticatedOriginPullApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestAuthenticatedOriginPullApiV1(unittest.TestCase):
    """ Test class to call Authenticated Origin Pull API sdk functions """

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = AuthenticatedOriginPullApiV1.new_instance(
            service_name="cis_services", crn=self.crn, zone_identifier=self.zone_id)
        self.service.set_service_url(self.endpoint)
        self._clean_zone_certificates()
        self._clean_hostname_certificates()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_zone_certificates()
        self._clean_hostname_certificates()
        print("Clean up complete")

    def _clean_zone_certificates(self):
        """ Clean up zone-level certificates """
        response = self.service.list_zone_origin_pull_certificates()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get('result')
        if resp is not None:
            for record in resp:
                self.service.delete_zone_origin_pull_certificate(
                    cert_identifier=record.get("id")
                )

    def _clean_hostname_certificates(self):
        """ Clean up hostname-level certificates """
        response = self.service.list_all_per_hostname_authenticated_origin_pull_certificates()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get('result')
        if resp is not None:
            for record in resp:
                self.service.delete_hostname_origin_pull_certificate(
                    cert_identifier=record.get("id")
                )

    def _upload_zone_certificate(self):
        """ Helper to upload a zone-level certificate """
        certificate = """-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKL0UG+mRKSzMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQwHhcNMTcwODIzMTUxMDEyWhcNMTgwODIzMTUxMDEyWjBF
MQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50
ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
CgKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmGdtcGbg/1
CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKnabIRuGvB
KwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpidtnKX/a+5
0GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+pyFxIXjbEI
dZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pEewooaeO2
izNTERcG9HzAacbVRn2Y2SWIyT/0aQIDAQABo1AwTjAdBgNVHQ4EFgQULwWKBQNL
L9s3cb3tTnyPVg+mpCMwHwYDVR0jBBgwFoAULwWKBQNLL9s3cb3tTnyPVg+mpCMw
DAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEANmBZbythkGZyJcpUoXhp
vNVbP8sWkdL+3Fy/FauVYOvkNBKKmHpMvJi8RyPXB3JkUWxFvyFqLLgJJLqmKFLx
-----END CERTIFICATE-----"""
        private_key = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBBeh61yX37mKQ
bNXpwzNa1Y8kepNPfClsSRFT1jPuWC912YZ21wZuD/UIZm7SMkaQyimmhSjhzd22
zeLCpFiYGKRQ/vvDBjZAaYNnDYW+QkImUqdpshG4a8ErDMRIheAqTbTXppM/r90C
MQfKjpJ6gryWQjJJS8rR/I5WWyISwKY6mJ22cpf9r7nQaMHv0IkfgRHaUtVmeF48
VH/NQ7I/FlBDidod/vK79vmOE7R/x/C36nIXEheNsQh1mWJZGREy3Osc4kiGuYnY
DUnuI6uKttvCKWXCOM1VRY9/cgncz3ZL2kR7Cihp47aLM1MRFwb0fMBpxtVGfZjZ
JYjJP/RpAgMBAAECggEAMfQYgVHODkNr0L1p8VJNJqZqQJmLqLqLqLqLqLqLqLqL
-----END PRIVATE KEY-----"""
        response = self.service.upload_zone_origin_pull_certificate(
            certificate=certificate,
            private_key=private_key
        )
        assert response is not None and response.get_status_code() == 201
        cert_id = response.get_result()['result']['id']
        return cert_id

    def _upload_hostname_certificate(self):
        """ Helper to upload a hostname-level certificate """
        certificate = """-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKL0UG+mRKSzMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQwHhcNMTcwODIzMTUxMDEyWhcNMTgwODIzMTUxMDEyWjBF
MQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50
ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
CgKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmGdtcGbg/1
CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKnabIRuGvB
KwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpidtnKX/a+5
0GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+pyFxIXjbEI
dZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pEewooaeO2
izNTERcG9HzAacbVRn2Y2SWIyT/0aQIDAQABo1AwTjAdBgNVHQ4EFgQULwWKBQNL
L9s3cb3tTnyPVg+mpCMwHwYDVR0jBBgwFoAULwWKBQNLL9s3cb3tTnyPVg+mpCMw
DAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEANmBZbythkGZyJcpUoXhp
vNVbP8sWkdL+3Fy/FauVYOvkNBKKmHpMvJi8RyPXB3JkUWxFvyFqLLgJJLqmKFLx
-----END CERTIFICATE-----"""
        private_key = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBBeh61yX37mKQ
bNXpwzNa1Y8kepNPfClsSRFT1jPuWC912YZ21wZuD/UIZm7SMkaQyimmhSjhzd22
zeLCpFiYGKRQ/vvDBjZAaYNnDYW+QkImUqdpshG4a8ErDMRIheAqTbTXppM/r90C
MQfKjpJ6gryWQjJJS8rR/I5WWyISwKY6mJ22cpf9r7nQaMHv0IkfgRHaUtVmeF48
VH/NQ7I/FlBDidod/vK79vmOE7R/x/C36nIXEheNsQh1mWJZGREy3Osc4kiGuYnY
DUnuI6uKttvCKWXCOM1VRY9/cgncz3ZL2kR7Cihp47aLM1MRFwb0fMBpxtVGfZjZ
JYjJP/RpAgMBAAECggEAMfQYgVHODkNr0L1p8VJNJqZqQJmLqLqLqLqLqLqLqLqL
-----END PRIVATE KEY-----"""
        response = self.service.upload_hostname_origin_pull_certificate(
            certificate=certificate,
            private_key=private_key
        )
        assert response is not None and response.get_status_code() == 201
        cert_id = response.get_result()['result']['id']
        return cert_id

    ################## Zone-Level Authenticated Origin Pull Tests ##################

    def test_1_get_zone_origin_pull_settings(self):
        """ test get zone origin pull settings """
        response = self.service.get_zone_origin_pull_settings()
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result'] is not None

    def test_2_set_zone_origin_pull_settings(self):
        """ test set zone origin pull settings """
        response = self.service.set_zone_origin_pull_settings(
            enabled=True
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['enabled'] == True

    def test_3_list_zone_origin_pull_certificates(self):
        """ test list zone origin pull certificates """
        response = self.service.list_zone_origin_pull_certificates()
        assert response is not None and response.get_status_code() == 200
        assert 'result' in response.get_result()

    def test_4_upload_zone_origin_pull_certificate(self):
        """ test upload zone origin pull certificate """
        cert_id = self._upload_zone_certificate()
        assert cert_id is not None
        return cert_id

    def test_5_get_zone_origin_pull_certificate(self):
        """ test get zone origin pull certificate """
        cert_id = self.test_4_upload_zone_origin_pull_certificate()
        response = self.service.get_zone_origin_pull_certificate(
            cert_identifier=cert_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == cert_id

    def test_6_delete_zone_origin_pull_certificate(self):
        """ test delete zone origin pull certificate """
        cert_id = self.test_4_upload_zone_origin_pull_certificate()
        response = self.service.delete_zone_origin_pull_certificate(
            cert_identifier=cert_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == cert_id

    ################## Per-Hostname Authenticated Origin Pull Tests ##################

    def test_7_list_all_per_hostname_authenticated_origin_pull_settings(self):
        """ test list all per hostname authenticated origin pull settings """
        response = self.service.list_all_per_hostname_authenticated_origin_pull_settings()
        assert response is not None and response.get_status_code() == 200
        assert 'result' in response.get_result()

    def test_8_set_hostname_origin_pull_settings(self):
        """ test set hostname origin pull settings """
        cert_id = self._upload_hostname_certificate()
        config = [
            {
                'hostname': 'example.com',
                'cert_id': cert_id,
                'enabled': True
            }
        ]
        response = self.service.set_hostname_origin_pull_settings(
            config=config
        )
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1

    def test_9_get_hostname_origin_pull_settings(self):
        """ test get hostname origin pull settings """
        cert_id = self._upload_hostname_certificate()
        hostname = 'example.com'
        config = [
            {
                'hostname': hostname,
                'cert_id': cert_id,
                'enabled': True
            }
        ]
        self.service.set_hostname_origin_pull_settings(config=config)
        
        response = self.service.get_hostname_origin_pull_settings(
            hostname=hostname
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result'] is not None

    def test_10_list_all_per_hostname_authenticated_origin_pull_certificates(self):
        """ test list all per hostname authenticated origin pull certificates """
        response = self.service.list_all_per_hostname_authenticated_origin_pull_certificates()
        assert response is not None and response.get_status_code() == 200
        assert 'result' in response.get_result()

    def test_11_upload_hostname_origin_pull_certificate(self):
        """ test upload hostname origin pull certificate """
        cert_id = self._upload_hostname_certificate()
        assert cert_id is not None
        return cert_id

    def test_12_get_hostname_origin_pull_certificate(self):
        """ test get hostname origin pull certificate """
        cert_id = self.test_11_upload_hostname_origin_pull_certificate()
        response = self.service.get_hostname_origin_pull_certificate(
            cert_identifier=cert_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == cert_id

    def test_13_delete_hostname_origin_pull_certificate(self):
        """ test delete hostname origin pull certificate """
        cert_id = self.test_11_upload_hostname_origin_pull_certificate()
        response = self.service.delete_hostname_origin_pull_certificate(
            cert_identifier=cert_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == cert_id


if __name__ == '__main__':
    unittest.main()
