# coding: utf-8

"""
    RadioManager

    RadioManager  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@pluxbox.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from radiomanager_sdk.configuration import Configuration


class ProgramRelations(object):
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
        'genre': 'BroadcastRelationsGenre',
        'items': 'ProgramRelationsItems',
        'blocks': 'ProgramRelationsBlocks',
        'broadcasts': 'ProgramRelationsBroadcasts',
        'presenters': 'ProgramRelationsPresenters',
        'tags': 'ProgramRelationsTags',
        'model_type': 'BroadcastRelationsModelType'
    }

    attribute_map = {
        'genre': 'genre',
        'items': 'items',
        'blocks': 'blocks',
        'broadcasts': 'broadcasts',
        'presenters': 'presenters',
        'tags': 'tags',
        'model_type': 'model_type'
    }

    def __init__(self, genre=None, items=None, blocks=None, broadcasts=None, presenters=None, tags=None, model_type=None, local_vars_configuration=None):  # noqa: E501
        """ProgramRelations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._genre = None
        self._items = None
        self._blocks = None
        self._broadcasts = None
        self._presenters = None
        self._tags = None
        self._model_type = None
        self.discriminator = None

        if genre is not None:
            self.genre = genre
        if items is not None:
            self.items = items
        if blocks is not None:
            self.blocks = blocks
        if broadcasts is not None:
            self.broadcasts = broadcasts
        if presenters is not None:
            self.presenters = presenters
        if tags is not None:
            self.tags = tags
        if model_type is not None:
            self.model_type = model_type

    @property
    def genre(self):
        """Gets the genre of this ProgramRelations.  # noqa: E501


        :return: The genre of this ProgramRelations.  # noqa: E501
        :rtype: BroadcastRelationsGenre
        """
        return self._genre

    @genre.setter
    def genre(self, genre):
        """Sets the genre of this ProgramRelations.


        :param genre: The genre of this ProgramRelations.  # noqa: E501
        :type: BroadcastRelationsGenre
        """

        self._genre = genre

    @property
    def items(self):
        """Gets the items of this ProgramRelations.  # noqa: E501


        :return: The items of this ProgramRelations.  # noqa: E501
        :rtype: ProgramRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ProgramRelations.


        :param items: The items of this ProgramRelations.  # noqa: E501
        :type: ProgramRelationsItems
        """

        self._items = items

    @property
    def blocks(self):
        """Gets the blocks of this ProgramRelations.  # noqa: E501


        :return: The blocks of this ProgramRelations.  # noqa: E501
        :rtype: ProgramRelationsBlocks
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this ProgramRelations.


        :param blocks: The blocks of this ProgramRelations.  # noqa: E501
        :type: ProgramRelationsBlocks
        """

        self._blocks = blocks

    @property
    def broadcasts(self):
        """Gets the broadcasts of this ProgramRelations.  # noqa: E501


        :return: The broadcasts of this ProgramRelations.  # noqa: E501
        :rtype: ProgramRelationsBroadcasts
        """
        return self._broadcasts

    @broadcasts.setter
    def broadcasts(self, broadcasts):
        """Sets the broadcasts of this ProgramRelations.


        :param broadcasts: The broadcasts of this ProgramRelations.  # noqa: E501
        :type: ProgramRelationsBroadcasts
        """

        self._broadcasts = broadcasts

    @property
    def presenters(self):
        """Gets the presenters of this ProgramRelations.  # noqa: E501


        :return: The presenters of this ProgramRelations.  # noqa: E501
        :rtype: ProgramRelationsPresenters
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """Sets the presenters of this ProgramRelations.


        :param presenters: The presenters of this ProgramRelations.  # noqa: E501
        :type: ProgramRelationsPresenters
        """

        self._presenters = presenters

    @property
    def tags(self):
        """Gets the tags of this ProgramRelations.  # noqa: E501


        :return: The tags of this ProgramRelations.  # noqa: E501
        :rtype: ProgramRelationsTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProgramRelations.


        :param tags: The tags of this ProgramRelations.  # noqa: E501
        :type: ProgramRelationsTags
        """

        self._tags = tags

    @property
    def model_type(self):
        """Gets the model_type of this ProgramRelations.  # noqa: E501


        :return: The model_type of this ProgramRelations.  # noqa: E501
        :rtype: BroadcastRelationsModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ProgramRelations.


        :param model_type: The model_type of this ProgramRelations.  # noqa: E501
        :type: BroadcastRelationsModelType
        """

        self._model_type = model_type

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
        if not isinstance(other, ProgramRelations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProgramRelations):
            return True

        return self.to_dict() != other.to_dict()
