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
from defectdojo_api_client.models.test_create import TestCreate  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestTestCreate(unittest.TestCase):
    """TestCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TestCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.test_create.TestCreate()  # noqa: E501
        if include_optional :
            return TestCreate(
                id = 56, 
                engagement = 56, 
                notes = [
                    56
                    ], 
                tags = [
                    '0'
                    ], 
                title = '0', 
                description = '0', 
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                estimated_time = '0', 
                actual_time = '0', 
                percent_complete = -2147483648, 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                version = '0', 
                lead = 56, 
                test_type = 56, 
                environment = 56
            )
        else :
            return TestCreate(
                engagement = 56,
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                test_type = 56,
        )

    def testTestCreate(self):
        """Test TestCreate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
