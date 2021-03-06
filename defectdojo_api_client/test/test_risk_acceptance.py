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
from defectdojo_api_client.models.risk_acceptance import RiskAcceptance  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestRiskAcceptance(unittest.TestCase):
    """RiskAcceptance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RiskAcceptance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.risk_acceptance.RiskAcceptance()  # noqa: E501
        if include_optional :
            return RiskAcceptance(
                id = 56, 
                name = '0', 
                path = '0', 
                accepted_by = '0', 
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                compensating_control = '0', 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                owner = 56, 
                accepted_findings = [
                    56
                    ], 
                notes = [
                    56
                    ]
            )
        else :
            return RiskAcceptance(
                name = '0',
                owner = 56,
                accepted_findings = [
                    56
                    ],
        )

    def testRiskAcceptance(self):
        """Test RiskAcceptance"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
