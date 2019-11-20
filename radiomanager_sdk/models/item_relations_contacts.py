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

from radiomanager_sdk.models.item_relations_contacts_params import ItemRelationsContactsParams  # noqa: F401,E501


class ItemRelationsContacts(object):
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
        'href': 'str',
        'model': 'str',
        'operation': 'str',
        'params': 'ItemRelationsContactsParams'
    }

    attribute_map = {
        'href': 'href',
        'model': 'model',
        'operation': 'operation',
        'params': 'params'
    }

    def __init__(self, href=None, model=None, operation=None, params=None):  # noqa: E501
        """ItemRelationsContacts - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._model = None
        self._operation = None
        self._params = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if model is not None:
            self.model = model
        if operation is not None:
            self.operation = operation
        if params is not None:
            self.params = params

    @property
    def href(self):
        """Gets the href of this ItemRelationsContacts.  # noqa: E501


        :return: The href of this ItemRelationsContacts.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ItemRelationsContacts.


        :param href: The href of this ItemRelationsContacts.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def model(self):
        """Gets the model of this ItemRelationsContacts.  # noqa: E501


        :return: The model of this ItemRelationsContacts.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ItemRelationsContacts.


        :param model: The model of this ItemRelationsContacts.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def operation(self):
        """Gets the operation of this ItemRelationsContacts.  # noqa: E501


        :return: The operation of this ItemRelationsContacts.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ItemRelationsContacts.


        :param operation: The operation of this ItemRelationsContacts.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def params(self):
        """Gets the params of this ItemRelationsContacts.  # noqa: E501


        :return: The params of this ItemRelationsContacts.  # noqa: E501
        :rtype: ItemRelationsContactsParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ItemRelationsContacts.


        :param params: The params of this ItemRelationsContacts.  # noqa: E501
        :type: ItemRelationsContactsParams
        """

        self._params = params

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
        if not isinstance(other, ItemRelationsContacts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
