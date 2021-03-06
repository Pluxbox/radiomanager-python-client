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

from radiomanager_sdk.models.block_relations_broadcast import BlockRelationsBroadcast  # noqa: F401,E501
from radiomanager_sdk.models.block_relations_items import BlockRelationsItems  # noqa: F401,E501
from radiomanager_sdk.models.block_relations_program import BlockRelationsProgram  # noqa: F401,E501


class BlockRelations(object):
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
        'items': 'BlockRelationsItems',
        'broadcast': 'BlockRelationsBroadcast',
        'program': 'BlockRelationsProgram'
    }

    attribute_map = {
        'items': 'items',
        'broadcast': 'broadcast',
        'program': 'program'
    }

    def __init__(self, items=None, broadcast=None, program=None):  # noqa: E501
        """BlockRelations - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._broadcast = None
        self._program = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if broadcast is not None:
            self.broadcast = broadcast
        if program is not None:
            self.program = program

    @property
    def items(self):
        """Gets the items of this BlockRelations.  # noqa: E501


        :return: The items of this BlockRelations.  # noqa: E501
        :rtype: BlockRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BlockRelations.


        :param items: The items of this BlockRelations.  # noqa: E501
        :type: BlockRelationsItems
        """

        self._items = items

    @property
    def broadcast(self):
        """Gets the broadcast of this BlockRelations.  # noqa: E501


        :return: The broadcast of this BlockRelations.  # noqa: E501
        :rtype: BlockRelationsBroadcast
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        """Sets the broadcast of this BlockRelations.


        :param broadcast: The broadcast of this BlockRelations.  # noqa: E501
        :type: BlockRelationsBroadcast
        """

        self._broadcast = broadcast

    @property
    def program(self):
        """Gets the program of this BlockRelations.  # noqa: E501


        :return: The program of this BlockRelations.  # noqa: E501
        :rtype: BlockRelationsProgram
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this BlockRelations.


        :param program: The program of this BlockRelations.  # noqa: E501
        :type: BlockRelationsProgram
        """

        self._program = program

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
        if not isinstance(other, BlockRelations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
