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


class ProgramOutputOnly(object):
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
        'external_station_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'external_station_id': '_external_station_id'
    }

    def __init__(self, id=None, updated_at=None, created_at=None, deleted_at=None, external_station_id=None):
        """
        ProgramOutputOnly - a model defined in Swagger
        """

        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._external_station_id = None

        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.deleted_at = deleted_at
        if external_station_id is not None:
          self.external_station_id = external_station_id

    @property
    def id(self):
        """
        Gets the id of this ProgramOutputOnly.

        :return: The id of this ProgramOutputOnly.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProgramOutputOnly.

        :param id: The id of this ProgramOutputOnly.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ProgramOutputOnly.

        :return: The updated_at of this ProgramOutputOnly.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ProgramOutputOnly.

        :param updated_at: The updated_at of this ProgramOutputOnly.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this ProgramOutputOnly.

        :return: The created_at of this ProgramOutputOnly.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ProgramOutputOnly.

        :param created_at: The created_at of this ProgramOutputOnly.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this ProgramOutputOnly.

        :return: The deleted_at of this ProgramOutputOnly.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this ProgramOutputOnly.

        :param deleted_at: The deleted_at of this ProgramOutputOnly.
        :type: datetime
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")

        self._deleted_at = deleted_at

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this ProgramOutputOnly.

        :return: The external_station_id of this ProgramOutputOnly.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this ProgramOutputOnly.

        :param external_station_id: The external_station_id of this ProgramOutputOnly.
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
        if not isinstance(other, ProgramOutputOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
