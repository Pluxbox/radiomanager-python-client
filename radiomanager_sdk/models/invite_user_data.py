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


class InviteUserData(object):
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
        'email': 'str',
        'role_id': 'int'
    }

    attribute_map = {
        'email': 'email',
        'role_id': 'role_id'
    }

    def __init__(self, email=None, role_id=None):
        """
        InviteUserData - a model defined in Swagger
        """

        self._email = None
        self._role_id = None
        self.discriminator = None

        self.email = email
        self.role_id = role_id

    @property
    def email(self):
        """
        Gets the email of this InviteUserData.

        :return: The email of this InviteUserData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this InviteUserData.

        :param email: The email of this InviteUserData.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def role_id(self):
        """
        Gets the role_id of this InviteUserData.

        :return: The role_id of this InviteUserData.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """
        Sets the role_id of this InviteUserData.

        :param role_id: The role_id of this InviteUserData.
        :type: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")

        self._role_id = role_id

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
        if not isinstance(other, InviteUserData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
