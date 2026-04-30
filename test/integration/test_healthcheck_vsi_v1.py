# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Healthcheck VSI V1
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import HealthcheckVsiV1
from ibm_cloud_networking_services.healthcheck_vsi_v1 import CustomNetwork

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestHealthcheckVsiV1(unittest.TestCase):
    """ Test class to call healthcheck vsi sdk functions """

    @unittest.skip("Authentication failing")
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = HealthcheckVsiV1.new_instance(
                            service_name="healthcheck_vsi")
        self.service.set_service_url(self.endpoint)
        self.vsi_doc_id = os.getenv("VSI_DOC_ID")
        self.origin_doc_id = os.getenv("ORIGIN_DOC_ID")

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## edit healthcheck vsi ######################
    def test_1_edit_healtcheck_vsi(self):
        """ test for success """
        # Construct a dict representation of a CustomNetwork
        custom_network_model = {}
        custom_network_model['vpc'] = 'crn:v1:bluemix:public:is:us-south:a/123456::vpc:r006-12345678-1234-1234-1234-123456789012'
        custom_network_model['id'] = '0717-12345678-1234-1234-1234-123456789012'
        custom_network_model['ipv4_cidr_block'] = '10.240.0.0/24'
        custom_network_model['ipv4_address'] = '10.240.0.5'

        # Set up parameter values
        vsi_doc_id = self.vsi_doc_id
        vsi_id = 'r006-12345678-1234-1234-1234-123456789012'
        state = 'UP'
        management_address = '10.240.0.4'
        management_subnet = '0717-12345678-1234-1234-1234-123456789012'
        name = 'healthcheck-vsi-1'
        login_credentials = 'encrypted-credentials'
        region = 'us-south'
        az = 'us-south-1'
        customer_networks = [custom_network_model]
        performance_profile = 'bx2-2x8'
        x_correlation_id = 'test-correlation-id'

        # invoke method
        response = self.service.edit_healtcheck_vsi(
            vsi_doc_id=vsi_doc_id,
            vsi_id=vsi_id,
            state=state,
            management_address=management_address,
            management_subnet=management_subnet,
            name=name,
            login_credentials=login_credentials,
            region=region,
            az=az,
            customer_networks=customer_networks,
            performance_profile=performance_profile,
            x_correlation_id=x_correlation_id,
        )
        assert response is not None and response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    ################## update origin status ###################
    def test_2_update_origin_status(self):
        """ test for success """
        # Set up parameter values
        vsi_doc_id = self.vsi_doc_id
        origin_doc_id = self.origin_doc_id
        status = 'UP'
        health_failure_reason = 'SUCCESS'
        x_correlation_id = 'test-correlation-id'

        # invoke method
        response = self.service.update_origin_status(
            vsi_doc_id=vsi_doc_id,
            origin_doc_id=origin_doc_id,
            status=status,
            health_failure_reason=health_failure_reason,
            x_correlation_id=x_correlation_id,
        )
        assert response is not None and response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    ################## update app status ###################
    def test_3_update_app_status(self):
        """ test for success """
        # Set up parameter values
        vsi_doc_id = self.vsi_doc_id
        application = 'custom-resolver'
        health = True
        subnet_crn = 'crn:v1:bluemix:public:is:us-south:a/123456::subnet:0717-12345678-1234-1234-1234-123456789012'
        x_correlation_id = 'test-correlation-id'

        # invoke method
        response = self.service.update_app_status(
            vsi_doc_id=vsi_doc_id,
            application=application,
            health=health,
            subnet_crn=subnet_crn,
            x_correlation_id=x_correlation_id,
        )
        assert response is not None and response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

if __name__ == '__main__':
    unittest.main()
