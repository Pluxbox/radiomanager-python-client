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


class Block(object):
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
        'id': 'int',
        'broadcast_id': 'int',
        'start': 'datetime',
        'stop': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'deleted_at': 'datetime',
        'external_station_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'broadcast_id': 'broadcast_id',
        'start': 'start',
        'stop': 'stop',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'deleted_at': 'deleted_at',
        'external_station_id': '_external_station_id'
    }

    def __init__(self, id=None, broadcast_id=None, start=None, stop=None, created_at=None, updated_at=None, deleted_at=None, external_station_id=None):  # noqa: E501
        """Block - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._broadcast_id = None
        self._start = None
        self._stop = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._external_station_id = None
        self.discriminator = None

        self.id = id
        self.broadcast_id = broadcast_id
        self.start = start
        self.stop = stop
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        if external_station_id is not None:
            self.external_station_id = external_station_id

    @property
    def id(self):
        """Gets the id of this Block.  # noqa: E501

        ID of the current Block.  # noqa: E501

        :return: The id of this Block.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Block.

        ID of the current Block.  # noqa: E501

        :param id: The id of this Block.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def broadcast_id(self):
        """Gets the broadcast_id of this Block.  # noqa: E501

        Currently assigned Broadcast connected to the current Block, identified by the Broadcast ID.  # noqa: E501

        :return: The broadcast_id of this Block.  # noqa: E501
        :rtype: int
        """
        return self._broadcast_id

    @broadcast_id.setter
    def broadcast_id(self, broadcast_id):
        """Sets the broadcast_id of this Block.

        Currently assigned Broadcast connected to the current Block, identified by the Broadcast ID.  # noqa: E501

        :param broadcast_id: The broadcast_id of this Block.  # noqa: E501
        :type: int
        """
        if broadcast_id is None:
            raise ValueError("Invalid value for `broadcast_id`, must not be `None`")  # noqa: E501

        self._broadcast_id = broadcast_id

    @property
    def start(self):
        """Gets the start of this Block.  # noqa: E501

        Start of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :return: The start of this Block.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Block.

        Start of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :param start: The start of this Block.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this Block.  # noqa: E501

        End of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :return: The stop of this Block.  # noqa: E501
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this Block.

        End of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :param stop: The stop of this Block.  # noqa: E501
        :type: datetime
        """
        if stop is None:
            raise ValueError("Invalid value for `stop`, must not be `None`")  # noqa: E501

        self._stop = stop

    @property
    def created_at(self):
        """Gets the created_at of this Block.  # noqa: E501

        Time of the creation of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :return: The created_at of this Block.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Block.

        Time of the creation of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :param created_at: The created_at of this Block.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Block.  # noqa: E501

        Time of the last update of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :return: The updated_at of this Block.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Block.

        Time of the last update of the Block (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :param updated_at: The updated_at of this Block.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Block.  # noqa: E501

        Moment when the Block got deleted (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :return: The deleted_at of this Block.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Block.

        Moment when the Block got deleted (formatted as a DateTime object), saved with an TimeZone.  # noqa: E501

        :param deleted_at: The deleted_at of this Block.  # noqa: E501
        :type: datetime
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def external_station_id(self):
        """Gets the external_station_id of this Block.  # noqa: E501


        :return: The external_station_id of this Block.  # noqa: E501
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """Sets the external_station_id of this Block.


        :param external_station_id: The external_station_id of this Block.  # noqa: E501
        :type: int
        """

        self._external_station_id = external_station_id

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
        if not isinstance(other, Block):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
