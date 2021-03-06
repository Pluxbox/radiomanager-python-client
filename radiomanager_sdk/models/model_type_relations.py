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

from radiomanager_sdk.models.model_type_relations_broadcasts import ModelTypeRelationsBroadcasts  # noqa: F401,E501
from radiomanager_sdk.models.model_type_relations_campaigns import ModelTypeRelationsCampaigns  # noqa: F401,E501
from radiomanager_sdk.models.model_type_relations_contacts import ModelTypeRelationsContacts  # noqa: F401,E501
from radiomanager_sdk.models.model_type_relations_items import ModelTypeRelationsItems  # noqa: F401,E501
from radiomanager_sdk.models.model_type_relations_presenters import ModelTypeRelationsPresenters  # noqa: F401,E501
from radiomanager_sdk.models.model_type_relations_programs import ModelTypeRelationsPrograms  # noqa: F401,E501


class ModelTypeRelations(object):
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
        'campaigns': 'ModelTypeRelationsCampaigns',
        'broadcasts': 'ModelTypeRelationsBroadcasts',
        'programs': 'ModelTypeRelationsPrograms',
        'contacts': 'ModelTypeRelationsContacts',
        'presenters': 'ModelTypeRelationsPresenters',
        'items': 'ModelTypeRelationsItems'
    }

    attribute_map = {
        'campaigns': 'campaigns',
        'broadcasts': 'broadcasts',
        'programs': 'programs',
        'contacts': 'contacts',
        'presenters': 'presenters',
        'items': 'items'
    }

    def __init__(self, campaigns=None, broadcasts=None, programs=None, contacts=None, presenters=None, items=None):  # noqa: E501
        """ModelTypeRelations - a model defined in Swagger"""  # noqa: E501

        self._campaigns = None
        self._broadcasts = None
        self._programs = None
        self._contacts = None
        self._presenters = None
        self._items = None
        self.discriminator = None

        if campaigns is not None:
            self.campaigns = campaigns
        if broadcasts is not None:
            self.broadcasts = broadcasts
        if programs is not None:
            self.programs = programs
        if contacts is not None:
            self.contacts = contacts
        if presenters is not None:
            self.presenters = presenters
        if items is not None:
            self.items = items

    @property
    def campaigns(self):
        """Gets the campaigns of this ModelTypeRelations.  # noqa: E501


        :return: The campaigns of this ModelTypeRelations.  # noqa: E501
        :rtype: ModelTypeRelationsCampaigns
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """Sets the campaigns of this ModelTypeRelations.


        :param campaigns: The campaigns of this ModelTypeRelations.  # noqa: E501
        :type: ModelTypeRelationsCampaigns
        """

        self._campaigns = campaigns

    @property
    def broadcasts(self):
        """Gets the broadcasts of this ModelTypeRelations.  # noqa: E501


        :return: The broadcasts of this ModelTypeRelations.  # noqa: E501
        :rtype: ModelTypeRelationsBroadcasts
        """
        return self._broadcasts

    @broadcasts.setter
    def broadcasts(self, broadcasts):
        """Sets the broadcasts of this ModelTypeRelations.


        :param broadcasts: The broadcasts of this ModelTypeRelations.  # noqa: E501
        :type: ModelTypeRelationsBroadcasts
        """

        self._broadcasts = broadcasts

    @property
    def programs(self):
        """Gets the programs of this ModelTypeRelations.  # noqa: E501


        :return: The programs of this ModelTypeRelations.  # noqa: E501
        :rtype: ModelTypeRelationsPrograms
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """Sets the programs of this ModelTypeRelations.


        :param programs: The programs of this ModelTypeRelations.  # noqa: E501
        :type: ModelTypeRelationsPrograms
        """

        self._programs = programs

    @property
    def contacts(self):
        """Gets the contacts of this ModelTypeRelations.  # noqa: E501


        :return: The contacts of this ModelTypeRelations.  # noqa: E501
        :rtype: ModelTypeRelationsContacts
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ModelTypeRelations.


        :param contacts: The contacts of this ModelTypeRelations.  # noqa: E501
        :type: ModelTypeRelationsContacts
        """

        self._contacts = contacts

    @property
    def presenters(self):
        """Gets the presenters of this ModelTypeRelations.  # noqa: E501


        :return: The presenters of this ModelTypeRelations.  # noqa: E501
        :rtype: ModelTypeRelationsPresenters
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """Sets the presenters of this ModelTypeRelations.


        :param presenters: The presenters of this ModelTypeRelations.  # noqa: E501
        :type: ModelTypeRelationsPresenters
        """

        self._presenters = presenters

    @property
    def items(self):
        """Gets the items of this ModelTypeRelations.  # noqa: E501


        :return: The items of this ModelTypeRelations.  # noqa: E501
        :rtype: ModelTypeRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ModelTypeRelations.


        :param items: The items of this ModelTypeRelations.  # noqa: E501
        :type: ModelTypeRelationsItems
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
        if not isinstance(other, ModelTypeRelations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
