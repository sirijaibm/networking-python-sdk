# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Bot Analytics
"""

import os
import unittest
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import BotAnalyticsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestBotAnalyticsV1(unittest.TestCase):
    """ Test class to call bot analytics sdk functions """

    @unittest.skip("Authentication failing")
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = BotAnalyticsV1.new_instance(
                            service_name="cis_services", 
                            crn=self.crn,
                            zone_identifier=self.zone_id)
        self.service.set_service_url(self.endpoint)
        
        # Set up time range for queries (last 24 hours)
        self.until = datetime.utcnow()
        self.since = self.until - timedelta(days=1)

    def tearDown(self):
        """ tear down """
        print("Clean up complete")
        
    ################## get bot score ######################
    def test_1_get_bot_score(self):
        """ test for success """
        response = self.service.get_bot_score(
            since=self.since,
            until=self.until
        )
        assert response is not None and response.get_status_code() == 200
        result = response.get_result()
        assert result is not None
        assert 'success' in result
        assert 'result' in result
    
    ################## get bot timeseries ######################
    def test_2_get_bot_timeseries(self):
        """ test for success """
        response = self.service.get_bot_timeseries(
            since=self.since,
            until=self.until
        )
        assert response is not None and response.get_status_code() == 200
        result = response.get_result()
        assert result is not None
        assert 'success' in result
        assert 'result' in result
        
    ################## get bot topns ######################
    def test_3_get_bot_topns(self):
        """ test for success """
        response = self.service.get_bot_topns(
            since=self.since,
            until=self.until
        )
        assert response is not None and response.get_status_code() == 200
        result = response.get_result()
        assert result is not None
        assert 'success' in result
        assert 'result' in result

if __name__ == '__main__':
    unittest.main()
