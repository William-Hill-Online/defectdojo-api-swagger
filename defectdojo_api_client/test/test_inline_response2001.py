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
from defectdojo_api_client.models.inline_response2001 import InlineResponse2001  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestInlineResponse2001(unittest.TestCase):
    """InlineResponse2001 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2001
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.inline_response2001.InlineResponse2001()  # noqa: E501
        if include_optional :
            return InlineResponse2001(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    defectdojo_api_client.models.endpoint.Endpoint(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        protocol = '0', 
                        host = '0', 
                        fqdn = '0', 
                        port = -2147483648, 
                        path = '0', 
                        query = '0', 
                        fragment = '0', 
                        remediated = True, 
                        product = 56, 
                        endpoint_params = [
                            56
                            ], )
                    ]
            )
        else :
            return InlineResponse2001(
                count = 56,
                results = [
                    defectdojo_api_client.models.endpoint.Endpoint(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        protocol = '0', 
                        host = '0', 
                        fqdn = '0', 
                        port = -2147483648, 
                        path = '0', 
                        query = '0', 
                        fragment = '0', 
                        remediated = True, 
                        product = 56, 
                        endpoint_params = [
                            56
                            ], )
                    ],
        )

    def testInlineResponse2001(self):
        """Test InlineResponse2001"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
