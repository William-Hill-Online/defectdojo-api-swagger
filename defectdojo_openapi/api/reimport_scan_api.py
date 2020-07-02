# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from defectdojo_openapi.api_client import ApiClient
from defectdojo_openapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ReimportScanApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reimport_scan_create(self, scan_date, scan_type, test, **kwargs):  # noqa: E501
        """reimport_scan_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reimport_scan_create(scan_date, scan_type, test, async_req=True)
        >>> result = thread.get()

        :param scan_date: (required)
        :type scan_date: date
        :param scan_type: (required)
        :type scan_type: str
        :param test: (required)
        :type test: int
        :param minimum_severity:
        :type minimum_severity: str
        :param active:
        :type active: bool
        :param verified:
        :type verified: bool
        :param endpoint_to_add:
        :type endpoint_to_add: int
        :param file:
        :type file: file
        :param push_to_jira:
        :type push_to_jira: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReImportScan
        """
        kwargs['_return_http_data_only'] = True
        return self.reimport_scan_create_with_http_info(scan_date, scan_type, test, **kwargs)  # noqa: E501

    def reimport_scan_create_with_http_info(self, scan_date, scan_type, test, **kwargs):  # noqa: E501
        """reimport_scan_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reimport_scan_create_with_http_info(scan_date, scan_type, test, async_req=True)
        >>> result = thread.get()

        :param scan_date: (required)
        :type scan_date: date
        :param scan_type: (required)
        :type scan_type: str
        :param test: (required)
        :type test: int
        :param minimum_severity:
        :type minimum_severity: str
        :param active:
        :type active: bool
        :param verified:
        :type verified: bool
        :param endpoint_to_add:
        :type endpoint_to_add: int
        :param file:
        :type file: file
        :param push_to_jira:
        :type push_to_jira: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ReImportScan, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'scan_date',
            'scan_type',
            'test',
            'minimum_severity',
            'active',
            'verified',
            'endpoint_to_add',
            'file',
            'push_to_jira'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reimport_scan_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scan_date' is set
        if self.api_client.client_side_validation and ('scan_date' not in local_var_params or  # noqa: E501
                                                        local_var_params['scan_date'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scan_date` when calling `reimport_scan_create`")  # noqa: E501
        # verify the required parameter 'scan_type' is set
        if self.api_client.client_side_validation and ('scan_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['scan_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scan_type` when calling `reimport_scan_create`")  # noqa: E501
        # verify the required parameter 'test' is set
        if self.api_client.client_side_validation and ('test' not in local_var_params or  # noqa: E501
                                                        local_var_params['test'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `test` when calling `reimport_scan_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'scan_date' in local_var_params:
            form_params.append(('scan_date', local_var_params['scan_date']))  # noqa: E501
        if 'minimum_severity' in local_var_params:
            form_params.append(('minimum_severity', local_var_params['minimum_severity']))  # noqa: E501
        if 'active' in local_var_params:
            form_params.append(('active', local_var_params['active']))  # noqa: E501
        if 'verified' in local_var_params:
            form_params.append(('verified', local_var_params['verified']))  # noqa: E501
        if 'scan_type' in local_var_params:
            form_params.append(('scan_type', local_var_params['scan_type']))  # noqa: E501
        if 'endpoint_to_add' in local_var_params:
            form_params.append(('endpoint_to_add', local_var_params['endpoint_to_add']))  # noqa: E501
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'test' in local_var_params:
            form_params.append(('test', local_var_params['test']))  # noqa: E501
        if 'push_to_jira' in local_var_params:
            form_params.append(('push_to_jira', local_var_params['push_to_jira']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/reimport-scan/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReImportScan',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
