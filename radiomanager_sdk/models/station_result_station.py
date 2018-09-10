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

from radiomanager_sdk.models.station_result_station_start_days import StationResultStationStartDays  # noqa: F401,E501


class StationResultStation(object):
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
        'id': 'int',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'system_name': 'str',
        'short_name': 'str',
        'medium_name': 'str',
        'website': 'str',
        'email': 'str',
        'keywords': 'list[str]',
        'description': 'str',
        'sms': 'str',
        'telephone': 'str',
        'genre_id': 'int',
        'language': 'str',
        'active': 'bool',
        'logo_rectangle': 'str',
        'logo_128x128': 'str',
        'logo_320x320': 'str',
        'logo_600x600': 'str',
        'pay_off': 'str',
        'pty_code': 'int',
        'pty_type': 'str',
        'station_key': 'str',
        'timezone': 'str',
        'start_days': 'StationResultStationStartDays'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'system_name': 'system_name',
        'short_name': 'short_name',
        'medium_name': 'medium_name',
        'website': 'website',
        'email': 'email',
        'keywords': 'keywords',
        'description': 'description',
        'sms': 'sms',
        'telephone': 'telephone',
        'genre_id': 'genre_id',
        'language': 'language',
        'active': 'active',
        'logo_rectangle': 'logo_rectangle',
        'logo_128x128': 'logo_128x128',
        'logo_320x320': 'logo_320x320',
        'logo_600x600': 'logo_600x600',
        'pay_off': 'pay_off',
        'pty_code': 'pty_code',
        'pty_type': 'pty_type',
        'station_key': 'station_key',
        'timezone': 'timezone',
        'start_days': 'start_days'
    }

    def __init__(self, id=None, name=None, created_at=None, updated_at=None, system_name=None, short_name=None, medium_name=None, website=None, email=None, keywords=None, description=None, sms=None, telephone=None, genre_id=None, language=None, active=None, logo_rectangle=None, logo_128x128=None, logo_320x320=None, logo_600x600=None, pay_off=None, pty_code=None, pty_type=None, station_key=None, timezone=None, start_days=None):  # noqa: E501
        """StationResultStation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._system_name = None
        self._short_name = None
        self._medium_name = None
        self._website = None
        self._email = None
        self._keywords = None
        self._description = None
        self._sms = None
        self._telephone = None
        self._genre_id = None
        self._language = None
        self._active = None
        self._logo_rectangle = None
        self._logo_128x128 = None
        self._logo_320x320 = None
        self._logo_600x600 = None
        self._pay_off = None
        self._pty_code = None
        self._pty_type = None
        self._station_key = None
        self._timezone = None
        self._start_days = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if system_name is not None:
            self.system_name = system_name
        if short_name is not None:
            self.short_name = short_name
        if medium_name is not None:
            self.medium_name = medium_name
        if website is not None:
            self.website = website
        if email is not None:
            self.email = email
        if keywords is not None:
            self.keywords = keywords
        if description is not None:
            self.description = description
        if sms is not None:
            self.sms = sms
        if telephone is not None:
            self.telephone = telephone
        if genre_id is not None:
            self.genre_id = genre_id
        if language is not None:
            self.language = language
        if active is not None:
            self.active = active
        if logo_rectangle is not None:
            self.logo_rectangle = logo_rectangle
        if logo_128x128 is not None:
            self.logo_128x128 = logo_128x128
        if logo_320x320 is not None:
            self.logo_320x320 = logo_320x320
        if logo_600x600 is not None:
            self.logo_600x600 = logo_600x600
        if pay_off is not None:
            self.pay_off = pay_off
        if pty_code is not None:
            self.pty_code = pty_code
        if pty_type is not None:
            self.pty_type = pty_type
        if station_key is not None:
            self.station_key = station_key
        if timezone is not None:
            self.timezone = timezone
        if start_days is not None:
            self.start_days = start_days

    @property
    def id(self):
        """Gets the id of this StationResultStation.  # noqa: E501


        :return: The id of this StationResultStation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StationResultStation.


        :param id: The id of this StationResultStation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StationResultStation.  # noqa: E501


        :return: The name of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StationResultStation.


        :param name: The name of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this StationResultStation.  # noqa: E501


        :return: The created_at of this StationResultStation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StationResultStation.


        :param created_at: The created_at of this StationResultStation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this StationResultStation.  # noqa: E501


        :return: The updated_at of this StationResultStation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this StationResultStation.


        :param updated_at: The updated_at of this StationResultStation.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def system_name(self):
        """Gets the system_name of this StationResultStation.  # noqa: E501


        :return: The system_name of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this StationResultStation.


        :param system_name: The system_name of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def short_name(self):
        """Gets the short_name of this StationResultStation.  # noqa: E501


        :return: The short_name of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this StationResultStation.


        :param short_name: The short_name of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def medium_name(self):
        """Gets the medium_name of this StationResultStation.  # noqa: E501


        :return: The medium_name of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._medium_name

    @medium_name.setter
    def medium_name(self, medium_name):
        """Sets the medium_name of this StationResultStation.


        :param medium_name: The medium_name of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._medium_name = medium_name

    @property
    def website(self):
        """Gets the website of this StationResultStation.  # noqa: E501


        :return: The website of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this StationResultStation.


        :param website: The website of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """Gets the email of this StationResultStation.  # noqa: E501


        :return: The email of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this StationResultStation.


        :param email: The email of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def keywords(self):
        """Gets the keywords of this StationResultStation.  # noqa: E501


        :return: The keywords of this StationResultStation.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this StationResultStation.


        :param keywords: The keywords of this StationResultStation.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def description(self):
        """Gets the description of this StationResultStation.  # noqa: E501


        :return: The description of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StationResultStation.


        :param description: The description of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sms(self):
        """Gets the sms of this StationResultStation.  # noqa: E501


        :return: The sms of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this StationResultStation.


        :param sms: The sms of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._sms = sms

    @property
    def telephone(self):
        """Gets the telephone of this StationResultStation.  # noqa: E501


        :return: The telephone of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this StationResultStation.


        :param telephone: The telephone of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def genre_id(self):
        """Gets the genre_id of this StationResultStation.  # noqa: E501


        :return: The genre_id of this StationResultStation.  # noqa: E501
        :rtype: int
        """
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        """Sets the genre_id of this StationResultStation.


        :param genre_id: The genre_id of this StationResultStation.  # noqa: E501
        :type: int
        """

        self._genre_id = genre_id

    @property
    def language(self):
        """Gets the language of this StationResultStation.  # noqa: E501


        :return: The language of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this StationResultStation.


        :param language: The language of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def active(self):
        """Gets the active of this StationResultStation.  # noqa: E501


        :return: The active of this StationResultStation.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this StationResultStation.


        :param active: The active of this StationResultStation.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def logo_rectangle(self):
        """Gets the logo_rectangle of this StationResultStation.  # noqa: E501


        :return: The logo_rectangle of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._logo_rectangle

    @logo_rectangle.setter
    def logo_rectangle(self, logo_rectangle):
        """Sets the logo_rectangle of this StationResultStation.


        :param logo_rectangle: The logo_rectangle of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._logo_rectangle = logo_rectangle

    @property
    def logo_128x128(self):
        """Gets the logo_128x128 of this StationResultStation.  # noqa: E501


        :return: The logo_128x128 of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._logo_128x128

    @logo_128x128.setter
    def logo_128x128(self, logo_128x128):
        """Sets the logo_128x128 of this StationResultStation.


        :param logo_128x128: The logo_128x128 of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._logo_128x128 = logo_128x128

    @property
    def logo_320x320(self):
        """Gets the logo_320x320 of this StationResultStation.  # noqa: E501


        :return: The logo_320x320 of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._logo_320x320

    @logo_320x320.setter
    def logo_320x320(self, logo_320x320):
        """Sets the logo_320x320 of this StationResultStation.


        :param logo_320x320: The logo_320x320 of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._logo_320x320 = logo_320x320

    @property
    def logo_600x600(self):
        """Gets the logo_600x600 of this StationResultStation.  # noqa: E501


        :return: The logo_600x600 of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._logo_600x600

    @logo_600x600.setter
    def logo_600x600(self, logo_600x600):
        """Sets the logo_600x600 of this StationResultStation.


        :param logo_600x600: The logo_600x600 of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._logo_600x600 = logo_600x600

    @property
    def pay_off(self):
        """Gets the pay_off of this StationResultStation.  # noqa: E501


        :return: The pay_off of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._pay_off

    @pay_off.setter
    def pay_off(self, pay_off):
        """Sets the pay_off of this StationResultStation.


        :param pay_off: The pay_off of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._pay_off = pay_off

    @property
    def pty_code(self):
        """Gets the pty_code of this StationResultStation.  # noqa: E501


        :return: The pty_code of this StationResultStation.  # noqa: E501
        :rtype: int
        """
        return self._pty_code

    @pty_code.setter
    def pty_code(self, pty_code):
        """Sets the pty_code of this StationResultStation.


        :param pty_code: The pty_code of this StationResultStation.  # noqa: E501
        :type: int
        """

        self._pty_code = pty_code

    @property
    def pty_type(self):
        """Gets the pty_type of this StationResultStation.  # noqa: E501


        :return: The pty_type of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._pty_type

    @pty_type.setter
    def pty_type(self, pty_type):
        """Sets the pty_type of this StationResultStation.


        :param pty_type: The pty_type of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._pty_type = pty_type

    @property
    def station_key(self):
        """Gets the station_key of this StationResultStation.  # noqa: E501


        :return: The station_key of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._station_key

    @station_key.setter
    def station_key(self, station_key):
        """Sets the station_key of this StationResultStation.


        :param station_key: The station_key of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._station_key = station_key

    @property
    def timezone(self):
        """Gets the timezone of this StationResultStation.  # noqa: E501


        :return: The timezone of this StationResultStation.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this StationResultStation.


        :param timezone: The timezone of this StationResultStation.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def start_days(self):
        """Gets the start_days of this StationResultStation.  # noqa: E501


        :return: The start_days of this StationResultStation.  # noqa: E501
        :rtype: StationResultStationStartDays
        """
        return self._start_days

    @start_days.setter
    def start_days(self, start_days):
        """Sets the start_days of this StationResultStation.


        :param start_days: The start_days of this StationResultStation.  # noqa: E501
        :type: StationResultStationStartDays
        """

        self._start_days = start_days

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
        if not isinstance(other, StationResultStation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
