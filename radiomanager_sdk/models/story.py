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


class Story(object):
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
        'recommended': 'bool',
        'field_values': 'object',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'model_type_id': 'model_type_id',
        'recommended': 'recommended',
        'field_values': 'field_values',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, model_type_id=None, recommended=None, field_values=None, name=None, description=None):  # noqa: E501
        """Story - a model defined in Swagger"""  # noqa: E501

        self._model_type_id = None
        self._recommended = None
        self._field_values = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.model_type_id = model_type_id
        if recommended is not None:
            self.recommended = recommended
        if field_values is not None:
            self.field_values = field_values
        self.name = name
        if description is not None:
            self.description = description

    @property
    def model_type_id(self):
        """Gets the model_type_id of this Story.  # noqa: E501


        :return: The model_type_id of this Story.  # noqa: E501
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """Sets the model_type_id of this Story.


        :param model_type_id: The model_type_id of this Story.  # noqa: E501
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")  # noqa: E501

        self._model_type_id = model_type_id

    @property
    def recommended(self):
        """Gets the recommended of this Story.  # noqa: E501


        :return: The recommended of this Story.  # noqa: E501
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """Sets the recommended of this Story.


        :param recommended: The recommended of this Story.  # noqa: E501
        :type: bool
        """

        self._recommended = recommended

    @property
    def field_values(self):
        """Gets the field_values of this Story.  # noqa: E501


        :return: The field_values of this Story.  # noqa: E501
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """Sets the field_values of this Story.


        :param field_values: The field_values of this Story.  # noqa: E501
        :type: object
        """

        self._field_values = field_values

    @property
    def name(self):
        """Gets the name of this Story.  # noqa: E501


        :return: The name of this Story.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Story.


        :param name: The name of this Story.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Story.  # noqa: E501


        :return: The description of this Story.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Story.


        :param description: The description of this Story.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, Story):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
