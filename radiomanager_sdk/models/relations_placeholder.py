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


class RelationsPlaceholder(object):
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
        'params': 'object'
    }

    attribute_map = {
        'href': 'href',
        'model': 'model',
        'operation': 'operation',
        'params': 'params'
    }

    def __init__(self, href=None, model=None, operation=None, params=None):  # noqa: E501
        """RelationsPlaceholder - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._model = None
        self._operation = None
        self._params = None
        self.discriminator = None

        self.href = href
        self.model = model
        self.operation = operation
        self.params = params

    @property
    def href(self):
        """Gets the href of this RelationsPlaceholder.  # noqa: E501

        HREF  # noqa: E501

        :return: The href of this RelationsPlaceholder.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this RelationsPlaceholder.

        HREF  # noqa: E501

        :param href: The href of this RelationsPlaceholder.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def model(self):
        """Gets the model of this RelationsPlaceholder.  # noqa: E501

        MODEL  # noqa: E501

        :return: The model of this RelationsPlaceholder.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this RelationsPlaceholder.

        MODEL  # noqa: E501

        :param model: The model of this RelationsPlaceholder.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def operation(self):
        """Gets the operation of this RelationsPlaceholder.  # noqa: E501

        OPERATION  # noqa: E501

        :return: The operation of this RelationsPlaceholder.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this RelationsPlaceholder.

        OPERATION  # noqa: E501

        :param operation: The operation of this RelationsPlaceholder.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def params(self):
        """Gets the params of this RelationsPlaceholder.  # noqa: E501

        PARAMS  # noqa: E501

        :return: The params of this RelationsPlaceholder.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RelationsPlaceholder.

        PARAMS  # noqa: E501

        :param params: The params of this RelationsPlaceholder.  # noqa: E501
        :type: object
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, RelationsPlaceholder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
