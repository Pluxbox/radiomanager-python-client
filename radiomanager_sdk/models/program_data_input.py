# coding: utf-8

"""
    Pluxbox Radiomanager Client

    Pluxbox RadioManager gives you the power, flexibility and speed you always wanted in a lightweight and easy-to-use web-based radio solution. With Pluxbox RadioManager you can organise your radio workflow and automate your omnichannel communication with your listeners. We offer wide range specialised services for the radio and connections like Hybrid Radio, Visual Radio, your website and social media without losing focus on your broadcast. For more information visit https://pluxbox.com

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProgramDataInput(object):
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
        'field_values': 'ProgramFieldValues',
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
        'tags': 'list[int]',
        'presenters': 'list[int]'
    }

    attribute_map = {
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
        'tags': 'tags',
        'presenters': 'presenters'
    }

    def __init__(self, model_type_id=None, field_values=None, title=None, disabled=None, genre_id=None, description=None, short_name=None, medium_name=None, website=None, email=None, recommended=None, language=None, pty_code_id=None, tags=None, presenters=None):
        """
        ProgramDataInput - a model defined in Swagger
        """

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
        self._tags = None
        self._presenters = None

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
        if tags is not None:
          self.tags = tags
        if presenters is not None:
          self.presenters = presenters

    @property
    def model_type_id(self):
        """
        Gets the model_type_id of this ProgramDataInput.

        :return: The model_type_id of this ProgramDataInput.
        :rtype: int
        """
        return self._model_type_id

    @model_type_id.setter
    def model_type_id(self, model_type_id):
        """
        Sets the model_type_id of this ProgramDataInput.

        :param model_type_id: The model_type_id of this ProgramDataInput.
        :type: int
        """
        if model_type_id is None:
            raise ValueError("Invalid value for `model_type_id`, must not be `None`")

        self._model_type_id = model_type_id

    @property
    def field_values(self):
        """
        Gets the field_values of this ProgramDataInput.

        :return: The field_values of this ProgramDataInput.
        :rtype: ProgramFieldValues
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this ProgramDataInput.

        :param field_values: The field_values of this ProgramDataInput.
        :type: ProgramFieldValues
        """

        self._field_values = field_values

    @property
    def title(self):
        """
        Gets the title of this ProgramDataInput.

        :return: The title of this ProgramDataInput.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProgramDataInput.

        :param title: The title of this ProgramDataInput.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def disabled(self):
        """
        Gets the disabled of this ProgramDataInput.

        :return: The disabled of this ProgramDataInput.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this ProgramDataInput.

        :param disabled: The disabled of this ProgramDataInput.
        :type: bool
        """

        self._disabled = disabled

    @property
    def genre_id(self):
        """
        Gets the genre_id of this ProgramDataInput.

        :return: The genre_id of this ProgramDataInput.
        :rtype: int
        """
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        """
        Sets the genre_id of this ProgramDataInput.

        :param genre_id: The genre_id of this ProgramDataInput.
        :type: int
        """

        self._genre_id = genre_id

    @property
    def description(self):
        """
        Gets the description of this ProgramDataInput.

        :return: The description of this ProgramDataInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProgramDataInput.

        :param description: The description of this ProgramDataInput.
        :type: str
        """

        self._description = description

    @property
    def short_name(self):
        """
        Gets the short_name of this ProgramDataInput.

        :return: The short_name of this ProgramDataInput.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this ProgramDataInput.

        :param short_name: The short_name of this ProgramDataInput.
        :type: str
        """

        self._short_name = short_name

    @property
    def medium_name(self):
        """
        Gets the medium_name of this ProgramDataInput.

        :return: The medium_name of this ProgramDataInput.
        :rtype: str
        """
        return self._medium_name

    @medium_name.setter
    def medium_name(self, medium_name):
        """
        Sets the medium_name of this ProgramDataInput.

        :param medium_name: The medium_name of this ProgramDataInput.
        :type: str
        """

        self._medium_name = medium_name

    @property
    def website(self):
        """
        Gets the website of this ProgramDataInput.

        :return: The website of this ProgramDataInput.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this ProgramDataInput.

        :param website: The website of this ProgramDataInput.
        :type: str
        """

        self._website = website

    @property
    def email(self):
        """
        Gets the email of this ProgramDataInput.

        :return: The email of this ProgramDataInput.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ProgramDataInput.

        :param email: The email of this ProgramDataInput.
        :type: str
        """

        self._email = email

    @property
    def recommended(self):
        """
        Gets the recommended of this ProgramDataInput.

        :return: The recommended of this ProgramDataInput.
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """
        Sets the recommended of this ProgramDataInput.

        :param recommended: The recommended of this ProgramDataInput.
        :type: bool
        """

        self._recommended = recommended

    @property
    def language(self):
        """
        Gets the language of this ProgramDataInput.

        :return: The language of this ProgramDataInput.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this ProgramDataInput.

        :param language: The language of this ProgramDataInput.
        :type: str
        """

        self._language = language

    @property
    def pty_code_id(self):
        """
        Gets the pty_code_id of this ProgramDataInput.

        :return: The pty_code_id of this ProgramDataInput.
        :rtype: int
        """
        return self._pty_code_id

    @pty_code_id.setter
    def pty_code_id(self, pty_code_id):
        """
        Sets the pty_code_id of this ProgramDataInput.

        :param pty_code_id: The pty_code_id of this ProgramDataInput.
        :type: int
        """

        self._pty_code_id = pty_code_id

    @property
    def tags(self):
        """
        Gets the tags of this ProgramDataInput.

        :return: The tags of this ProgramDataInput.
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ProgramDataInput.

        :param tags: The tags of this ProgramDataInput.
        :type: list[int]
        """

        self._tags = tags

    @property
    def presenters(self):
        """
        Gets the presenters of this ProgramDataInput.

        :return: The presenters of this ProgramDataInput.
        :rtype: list[int]
        """
        return self._presenters

    @presenters.setter
    def presenters(self, presenters):
        """
        Sets the presenters of this ProgramDataInput.

        :param presenters: The presenters of this ProgramDataInput.
        :type: list[int]
        """

        self._presenters = presenters

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
        if not isinstance(other, ProgramDataInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
