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
        self._clean_access_certificates()
        self._clean_access_applications()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_access_certificates()
        self._clean_access_applications()
        print("Clean up complete")
        
    def _clean_access_certificates(self):
        response = self.service.list_access_certificates(zone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get('result')
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
        resp = response.get_result().get('result')
        if resp is not None:
           for record in resp:
               # Clean policies first
               policies_response = self.service.list_access_policies(
                   zone_id=self.zone_id,
                   app_id=record.get("id")
               )
               if policies_response.status_code == 200:
                   policies = policies_response.get_result().get('result')
                   if policies is not None:
                       for policy in policies:
                           self.service.delete_access_policy(
                               zone_id=self.zone_id,
                               app_id=record.get("id"),
                               policy_id=policy.get("id")
                           )
               # Delete application
               self.service.delete_access_application(
                   zone_id=self.zone_id,
                   app_id=record.get("id")
            ) 
    
    def _create_access_certificate(self):
        """ create access certificate """
        name = 'Test Certificate'
        certificate = '-----BEGIN CERTIFICATE-----\nMIIBkTCB+wIJAIxdK4iNZEqcMA0GCSqGSIb3DQEBCwUAMBExDzANBgNVBAMMBnRlc3RjYTAeFw0xODA5MTkxODI5MDFaFw0xOTA5MTkxODI5MDFaMBExDzANBgNVBAMMBnRlc3RjYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAqCfJfPvJJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKqQjJqzJKq\n-----END CERTIFICATE-----'
        response = self.service.create_access_certificate(
            zone_id=self.zone_id,
            name=name,
            certificate=certificate,
            associated_hostnames=['example.com']
            )
        assert response is not None and response.get_status_code() == 201
        cert_id = response.get_result()['result']['id']
        return cert_id
    
    def _create_access_application(self):
        """ create access application """
        name = 'Test Application'
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
    
            
    ################## create access certificate ######################
    def test_1_create_access_certificate(self):
        """ test for success """
        cert_id = self._create_access_certificate()
        assert cert_id is not None
        return cert_id
        
    
    ################## list access certificates ###################
    def test_2_list_access_certificates(self):
        """ test for success """
        self.test_1_create_access_certificate()
        
        #List certificates
        response = self.service.list_access_certificates(zone_id=self.zone_id) 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get access certificate by id ###################
    def test_3_get_access_certificate(self):
        """ test for success """
        cert_id = self.test_1_create_access_certificate()
        
        #Get certificate
        response = self.service.get_access_certificate(
            zone_id=self.zone_id,
            cert_id=cert_id)
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == cert_id
        
    ################## update access certificate by id ###################
    def test_4_update_access_certificate(self):
        """ test for success """
        cert_id = self.test_1_create_access_certificate()
        
        # Update certificate
        response = self.service.update_access_certificate(
            zone_id=self.zone_id,
            cert_id=cert_id,
            name='Updated Test Certificate',
            associated_hostnames=['updated.example.com']
        )
        assert response is not None and response.get_status_code() == 200
        updated_cert_id = response.get_result()['result']['id']
        assert updated_cert_id == cert_id
        return updated_cert_id
        
    ################# delete access certificate by id ###################
    def test_5_delete_access_certificate(self):
        """ test for success """
        cert_id = self.test_4_update_access_certificate()
        
        #Delete certificate
        response = self.service.delete_access_certificate(
            zone_id=self.zone_id,
            cert_id=cert_id)
        assert response is not None and response.get_status_code() == 200
        delete_cert_id = response.get_result()['result']['id']
        assert delete_cert_id == cert_id
        
    ################## create access application ######################
    def test_6_create_access_application(self):
        """ test for success """
        app_id = self._create_access_application()
        assert app_id is not None
        return app_id
        
    
    ################## list access applications ###################
    def test_7_list_access_applications(self):
        """ test for success """
        self.test_6_create_access_application()
        
        #List applications
        response = self.service.list_access_applications(zone_id=self.zone_id) 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get access application by id ###################
    def test_8_get_access_application(self):
        """ test for success """
        app_id = self.test_6_create_access_application()
        
        #Get application
        response = self.service.get_access_application(
            zone_id=self.zone_id,
            app_id=app_id)
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == app_id
        
    ################## update access application by id ###################
    def test_9_update_access_application(self):
        """ test for success """
        app_id = self.test_6_create_access_application()
        
        # Update application
        response = self.service.update_access_application(
            zone_id=self.zone_id,
            app_id=app_id,
            name='Updated Test Application',
            domain='updated.example.com',
            session_duration='12h'
        )
        assert response is not None and response.get_status_code() == 200
        updated_app_id = response.get_result()['result']['id']
        assert updated_app_id == app_id
        return updated_app_id
        
    ################# delete access application by id ###################
    def test_10_delete_access_application(self):
        """ test for success """
        app_id = self.test_9_update_access_application()
        
        #Delete application
        response = self.service.delete_access_application(
            zone_id=self.zone_id,
            app_id=app_id)
        assert response is not None and response.get_status_code() == 200
        delete_app_id = response.get_result()['result']['id']
        assert delete_app_id == app_id
        
    ################## create access policy ######################
    def test_11_create_access_policy(self):
        """ test for success """
        app_id = self._create_access_application()
        
        # Create policy
        response = self.service.create_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            name='Test Policy',
            decision='allow'
        )
        assert response is not None and response.get_status_code() == 201
        policy_id = response.get_result()['result']['id']
        return app_id, policy_id
        
    
    ################## list access policies ###################
    def test_12_list_access_policies(self):
        """ test for success """
        app_id, policy_id = self.test_11_create_access_policy()
        
        #List policies
        response = self.service.list_access_policies(
            zone_id=self.zone_id,
            app_id=app_id) 
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get access policy by id ###################
    def test_13_get_access_policy(self):
        """ test for success """
        app_id, policy_id = self.test_11_create_access_policy()
        
        #Get policy
        response = self.service.get_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            policy_id=policy_id)
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result']['id'] == policy_id
        
    ################## update access policy by id ###################
    def test_14_update_access_policy(self):
        """ test for success """
        app_id, policy_id = self.test_11_create_access_policy()
        
        # Update policy
        response = self.service.update_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            policy_id=policy_id,
            name='Updated Test Policy',
            decision='deny'
        )
        assert response is not None and response.get_status_code() == 200
        updated_policy_id = response.get_result()['result']['id']
        assert updated_policy_id == policy_id
        return app_id, updated_policy_id
        
    ################# delete access policy by id ###################
    def test_15_delete_access_policy(self):
        """ test for success """
        app_id, policy_id = self.test_14_update_access_policy()
        
        #Delete policy
        response = self.service.delete_access_policy(
            zone_id=self.zone_id,
            app_id=app_id,
            policy_id=policy_id)
        assert response is not None and response.get_status_code() == 200
        delete_policy_id = response.get_result()['result']['id']
        assert delete_policy_id == policy_id
        
    ################## get access cert settings ###################
    def test_16_get_access_cert_settings(self):
        """ test for success """
        
        #Get cert settings
        response = self.service.get_access_cert_settings(zone_id=self.zone_id)
        assert response is not None and response.get_status_code() == 200
        
    ################## update access cert settings ###################
    def test_17_update_access_cert_settings(self):
        """ test for success """
        
        # Update cert settings
        settings = [{
            'hostname': 'example.com',
            'client_certificate_forwarding': True
        }]
        response = self.service.update_access_cert_settings(
            zone_id=self.zone_id,
            settings=settings
        )
        assert response is not None and response.get_status_code() == 200
        
    ################## create access organization ###################
    def test_18_create_access_organization(self):
        """ test for success """
        
        # Create organization
        response = self.service.create_access_organization(
            name='Test Organization',
            auth_domain='test-auth.example.com'
        )
        assert response is not None and response.get_status_code() == 201
        
if __name__ == '__main__':
    unittest.main()
