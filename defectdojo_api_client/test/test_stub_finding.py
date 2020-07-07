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
from defectdojo_api_client.models.stub_finding import StubFinding  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestStubFinding(unittest.TestCase):
    """StubFinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StubFinding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.stub_finding.StubFinding()  # noqa: E501
        if include_optional :
            return StubFinding(
                id = 56, 
                title = '0', 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                severity = '0', 
                description = '0', 
                test = 56, 
                reporter = 56
            )
        else :
            return StubFinding(
                title = '0',
        )

    def testStubFinding(self):
        """Test StubFinding"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
