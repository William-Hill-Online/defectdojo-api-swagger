# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import defectdojo_api_client
from defectdojo_api_client.api.scans_api import ScansApi  # noqa: E501
from defectdojo_api_client.rest import ApiException


class TestScansApi(unittest.TestCase):
    """ScansApi unit test stubs"""

    def setUp(self):
        self.api = defectdojo_api_client.api.scans_api.ScansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_scans_list(self):
        """Test case for scans_list

        """
        pass

    def test_scans_read(self):
        """Test case for scans_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
