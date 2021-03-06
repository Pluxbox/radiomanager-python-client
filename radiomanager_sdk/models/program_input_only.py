# coding: utf-8

"""
    RadioManager

    RadioManager  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProgramInputOnly(object):
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
        'tags': 'list[int]',
        'presenters': 'list[int]'
    }

    attribute_map = {
        'tags': 'tags',
        'presenters': 'presenters'
    }

    def __init__(self, tags=None, presenters=None):  # noqa: E501
        """ProgramInputOnly - a model defined in Swagger"""  # noqa: E501

        self._tags = None
        self._presenters = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if presenters is not None:
            self.presenters = presenters

    @property
    def tags(self):
        """Gets the tags of this ProgramInputOnly.  # noqa: E501


        :return: The tags of this ProgramInputOnly.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProgramInputOnly.


        :param tags: The tags of this ProgramInputOnly.  # noqa: E501
        :type: list[int]
        """

        self._tags = tags

    @property
    def presenters(self):
        """Gets the presenters of this ProgramInputOnly.  # noqa: E501


        :return: The presenters of this ProgramInputOnly.  # noqa: E501
        :rtype: list[int]
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """Sets the presenters of this ProgramInputOnly.


        :param presenters: The presenters of this ProgramInputOnly.  # noqa: E501
        :type: list[int]
        """

        self._presenters = presenters

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProgramInputOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
