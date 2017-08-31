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


class Item(object):
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
        'block_id': 'int',
        'external_id': 'str',
        'field_values': 'ImportItemFieldValues',
        'title': 'str',
        'duration': 'int',
        'start': 'datetime',
        'status': 'str',
        '_import': 'int',
        'campaign_id': 'int',
        'recommended': 'bool',
        'station_draft_id': 'int',
        'program_draft_id': 'int',
        'user_draft_id': 'int',
        'static_start': 'bool',
        'details': 'str'
    }

    attribute_map = {
        'model_type_id': 'model_type_id',
        'block_id': 'block_id',
        'external_id': 'external_id',
        'field_values': 'field_values',
        'title': 'title',
        'duration': 'duration',
        'start': 'start',
        'status': 'status',
        '_import': 'import',
        'campaign_id': 'campaign_id',
        'recommended': 'recommended',
        'station_draft_id': 'station_draft_id',
        'program_draft_id': 'program_draft_id',
        'user_draft_id': 'user_draft_id',
        'static_start': 'static_start',
        'details': 'details'
    }

    def __init__(self, model_type_id=None, block_id=None, external_id=None, field_values=None, title=None, duration=None, start=None, status=None, _import=None, campaign_id=None, recommended=None, station_draft_id=None, program_draft_id=None, user_draft_id=None, static_start=None, details=None):
        """
        Item - a model defined in Swagger
        """

        self._model_type_id = None
        self._block_id = None
        self._external_id = None
        self._field_values = None
        self._title = None
        self._duration = None
        self._start = None
        self._status = None
        self.__import = None
        self._campaign_id = None
        self._recommended = None
        self._station_draft_id = None
        self._program_draft_id = None
        self._user_draft_id = None
        self._static_start = None
        self._details = None

        self.model_type_id = model_type_id
        if block_id is not None:
          self.block_id = block_id
        if external_id is not None:
          self.external_id = external_id
        if field_values is not None:
          self.field_values = field_values
        if title is not None:
          self.title = title
        if duration is not None:
          self.duration = duration
        if start is not None:
          self.start = start
        if status is not None:
          self.status = status
        if _import is not None:
          self._import = _import
        if campaign_id is not None:
          self.campaign_id = campaign_id
        if recommended is not None:
          self.recommended = recommended
        if station_draft_id is not None:
          self.station_draft_id = station_draft_id
        if program_draft_id is not None:
          self.program_draft_id = program_draft_id
        if user_draft_id is not None:
          self.user_draft_id = user_draft_id
        if static_start is not None:
          self.static_start = static_start
        if details is not None:
          self.details = details

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this Item.

        :return: The model_type_id of this Item.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this Item.

        :param model_type_id: The model_type_id of this Item.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def block_id(self):
        """
        Gets the block_id of this Item.

        :return: The block_id of this Item.
        :rtype: int
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """
        Sets the block_id of this Item.

        :param block_id: The block_id of this Item.
        :type: int
        """

        self._block_id = block_id

    @property
    def external_id(self):
        """
        Gets the external_id of this Item.

        :return: The external_id of this Item.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this Item.

        :param external_id: The external_id of this Item.
        :type: str
        """

        self._external_id = external_id

    @property
    def field_values(self):
        """
        Gets the field_values of this Item.

        :return: The field_values of this Item.
        :rtype: ImportItemFieldValues
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this Item.

        :param field_values: The field_values of this Item.
        :type: ImportItemFieldValues
        """

        self._field_values = field_values

    @property
    def title(self):
        """
        Gets the title of this Item.

        :return: The title of this Item.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Item.

        :param title: The title of this Item.
        :type: str
        """

        self._title = title

    @property
    def duration(self):
        """
        Gets the duration of this Item.

        :return: The duration of this Item.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this Item.

        :param duration: The duration of this Item.
        :type: int
        """

        self._duration = duration

    @property
    def start(self):
        """
        Gets the start of this Item.

        :return: The start of this Item.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this Item.

        :param start: The start of this Item.
        :type: datetime
        """

        self._start = start

    @property
    def status(self):
        """
        Gets the status of this Item.

        :return: The status of this Item.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Item.

        :param status: The status of this Item.
        :type: str
        """
        allowed_values = ["scheduled", "playing", "played"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def _import(self):
        """
        Gets the _import of this Item.

        :return: The _import of this Item.
        :rtype: int
        """
        return self.__import

    @_import.setter
    def _import(self, _import):
        """
        Sets the _import of this Item.

        :param _import: The _import of this Item.
        :type: int
        """

        self.__import = _import

    @property
    def campaign_id(self):
        """
        Gets the campaign_id of this Item.

        :return: The campaign_id of this Item.
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Sets the campaign_id of this Item.

        :param campaign_id: The campaign_id of this Item.
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def recommended(self):
        """
        Gets the recommended of this Item.

        :return: The recommended of this Item.
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """
        Sets the recommended of this Item.

        :param recommended: The recommended of this Item.
        :type: bool
        """

        self._recommended = recommended

    @property
    def station_draft_id(self):
        """
        Gets the station_draft_id of this Item.

        :return: The station_draft_id of this Item.
        :rtype: int
        """
        return self._station_draft_id

    @station_draft_id.setter
    def station_draft_id(self, station_draft_id):
        """
        Sets the station_draft_id of this Item.

        :param station_draft_id: The station_draft_id of this Item.
        :type: int
        """

        self._station_draft_id = station_draft_id

    @property
    def program_draft_id(self):
        """
        Gets the program_draft_id of this Item.

        :return: The program_draft_id of this Item.
        :rtype: int
        """
        return self._program_draft_id

    @program_draft_id.setter
    def program_draft_id(self, program_draft_id):
        """
        Sets the program_draft_id of this Item.

        :param program_draft_id: The program_draft_id of this Item.
        :type: int
        """

        self._program_draft_id = program_draft_id

    @property
    def user_draft_id(self):
        """
        Gets the user_draft_id of this Item.

        :return: The user_draft_id of this Item.
        :rtype: int
        """
        return self._user_draft_id

    @user_draft_id.setter
    def user_draft_id(self, user_draft_id):
        """
        Sets the user_draft_id of this Item.

        :param user_draft_id: The user_draft_id of this Item.
        :type: int
        """

        self._user_draft_id = user_draft_id

    @property
    def static_start(self):
        """
        Gets the static_start of this Item.

        :return: The static_start of this Item.
        :rtype: bool
        """
        return self._static_start

    @static_start.setter
    def static_start(self, static_start):
        """
        Sets the static_start of this Item.

        :param static_start: The static_start of this Item.
        :type: bool
        """

        self._static_start = static_start

    @property
    def details(self):
        """
        Gets the details of this Item.

        :return: The details of this Item.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Item.

        :param details: The details of this Item.
        :type: str
        """

        self._details = details

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
        if not isinstance(other, Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
