# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from defectdojo_api_client.configuration import Configuration


class User(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'last_login': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'last_login': 'last_login'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, email=None, last_login=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._last_login = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        self.last_login = last_login

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 150):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `150`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and not re.search(r'^[\w.@+-]+$', username)):  # noqa: E501
            raise ValueError(r"Invalid value for `username`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 30):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 150):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `150`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type email: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501


        :return: The last_login of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.


        :param last_login: The last_login of this User.  # noqa: E501
        :type last_login: datetime
        """

        self._last_login = last_login

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
