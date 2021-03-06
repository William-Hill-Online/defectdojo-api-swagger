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
from defectdojo_api_client.models.system_settings import SystemSettings  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestSystemSettings(unittest.TestCase):
    """SystemSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.system_settings.SystemSettings()  # noqa: E501
        if include_optional :
            return SystemSettings(
                enable_auditlog = True, 
                enable_deduplication = True, 
                delete_dupulicates = True, 
                max_dupes = 56, 
                enable_jira = True, 
                enable_benchmark = True, 
                enable_product_grade = True, 
                enable_finding_sla = True
            )
        else :
            return SystemSettings(
        )

    def testSystemSettings(self):
        """Test SystemSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
