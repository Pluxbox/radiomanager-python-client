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


class CampaignOutputOnly(object):
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
        'id': 'int',
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'deleted_at': 'datetime',
        'item': 'CampaignTemplateItem',
        'external_station_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'item': 'item',
        'external_station_id': '_external_station_id'
    }

    def __init__(self, id=None, updated_at=None, created_at=None, deleted_at=None, item=None, external_station_id=None, local_vars_configuration=None):  # noqa: E501
        """CampaignOutputOnly - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._item = None
        self._external_station_id = None
        self.discriminator = None

        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.deleted_at = deleted_at
        if item is not None:
            self.item = item
        if external_station_id is not None:
            self.external_station_id = external_station_id

    @property
    def id(self):
        """Gets the id of this CampaignOutputOnly.  # noqa: E501


        :return: The id of this CampaignOutputOnly.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CampaignOutputOnly.


        :param id: The id of this CampaignOutputOnly.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this CampaignOutputOnly.  # noqa: E501


        :return: The updated_at of this CampaignOutputOnly.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CampaignOutputOnly.


        :param updated_at: The updated_at of this CampaignOutputOnly.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this CampaignOutputOnly.  # noqa: E501


        :return: The created_at of this CampaignOutputOnly.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CampaignOutputOnly.


        :param created_at: The created_at of this CampaignOutputOnly.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this CampaignOutputOnly.  # noqa: E501


        :return: The deleted_at of this CampaignOutputOnly.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this CampaignOutputOnly.


        :param deleted_at: The deleted_at of this CampaignOutputOnly.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted_at is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def item(self):
        """Gets the item of this CampaignOutputOnly.  # noqa: E501


        :return: The item of this CampaignOutputOnly.  # noqa: E501
        :rtype: CampaignTemplateItem
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this CampaignOutputOnly.


        :param item: The item of this CampaignOutputOnly.  # noqa: E501
        :type: CampaignTemplateItem
        """

        self._item = item

    @property
    def external_station_id(self):
        """Gets the external_station_id of this CampaignOutputOnly.  # noqa: E501


        :return: The external_station_id of this CampaignOutputOnly.  # noqa: E501
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """Sets the external_station_id of this CampaignOutputOnly.


        :param external_station_id: The external_station_id of this CampaignOutputOnly.  # noqa: E501
        :type: int
        """

        self._external_station_id = external_station_id

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
        if not isinstance(other, CampaignOutputOnly):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignOutputOnly):
            return True

        return self.to_dict() != other.to_dict()
