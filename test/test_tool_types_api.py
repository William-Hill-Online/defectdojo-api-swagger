# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import defectdojo_api_swagger
from defectdojo_api_swagger.api.tool_types_api import ToolTypesApi  # noqa: E501
from defectdojo_api_swagger.rest import ApiException


class TestToolTypesApi(unittest.TestCase):
    """ToolTypesApi unit test stubs"""

    def setUp(self):
        self.api = defectdojo_api_swagger.api.tool_types_api.ToolTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tool_types_create(self):
        """Test case for tool_types_create

        """
        pass

    def test_tool_types_delete(self):
        """Test case for tool_types_delete

        """
        pass

    def test_tool_types_list(self):
        """Test case for tool_types_list

        """
        pass

    def test_tool_types_partial_update(self):
        """Test case for tool_types_partial_update

        """
        pass

    def test_tool_types_read(self):
        """Test case for tool_types_read

        """
        pass

    def test_tool_types_update(self):
        """Test case for tool_types_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
