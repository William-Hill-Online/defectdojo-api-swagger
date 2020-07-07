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
from defectdojo_api_client.models.tool_configuration import ToolConfiguration  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestToolConfiguration(unittest.TestCase):
    """ToolConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ToolConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.tool_configuration.ToolConfiguration()  # noqa: E501
        if include_optional :
            return ToolConfiguration(
                id = 56, 
                configuration_url = '0', 
                name = '0', 
                description = '0', 
                url = '0', 
                authentication_type = 'API', 
                username = '0', 
                password = '0', 
                auth_title = '0', 
                ssh = '0', 
                api_key = '0', 
                tool_type = 56
            )
        else :
            return ToolConfiguration(
                configuration_url = '0',
                name = '0',
                tool_type = 56,
        )

    def testToolConfiguration(self):
        """Test ToolConfiguration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
