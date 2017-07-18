# coding: utf-8

"""
    Pluxbox Radiomanager Client

    Pluxbox RadioManager gives you the power, flexibility and speed you always wanted in a lightweight and easy-to-use web-based radio solution. With Pluxbox RadioManager you can organise your radio workflow and automate your omnichannel communication with your listeners. We offer wide range specialised services for the radio and connections like Hybrid Radio, Visual Radio, your website and social media without losing focus on your broadcast. For more information visit https://pluxbox.com

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BroadcastInputOnly(object):
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
        'tags': 'list[int]',
        'presenters': 'list[int]'
    }

    attribute_map = {
        'tags': 'tags',
        'presenters': 'presenters'
    }

    def __init__(self, tags=None, presenters=None):
        """
        BroadcastInputOnly - a model defined in Swagger
        """

        self._tags = None
        self._presenters = None

        if tags is not None:
          self.tags = tags
        if presenters is not None:
          self.presenters = presenters

    @property
    def tags(self):
        """
        Gets the tags of this BroadcastInputOnly.

        :return: The tags of this BroadcastInputOnly.
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BroadcastInputOnly.

        :param tags: The tags of this BroadcastInputOnly.
        :type: list[int]
        """

        self._tags = tags

    @property
    def presenters(self):
        """
        Gets the presenters of this BroadcastInputOnly.

        :return: The presenters of this BroadcastInputOnly.
        :rtype: list[int]
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """
        Sets the presenters of this BroadcastInputOnly.

        :param presenters: The presenters of this BroadcastInputOnly.
        :type: list[int]
        """

        self._presenters = presenters

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
        if not isinstance(other, BroadcastInputOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
