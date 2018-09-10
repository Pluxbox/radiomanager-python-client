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


class ModelTypeRelationsCampaignsParams(object):
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
        'model_type_id': 'int'
    }

    attribute_map = {
        'model_type_id': 'model_type_id'
    }

    def __init__(self, model_type_id=None):  # noqa: E501
        """ModelTypeRelationsCampaignsParams - a model defined in Swagger"""  # noqa: E501

        self._model_type_id = None
        self.discriminator = None

        if model_type_id is not None:
            self.model_type_id = model_type_id

    @property
    def model_type_id(self):
        """Gets the model_type_id of this ModelTypeRelationsCampaignsParams.  # noqa: E501


        :return: The model_type_id of this ModelTypeRelationsCampaignsParams.  # noqa: E501
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """Sets the model_type_id of this ModelTypeRelationsCampaignsParams.


        :param model_type_id: The model_type_id of this ModelTypeRelationsCampaignsParams.  # noqa: E501
        :type: int
        """

        self._model_type_id = model_type_id

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
        if not isinstance(other, ModelTypeRelationsCampaignsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
