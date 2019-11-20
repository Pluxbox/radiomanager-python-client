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


class ImportItem(object):
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
        'model_type_id': 'int',
        'external_id': 'str',
        'field_values': 'object',
        'title': 'str',
        'duration': 'int',
        'start': 'datetime',
        'recommended': 'bool',
        'static_start': 'bool',
        'details': 'str',
        'contacts': 'list[int]',
        'tags': 'list[int]'
    }

    attribute_map = {
        'model_type_id': 'model_type_id',
        'external_id': 'external_id',
        'field_values': 'field_values',
        'title': 'title',
        'duration': 'duration',
        'start': 'start',
        'recommended': 'recommended',
        'static_start': 'static_start',
        'details': 'details',
        'contacts': 'contacts',
        'tags': 'tags'
    }

    def __init__(self, model_type_id=None, external_id=None, field_values=None, title=None, duration=None, start=None, recommended=None, static_start=None, details=None, contacts=None, tags=None):  # noqa: E501
        """ImportItem - a model defined in Swagger"""  # noqa: E501

        self._model_type_id = None
        self._external_id = None
        self._field_values = None
        self._title = None
        self._duration = None
        self._start = None
        self._recommended = None
        self._static_start = None
        self._details = None
        self._contacts = None
        self._tags = None
        self.discriminator = None

        self.model_type_id = model_type_id
        self.external_id = external_id
        if field_values is not None:
            self.field_values = field_values
        if title is not None:
            self.title = title
        if duration is not None:
            self.duration = duration
        if start is not None:
            self.start = start
        if recommended is not None:
            self.recommended = recommended
        if static_start is not None:
            self.static_start = static_start
        if details is not None:
            self.details = details
        if contacts is not None:
            self.contacts = contacts
        if tags is not None:
            self.tags = tags

    @property
    def model_type_id(self):
        """Gets the model_type_id of this ImportItem.  # noqa: E501


        :return: The model_type_id of this ImportItem.  # noqa: E501
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """Sets the model_type_id of this ImportItem.


        :param model_type_id: The model_type_id of this ImportItem.  # noqa: E501
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")  # noqa: E501

        self._model_type_id = model_type_id

    @property
    def external_id(self):
        """Gets the external_id of this ImportItem.  # noqa: E501


        :return: The external_id of this ImportItem.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ImportItem.


        :param external_id: The external_id of this ImportItem.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

    @property
    def field_values(self):
        """Gets the field_values of this ImportItem.  # noqa: E501


        :return: The field_values of this ImportItem.  # noqa: E501
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """Sets the field_values of this ImportItem.


        :param field_values: The field_values of this ImportItem.  # noqa: E501
        :type: object
        """

        self._field_values = field_values

    @property
    def title(self):
        """Gets the title of this ImportItem.  # noqa: E501


        :return: The title of this ImportItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ImportItem.


        :param title: The title of this ImportItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def duration(self):
        """Gets the duration of this ImportItem.  # noqa: E501


        :return: The duration of this ImportItem.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ImportItem.


        :param duration: The duration of this ImportItem.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def start(self):
        """Gets the start of this ImportItem.  # noqa: E501


        :return: The start of this ImportItem.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ImportItem.


        :param start: The start of this ImportItem.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def recommended(self):
        """Gets the recommended of this ImportItem.  # noqa: E501


        :return: The recommended of this ImportItem.  # noqa: E501
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """Sets the recommended of this ImportItem.


        :param recommended: The recommended of this ImportItem.  # noqa: E501
        :type: bool
        """

        self._recommended = recommended

    @property
    def static_start(self):
        """Gets the static_start of this ImportItem.  # noqa: E501


        :return: The static_start of this ImportItem.  # noqa: E501
        :rtype: bool
        """
        return self._static_start

    @static_start.setter
    def static_start(self, static_start):
        """Sets the static_start of this ImportItem.


        :param static_start: The static_start of this ImportItem.  # noqa: E501
        :type: bool
        """

        self._static_start = static_start

    @property
    def details(self):
        """Gets the details of this ImportItem.  # noqa: E501


        :return: The details of this ImportItem.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ImportItem.


        :param details: The details of this ImportItem.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def contacts(self):
        """Gets the contacts of this ImportItem.  # noqa: E501


        :return: The contacts of this ImportItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ImportItem.


        :param contacts: The contacts of this ImportItem.  # noqa: E501
        :type: list[int]
        """

        self._contacts = contacts

    @property
    def tags(self):
        """Gets the tags of this ImportItem.  # noqa: E501


        :return: The tags of this ImportItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ImportItem.


        :param tags: The tags of this ImportItem.  # noqa: E501
        :type: list[int]
        """

        self._tags = tags

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
        if not isinstance(other, ImportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
