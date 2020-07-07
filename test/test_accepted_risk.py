# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import defectdojo_api_client
from defectdojo_api_client.models.accepted_risk import AcceptedRisk  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestAcceptedRisk(unittest.TestCase):
    """AcceptedRisk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AcceptedRisk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.accepted_risk.AcceptedRisk()  # noqa: E501
        if include_optional :
            return AcceptedRisk(
                cve = '0', 
                justification = '0', 
                accepted_by = '0'
            )
        else :
            return AcceptedRisk(
                cve = '0',
                justification = '0',
                accepted_by = '0',
        )

    def testAcceptedRisk(self):
        """Test AcceptedRisk"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
