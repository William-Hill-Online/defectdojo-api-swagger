# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JIRA(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'project_key': 'str',
        'component': 'str',
        'push_all_issues': 'bool',
        'enable_engagement_epic_mapping': 'bool',
        'push_notes': 'bool',
        'product': 'int',
        'conf': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_key': 'project_key',
        'component': 'component',
        'push_all_issues': 'push_all_issues',
        'enable_engagement_epic_mapping': 'enable_engagement_epic_mapping',
        'push_notes': 'push_notes',
        'product': 'product',
        'conf': 'conf'
    }

    def __init__(self, id=None, project_key=None, component=None, push_all_issues=None, enable_engagement_epic_mapping=None, push_notes=None, product=None, conf=None):  # noqa: E501
        """JIRA - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._project_key = None
        self._component = None
        self._push_all_issues = None
        self._enable_engagement_epic_mapping = None
        self._push_notes = None
        self._product = None
        self._conf = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_key is not None:
            self.project_key = project_key
        if component is not None:
            self.component = component
        if push_all_issues is not None:
            self.push_all_issues = push_all_issues
        if enable_engagement_epic_mapping is not None:
            self.enable_engagement_epic_mapping = enable_engagement_epic_mapping
        if push_notes is not None:
            self.push_notes = push_notes
        self.product = product
        if conf is not None:
            self.conf = conf

    @property
    def id(self):
        """Gets the id of this JIRA.  # noqa: E501


        :return: The id of this JIRA.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JIRA.


        :param id: The id of this JIRA.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_key(self):
        """Gets the project_key of this JIRA.  # noqa: E501


        :return: The project_key of this JIRA.  # noqa: E501
        :rtype: str
        """
        return self._project_key

    @project_key.setter
    def project_key(self, project_key):
        """Sets the project_key of this JIRA.


        :param project_key: The project_key of this JIRA.  # noqa: E501
        :type: str
        """
        if project_key is not None and len(project_key) > 200:
            raise ValueError("Invalid value for `project_key`, length must be less than or equal to `200`")  # noqa: E501

        self._project_key = project_key

    @property
    def component(self):
        """Gets the component of this JIRA.  # noqa: E501


        :return: The component of this JIRA.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this JIRA.


        :param component: The component of this JIRA.  # noqa: E501
        :type: str
        """
        if component is not None and len(component) > 200:
            raise ValueError("Invalid value for `component`, length must be less than or equal to `200`")  # noqa: E501

        self._component = component

    @property
    def push_all_issues(self):
        """Gets the push_all_issues of this JIRA.  # noqa: E501

        Automatically maintain parity with JIRA. Always create and update JIRA tickets for findings in this Product.  # noqa: E501

        :return: The push_all_issues of this JIRA.  # noqa: E501
        :rtype: bool
        """
        return self._push_all_issues

    @push_all_issues.setter
    def push_all_issues(self, push_all_issues):
        """Sets the push_all_issues of this JIRA.

        Automatically maintain parity with JIRA. Always create and update JIRA tickets for findings in this Product.  # noqa: E501

        :param push_all_issues: The push_all_issues of this JIRA.  # noqa: E501
        :type: bool
        """

        self._push_all_issues = push_all_issues

    @property
    def enable_engagement_epic_mapping(self):
        """Gets the enable_engagement_epic_mapping of this JIRA.  # noqa: E501


        :return: The enable_engagement_epic_mapping of this JIRA.  # noqa: E501
        :rtype: bool
        """
        return self._enable_engagement_epic_mapping

    @enable_engagement_epic_mapping.setter
    def enable_engagement_epic_mapping(self, enable_engagement_epic_mapping):
        """Sets the enable_engagement_epic_mapping of this JIRA.


        :param enable_engagement_epic_mapping: The enable_engagement_epic_mapping of this JIRA.  # noqa: E501
        :type: bool
        """

        self._enable_engagement_epic_mapping = enable_engagement_epic_mapping

    @property
    def push_notes(self):
        """Gets the push_notes of this JIRA.  # noqa: E501


        :return: The push_notes of this JIRA.  # noqa: E501
        :rtype: bool
        """
        return self._push_notes

    @push_notes.setter
    def push_notes(self, push_notes):
        """Sets the push_notes of this JIRA.


        :param push_notes: The push_notes of this JIRA.  # noqa: E501
        :type: bool
        """

        self._push_notes = push_notes

    @property
    def product(self):
        """Gets the product of this JIRA.  # noqa: E501


        :return: The product of this JIRA.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this JIRA.


        :param product: The product of this JIRA.  # noqa: E501
        :type: int
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def conf(self):
        """Gets the conf of this JIRA.  # noqa: E501


        :return: The conf of this JIRA.  # noqa: E501
        :rtype: int
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this JIRA.


        :param conf: The conf of this JIRA.  # noqa: E501
        :type: int
        """

        self._conf = conf

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JIRA, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JIRA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other