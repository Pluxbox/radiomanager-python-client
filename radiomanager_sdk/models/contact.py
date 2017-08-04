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


class Contact(object):
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
        'field_values': 'ContactFieldValues',
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'model_type_id': 'model_type_id',
        'field_values': 'field_values',
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'phone': 'phone'
    }

    def __init__(self, model_type_id=None, field_values=None, email=None, firstname=None, lastname=None, phone=None):
        """
        Contact - a model defined in Swagger
        """

        self._model_type_id = None
        self._field_values = None
        self._email = None
        self._firstname = None
        self._lastname = None
        self._phone = None
        self.discriminator = None

        self.model_type_id = model_type_id
        if field_values is not None:
          self.field_values = field_values
        if email is not None:
          self.email = email
        self.firstname = firstname
        self.lastname = lastname
        if phone is not None:
          self.phone = phone

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this Contact.

        :return: The model_type_id of this Contact.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this Contact.

        :param model_type_id: The model_type_id of this Contact.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this Contact.

        :return: The field_values of this Contact.
        :rtype: ContactFieldValues
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this Contact.

        :param field_values: The field_values of this Contact.
        :type: ContactFieldValues
        """

        self._field_values = field_values

    @property
    def email(self):
        """
        Gets the email of this Contact.

        :return: The email of this Contact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Contact.

        :param email: The email of this Contact.
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """
        Gets the firstname of this Contact.

        :return: The firstname of this Contact.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Contact.

        :param firstname: The firstname of this Contact.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this Contact.

        :return: The lastname of this Contact.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Contact.

        :param lastname: The lastname of this Contact.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def phone(self):
        """
        Gets the phone of this Contact.

        :return: The phone of this Contact.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Contact.

        :param phone: The phone of this Contact.
        :type: str
        """

        self._phone = phone

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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
