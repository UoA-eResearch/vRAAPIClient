#!/usr/bin/python
__author__ = 'https://github.com/maksteel'

import log, json
from catalog import ConsumerClient
logger = log.getLogger()

class CerConsumerClient(ConsumerClient):
    """
    Class to make CeR entitled catalog items requests to vRA
    +--------------------------------------+-----------------------------------+
    |                 Id                   |                Name               |
    +--------------------------------------+-----------------------------------+
    | e16d4f88-2620-4284-9337-3d0a447c62e4 |             CER-Linux             |
    | 4524185f-695b-46f0-af06-2b99ef2e3ec9 |            CER-Windows            |
    | f6afc33b-cf2a-43d3-b539-787b45935a94 | eResearch Cluster Resource Report |
    | 0e80c697-9650-4bb9-ae40-5c30165a62aa |  eResearch Cluster Storage Report |
    +--------------------------------------+-----------------------------------+
    """

    def __init__(self, username, password, host="m4lbvrap01.uoa.auckland.ac.nz", tenant="Research"):
        """
        Creates a connection to the UoA-ITS-CeR vRA REST API using the provided
        username and password.
        Parameters:
                    user = user account with access to the vRA portal
                    passowrd = valid password for above user
                    host = m4lbvrap01.uoa.auckland.ac.nz (Default)
                    tenant = Research (Default)
        """
        ConsumerClient.__init__(self, host, username, password, tenant)
        self.catalog = self.getEntitledCatalogItemViews(show='json')
        logger.debug(json.dumps(self.catalog, sort_keys=True, indent=4, separators=(',', ': ')))

    def requestEResearchClusterResourceReport(self, email=[], description="[API] resource report", catalogItem=2):
        """
        Function that will submit a request for eResearch Cluster Resource Report and 
        returns the requestID.
        
        Parameters:
            email = list of strings, each string has to be a valid email address
            description = [API] resource report 
            catalogItem = 2, represents resource report
        """
        # Step1: get the request template i.e. a json object that we fill to get the service
        service = self.getEntitledCatalogItemsRequestsTemplate(id=self.catalog[catalogItem]['catalogItemId'])
        logger.debug("Request Template")
        logger.debug(json.dumps(service, sort_keys=True, indent=4, separators=(',', ': ')))

        # Step2: fill the template as per the need
        service["data"]["email"] = email
        service["description"] = description
        logger.debug("Filled Request Template")
        logger.debug(json.dumps(service, sort_keys=True, indent=4, separators=(',', ': ')))

        # Step3: post a request with filled template
        reqId = self.requestEntitledCatalogItemsById(id=self.catalog[catalogItem]['catalogItemId'], payload=service)
        logger.debug("Request Id %s" %reqId)
        return reqId

    def requestEResearchClusterStorageReport(self, email=[], description="[API] storage report", catalogItem=3):
        """
        Function that will submit a request for eResearch Cluster Resource Report and 
        returns the requestID.
        
        Parameters:
            email = list of strings, each string has to be a valid email address
            description = [API] storage report 
            catalogItem = 3, represents storage report
        """
        # Step1: get the request template i.e. a json object that we fill to get the service
        service = self.getEntitledCatalogItemsRequestsTemplate(id=self.catalog[catalogItem]['catalogItemId'])
        logger.debug("Request Template")
        logger.debug(json.dumps(service, sort_keys=True, indent=4, separators=(',', ': ')))

        # Step2: fill the template as per the need
        service["data"]["email"] = email
        service["description"] = description
        logger.debug("Filled Request Template")
        logger.debug(json.dumps(service, sort_keys=True, indent=4, separators=(',', ': ')))

        # Step3: post a request with filled template
        reqId = self.requestEntitledCatalogItemsById(id=self.catalog[catalogItem]['catalogItemId'], payload=service)
        logger.debug("Request Id %s" %reqId)
        return reqId