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
from defectdojo_api_swagger.api.finding_templates_api import FindingTemplatesApi  # noqa: E501
from defectdojo_api_swagger.rest import ApiException


class TestFindingTemplatesApi(unittest.TestCase):
    """FindingTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = defectdojo_api_swagger.api.finding_templates_api.FindingTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_finding_templates_create(self):
        """Test case for finding_templates_create

        """
        pass

    def test_finding_templates_list(self):
        """Test case for finding_templates_list

        """
        pass

    def test_finding_templates_partial_update(self):
        """Test case for finding_templates_partial_update

        """
        pass

    def test_finding_templates_read(self):
        """Test case for finding_templates_read

        """
        pass

    def test_finding_templates_update(self):
        """Test case for finding_templates_update

        """
        pass


if __name__ == '__main__':
    unittest.main()