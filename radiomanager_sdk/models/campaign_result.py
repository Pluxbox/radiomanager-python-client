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


class CampaignResult(object):
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
        'id': 'int',
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'deleted_at': 'datetime',
        'item': 'list[Item]',
        'external_station_id': 'int',
        'model_type_id': 'int',
        'field_values': 'object',
        'title': 'str',
        'start': 'datetime',
        'stop': 'datetime',
        'recommended': 'bool',
        'description': 'str',
        'items': 'CampaignRelationsItems',
        'model_type': 'BroadcastRelationsModelType'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'item': 'item',
        'external_station_id': '_external_station_id',
        'model_type_id': 'model_type_id',
        'field_values': 'field_values',
        'title': 'title',
        'start': 'start',
        'stop': 'stop',
        'recommended': 'recommended',
        'description': 'description',
        'items': 'items',
        'model_type': 'model_type'
    }

    def __init__(self, id=None, updated_at=None, created_at=None, deleted_at=None, item=None, external_station_id=None, model_type_id=None, field_values=None, title=None, start=None, stop=None, recommended=None, description=None, items=None, model_type=None):
        """
        CampaignResult - a model defined in Swagger
        """

        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._item = None
        self._external_station_id = None
        self._model_type_id = None
        self._field_values = None
        self._title = None
        self._start = None
        self._stop = None
        self._recommended = None
        self._description = None
        self._items = None
        self._model_type = None

        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.deleted_at = deleted_at
        if item is not None:
          self.item = item
        if external_station_id is not None:
          self.external_station_id = external_station_id
        self.model_type_id = model_type_id
        if field_values is not None:
          self.field_values = field_values
        if title is not None:
          self.title = title
        self.start = start
        self.stop = stop
        if recommended is not None:
          self.recommended = recommended
        if description is not None:
          self.description = description
        if items is not None:
          self.items = items
        if model_type is not None:
          self.model_type = model_type

    @property
    def id(self):
        """
        Gets the id of this CampaignResult.

        :return: The id of this CampaignResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignResult.

        :param id: The id of this CampaignResult.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CampaignResult.

        :return: The updated_at of this CampaignResult.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CampaignResult.

        :param updated_at: The updated_at of this CampaignResult.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this CampaignResult.

        :return: The created_at of this CampaignResult.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CampaignResult.

        :param created_at: The created_at of this CampaignResult.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this CampaignResult.

        :return: The deleted_at of this CampaignResult.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this CampaignResult.

        :param deleted_at: The deleted_at of this CampaignResult.
        :type: datetime
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")

        self._deleted_at = deleted_at

    @property
    def item(self):
        """
        Gets the item of this CampaignResult.

        :return: The item of this CampaignResult.
        :rtype: list[Item]
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this CampaignResult.

        :param item: The item of this CampaignResult.
        :type: list[Item]
        """

        self._item = item

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this CampaignResult.

        :return: The external_station_id of this CampaignResult.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this CampaignResult.

        :param external_station_id: The external_station_id of this CampaignResult.
        :type: int
        """

        self._external_station_id = external_station_id

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this CampaignResult.

        :return: The model_type_id of this CampaignResult.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this CampaignResult.

        :param model_type_id: The model_type_id of this CampaignResult.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this CampaignResult.

        :return: The field_values of this CampaignResult.
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this CampaignResult.

        :param field_values: The field_values of this CampaignResult.
        :type: object
        """

        self._field_values = field_values

    @property
    def title(self):
        """
        Gets the title of this CampaignResult.

        :return: The title of this CampaignResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CampaignResult.

        :param title: The title of this CampaignResult.
        :type: str
        """

        self._title = title

    @property
    def start(self):
        """
        Gets the start of this CampaignResult.

        :return: The start of this CampaignResult.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this CampaignResult.

        :param start: The start of this CampaignResult.
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")

        self._start = start

    @property
    def stop(self):
        """
        Gets the stop of this CampaignResult.

        :return: The stop of this CampaignResult.
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """
        Sets the stop of this CampaignResult.

        :param stop: The stop of this CampaignResult.
        :type: datetime
        """
        if stop is None:
            raise ValueError("Invalid value for `stop`, must not be `None`")

        self._stop = stop

    @property
    def recommended(self):
        """
        Gets the recommended of this CampaignResult.

        :return: The recommended of this CampaignResult.
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """
        Sets the recommended of this CampaignResult.

        :param recommended: The recommended of this CampaignResult.
        :type: bool
        """

        self._recommended = recommended

    @property
    def description(self):
        """
        Gets the description of this CampaignResult.

        :return: The description of this CampaignResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CampaignResult.

        :param description: The description of this CampaignResult.
        :type: str
        """

        self._description = description

    @property
    def items(self):
        """
        Gets the items of this CampaignResult.

        :return: The items of this CampaignResult.
        :rtype: CampaignRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CampaignResult.

        :param items: The items of this CampaignResult.
        :type: CampaignRelationsItems
        """

        self._items = items

    @property
    def model_type(self):
        """
        Gets the model_type of this CampaignResult.

        :return: The model_type of this CampaignResult.
        :rtype: BroadcastRelationsModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CampaignResult.

        :param model_type: The model_type of this CampaignResult.
        :type: BroadcastRelationsModelType
        """

        self._model_type = model_type

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
        if not isinstance(other, CampaignResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
