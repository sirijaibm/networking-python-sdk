# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.

"""
Integration test code to execute Edge Functions API
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import EdgeFunctionsApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')

class TestEdgeFunctionsApiV1(unittest.TestCase):
    """ Test class to call edge functions api sdk functions """

    @unittest.skip("Authentication failing")
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.service = EdgeFunctionsApiV1.new_instance(
                            service_name="cis_services", crn=self.crn, zone_identifier=self.zone_id)
        self.service.set_service_url(self.endpoint)        
        self._clean_edge_functions_actions()
        self._clean_edge_functions_triggers()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_edge_functions_actions()
        self._clean_edge_functions_triggers()
        print("Clean up complete")
        
    def _clean_edge_functions_actions(self):
        response = self.service.list_edge_functions_actions()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get('result')
        if resp is not None:
           for record in resp:
               script_name = record.get("id")
               if script_name:
                   self.service.delete_edge_functions_action(
                       script_name=script_name
                   )  
    
    def _clean_edge_functions_triggers(self):
        response = self.service.list_edge_functions_triggers()
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get('result')
        if resp is not None:
           for record in resp:
               route_id = record.get("id")
               if route_id:
                   self.service.delete_edge_functions_trigger(
                       route_id=route_id
                   ) 
    
    def _create_edge_functions_action(self, script_name):
        """ create edge functions action """
        edge_functions_action = """
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  return new Response('Hello from Edge Function!', {
    headers: { 'content-type': 'text/plain' },
  })
}
"""
        response = self.service.update_edge_functions_action(
            script_name=script_name,
            edge_functions_action=edge_functions_action
        )
        assert response is not None and response.get_status_code() == 200
        return script_name
    
    def _create_edge_functions_trigger(self, pattern, script):
        """ create edge functions trigger """
        response = self.service.create_edge_functions_trigger(
            pattern=pattern,
            script=script
        )
        assert response is not None and response.get_status_code() == 200
        route_id = response.get_result()['result']['id']
        return route_id
    
    ################## list edge functions actions ######################
    def test_1_list_edge_functions_actions(self):
        """ test for success """
        script_name = 'test-script-list'
        self._create_edge_functions_action(script_name=script_name)
        
        response = self.service.list_edge_functions_actions()
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result'] is not None
        
    ################## update edge functions action ######################
    def test_2_update_edge_functions_action(self):
        """ test for success """
        script_name = 'test-script-update'
        edge_functions_action = """
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  return new Response('Updated Edge Function!', {
    headers: { 'content-type': 'text/plain' },
  })
}
"""
        response = self.service.update_edge_functions_action(
            script_name=script_name,
            edge_functions_action=edge_functions_action
        )
        assert response is not None and response.get_status_code() == 200
        
    ################## get edge functions action ######################
    def test_3_get_edge_functions_action(self):
        """ test for success """
        script_name = 'test-script-get'
        self._create_edge_functions_action(script_name=script_name)
        
        response = self.service.get_edge_functions_action(
            script_name=script_name
        )
        assert response is not None and response.get_status_code() == 200
        
    ################## delete edge functions action ######################
    def test_4_delete_edge_functions_action(self):
        """ test for success """
        script_name = 'test-script-delete'
        self._create_edge_functions_action(script_name=script_name)
        
        response = self.service.delete_edge_functions_action(
            script_name=script_name
        )
        assert response is not None and response.get_status_code() == 200
        delete_result = response.get_result()['result']
        assert delete_result is not None
        
    ################## create edge functions trigger ######################
    def test_5_create_edge_functions_trigger(self):
        """ test for success """
        script_name = 'test-script-trigger'
        self._create_edge_functions_action(script_name=script_name)
        
        pattern = 'example.com/*'
        response = self.service.create_edge_functions_trigger(
            pattern=pattern,
            script=script_name
        )
        assert response is not None and response.get_status_code() == 200
        route_id = response.get_result()['result']['id']
        return route_id
        
    ################## list edge functions triggers ######################
    def test_6_list_edge_functions_triggers(self):
        """ test for success """
        self.test_5_create_edge_functions_trigger()
        
        response = self.service.list_edge_functions_triggers()
        assert response is not None and response.get_status_code() == 200
        assert len(response.get_result()['result']) >= 1
        
    ################## get edge functions trigger ######################
    def test_7_get_edge_functions_trigger(self):
        """ test for success """
        route_id = self.test_5_create_edge_functions_trigger()
        
        response = self.service.get_edge_functions_trigger(
            route_id=route_id
        )
        assert response is not None and response.get_status_code() == 200
        assert response.get_result()['result'] is not None
        
    ################## update edge functions trigger ######################
    def test_8_update_edge_functions_trigger(self):
        """ test for success """
        route_id = self.test_5_create_edge_functions_trigger()
        
        script_name = 'test-script-trigger-updated'
        self._create_edge_functions_action(script_name=script_name)
        
        pattern = 'example.com/updated/*'
        response = self.service.update_edge_functions_trigger(
            route_id=route_id,
            pattern=pattern,
            script=script_name
        )
        assert response is not None and response.get_status_code() == 200
        updated_route_id = response.get_result()['result']['id']
        assert updated_route_id == route_id
        
    ################## delete edge functions trigger ######################
    def test_9_delete_edge_functions_trigger(self):
        """ test for success """
        route_id = self.test_5_create_edge_functions_trigger()
        
        response = self.service.delete_edge_functions_trigger(
            route_id=route_id
        )
        assert response is not None and response.get_status_code() == 200
        delete_result = response.get_result()['result']
        assert delete_result is not None
        
if __name__ == '__main__':
    unittest.main()
