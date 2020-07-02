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

from defectdojo_openapi.configuration import Configuration


class RiskAcceptance(object):
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
        'name': 'str',
        'path': 'str',
        'accepted_by': 'str',
        'expiration_date': 'datetime',
        'compensating_control': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'owner': 'int',
        'accepted_findings': 'list[int]',
        'notes': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'accepted_by': 'accepted_by',
        'expiration_date': 'expiration_date',
        'compensating_control': 'compensating_control',
        'created': 'created',
        'updated': 'updated',
        'owner': 'owner',
        'accepted_findings': 'accepted_findings',
        'notes': 'notes'
    }

    def __init__(self, id=None, name=None, path=None, accepted_by=None, expiration_date=None, compensating_control=None, created=None, updated=None, owner=None, accepted_findings=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """RiskAcceptance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._path = None
        self._accepted_by = None
        self._expiration_date = None
        self._compensating_control = None
        self._created = None
        self._updated = None
        self._owner = None
        self._accepted_findings = None
        self._notes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if path is not None:
            self.path = path
        self.accepted_by = accepted_by
        self.expiration_date = expiration_date
        self.compensating_control = compensating_control
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        self.owner = owner
        self.accepted_findings = accepted_findings
        if notes is not None:
            self.notes = notes

    @property
    def id(self):
        """Gets the id of this RiskAcceptance.  # noqa: E501


        :return: The id of this RiskAcceptance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RiskAcceptance.


        :param id: The id of this RiskAcceptance.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RiskAcceptance.  # noqa: E501

        Descriptive name which in the future may also be used to group risk acceptances together across engagements and products  # noqa: E501

        :return: The name of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RiskAcceptance.

        Descriptive name which in the future may also be used to group risk acceptances together across engagements and products  # noqa: E501

        :param name: The name of this RiskAcceptance.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this RiskAcceptance.  # noqa: E501


        :return: The path of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RiskAcceptance.


        :param path: The path of this RiskAcceptance.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def accepted_by(self):
        """Gets the accepted_by of this RiskAcceptance.  # noqa: E501

        The entity or person that accepts the risk.  # noqa: E501

        :return: The accepted_by of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._accepted_by

    @accepted_by.setter
    def accepted_by(self, accepted_by):
        """Sets the accepted_by of this RiskAcceptance.

        The entity or person that accepts the risk.  # noqa: E501

        :param accepted_by: The accepted_by of this RiskAcceptance.  # noqa: E501
        :type accepted_by: str
        """
        if (self.local_vars_configuration.client_side_validation and
                accepted_by is not None and len(accepted_by) > 200):
            raise ValueError("Invalid value for `accepted_by`, length must be less than or equal to `200`")  # noqa: E501

        self._accepted_by = accepted_by

    @property
    def expiration_date(self):
        """Gets the expiration_date of this RiskAcceptance.  # noqa: E501


        :return: The expiration_date of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this RiskAcceptance.


        :param expiration_date: The expiration_date of this RiskAcceptance.  # noqa: E501
        :type expiration_date: datetime
        """

        self._expiration_date = expiration_date

    @property
    def compensating_control(self):
        """Gets the compensating_control of this RiskAcceptance.  # noqa: E501

        If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s).  # noqa: E501

        :return: The compensating_control of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._compensating_control

    @compensating_control.setter
    def compensating_control(self, compensating_control):
        """Sets the compensating_control of this RiskAcceptance.

        If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s).  # noqa: E501

        :param compensating_control: The compensating_control of this RiskAcceptance.  # noqa: E501
        :type compensating_control: str
        """

        self._compensating_control = compensating_control

    @property
    def created(self):
        """Gets the created of this RiskAcceptance.  # noqa: E501


        :return: The created of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RiskAcceptance.


        :param created: The created of this RiskAcceptance.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this RiskAcceptance.  # noqa: E501


        :return: The updated of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RiskAcceptance.


        :param updated: The updated of this RiskAcceptance.  # noqa: E501
        :type updated: datetime
        """

        self._updated = updated

    @property
    def owner(self):
        """Gets the owner of this RiskAcceptance.  # noqa: E501

        Only the owner and staff users can edit the risk acceptance.  # noqa: E501

        :return: The owner of this RiskAcceptance.  # noqa: E501
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RiskAcceptance.

        Only the owner and staff users can edit the risk acceptance.  # noqa: E501

        :param owner: The owner of this RiskAcceptance.  # noqa: E501
        :type owner: int
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def accepted_findings(self):
        """Gets the accepted_findings of this RiskAcceptance.  # noqa: E501


        :return: The accepted_findings of this RiskAcceptance.  # noqa: E501
        :rtype: list[int]
        """
        return self._accepted_findings

    @accepted_findings.setter
    def accepted_findings(self, accepted_findings):
        """Sets the accepted_findings of this RiskAcceptance.


        :param accepted_findings: The accepted_findings of this RiskAcceptance.  # noqa: E501
        :type accepted_findings: list[int]
        """
        if self.local_vars_configuration.client_side_validation and accepted_findings is None:  # noqa: E501
            raise ValueError("Invalid value for `accepted_findings`, must not be `None`")  # noqa: E501

        self._accepted_findings = accepted_findings

    @property
    def notes(self):
        """Gets the notes of this RiskAcceptance.  # noqa: E501


        :return: The notes of this RiskAcceptance.  # noqa: E501
        :rtype: list[int]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this RiskAcceptance.


        :param notes: The notes of this RiskAcceptance.  # noqa: E501
        :type notes: list[int]
        """

        self._notes = notes

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
        if not isinstance(other, RiskAcceptance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RiskAcceptance):
            return True

        return self.to_dict() != other.to_dict()