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

from radiomanager_sdk.models.import_item import ImportItem  # noqa: F401,E501


class Data(object):
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
        'start': 'datetime',
        'allow_playlist_past': 'int',
        'items': 'list[ImportItem]'
    }

    attribute_map = {
        'start': 'start',
        'allow_playlist_past': 'allow_playlist_past',
        'items': 'items'
    }

    def __init__(self, start=None, allow_playlist_past=None, items=None):  # noqa: E501
        """Data - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._allow_playlist_past = None
        self._items = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if allow_playlist_past is not None:
            self.allow_playlist_past = allow_playlist_past
        if items is not None:
            self.items = items

    @property
    def start(self):
        """Gets the start of this Data.  # noqa: E501


        :return: The start of this Data.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Data.


        :param start: The start of this Data.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def allow_playlist_past(self):
        """Gets the allow_playlist_past of this Data.  # noqa: E501


        :return: The allow_playlist_past of this Data.  # noqa: E501
        :rtype: int
        """
        return self._allow_playlist_past

    @allow_playlist_past.setter
    def allow_playlist_past(self, allow_playlist_past):
        """Sets the allow_playlist_past of this Data.


        :param allow_playlist_past: The allow_playlist_past of this Data.  # noqa: E501
        :type: int
        """

        self._allow_playlist_past = allow_playlist_past

    @property
    def items(self):
        """Gets the items of this Data.  # noqa: E501


        :return: The items of this Data.  # noqa: E501
        :rtype: list[ImportItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Data.


        :param items: The items of this Data.  # noqa: E501
        :type: list[ImportItem]
        """

        self._items = items

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
        if not isinstance(other, Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
