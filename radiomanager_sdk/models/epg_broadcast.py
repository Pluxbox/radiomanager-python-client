# coding: utf-8

"""
    RadioManager

    RadioManager

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EPGBroadcast(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        '_2016_01_11': 'list[BroadcastResult]',
        'next_page_url': 'str',
        'prev_page_url': 'str'
    }

    attribute_map = {
        '_2016_01_11': '2016-01-11',
        'next_page_url': 'next_page_url',
        'prev_page_url': 'prev_page_url'
    }

    def __init__(self, _2016_01_11=None, next_page_url='https://raidiomanager.pluxbox.com/api/v1/broadcasts/epg/{identifier}/2016-01-12', prev_page_url='https://raidiomanager.pluxbox.com/pb/api/v1/broadcasts/epg/{identifier}/2016-01-10'):
        """
        EPGBroadcast - a model defined in Swagger
        """

        self.__2016_01_11 = None
        self._next_page_url = None
        self._prev_page_url = None

        self._2016_01_11 = _2016_01_11
        self.next_page_url = next_page_url
        self.prev_page_url = prev_page_url

    @property
    def _2016_01_11(self):
        """
        Gets the _2016_01_11 of this EPGBroadcast.

        :return: The _2016_01_11 of this EPGBroadcast.
        :rtype: list[BroadcastResult]
        """
        return self.__2016_01_11

    @_2016_01_11.setter
    def _2016_01_11(self, _2016_01_11):
        """
        Sets the _2016_01_11 of this EPGBroadcast.

        :param _2016_01_11: The _2016_01_11 of this EPGBroadcast.
        :type: list[BroadcastResult]
        """
        if _2016_01_11 is None:
            raise ValueError("Invalid value for `_2016_01_11`, must not be `None`")

        self.__2016_01_11 = _2016_01_11

    @property
    def next_page_url(self):
        """
        Gets the next_page_url of this EPGBroadcast.

        :return: The next_page_url of this EPGBroadcast.
        :rtype: str
        """
        return self._next_page_url

    @next_page_url.setter
    def next_page_url(self, next_page_url):
        """
        Sets the next_page_url of this EPGBroadcast.

        :param next_page_url: The next_page_url of this EPGBroadcast.
        :type: str
        """
        if next_page_url is None:
            raise ValueError("Invalid value for `next_page_url`, must not be `None`")

        self._next_page_url = next_page_url

    @property
    def prev_page_url(self):
        """
        Gets the prev_page_url of this EPGBroadcast.

        :return: The prev_page_url of this EPGBroadcast.
        :rtype: str
        """
        return self._prev_page_url

    @prev_page_url.setter
    def prev_page_url(self, prev_page_url):
        """
        Sets the prev_page_url of this EPGBroadcast.

        :param prev_page_url: The prev_page_url of this EPGBroadcast.
        :type: str
        """
        if prev_page_url is None:
            raise ValueError("Invalid value for `prev_page_url`, must not be `None`")

        self._prev_page_url = prev_page_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EPGBroadcast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
