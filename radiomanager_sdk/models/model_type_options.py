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


class ModelTypeOptions(object):
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
        'color': 'str',
        'sub_broadcast': 'bool'
    }

    attribute_map = {
        'color': 'color',
        'sub_broadcast': 'subBroadcast'
    }

    def __init__(self, color=None, sub_broadcast=None):  # noqa: E501
        """ModelTypeOptions - a model defined in Swagger"""  # noqa: E501

        self._color = None
        self._sub_broadcast = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if sub_broadcast is not None:
            self.sub_broadcast = sub_broadcast

    @property
    def color(self):
        """Gets the color of this ModelTypeOptions.  # noqa: E501


        :return: The color of this ModelTypeOptions.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ModelTypeOptions.


        :param color: The color of this ModelTypeOptions.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def sub_broadcast(self):
        """Gets the sub_broadcast of this ModelTypeOptions.  # noqa: E501


        :return: The sub_broadcast of this ModelTypeOptions.  # noqa: E501
        :rtype: bool
        """
        return self._sub_broadcast

    @sub_broadcast.setter
    def sub_broadcast(self, sub_broadcast):
        """Sets the sub_broadcast of this ModelTypeOptions.


        :param sub_broadcast: The sub_broadcast of this ModelTypeOptions.  # noqa: E501
        :type: bool
        """

        self._sub_broadcast = sub_broadcast

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
        if not isinstance(other, ModelTypeOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
