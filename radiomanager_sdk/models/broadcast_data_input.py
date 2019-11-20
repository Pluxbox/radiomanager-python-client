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

from radiomanager_sdk.models.broadcast import Broadcast  # noqa: F401,E501
from radiomanager_sdk.models.broadcast_input_only import BroadcastInputOnly  # noqa: F401,E501


class BroadcastDataInput(object):
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
        'program_id': 'int',
        'model_type_id': 'int',
        'station_id': 'int',
        'field_values': 'object',
        'title': 'str',
        'start': 'datetime',
        'stop': 'datetime',
        'genre_id': 'int',
        'description': 'str',
        'short_name': 'str',
        'medium_name': 'str',
        'website': 'str',
        'email': 'str',
        'recommended': 'bool',
        'language': 'str',
        'published': 'bool',
        'repetition_uid': 'str',
        'repetition_type': 'str',
        'repetition_end': 'datetime',
        'repetition_start': 'datetime',
        'repetition_days': 'str',
        'pty_code_id': 'int',
        'tags': 'list[int]',
        'presenters': 'list[int]'
    }

    attribute_map = {
        'program_id': 'program_id',
        'model_type_id': 'model_type_id',
        'station_id': 'station_id',
        'field_values': 'field_values',
        'title': 'title',
        'start': 'start',
        'stop': 'stop',
        'genre_id': 'genre_id',
        'description': 'description',
        'short_name': 'short_name',
        'medium_name': 'medium_name',
        'website': 'website',
        'email': 'email',
        'recommended': 'recommended',
        'language': 'language',
        'published': 'published',
        'repetition_uid': 'repetition_uid',
        'repetition_type': 'repetition_type',
        'repetition_end': 'repetition_end',
        'repetition_start': 'repetition_start',
        'repetition_days': 'repetition_days',
        'pty_code_id': 'pty_code_id',
        'tags': 'tags',
        'presenters': 'presenters'
    }

    def __init__(self, program_id=None, model_type_id=None, station_id=None, field_values=None, title=None, start=None, stop=None, genre_id=None, description=None, short_name=None, medium_name=None, website=None, email=None, recommended=None, language=None, published=None, repetition_uid=None, repetition_type=None, repetition_end=None, repetition_start=None, repetition_days=None, pty_code_id=None, tags=None, presenters=None):  # noqa: E501
        """BroadcastDataInput - a model defined in Swagger"""  # noqa: E501

        self._program_id = None
        self._model_type_id = None
        self._station_id = None
        self._field_values = None
        self._title = None
        self._start = None
        self._stop = None
        self._genre_id = None
        self._description = None
        self._short_name = None
        self._medium_name = None
        self._website = None
        self._email = None
        self._recommended = None
        self._language = None
        self._published = None
        self._repetition_uid = None
        self._repetition_type = None
        self._repetition_end = None
        self._repetition_start = None
        self._repetition_days = None
        self._pty_code_id = None
        self._tags = None
        self._presenters = None
        self.discriminator = None

        if program_id is not None:
            self.program_id = program_id
        if model_type_id is not None:
            self.model_type_id = model_type_id
        if station_id is not None:
            self.station_id = station_id
        if field_values is not None:
            self.field_values = field_values
        if title is not None:
            self.title = title
        if start is not None:
            self.start = start
        if stop is not None:
            self.stop = stop
        if genre_id is not None:
            self.genre_id = genre_id
        if description is not None:
            self.description = description
        if short_name is not None:
            self.short_name = short_name
        if medium_name is not None:
            self.medium_name = medium_name
        if website is not None:
            self.website = website
        if email is not None:
            self.email = email
        if recommended is not None:
            self.recommended = recommended
        if language is not None:
            self.language = language
        if published is not None:
            self.published = published
        if repetition_uid is not None:
            self.repetition_uid = repetition_uid
        if repetition_type is not None:
            self.repetition_type = repetition_type
        if repetition_end is not None:
            self.repetition_end = repetition_end
        if repetition_start is not None:
            self.repetition_start = repetition_start
        if repetition_days is not None:
            self.repetition_days = repetition_days
        if pty_code_id is not None:
            self.pty_code_id = pty_code_id
        if tags is not None:
            self.tags = tags
        if presenters is not None:
            self.presenters = presenters

    @property
    def program_id(self):
        """Gets the program_id of this BroadcastDataInput.  # noqa: E501


        :return: The program_id of this BroadcastDataInput.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this BroadcastDataInput.


        :param program_id: The program_id of this BroadcastDataInput.  # noqa: E501
        :type: int
        """

        self._program_id = program_id

    @property
    def model_type_id(self):
        """Gets the model_type_id of this BroadcastDataInput.  # noqa: E501


        :return: The model_type_id of this BroadcastDataInput.  # noqa: E501
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """Sets the model_type_id of this BroadcastDataInput.


        :param model_type_id: The model_type_id of this BroadcastDataInput.  # noqa: E501
        :type: int
        """

        self._model_type_id = model_type_id

    @property
    def station_id(self):
        """Gets the station_id of this BroadcastDataInput.  # noqa: E501


        :return: The station_id of this BroadcastDataInput.  # noqa: E501
        :rtype: int
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id):
        """Sets the station_id of this BroadcastDataInput.


        :param station_id: The station_id of this BroadcastDataInput.  # noqa: E501
        :type: int
        """

        self._station_id = station_id

    @property
    def field_values(self):
        """Gets the field_values of this BroadcastDataInput.  # noqa: E501


        :return: The field_values of this BroadcastDataInput.  # noqa: E501
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """Sets the field_values of this BroadcastDataInput.


        :param field_values: The field_values of this BroadcastDataInput.  # noqa: E501
        :type: object
        """

        self._field_values = field_values

    @property
    def title(self):
        """Gets the title of this BroadcastDataInput.  # noqa: E501


        :return: The title of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BroadcastDataInput.


        :param title: The title of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def start(self):
        """Gets the start of this BroadcastDataInput.  # noqa: E501


        :return: The start of this BroadcastDataInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BroadcastDataInput.


        :param start: The start of this BroadcastDataInput.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this BroadcastDataInput.  # noqa: E501


        :return: The stop of this BroadcastDataInput.  # noqa: E501
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this BroadcastDataInput.


        :param stop: The stop of this BroadcastDataInput.  # noqa: E501
        :type: datetime
        """

        self._stop = stop

    @property
    def genre_id(self):
        """Gets the genre_id of this BroadcastDataInput.  # noqa: E501


        :return: The genre_id of this BroadcastDataInput.  # noqa: E501
        :rtype: int
        """
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        """Sets the genre_id of this BroadcastDataInput.


        :param genre_id: The genre_id of this BroadcastDataInput.  # noqa: E501
        :type: int
        """

        self._genre_id = genre_id

    @property
    def description(self):
        """Gets the description of this BroadcastDataInput.  # noqa: E501


        :return: The description of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BroadcastDataInput.


        :param description: The description of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def short_name(self):
        """Gets the short_name of this BroadcastDataInput.  # noqa: E501


        :return: The short_name of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this BroadcastDataInput.


        :param short_name: The short_name of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def medium_name(self):
        """Gets the medium_name of this BroadcastDataInput.  # noqa: E501


        :return: The medium_name of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._medium_name

    @medium_name.setter
    def medium_name(self, medium_name):
        """Sets the medium_name of this BroadcastDataInput.


        :param medium_name: The medium_name of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._medium_name = medium_name

    @property
    def website(self):
        """Gets the website of this BroadcastDataInput.  # noqa: E501


        :return: The website of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this BroadcastDataInput.


        :param website: The website of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """Gets the email of this BroadcastDataInput.  # noqa: E501


        :return: The email of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BroadcastDataInput.


        :param email: The email of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def recommended(self):
        """Gets the recommended of this BroadcastDataInput.  # noqa: E501


        :return: The recommended of this BroadcastDataInput.  # noqa: E501
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """Sets the recommended of this BroadcastDataInput.


        :param recommended: The recommended of this BroadcastDataInput.  # noqa: E501
        :type: bool
        """

        self._recommended = recommended

    @property
    def language(self):
        """Gets the language of this BroadcastDataInput.  # noqa: E501


        :return: The language of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BroadcastDataInput.


        :param language: The language of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def published(self):
        """Gets the published of this BroadcastDataInput.  # noqa: E501


        :return: The published of this BroadcastDataInput.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this BroadcastDataInput.


        :param published: The published of this BroadcastDataInput.  # noqa: E501
        :type: bool
        """

        self._published = published

    @property
    def repetition_uid(self):
        """Gets the repetition_uid of this BroadcastDataInput.  # noqa: E501


        :return: The repetition_uid of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._repetition_uid

    @repetition_uid.setter
    def repetition_uid(self, repetition_uid):
        """Sets the repetition_uid of this BroadcastDataInput.


        :param repetition_uid: The repetition_uid of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._repetition_uid = repetition_uid

    @property
    def repetition_type(self):
        """Gets the repetition_type of this BroadcastDataInput.  # noqa: E501


        :return: The repetition_type of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._repetition_type

    @repetition_type.setter
    def repetition_type(self, repetition_type):
        """Sets the repetition_type of this BroadcastDataInput.


        :param repetition_type: The repetition_type of this BroadcastDataInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["1 week", "2 week", "4 week", "1 month"]  # noqa: E501
        if repetition_type not in allowed_values:
            raise ValueError(
                "Invalid value for `repetition_type` ({0}), must be one of {1}"  # noqa: E501
                .format(repetition_type, allowed_values)
            )

        self._repetition_type = repetition_type

    @property
    def repetition_end(self):
        """Gets the repetition_end of this BroadcastDataInput.  # noqa: E501


        :return: The repetition_end of this BroadcastDataInput.  # noqa: E501
        :rtype: datetime
        """
        return self._repetition_end

    @repetition_end.setter
    def repetition_end(self, repetition_end):
        """Sets the repetition_end of this BroadcastDataInput.


        :param repetition_end: The repetition_end of this BroadcastDataInput.  # noqa: E501
        :type: datetime
        """

        self._repetition_end = repetition_end

    @property
    def repetition_start(self):
        """Gets the repetition_start of this BroadcastDataInput.  # noqa: E501


        :return: The repetition_start of this BroadcastDataInput.  # noqa: E501
        :rtype: datetime
        """
        return self._repetition_start

    @repetition_start.setter
    def repetition_start(self, repetition_start):
        """Sets the repetition_start of this BroadcastDataInput.


        :param repetition_start: The repetition_start of this BroadcastDataInput.  # noqa: E501
        :type: datetime
        """

        self._repetition_start = repetition_start

    @property
    def repetition_days(self):
        """Gets the repetition_days of this BroadcastDataInput.  # noqa: E501


        :return: The repetition_days of this BroadcastDataInput.  # noqa: E501
        :rtype: str
        """
        return self._repetition_days

    @repetition_days.setter
    def repetition_days(self, repetition_days):
        """Sets the repetition_days of this BroadcastDataInput.


        :param repetition_days: The repetition_days of this BroadcastDataInput.  # noqa: E501
        :type: str
        """

        self._repetition_days = repetition_days

    @property
    def pty_code_id(self):
        """Gets the pty_code_id of this BroadcastDataInput.  # noqa: E501


        :return: The pty_code_id of this BroadcastDataInput.  # noqa: E501
        :rtype: int
        """
        return self._pty_code_id

    @pty_code_id.setter
    def pty_code_id(self, pty_code_id):
        """Sets the pty_code_id of this BroadcastDataInput.


        :param pty_code_id: The pty_code_id of this BroadcastDataInput.  # noqa: E501
        :type: int
        """

        self._pty_code_id = pty_code_id

    @property
    def tags(self):
        """Gets the tags of this BroadcastDataInput.  # noqa: E501


        :return: The tags of this BroadcastDataInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BroadcastDataInput.


        :param tags: The tags of this BroadcastDataInput.  # noqa: E501
        :type: list[int]
        """

        self._tags = tags

    @property
    def presenters(self):
        """Gets the presenters of this BroadcastDataInput.  # noqa: E501


        :return: The presenters of this BroadcastDataInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """Sets the presenters of this BroadcastDataInput.


        :param presenters: The presenters of this BroadcastDataInput.  # noqa: E501
        :type: list[int]
        """

        self._presenters = presenters

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
        if not isinstance(other, BroadcastDataInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
