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


class CampaignRelations(object):
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
        'items': 'CampaignRelationsItems',
        'model_type': 'BroadcastRelationsModelType'
    }

    attribute_map = {
        'items': 'items',
        'model_type': 'model_type'
    }

    def __init__(self, items=None, model_type=None, local_vars_configuration=None):  # noqa: E501
        """CampaignRelations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._model_type = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if model_type is not None:
            self.model_type = model_type

    @property
    def items(self):
        """Gets the items of this CampaignRelations.  # noqa: E501


        :return: The items of this CampaignRelations.  # noqa: E501
        :rtype: CampaignRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CampaignRelations.


        :param items: The items of this CampaignRelations.  # noqa: E501
        :type: CampaignRelationsItems
        """

        self._items = items

    @property
    def model_type(self):
        """Gets the model_type of this CampaignRelations.  # noqa: E501


        :return: The model_type of this CampaignRelations.  # noqa: E501
        :rtype: BroadcastRelationsModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this CampaignRelations.


        :param model_type: The model_type of this CampaignRelations.  # noqa: E501
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
        if not isinstance(other, CampaignRelations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignRelations):
            return True

        return self.to_dict() != other.to_dict()
