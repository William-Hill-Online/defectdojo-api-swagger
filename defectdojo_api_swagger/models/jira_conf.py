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


class JIRAConf(object):
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
        'configuration_name': 'str',
        'url': 'str',
        'username': 'str',
        'password': 'str',
        'default_issue_type': 'str',
        'epic_name_id': 'int',
        'open_status_key': 'int',
        'close_status_key': 'int',
        'info_mapping_severity': 'str',
        'low_mapping_severity': 'str',
        'medium_mapping_severity': 'str',
        'high_mapping_severity': 'str',
        'critical_mapping_severity': 'str',
        'finding_text': 'str',
        'accepted_mapping_resolution': 'str',
        'false_positive_mapping_resolution': 'str'
    }

    attribute_map = {
        'id': 'id',
        'configuration_name': 'configuration_name',
        'url': 'url',
        'username': 'username',
        'password': 'password',
        'default_issue_type': 'default_issue_type',
        'epic_name_id': 'epic_name_id',
        'open_status_key': 'open_status_key',
        'close_status_key': 'close_status_key',
        'info_mapping_severity': 'info_mapping_severity',
        'low_mapping_severity': 'low_mapping_severity',
        'medium_mapping_severity': 'medium_mapping_severity',
        'high_mapping_severity': 'high_mapping_severity',
        'critical_mapping_severity': 'critical_mapping_severity',
        'finding_text': 'finding_text',
        'accepted_mapping_resolution': 'accepted_mapping_resolution',
        'false_positive_mapping_resolution': 'false_positive_mapping_resolution'
    }

    def __init__(self, id=None, configuration_name=None, url=None, username=None, password=None, default_issue_type=None, epic_name_id=None, open_status_key=None, close_status_key=None, info_mapping_severity=None, low_mapping_severity=None, medium_mapping_severity=None, high_mapping_severity=None, critical_mapping_severity=None, finding_text=None, accepted_mapping_resolution=None, false_positive_mapping_resolution=None):  # noqa: E501
        """JIRAConf - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._configuration_name = None
        self._url = None
        self._username = None
        self._password = None
        self._default_issue_type = None
        self._epic_name_id = None
        self._open_status_key = None
        self._close_status_key = None
        self._info_mapping_severity = None
        self._low_mapping_severity = None
        self._medium_mapping_severity = None
        self._high_mapping_severity = None
        self._critical_mapping_severity = None
        self._finding_text = None
        self._accepted_mapping_resolution = None
        self._false_positive_mapping_resolution = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if configuration_name is not None:
            self.configuration_name = configuration_name
        self.url = url
        self.username = username
        self.password = password
        if default_issue_type is not None:
            self.default_issue_type = default_issue_type
        self.epic_name_id = epic_name_id
        self.open_status_key = open_status_key
        self.close_status_key = close_status_key
        self.info_mapping_severity = info_mapping_severity
        self.low_mapping_severity = low_mapping_severity
        self.medium_mapping_severity = medium_mapping_severity
        self.high_mapping_severity = high_mapping_severity
        self.critical_mapping_severity = critical_mapping_severity
        if finding_text is not None:
            self.finding_text = finding_text
        if accepted_mapping_resolution is not None:
            self.accepted_mapping_resolution = accepted_mapping_resolution
        if false_positive_mapping_resolution is not None:
            self.false_positive_mapping_resolution = false_positive_mapping_resolution

    @property
    def id(self):
        """Gets the id of this JIRAConf.  # noqa: E501


        :return: The id of this JIRAConf.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JIRAConf.


        :param id: The id of this JIRAConf.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def configuration_name(self):
        """Gets the configuration_name of this JIRAConf.  # noqa: E501

        Enter a name to give to this configuration  # noqa: E501

        :return: The configuration_name of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._configuration_name

    @configuration_name.setter
    def configuration_name(self, configuration_name):
        """Sets the configuration_name of this JIRAConf.

        Enter a name to give to this configuration  # noqa: E501

        :param configuration_name: The configuration_name of this JIRAConf.  # noqa: E501
        :type: str
        """
        if configuration_name is not None and len(configuration_name) > 2000:
            raise ValueError("Invalid value for `configuration_name`, length must be less than or equal to `2000`")  # noqa: E501
        if configuration_name is not None and len(configuration_name) < 1:
            raise ValueError("Invalid value for `configuration_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._configuration_name = configuration_name

    @property
    def url(self):
        """Gets the url of this JIRAConf.  # noqa: E501

        For configuring Jira, view: https://defectdojo.readthedocs.io/en/latest/features.html#jira-integration  # noqa: E501

        :return: The url of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this JIRAConf.

        For configuring Jira, view: https://defectdojo.readthedocs.io/en/latest/features.html#jira-integration  # noqa: E501

        :param url: The url of this JIRAConf.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if url is not None and len(url) > 2000:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `2000`")  # noqa: E501
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def username(self):
        """Gets the username of this JIRAConf.  # noqa: E501


        :return: The username of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this JIRAConf.


        :param username: The username of this JIRAConf.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if username is not None and len(username) > 2000:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `2000`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this JIRAConf.  # noqa: E501


        :return: The password of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this JIRAConf.


        :param password: The password of this JIRAConf.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) > 2000:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `2000`")  # noqa: E501
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def default_issue_type(self):
        """Gets the default_issue_type of this JIRAConf.  # noqa: E501

        You can define extra issue types in settings.py  # noqa: E501

        :return: The default_issue_type of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._default_issue_type

    @default_issue_type.setter
    def default_issue_type(self, default_issue_type):
        """Sets the default_issue_type of this JIRAConf.

        You can define extra issue types in settings.py  # noqa: E501

        :param default_issue_type: The default_issue_type of this JIRAConf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Task", "Story", "Epic", "Spike", "Bug", "Security"]  # noqa: E501
        if default_issue_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_issue_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_issue_type, allowed_values)
            )

        self._default_issue_type = default_issue_type

    @property
    def epic_name_id(self):
        """Gets the epic_name_id of this JIRAConf.  # noqa: E501

        To obtain the 'Epic name id' visit https://<YOUR JIRA URL>/rest/api/2/field and search for Epic Name. Copy the number out of cf[number] and paste it here.  # noqa: E501

        :return: The epic_name_id of this JIRAConf.  # noqa: E501
        :rtype: int
        """
        return self._epic_name_id

    @epic_name_id.setter
    def epic_name_id(self, epic_name_id):
        """Sets the epic_name_id of this JIRAConf.

        To obtain the 'Epic name id' visit https://<YOUR JIRA URL>/rest/api/2/field and search for Epic Name. Copy the number out of cf[number] and paste it here.  # noqa: E501

        :param epic_name_id: The epic_name_id of this JIRAConf.  # noqa: E501
        :type: int
        """
        if epic_name_id is None:
            raise ValueError("Invalid value for `epic_name_id`, must not be `None`")  # noqa: E501
        if epic_name_id is not None and epic_name_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `epic_name_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if epic_name_id is not None and epic_name_id < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `epic_name_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._epic_name_id = epic_name_id

    @property
    def open_status_key(self):
        """Gets the open_status_key of this JIRAConf.  # noqa: E501

        To obtain the 'open status key' visit https://<YOUR JIRA URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields  # noqa: E501

        :return: The open_status_key of this JIRAConf.  # noqa: E501
        :rtype: int
        """
        return self._open_status_key

    @open_status_key.setter
    def open_status_key(self, open_status_key):
        """Sets the open_status_key of this JIRAConf.

        To obtain the 'open status key' visit https://<YOUR JIRA URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields  # noqa: E501

        :param open_status_key: The open_status_key of this JIRAConf.  # noqa: E501
        :type: int
        """
        if open_status_key is None:
            raise ValueError("Invalid value for `open_status_key`, must not be `None`")  # noqa: E501
        if open_status_key is not None and open_status_key > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `open_status_key`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if open_status_key is not None and open_status_key < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `open_status_key`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._open_status_key = open_status_key

    @property
    def close_status_key(self):
        """Gets the close_status_key of this JIRAConf.  # noqa: E501

        To obtain the 'open status key' visit https://<YOUR JIRA URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields  # noqa: E501

        :return: The close_status_key of this JIRAConf.  # noqa: E501
        :rtype: int
        """
        return self._close_status_key

    @close_status_key.setter
    def close_status_key(self, close_status_key):
        """Sets the close_status_key of this JIRAConf.

        To obtain the 'open status key' visit https://<YOUR JIRA URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields  # noqa: E501

        :param close_status_key: The close_status_key of this JIRAConf.  # noqa: E501
        :type: int
        """
        if close_status_key is None:
            raise ValueError("Invalid value for `close_status_key`, must not be `None`")  # noqa: E501
        if close_status_key is not None and close_status_key > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `close_status_key`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if close_status_key is not None and close_status_key < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `close_status_key`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._close_status_key = close_status_key

    @property
    def info_mapping_severity(self):
        """Gets the info_mapping_severity of this JIRAConf.  # noqa: E501

        Maps to the 'Priority' field in Jira. For example: Info  # noqa: E501

        :return: The info_mapping_severity of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._info_mapping_severity

    @info_mapping_severity.setter
    def info_mapping_severity(self, info_mapping_severity):
        """Sets the info_mapping_severity of this JIRAConf.

        Maps to the 'Priority' field in Jira. For example: Info  # noqa: E501

        :param info_mapping_severity: The info_mapping_severity of this JIRAConf.  # noqa: E501
        :type: str
        """
        if info_mapping_severity is None:
            raise ValueError("Invalid value for `info_mapping_severity`, must not be `None`")  # noqa: E501
        if info_mapping_severity is not None and len(info_mapping_severity) > 200:
            raise ValueError("Invalid value for `info_mapping_severity`, length must be less than or equal to `200`")  # noqa: E501
        if info_mapping_severity is not None and len(info_mapping_severity) < 1:
            raise ValueError("Invalid value for `info_mapping_severity`, length must be greater than or equal to `1`")  # noqa: E501

        self._info_mapping_severity = info_mapping_severity

    @property
    def low_mapping_severity(self):
        """Gets the low_mapping_severity of this JIRAConf.  # noqa: E501

        Maps to the 'Priority' field in Jira. For example: Low  # noqa: E501

        :return: The low_mapping_severity of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._low_mapping_severity

    @low_mapping_severity.setter
    def low_mapping_severity(self, low_mapping_severity):
        """Sets the low_mapping_severity of this JIRAConf.

        Maps to the 'Priority' field in Jira. For example: Low  # noqa: E501

        :param low_mapping_severity: The low_mapping_severity of this JIRAConf.  # noqa: E501
        :type: str
        """
        if low_mapping_severity is None:
            raise ValueError("Invalid value for `low_mapping_severity`, must not be `None`")  # noqa: E501
        if low_mapping_severity is not None and len(low_mapping_severity) > 200:
            raise ValueError("Invalid value for `low_mapping_severity`, length must be less than or equal to `200`")  # noqa: E501
        if low_mapping_severity is not None and len(low_mapping_severity) < 1:
            raise ValueError("Invalid value for `low_mapping_severity`, length must be greater than or equal to `1`")  # noqa: E501

        self._low_mapping_severity = low_mapping_severity

    @property
    def medium_mapping_severity(self):
        """Gets the medium_mapping_severity of this JIRAConf.  # noqa: E501

        Maps to the 'Priority' field in Jira. For example: Medium  # noqa: E501

        :return: The medium_mapping_severity of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._medium_mapping_severity

    @medium_mapping_severity.setter
    def medium_mapping_severity(self, medium_mapping_severity):
        """Sets the medium_mapping_severity of this JIRAConf.

        Maps to the 'Priority' field in Jira. For example: Medium  # noqa: E501

        :param medium_mapping_severity: The medium_mapping_severity of this JIRAConf.  # noqa: E501
        :type: str
        """
        if medium_mapping_severity is None:
            raise ValueError("Invalid value for `medium_mapping_severity`, must not be `None`")  # noqa: E501
        if medium_mapping_severity is not None and len(medium_mapping_severity) > 200:
            raise ValueError("Invalid value for `medium_mapping_severity`, length must be less than or equal to `200`")  # noqa: E501
        if medium_mapping_severity is not None and len(medium_mapping_severity) < 1:
            raise ValueError("Invalid value for `medium_mapping_severity`, length must be greater than or equal to `1`")  # noqa: E501

        self._medium_mapping_severity = medium_mapping_severity

    @property
    def high_mapping_severity(self):
        """Gets the high_mapping_severity of this JIRAConf.  # noqa: E501

        Maps to the 'Priority' field in Jira. For example: High  # noqa: E501

        :return: The high_mapping_severity of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._high_mapping_severity

    @high_mapping_severity.setter
    def high_mapping_severity(self, high_mapping_severity):
        """Sets the high_mapping_severity of this JIRAConf.

        Maps to the 'Priority' field in Jira. For example: High  # noqa: E501

        :param high_mapping_severity: The high_mapping_severity of this JIRAConf.  # noqa: E501
        :type: str
        """
        if high_mapping_severity is None:
            raise ValueError("Invalid value for `high_mapping_severity`, must not be `None`")  # noqa: E501
        if high_mapping_severity is not None and len(high_mapping_severity) > 200:
            raise ValueError("Invalid value for `high_mapping_severity`, length must be less than or equal to `200`")  # noqa: E501
        if high_mapping_severity is not None and len(high_mapping_severity) < 1:
            raise ValueError("Invalid value for `high_mapping_severity`, length must be greater than or equal to `1`")  # noqa: E501

        self._high_mapping_severity = high_mapping_severity

    @property
    def critical_mapping_severity(self):
        """Gets the critical_mapping_severity of this JIRAConf.  # noqa: E501

        Maps to the 'Priority' field in Jira. For example: Critical  # noqa: E501

        :return: The critical_mapping_severity of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._critical_mapping_severity

    @critical_mapping_severity.setter
    def critical_mapping_severity(self, critical_mapping_severity):
        """Sets the critical_mapping_severity of this JIRAConf.

        Maps to the 'Priority' field in Jira. For example: Critical  # noqa: E501

        :param critical_mapping_severity: The critical_mapping_severity of this JIRAConf.  # noqa: E501
        :type: str
        """
        if critical_mapping_severity is None:
            raise ValueError("Invalid value for `critical_mapping_severity`, must not be `None`")  # noqa: E501
        if critical_mapping_severity is not None and len(critical_mapping_severity) > 200:
            raise ValueError("Invalid value for `critical_mapping_severity`, length must be less than or equal to `200`")  # noqa: E501
        if critical_mapping_severity is not None and len(critical_mapping_severity) < 1:
            raise ValueError("Invalid value for `critical_mapping_severity`, length must be greater than or equal to `1`")  # noqa: E501

        self._critical_mapping_severity = critical_mapping_severity

    @property
    def finding_text(self):
        """Gets the finding_text of this JIRAConf.  # noqa: E501

        Additional text that will be added to the finding in Jira. For example including how the finding was created or who to contact for more information.  # noqa: E501

        :return: The finding_text of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._finding_text

    @finding_text.setter
    def finding_text(self, finding_text):
        """Sets the finding_text of this JIRAConf.

        Additional text that will be added to the finding in Jira. For example including how the finding was created or who to contact for more information.  # noqa: E501

        :param finding_text: The finding_text of this JIRAConf.  # noqa: E501
        :type: str
        """

        self._finding_text = finding_text

    @property
    def accepted_mapping_resolution(self):
        """Gets the accepted_mapping_resolution of this JIRAConf.  # noqa: E501

        JIRA resolution names (comma-separated values) that maps to an Accepted Finding  # noqa: E501

        :return: The accepted_mapping_resolution of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._accepted_mapping_resolution

    @accepted_mapping_resolution.setter
    def accepted_mapping_resolution(self, accepted_mapping_resolution):
        """Sets the accepted_mapping_resolution of this JIRAConf.

        JIRA resolution names (comma-separated values) that maps to an Accepted Finding  # noqa: E501

        :param accepted_mapping_resolution: The accepted_mapping_resolution of this JIRAConf.  # noqa: E501
        :type: str
        """
        if accepted_mapping_resolution is not None and len(accepted_mapping_resolution) > 300:
            raise ValueError("Invalid value for `accepted_mapping_resolution`, length must be less than or equal to `300`")  # noqa: E501

        self._accepted_mapping_resolution = accepted_mapping_resolution

    @property
    def false_positive_mapping_resolution(self):
        """Gets the false_positive_mapping_resolution of this JIRAConf.  # noqa: E501

        JIRA resolution names (comma-separated values) that maps to a False Positive Finding  # noqa: E501

        :return: The false_positive_mapping_resolution of this JIRAConf.  # noqa: E501
        :rtype: str
        """
        return self._false_positive_mapping_resolution

    @false_positive_mapping_resolution.setter
    def false_positive_mapping_resolution(self, false_positive_mapping_resolution):
        """Sets the false_positive_mapping_resolution of this JIRAConf.

        JIRA resolution names (comma-separated values) that maps to a False Positive Finding  # noqa: E501

        :param false_positive_mapping_resolution: The false_positive_mapping_resolution of this JIRAConf.  # noqa: E501
        :type: str
        """
        if false_positive_mapping_resolution is not None and len(false_positive_mapping_resolution) > 300:
            raise ValueError("Invalid value for `false_positive_mapping_resolution`, length must be less than or equal to `300`")  # noqa: E501

        self._false_positive_mapping_resolution = false_positive_mapping_resolution

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
        if issubclass(JIRAConf, dict):
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
        if not isinstance(other, JIRAConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
