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


class ContactResult(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'deleted_at': 'datetime',
        'external_station_id': 'int',
        'model_type_id': 'int',
        'field_values': 'object',
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'phone': 'str',
        'tags': 'ContactRelationsTags',
        'items': 'ContactRelationsItems',
        'model_type': 'BroadcastRelationsModelType'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'deleted_at': 'deleted_at',
        'external_station_id': '_external_station_id',
        'model_type_id': 'model_type_id',
        'field_values': 'field_values',
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'phone': 'phone',
        'tags': 'tags',
        'items': 'items',
        'model_type': 'model_type'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, deleted_at=None, external_station_id=None, model_type_id=None, field_values=None, email=None, firstname=None, lastname=None, phone=None, tags=None, items=None, model_type=None):
        """
        ContactResult - a model defined in Swagger
        """

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._external_station_id = None
        self._model_type_id = None
        self._field_values = None
        self._email = None
        self._firstname = None
        self._lastname = None
        self._phone = None
        self._tags = None
        self._items = None
        self._model_type = None

        if id is not None:
          self.id = id
        if created_at is not None:
          self.created_at = created_at
        if updated_at is not None:
          self.updated_at = updated_at
        if deleted_at is not None:
          self.deleted_at = deleted_at
        if external_station_id is not None:
          self.external_station_id = external_station_id
        self.model_type_id = model_type_id
        if field_values is not None:
          self.field_values = field_values
        if email is not None:
          self.email = email
        self.firstname = firstname
        self.lastname = lastname
        if phone is not None:
          self.phone = phone
        if tags is not None:
          self.tags = tags
        if items is not None:
          self.items = items
        if model_type is not None:
          self.model_type = model_type

    @property
    def id(self):
        """
        Gets the id of this ContactResult.

        :return: The id of this ContactResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContactResult.

        :param id: The id of this ContactResult.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this ContactResult.

        :return: The created_at of this ContactResult.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ContactResult.

        :param created_at: The created_at of this ContactResult.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ContactResult.

        :return: The updated_at of this ContactResult.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ContactResult.

        :param updated_at: The updated_at of this ContactResult.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this ContactResult.

        :return: The deleted_at of this ContactResult.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this ContactResult.

        :param deleted_at: The deleted_at of this ContactResult.
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this ContactResult.

        :return: The external_station_id of this ContactResult.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this ContactResult.

        :param external_station_id: The external_station_id of this ContactResult.
        :type: int
        """

        self._external_station_id = external_station_id

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this ContactResult.

        :return: The model_type_id of this ContactResult.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this ContactResult.

        :param model_type_id: The model_type_id of this ContactResult.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this ContactResult.

        :return: The field_values of this ContactResult.
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this ContactResult.

        :param field_values: The field_values of this ContactResult.
        :type: object
        """

        self._field_values = field_values

    @property
    def email(self):
        """
        Gets the email of this ContactResult.

        :return: The email of this ContactResult.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ContactResult.

        :param email: The email of this ContactResult.
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """
        Gets the firstname of this ContactResult.

        :return: The firstname of this ContactResult.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this ContactResult.

        :param firstname: The firstname of this ContactResult.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this ContactResult.

        :return: The lastname of this ContactResult.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this ContactResult.

        :param lastname: The lastname of this ContactResult.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def phone(self):
        """
        Gets the phone of this ContactResult.

        :return: The phone of this ContactResult.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this ContactResult.

        :param phone: The phone of this ContactResult.
        :type: str
        """

        self._phone = phone

    @property
    def tags(self):
        """
        Gets the tags of this ContactResult.

        :return: The tags of this ContactResult.
        :rtype: ContactRelationsTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ContactResult.

        :param tags: The tags of this ContactResult.
        :type: ContactRelationsTags
        """

        self._tags = tags

    @property
    def items(self):
        """
        Gets the items of this ContactResult.

        :return: The items of this ContactResult.
        :rtype: ContactRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ContactResult.

        :param items: The items of this ContactResult.
        :type: ContactRelationsItems
        """

        self._items = items

    @property
    def model_type(self):
        """
        Gets the model_type of this ContactResult.

        :return: The model_type of this ContactResult.
        :rtype: BroadcastRelationsModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ContactResult.

        :param model_type: The model_type of this ContactResult.
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
        if not isinstance(other, ContactResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
