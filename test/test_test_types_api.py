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
from defectdojo_api_swagger.api.test_types_api import TestTypesApi  # noqa: E501
from defectdojo_api_swagger.rest import ApiException


class TestTestTypesApi(unittest.TestCase):
    """TestTypesApi unit test stubs"""

    def setUp(self):
        self.api = defectdojo_api_swagger.api.test_types_api.TestTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_test_types_create(self):
        """Test case for test_types_create

        """
        pass

    def test_test_types_list(self):
        """Test case for test_types_list

        """
        pass

    def test_test_types_partial_update(self):
        """Test case for test_types_partial_update

        """
        pass

    def test_test_types_read(self):
        """Test case for test_types_read

        """
        pass

    def test_test_types_update(self):
        """Test case for test_types_update

        """
        pass


if __name__ == '__main__':
    unittest.main()