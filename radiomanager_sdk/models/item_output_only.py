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


class ItemOutputOnly(object):
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
        'id': 'int',
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'deleted_at': 'datetime',
        'data_modified': 'int',
        'order': 'int',
        'templateblock_id': 'int',
        'templateitem_id': 'int',
        'external_station_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'data_modified': 'data_modified',
        'order': 'order',
        'templateblock_id': 'templateblock_id',
        'templateitem_id': 'templateitem_id',
        'external_station_id': '_external_station_id'
    }

    def __init__(self, id=None, updated_at=None, created_at=None, deleted_at=None, data_modified=None, order=None, templateblock_id=None, templateitem_id=None, external_station_id=None):
        """
        ItemOutputOnly - a model defined in Swagger
        """

        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._data_modified = None
        self._order = None
        self._templateblock_id = None
        self._templateitem_id = None
        self._external_station_id = None

        if id is not None:
          self.id = id
        if updated_at is not None:
          self.updated_at = updated_at
        if created_at is not None:
          self.created_at = created_at
        if deleted_at is not None:
          self.deleted_at = deleted_at
        if data_modified is not None:
          self.data_modified = data_modified
        if order is not None:
          self.order = order
        if templateblock_id is not None:
          self.templateblock_id = templateblock_id
        if templateitem_id is not None:
          self.templateitem_id = templateitem_id
        if external_station_id is not None:
          self.external_station_id = external_station_id

    @property
    def id(self):
        """
        Gets the id of this ItemOutputOnly.

        :return: The id of this ItemOutputOnly.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ItemOutputOnly.

        :param id: The id of this ItemOutputOnly.
        :type: int
        """

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ItemOutputOnly.

        :return: The updated_at of this ItemOutputOnly.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ItemOutputOnly.

        :param updated_at: The updated_at of this ItemOutputOnly.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this ItemOutputOnly.

        :return: The created_at of this ItemOutputOnly.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ItemOutputOnly.

        :param created_at: The created_at of this ItemOutputOnly.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this ItemOutputOnly.

        :return: The deleted_at of this ItemOutputOnly.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this ItemOutputOnly.

        :param deleted_at: The deleted_at of this ItemOutputOnly.
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def data_modified(self):
        """
        Gets the data_modified of this ItemOutputOnly.

        :return: The data_modified of this ItemOutputOnly.
        :rtype: int
        """
        return self._data_modified

    @data_modified.setter
    def data_modified(self, data_modified):
        """
        Sets the data_modified of this ItemOutputOnly.

        :param data_modified: The data_modified of this ItemOutputOnly.
        :type: int
        """

        self._data_modified = data_modified

    @property
    def order(self):
        """
        Gets the order of this ItemOutputOnly.

        :return: The order of this ItemOutputOnly.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ItemOutputOnly.

        :param order: The order of this ItemOutputOnly.
        :type: int
        """

        self._order = order

    @property
    def templateblock_id(self):
        """
        Gets the templateblock_id of this ItemOutputOnly.

        :return: The templateblock_id of this ItemOutputOnly.
        :rtype: int
        """
        return self._templateblock_id

    @templateblock_id.setter
    def templateblock_id(self, templateblock_id):
        """
        Sets the templateblock_id of this ItemOutputOnly.

        :param templateblock_id: The templateblock_id of this ItemOutputOnly.
        :type: int
        """

        self._templateblock_id = templateblock_id

    @property
    def templateitem_id(self):
        """
        Gets the templateitem_id of this ItemOutputOnly.

        :return: The templateitem_id of this ItemOutputOnly.
        :rtype: int
        """
        return self._templateitem_id

    @templateitem_id.setter
    def templateitem_id(self, templateitem_id):
        """
        Sets the templateitem_id of this ItemOutputOnly.

        :param templateitem_id: The templateitem_id of this ItemOutputOnly.
        :type: int
        """

        self._templateitem_id = templateitem_id

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this ItemOutputOnly.

        :return: The external_station_id of this ItemOutputOnly.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this ItemOutputOnly.

        :param external_station_id: The external_station_id of this ItemOutputOnly.
        :type: int
        """

        self._external_station_id = external_station_id

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
        if not isinstance(other, ItemOutputOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
