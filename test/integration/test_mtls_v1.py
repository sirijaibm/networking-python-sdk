# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute MTLS
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import MtlsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestMtlsV1(unittest.TestCase):
    """ Test class to call MTLS sdk functions """

    @unittest.skip("Authentication failing")
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = MtlsV1.new_instance(
                            service_name="cis_services", crn=self.crn)
        self.service.set_service_url(self.endpoint)        
        self._clean_access_policies()
        self._clean_access_applications()
        self._clean_access_certificates()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_access_policies()
        self._clean_access_applications()
        self._clean_access_certificates()
        print("Clean up complete")
        
    def _clean_access_certificates(self):
        response = self.service.list_access_certificates(zone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result()['result']
        if resp is not None:
           for record in resp:
               self.service.delete_access_certificate(
                   zone_id=self.zone_id,
                   cert_id=record.get("id")
            )  
    
    def _clean_access_applications(self):
        response = self.service.list_access_applications(zone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result()['result']
        if resp is not None:
           for record in resp:
               self.service.delete_access_application(
                   zone_id=self.zone_id,
                   app_id=record.get("id")
            ) 
    
    def _clean_access_policies(self):
        # First get all applications
        response = self.service.list_access_applications(zone_id=self.zone_id)
        if response is not None and response.status_code == 200:
            apps = response.get_result()['result']
            if apps is not None:
                for app in apps:
                    app_id = app.get("id")
                    # Get policies for each application
                    policy_response = self.service.list_access_policies(
                        zone_id=self.zone_id,
                        app_id=app_id
                    )
                    if policy_response is not None and policy_response.status_code == 200:
                        policies = policy_response.get_result()['result']
                        if policies is not None:
                            for policy in policies:
                                self.service.delete_access_policy(
                                    zone_id=self.zone_id,
                                    app_id=app_id,
                                    policy_id=policy.get("id")
                                )
    
    def _create_access_certificate(self, name, certificate):
        """ create access certificate """
        response = self.service.create_access_certificate(
            zone_id=self.zone_id,
            name=name,
            certificate=certificate,
            associated_hostnames=['example.com']
        )
        assert response is not None and response.get_status_code() == 201
        cert_id = response.get_result()['result']['id']
        return cert_id
    
    def _create_access_application(self, name, domain):
        """ create access application """
        response = self.service.create_access_application(
            zone_id=self.zone_id,
            name=name,
            domain=domain,
            session_duration='24h'
        )
        assert response is not None and response.get_status_code() == 201
        app_id = response.get_result()['result']['id']
        return app_id
    
            
    ################## create access certificate ######################
    def test_1_create_access_certificate(self):
        """ test for success """
        name = 'My Test Certificate'
        certificate = '-----BEGIN CERTIFICATE-----\nMIIBkTCB+wIJAIxdK4iNZEqcMA0GCSqGSIb3DQEBCwUAMCExHzAdBgNVBAoMFkF1\ndGhlbnRpY2F0ZWQgT3JpZ2luIENBMB4XDTE5MDEwMTAwMDAwMFoXDTI5MDEwMTAw\nMDAwMFowITEfMB0GA1UECgwWQXV0aGVudGljYXRlZCBPcmlnaW4gQ0EwXDANBgkq\nhkiG9w0BAQEFAANLADBIAkEAqGb8ovgPfTkfz+MichikfnZ0dXIcJmHV81TbC0vj\n+J1FP80X96+OdZJZ+LsWbOB6hBg0+nMjvOAaEuvGj4VDdQIDAQABMA0GCSqGSIb3\nDQEBCwUAA0EAU4BfQKbT1+pxGoVN+cfUwhLAq4hBYB38Sfhn9VYt+VJ2VsPQEb8V\nZgkeJ0Lrry5W7kDBtIMwLJL+FzUjH4Flvw==\n-----END CERTIFICATE-----'
        
        response = self.service.create_access_certificate(
            zone_id=self.zone_id,
            name=name,
            certificate=certificate,
            associated_hostnames=['example.com']
        )
        assert response is not None and response.get_status_code() == 201
        cert_id = response.get_result()['result']['id']
        return cert_id
        
    
    ################## list access certificates ###################
    def test_2_list_access_certificates(self):
        """ test for success """
        self.test_1_create_access_certificate()
        
        response = self.service.list_access_certificates(zone_id=self.zone_id) 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get access certificate by id ###################
    def test_3_get_access_certificate(self):
        """ test for success """
        cert_id = self.test_1_create_access_certificate()
        
        response = self.service.get_access_certificate(
            zone_id=self.zone_id,
            cert_id=cert_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == cert_id
        
    ################## update access certificate ###################
    def test_4_update_access_certificate(self):
        """ test for success """
        cert_id = self.test_1_create_access_certificate()
        
        response = self.service.update_access_certificate(
            zone_id=self.zone_id,
            cert_id=cert_id,
            name='Updated Certificate Name',
            associated_hostnames=['updated.example.com']
        )
        assert response is not None and response.get_status_code() == 200
        updated_cert_id = response.get_result()['result']['id']
        assert updated_cert_id == cert_id
        return updated_cert_id
        
    ################## delete access certificate ###################        
    def test_5_delete_access_certificate(self):
        """ test for success """
        cert_id = self.test_4_update_access_certificate()
        
        response = self.service.delete_access_certificate(
            zone_id=self.zone_id,
            cert_id=cert_id
        )
        assert response is not None and response.get_status_code() == 200
        delete_cert_id = response.get_result()['result']['id']
        assert delete_cert_id == cert_id
        
    ################## create access application ######################
    def test_6_create_access_application(self):
        """ test for success """
        name = 'My Test Application'
        domain = 'test.example.com'
        
        response = self.service.create_access_application(
            zone_id=self.zone_id,
            name=name,
            domain=domain,
            session_duration='24h'
        )
        assert response is not None and response.get_status_code() == 201
        app_id = response.get_result()['result']['id']
        return app_id
        
    ################## list access applications ###################
    def test_7_list_access_applications(self):
        """ test for success """
        self.test_6_create_access_application()
        
        response = self.service.list_access_applications(zone_id=self.zone_id) 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get access application by id ###################
    def test_8_get_access_application(self):
        """ test for success """
        app_id = self.test_6_create_access_application()
        
        response = self.service.get_access_application(
            zone_id=self.zone_id,
            app_id=app_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == app_id
        
    ################## update access application ###################
    def test_9_update_access_application(self):
        """ test for success """
        app_id = self.test_6_create_access_application()
        
        response = self.service.update_access_application(
            zone_id=self.zone_id,
            app_id=app_id,
            name='Updated Application Name',
            domain='updated.example.com',
            session_duration='12h'
        )
        assert response is not None and response.get_status_code() == 200
        updated_app_id = response.get_result()['result']['id']
        assert updated_app_id == app_id
        return updated_app_id
        
    ################## delete access application ###################        
    def test_10_delete_access_application(self):
        """ test for success """
        app_id = self.test_9_update_access_application()
        
        response = self.service.delete_access_application(
            zone_id=self.zone_id,
            app_id=app_id
        )
        assert response is not None and response.get_status_code() == 200
        delete_app_id = response.get_result()['result']['id']
        assert delete_app_id == app_id
        
    ################## create access policy ######################
    def test_11_create_access_policy(self):
        """ test for success """
        app_id = self._create_access_application(
            name='Policy Test Application',
            domain='policy.example.com'
        )
        
        # Construct policy rule
        policy_rule_model = {
            'certificate': {}
        }
        
        response = self.service.create_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            name='My Test Policy',
            decision='allow',
            include=[policy_rule_model]
        )
        assert response is not None and response.get_status_code() == 201
        policy_id = response.get_result()['result']['id']
        return app_id, policy_id
        
    ################## list access policies ###################
    def test_12_list_access_policies(self):
        """ test for success """
        app_id, policy_id = self.test_11_create_access_policy()
        
        response = self.service.list_access_policies(
            zone_id=self.zone_id,
            app_id=app_id
        ) 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get access policy by id ###################
    def test_13_get_access_policy(self):
        """ test for success """
        app_id, policy_id = self.test_11_create_access_policy()
        
        response = self.service.get_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            policy_id=policy_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == policy_id
        
    ################## update access policy ###################
    def test_14_update_access_policy(self):
        """ test for success """
        app_id, policy_id = self.test_11_create_access_policy()
        
        # Construct updated policy rule
        policy_rule_model = {
            'certificate': {}
        }
        
        response = self.service.update_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            policy_id=policy_id,
            name='Updated Policy Name',
            decision='allow',
            include=[policy_rule_model]
        )
        assert response is not None and response.get_status_code() == 200
        updated_policy_id = response.get_result()['result']['id']
        assert updated_policy_id == policy_id
        return app_id, updated_policy_id
        
    ################## delete access policy ###################        
    def test_15_delete_access_policy(self):
        """ test for success """
        app_id, policy_id = self.test_14_update_access_policy()
        
        response = self.service.delete_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            policy_id=policy_id
        )
        assert response is not None and response.get_status_code() == 200
        delete_policy_id = response.get_result()['result']['id']
        assert delete_policy_id == policy_id
        
    ################## get access cert settings ###################
    def test_16_get_access_cert_settings(self):
        """ test for success """
        response = self.service.get_access_cert_settings(zone_id=self.zone_id)
        assert response is not None and response.get_status_code() == 200
        
    ################## update access cert settings ###################
    def test_17_update_access_cert_settings(self):
        """ test for success """
        # Construct settings
        settings_model = {
            'hostname': 'example.com',
            'client_certificate_forwarding': True
        }
        
        response = self.service.update_access_cert_settings(
            zone_id=self.zone_id,
            settings=[settings_model]
        )
        assert response is not None and response.get_status_code() == 200
        
    ################## create access organization ######################
    def test_18_create_access_organization(self):
        """ test for success """
        response = self.service.create_access_organization(
            name='My Test Organization',
            auth_domain='test-org.cloudflareaccess.com'
        )
        assert response is not None and response.get_status_code() == 201
        
if __name__ == '__main__':
    unittest.main()
