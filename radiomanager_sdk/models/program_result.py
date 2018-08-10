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


class ProgramResult(object):
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
        'external_station_id': 'int',
        'model_type_id': 'int',
        'field_values': 'object',
        'title': 'str',
        'disabled': 'bool',
        'genre_id': 'int',
        'description': 'str',
        'short_name': 'str',
        'medium_name': 'str',
        'website': 'str',
        'email': 'str',
        'recommended': 'bool',
        'language': 'str',
        'pty_code_id': 'int',
        'genre': 'BroadcastRelationsGenre',
        'items': 'ProgramRelationsItems',
        'blocks': 'ProgramRelationsBlocks',
        'broadcasts': 'ProgramRelationsBroadcasts',
        'presenters': 'ProgramRelationsPresenters',
        'tags': 'ProgramRelationsTags',
        'model_type': 'BroadcastRelationsModelType'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'external_station_id': '_external_station_id',
        'model_type_id': 'model_type_id',
        'field_values': 'field_values',
        'title': 'title',
        'disabled': 'disabled',
        'genre_id': 'genre_id',
        'description': 'description',
        'short_name': 'short_name',
        'medium_name': 'medium_name',
        'website': 'website',
        'email': 'email',
        'recommended': 'recommended',
        'language': 'language',
        'pty_code_id': 'pty_code_id',
        'genre': 'genre',
        'items': 'items',
        'blocks': 'blocks',
        'broadcasts': 'broadcasts',
        'presenters': 'presenters',
        'tags': 'tags',
        'model_type': 'model_type'
    }

    def __init__(self, id=None, updated_at=None, created_at=None, deleted_at=None, external_station_id=None, model_type_id=None, field_values=None, title=None, disabled=None, genre_id=None, description=None, short_name=None, medium_name=None, website=None, email=None, recommended=None, language=None, pty_code_id=None, genre=None, items=None, blocks=None, broadcasts=None, presenters=None, tags=None, model_type=None):
        """
        ProgramResult - a model defined in Swagger
        """

        self._id = None
        self._updated_at = None
        self._created_at = None
        self._deleted_at = None
        self._external_station_id = None
        self._model_type_id = None
        self._field_values = None
        self._title = None
        self._disabled = None
        self._genre_id = None
        self._description = None
        self._short_name = None
        self._medium_name = None
        self._website = None
        self._email = None
        self._recommended = None
        self._language = None
        self._pty_code_id = None
        self._genre = None
        self._items = None
        self._blocks = None
        self._broadcasts = None
        self._presenters = None
        self._tags = None
        self._model_type = None

        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.deleted_at = deleted_at
        if external_station_id is not None:
          self.external_station_id = external_station_id
        self.model_type_id = model_type_id
        if field_values is not None:
          self.field_values = field_values
        self.title = title
        if disabled is not None:
          self.disabled = disabled
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
        if pty_code_id is not None:
          self.pty_code_id = pty_code_id
        if genre is not None:
          self.genre = genre
        if items is not None:
          self.items = items
        if blocks is not None:
          self.blocks = blocks
        if broadcasts is not None:
          self.broadcasts = broadcasts
        if presenters is not None:
          self.presenters = presenters
        if tags is not None:
          self.tags = tags
        if model_type is not None:
          self.model_type = model_type

    @property
    def id(self):
        """
        Gets the id of this ProgramResult.

        :return: The id of this ProgramResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProgramResult.

        :param id: The id of this ProgramResult.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ProgramResult.

        :return: The updated_at of this ProgramResult.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ProgramResult.

        :param updated_at: The updated_at of this ProgramResult.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this ProgramResult.

        :return: The created_at of this ProgramResult.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ProgramResult.

        :param created_at: The created_at of this ProgramResult.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this ProgramResult.

        :return: The deleted_at of this ProgramResult.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this ProgramResult.

        :param deleted_at: The deleted_at of this ProgramResult.
        :type: datetime
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")

        self._deleted_at = deleted_at

    @property
    def external_station_id(self):
        """
        Gets the external_station_id of this ProgramResult.

        :return: The external_station_id of this ProgramResult.
        :rtype: int
        """
        return self._external_station_id

    @external_station_id.setter
    def external_station_id(self, external_station_id):
        """
        Sets the external_station_id of this ProgramResult.

        :param external_station_id: The external_station_id of this ProgramResult.
        :type: int
        """

        self._external_station_id = external_station_id

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this ProgramResult.

        :return: The model_type_id of this ProgramResult.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this ProgramResult.

        :param model_type_id: The model_type_id of this ProgramResult.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this ProgramResult.

        :return: The field_values of this ProgramResult.
        :rtype: object
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this ProgramResult.

        :param field_values: The field_values of this ProgramResult.
        :type: object
        """

        self._field_values = field_values

    @property
    def title(self):
        """
        Gets the title of this ProgramResult.

        :return: The title of this ProgramResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProgramResult.

        :param title: The title of this ProgramResult.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def disabled(self):
        """
        Gets the disabled of this ProgramResult.

        :return: The disabled of this ProgramResult.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this ProgramResult.

        :param disabled: The disabled of this ProgramResult.
        :type: bool
        """

        self._disabled = disabled

    @property
    def genre_id(self):
        """
        Gets the genre_id of this ProgramResult.

        :return: The genre_id of this ProgramResult.
        :rtype: int
        """
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        """
        Sets the genre_id of this ProgramResult.

        :param genre_id: The genre_id of this ProgramResult.
        :type: int
        """

        self._genre_id = genre_id

    @property
    def description(self):
        """
        Gets the description of this ProgramResult.

        :return: The description of this ProgramResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProgramResult.

        :param description: The description of this ProgramResult.
        :type: str
        """

        self._description = description

    @property
    def short_name(self):
        """
        Gets the short_name of this ProgramResult.

        :return: The short_name of this ProgramResult.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this ProgramResult.

        :param short_name: The short_name of this ProgramResult.
        :type: str
        """

        self._short_name = short_name

    @property
    def medium_name(self):
        """
        Gets the medium_name of this ProgramResult.

        :return: The medium_name of this ProgramResult.
        :rtype: str
        """
        return self._medium_name

    @medium_name.setter
    def medium_name(self, medium_name):
        """
        Sets the medium_name of this ProgramResult.

        :param medium_name: The medium_name of this ProgramResult.
        :type: str
        """

        self._medium_name = medium_name

    @property
    def website(self):
        """
        Gets the website of this ProgramResult.

        :return: The website of this ProgramResult.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this ProgramResult.

        :param website: The website of this ProgramResult.
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """
        Gets the email of this ProgramResult.

        :return: The email of this ProgramResult.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ProgramResult.

        :param email: The email of this ProgramResult.
        :type: str
        """

        self._email = email

    @property
    def recommended(self):
        """
        Gets the recommended of this ProgramResult.

        :return: The recommended of this ProgramResult.
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """
        Sets the recommended of this ProgramResult.

        :param recommended: The recommended of this ProgramResult.
        :type: bool
        """

        self._recommended = recommended

    @property
    def language(self):
        """
        Gets the language of this ProgramResult.

        :return: The language of this ProgramResult.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this ProgramResult.

        :param language: The language of this ProgramResult.
        :type: str
        """

        self._language = language

    @property
    def pty_code_id(self):
        """
        Gets the pty_code_id of this ProgramResult.

        :return: The pty_code_id of this ProgramResult.
        :rtype: int
        """
        return self._pty_code_id

    @pty_code_id.setter
    def pty_code_id(self, pty_code_id):
        """
        Sets the pty_code_id of this ProgramResult.

        :param pty_code_id: The pty_code_id of this ProgramResult.
        :type: int
        """

        self._pty_code_id = pty_code_id

    @property
    def genre(self):
        """
        Gets the genre of this ProgramResult.

        :return: The genre of this ProgramResult.
        :rtype: BroadcastRelationsGenre
        """
        return self._genre

    @genre.setter
    def genre(self, genre):
        """
        Sets the genre of this ProgramResult.

        :param genre: The genre of this ProgramResult.
        :type: BroadcastRelationsGenre
        """

        self._genre = genre

    @property
    def items(self):
        """
        Gets the items of this ProgramResult.

        :return: The items of this ProgramResult.
        :rtype: ProgramRelationsItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ProgramResult.

        :param items: The items of this ProgramResult.
        :type: ProgramRelationsItems
        """

        self._items = items

    @property
    def blocks(self):
        """
        Gets the blocks of this ProgramResult.

        :return: The blocks of this ProgramResult.
        :rtype: ProgramRelationsBlocks
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """
        Sets the blocks of this ProgramResult.

        :param blocks: The blocks of this ProgramResult.
        :type: ProgramRelationsBlocks
        """

        self._blocks = blocks

    @property
    def broadcasts(self):
        """
        Gets the broadcasts of this ProgramResult.

        :return: The broadcasts of this ProgramResult.
        :rtype: ProgramRelationsBroadcasts
        """
        return self._broadcasts

    @broadcasts.setter
    def broadcasts(self, broadcasts):
        """
        Sets the broadcasts of this ProgramResult.

        :param broadcasts: The broadcasts of this ProgramResult.
        :type: ProgramRelationsBroadcasts
        """

        self._broadcasts = broadcasts

    @property
    def presenters(self):
        """
        Gets the presenters of this ProgramResult.

        :return: The presenters of this ProgramResult.
        :rtype: ProgramRelationsPresenters
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """
        Sets the presenters of this ProgramResult.

        :param presenters: The presenters of this ProgramResult.
        :type: ProgramRelationsPresenters
        """

        self._presenters = presenters

    @property
    def tags(self):
        """
        Gets the tags of this ProgramResult.

        :return: The tags of this ProgramResult.
        :rtype: ProgramRelationsTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ProgramResult.

        :param tags: The tags of this ProgramResult.
        :type: ProgramRelationsTags
        """

        self._tags = tags

    @property
    def model_type(self):
        """
        Gets the model_type of this ProgramResult.

        :return: The model_type of this ProgramResult.
        :rtype: BroadcastRelationsModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ProgramResult.

        :param model_type: The model_type of this ProgramResult.
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
        if not isinstance(other, ProgramResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
