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


class PresenterEPGResult(object):
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
        'model_type_id': 'int',
        'field_values': 'object',
        'firstname': 'str',
        'lastname': 'str',
        'active': 'bool',
        'name': 'str',
        'id': 'int',
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'deleted_at': 'datetime',
        'external_station_id': 'int'
    }

    attribute_map = {
        'model_type_id': 'model_type_id',
        'field_values': 'field_values',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'active': 'active',
        'name': 'name',
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'external_station_id': '_external_station_id'
    }

    def __init__(self, model_type_id=None, field_values=None, firstname=None, lastname=None, active=None, name=None, id=None, updated_at=None, created_at=None, deleted_at=None, external_station_id=None):
        """
        PresenterEPGResult - a model defined in Swagger
        """

        self._model_type_id = None
        self._field_values = None
        self._firstname = None
        self._lastname = None
        self._active = None
        self._name = None
        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._external_station_id = None

        self.model_type_id = model_type_id
        if field_values is not None:
          self.field_values = field_values
        if firstname is not None:
          self.firstname = firstname
        if lastname is not None:
          self.lastname = lastname
        if active is not None:
          self.active = active
        if name is not None:
          self.name = name
        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.deleted_at = deleted_at
        if external_station_id is not None:
          self.external_station_id = external_station_id

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this PresenterEPGResult.

        :return: The model_type_id of this PresenterEPGResult.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this PresenterEPGResult.

        :param model_type_id: The model_type_id of this PresenterEPGResult.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this PresenterEPGResult.

        :return: The field_values of this PresenterEPGResult.
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this PresenterEPGResult.

        :param field_values: The field_values of this PresenterEPGResult.
        :type: object
        """

        self._field_values = field_values

    @property
    def firstname(self):
        """
        Gets the firstname of this PresenterEPGResult.

        :return: The firstname of this PresenterEPGResult.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this PresenterEPGResult.

        :param firstname: The firstname of this PresenterEPGResult.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this PresenterEPGResult.

        :return: The lastname of this PresenterEPGResult.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this PresenterEPGResult.

        :param lastname: The lastname of this PresenterEPGResult.
        :type: str
        """

        self._lastname = lastname

    @property
    def active(self):
        """
        Gets the active of this PresenterEPGResult.

        :return: The active of this PresenterEPGResult.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PresenterEPGResult.

        :param active: The active of this PresenterEPGResult.
        :type: bool
        """

        self._active = active

    @property
    def name(self):
        """
        Gets the name of this PresenterEPGResult.

        :return: The name of this PresenterEPGResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PresenterEPGResult.

        :param name: The name of this PresenterEPGResult.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this PresenterEPGResult.

        :return: The id of this PresenterEPGResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PresenterEPGResult.

        :param id: The id of this PresenterEPGResult.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this PresenterEPGResult.

        :return: The updated_at of this PresenterEPGResult.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this PresenterEPGResult.

        :param updated_at: The updated_at of this PresenterEPGResult.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this PresenterEPGResult.

        :return: The created_at of this PresenterEPGResult.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this PresenterEPGResult.

        :param created_at: The created_at of this PresenterEPGResult.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this PresenterEPGResult.

        :return: The deleted_at of this PresenterEPGResult.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this PresenterEPGResult.

        :param deleted_at: The deleted_at of this PresenterEPGResult.
        :type: datetime
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")

        self._deleted_at = deleted_at

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this PresenterEPGResult.

        :return: The external_station_id of this PresenterEPGResult.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this PresenterEPGResult.

        :param external_station_id: The external_station_id of this PresenterEPGResult.
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
        if not isinstance(other, PresenterEPGResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other