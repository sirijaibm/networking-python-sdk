# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Bot Management
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import BotManagementV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestBotManagementV1(unittest.TestCase):
    """ Test class to call bot management sdk functions """

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = BotManagementV1.new_instance(
                            service_name="cis_services",
                            crn=self.crn,
                            zone_identifier=self.zone_id)
        self.service.set_service_url(self.endpoint)

        response = self.service.get_bot_management()
        assert response is not None
        assert response.status_code == 200
        result = response.get_result()['result']
        self.fight_mode = result.get('fight_mode')
        self.session_score = result.get('session_score')
        self.enable_js = result.get('enable_js')
        self.auth_id_logging = result.get('auth_id_logging')
        self.use_latest_model = result.get('use_latest_model')

    def tearDown(self):
        """ tear down """
        response = self.service.update_bot_management(
            fight_mode=self.fight_mode,
            session_score=self.session_score,
            enable_js=self.enable_js,
            auth_id_logging=self.auth_id_logging,
            use_latest_model=self.use_latest_model,
        )
        assert response is not None
        assert response.get_status_code() == 200
        print("Clean up complete")

    ################## get Bot management setting ######################
    def test_1_get_bot_management(self):
        """ test for success """
        response = self.service.get_bot_management()
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result'] is not None

    ################## update Bot management setting ###################
    def test_2_update_bot_management(self):
        """ test for success """
        response = self.service.update_bot_management(
            fight_mode=self.fight_mode,
            session_score=self.session_score,
            enable_js=self.enable_js,
            auth_id_logging=self.auth_id_logging,
            use_latest_model=self.use_latest_model,
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result'] is not None


if __name__ == '__main__':
    unittest.main()
