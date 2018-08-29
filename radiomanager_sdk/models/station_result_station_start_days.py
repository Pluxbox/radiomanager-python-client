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


class StationResultStationStartDays(object):
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
        'monday': 'str',
        'tuesday': 'str',
        'wednesday': 'str',
        'thursday': 'str',
        'friday': 'str',
        'saturday': 'str',
        'sunday': 'str'
    }

    attribute_map = {
        'monday': 'monday',
        'tuesday': 'tuesday',
        'wednesday': 'wednesday',
        'thursday': 'thursday',
        'friday': 'friday',
        'saturday': 'saturday',
        'sunday': 'sunday'
    }

    def __init__(self, monday=None, tuesday=None, wednesday=None, thursday=None, friday=None, saturday=None, sunday=None):
        """
        StationResultStationStartDays - a model defined in Swagger
        """

        self._monday = None
        self._tuesday = None
        self._wednesday = None
        self._thursday = None
        self._friday = None
        self._saturday = None
        self._sunday = None

        if monday is not None:
          self.monday = monday
        if tuesday is not None:
          self.tuesday = tuesday
        if wednesday is not None:
          self.wednesday = wednesday
        if thursday is not None:
          self.thursday = thursday
        if friday is not None:
          self.friday = friday
        if saturday is not None:
          self.saturday = saturday
        if sunday is not None:
          self.sunday = sunday

    @property
    def monday(self):
        """
        Gets the monday of this StationResultStationStartDays.

        :return: The monday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._monday

    @monday.setter
    def monday(self, monday):
        """
        Sets the monday of this StationResultStationStartDays.

        :param monday: The monday of this StationResultStationStartDays.
        :type: str
        """

        self._monday = monday

    @property
    def tuesday(self):
        """
        Gets the tuesday of this StationResultStationStartDays.

        :return: The tuesday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._tuesday

    @tuesday.setter
    def tuesday(self, tuesday):
        """
        Sets the tuesday of this StationResultStationStartDays.

        :param tuesday: The tuesday of this StationResultStationStartDays.
        :type: str
        """

        self._tuesday = tuesday

    @property
    def wednesday(self):
        """
        Gets the wednesday of this StationResultStationStartDays.

        :return: The wednesday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._wednesday

    @wednesday.setter
    def wednesday(self, wednesday):
        """
        Sets the wednesday of this StationResultStationStartDays.

        :param wednesday: The wednesday of this StationResultStationStartDays.
        :type: str
        """

        self._wednesday = wednesday

    @property
    def thursday(self):
        """
        Gets the thursday of this StationResultStationStartDays.

        :return: The thursday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._thursday

    @thursday.setter
    def thursday(self, thursday):
        """
        Sets the thursday of this StationResultStationStartDays.

        :param thursday: The thursday of this StationResultStationStartDays.
        :type: str
        """

        self._thursday = thursday

    @property
    def friday(self):
        """
        Gets the friday of this StationResultStationStartDays.

        :return: The friday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._friday

    @friday.setter
    def friday(self, friday):
        """
        Sets the friday of this StationResultStationStartDays.

        :param friday: The friday of this StationResultStationStartDays.
        :type: str
        """

        self._friday = friday

    @property
    def saturday(self):
        """
        Gets the saturday of this StationResultStationStartDays.

        :return: The saturday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._saturday

    @saturday.setter
    def saturday(self, saturday):
        """
        Sets the saturday of this StationResultStationStartDays.

        :param saturday: The saturday of this StationResultStationStartDays.
        :type: str
        """

        self._saturday = saturday

    @property
    def sunday(self):
        """
        Gets the sunday of this StationResultStationStartDays.

        :return: The sunday of this StationResultStationStartDays.
        :rtype: str
        """
        return self._sunday

    @sunday.setter
    def sunday(self, sunday):
        """
        Sets the sunday of this StationResultStationStartDays.

        :param sunday: The sunday of this StationResultStationStartDays.
        :type: str
        """

        self._sunday = sunday

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
        if not isinstance(other, StationResultStationStartDays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
