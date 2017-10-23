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


class PresenterResult(object):
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
        'external_station_id': 'int',
        'model_type_id': 'int',
        'field_values': 'object',
        'firstname': 'str',
        'lastname': 'str',
        'active': 'bool',
        'name': 'str',
        'programs': 'PresenterRelationsPrograms',
        'broadcasts': 'PresenterRelationsBroadcasts',
        'model_type': 'BroadcastRelationsModelType'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'external_station_id': '_external_station_id',
        'model_type_id': 'model_type_id',
        'field_values': 'field_values',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'active': 'active',
        'name': 'name',
        'programs': 'programs',
        'broadcasts': 'broadcasts',
        'model_type': 'model_type'
    }

    def __init__(self, id=None, updated_at=None, created_at=None, deleted_at=None, external_station_id=None, model_type_id=None, field_values=None, firstname=None, lastname=None, active=None, name=None, programs=None, broadcasts=None, model_type=None):
        """
        PresenterResult - a model defined in Swagger
        """

        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._external_station_id = None
        self._model_type_id = None
        self._field_values = None
        self._firstname = None
        self._lastname = None
        self._active = None
        self._name = None
        self._programs = None
        self._broadcasts = None
        self._model_type = None

        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.deleted_at = deleted_at
        if external_station_id is not None:
          self.external_station_id = external_station_id
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
        if programs is not None:
          self.programs = programs
        if broadcasts is not None:
          self.broadcasts = broadcasts
        if model_type is not None:
          self.model_type = model_type

    @property
    def id(self):
        """
        Gets the id of this PresenterResult.

        :return: The id of this PresenterResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PresenterResult.

        :param id: The id of this PresenterResult.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this PresenterResult.

        :return: The updated_at of this PresenterResult.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this PresenterResult.

        :param updated_at: The updated_at of this PresenterResult.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this PresenterResult.

        :return: The created_at of this PresenterResult.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this PresenterResult.

        :param created_at: The created_at of this PresenterResult.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this PresenterResult.

        :return: The deleted_at of this PresenterResult.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this PresenterResult.

        :param deleted_at: The deleted_at of this PresenterResult.
        :type: datetime
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")

        self._deleted_at = deleted_at

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this PresenterResult.

        :return: The external_station_id of this PresenterResult.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this PresenterResult.

        :param external_station_id: The external_station_id of this PresenterResult.
        :type: int
        """

        self._external_station_id = external_station_id

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this PresenterResult.

        :return: The model_type_id of this PresenterResult.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this PresenterResult.

        :param model_type_id: The model_type_id of this PresenterResult.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this PresenterResult.

        :return: The field_values of this PresenterResult.
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this PresenterResult.

        :param field_values: The field_values of this PresenterResult.
        :type: object
        """

        self._field_values = field_values

    @property
    def firstname(self):
        """
        Gets the firstname of this PresenterResult.

        :return: The firstname of this PresenterResult.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this PresenterResult.

        :param firstname: The firstname of this PresenterResult.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this PresenterResult.

        :return: The lastname of this PresenterResult.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this PresenterResult.

        :param lastname: The lastname of this PresenterResult.
        :type: str
        """

        self._lastname = lastname

    @property
    def active(self):
        """
        Gets the active of this PresenterResult.

        :return: The active of this PresenterResult.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PresenterResult.

        :param active: The active of this PresenterResult.
        :type: bool
        """

        self._active = active

    @property
    def name(self):
        """
        Gets the name of this PresenterResult.

        :return: The name of this PresenterResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PresenterResult.

        :param name: The name of this PresenterResult.
        :type: str
        """

        self._name = name

    @property
    def programs(self):
        """
        Gets the programs of this PresenterResult.

        :return: The programs of this PresenterResult.
        :rtype: PresenterRelationsPrograms
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """
        Sets the programs of this PresenterResult.

        :param programs: The programs of this PresenterResult.
        :type: PresenterRelationsPrograms
        """

        self._programs = programs

    @property
    def broadcasts(self):
        """
        Gets the broadcasts of this PresenterResult.

        :return: The broadcasts of this PresenterResult.
        :rtype: PresenterRelationsBroadcasts
        """
        return self._broadcasts

    @broadcasts.setter
    def broadcasts(self, broadcasts):
        """
        Sets the broadcasts of this PresenterResult.

        :param broadcasts: The broadcasts of this PresenterResult.
        :type: PresenterRelationsBroadcasts
        """

        self._broadcasts = broadcasts

    @property
    def model_type(self):
        """
        Gets the model_type of this PresenterResult.

        :return: The model_type of this PresenterResult.
        :rtype: BroadcastRelationsModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this PresenterResult.

        :param model_type: The model_type of this PresenterResult.
        :type: BroadcastRelationsModelType
        """

        self._model_type = model_type

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
        if not isinstance(other, PresenterResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
