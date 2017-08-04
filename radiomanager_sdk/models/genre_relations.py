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


class GenreRelations(object):
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
        'broadcasts': 'GenreRelationsBroadcasts',
        'programs': 'GenreRelationsPrograms'
    }

    attribute_map = {
        'broadcasts': 'broadcasts',
        'programs': 'programs'
    }

    def __init__(self, broadcasts=None, programs=None):
        """
        GenreRelations - a model defined in Swagger
        """

        self._broadcasts = None
        self._programs = None
        self.discriminator = None

        if broadcasts is not None:
          self.broadcasts = broadcasts
        if programs is not None:
          self.programs = programs

    @property
    def broadcasts(self):
        """
        Gets the broadcasts of this GenreRelations.

        :return: The broadcasts of this GenreRelations.
        :rtype: GenreRelationsBroadcasts
        """
        return self._broadcasts

    @broadcasts.setter
    def broadcasts(self, broadcasts):
        """
        Sets the broadcasts of this GenreRelations.

        :param broadcasts: The broadcasts of this GenreRelations.
        :type: GenreRelationsBroadcasts
        """

        self._broadcasts = broadcasts

    @property
    def programs(self):
        """
        Gets the programs of this GenreRelations.

        :return: The programs of this GenreRelations.
        :rtype: GenreRelationsPrograms
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """
        Sets the programs of this GenreRelations.

        :param programs: The programs of this GenreRelations.
        :type: GenreRelationsPrograms
        """

        self._programs = programs

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
        if not isinstance(other, GenreRelations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
