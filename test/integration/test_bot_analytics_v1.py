# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code for Bot Analytics Service
"""

import os
import unittest
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.bot_analytics_v1 import BotAnalyticsV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestBotAnalyticsV1(unittest.TestCase):
    """ Bot Analytics API test class """

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.bot_analytics = BotAnalyticsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.bot_analytics.set_service_url(self.endpoint)

        self.until = datetime.utcnow()
        self.since = self.until - timedelta(days=1)

    def tearDown(self):
        """ tear down """
        print("Clean up complete")

    def test_1_get_bot_score(self):
        """ test for success """
        response = self.bot_analytics.get_bot_score(
            since=self.since,
            until=self.until,
        )
        assert response is not None
        assert response.status_code == 200

    def test_2_get_bot_timeseries(self):
        """ test for success """
        response = self.bot_analytics.get_bot_timeseries(
            since=self.since,
            until=self.until,
        )
        assert response is not None
        assert response.status_code == 200

    def test_3_get_bot_topns(self):
        """ test for success """
        response = self.bot_analytics.get_bot_topns(
            since=self.since,
            until=self.until,
        )
        assert response is not None
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
