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


class FindingToFindingImages(object):
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
        'finding_id': 'int',
        'images': 'list[FindingImage]'
    }

    attribute_map = {
        'finding_id': 'finding_id',
        'images': 'images'
    }

    def __init__(self, finding_id=None, images=None):  # noqa: E501
        """FindingToFindingImages - a model defined in Swagger"""  # noqa: E501

        self._finding_id = None
        self._images = None
        self.discriminator = None

        self.finding_id = finding_id
        self.images = images

    @property
    def finding_id(self):
        """Gets the finding_id of this FindingToFindingImages.  # noqa: E501


        :return: The finding_id of this FindingToFindingImages.  # noqa: E501
        :rtype: int
        """
        return self._finding_id

    @finding_id.setter
    def finding_id(self, finding_id):
        """Sets the finding_id of this FindingToFindingImages.


        :param finding_id: The finding_id of this FindingToFindingImages.  # noqa: E501
        :type: int
        """
        if finding_id is None:
            raise ValueError("Invalid value for `finding_id`, must not be `None`")  # noqa: E501

        self._finding_id = finding_id

    @property
    def images(self):
        """Gets the images of this FindingToFindingImages.  # noqa: E501


        :return: The images of this FindingToFindingImages.  # noqa: E501
        :rtype: list[FindingImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this FindingToFindingImages.


        :param images: The images of this FindingToFindingImages.  # noqa: E501
        :type: list[FindingImage]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

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
        if issubclass(FindingToFindingImages, dict):
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
        if not isinstance(other, FindingToFindingImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other