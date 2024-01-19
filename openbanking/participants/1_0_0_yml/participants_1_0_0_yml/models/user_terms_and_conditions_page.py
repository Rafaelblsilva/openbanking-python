# coding: utf-8

"""
    Participantes Open Finance Brasil

    Informações sobre os participantes do Open Finance Brasil que estão registrados no Diretório.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserTermsAndConditionsPage(object):
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
        'total_pages': 'int',
        'total_size': 'int',
        'pageable': 'Pageable',
        'number_of_elements': 'int',
        'size': 'int',
        'content': 'list[TermsAndConditionsDetail]',
        'offset': 'int',
        'empty': 'bool',
        'page_number': 'int'
    }

    attribute_map = {
        'total_pages': 'totalPages',
        'total_size': 'totalSize',
        'pageable': 'pageable',
        'number_of_elements': 'numberOfElements',
        'size': 'size',
        'content': 'content',
        'offset': 'offset',
        'empty': 'empty',
        'page_number': 'pageNumber'
    }

    def __init__(self, total_pages=None, total_size=None, pageable=None, number_of_elements=None, size=None, content=None, offset=None, empty=None, page_number=None):  # noqa: E501
        """UserTermsAndConditionsPage - a model defined in Swagger"""  # noqa: E501
        self._total_pages = None
        self._total_size = None
        self._pageable = None
        self._number_of_elements = None
        self._size = None
        self._content = None
        self._offset = None
        self._empty = None
        self._page_number = None
        self.discriminator = None
        if total_pages is not None:
            self.total_pages = total_pages
        if total_size is not None:
            self.total_size = total_size
        if pageable is not None:
            self.pageable = pageable
        if number_of_elements is not None:
            self.number_of_elements = number_of_elements
        if size is not None:
            self.size = size
        if content is not None:
            self.content = content
        if offset is not None:
            self.offset = offset
        if empty is not None:
            self.empty = empty
        if page_number is not None:
            self.page_number = page_number

    @property
    def total_pages(self):
        """Gets the total_pages of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The total_pages of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this UserTermsAndConditionsPage.


        :param total_pages: The total_pages of this UserTermsAndConditionsPage.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total_size(self):
        """Gets the total_size of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The total_size of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this UserTermsAndConditionsPage.


        :param total_size: The total_size of this UserTermsAndConditionsPage.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def pageable(self):
        """Gets the pageable of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The pageable of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: Pageable
        """
        return self._pageable

    @pageable.setter
    def pageable(self, pageable):
        """Sets the pageable of this UserTermsAndConditionsPage.


        :param pageable: The pageable of this UserTermsAndConditionsPage.  # noqa: E501
        :type: Pageable
        """

        self._pageable = pageable

    @property
    def number_of_elements(self):
        """Gets the number_of_elements of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The number_of_elements of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """Sets the number_of_elements of this UserTermsAndConditionsPage.


        :param number_of_elements: The number_of_elements of this UserTermsAndConditionsPage.  # noqa: E501
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def size(self):
        """Gets the size of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The size of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UserTermsAndConditionsPage.


        :param size: The size of this UserTermsAndConditionsPage.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def content(self):
        """Gets the content of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The content of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: list[TermsAndConditionsDetail]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UserTermsAndConditionsPage.


        :param content: The content of this UserTermsAndConditionsPage.  # noqa: E501
        :type: list[TermsAndConditionsDetail]
        """

        self._content = content

    @property
    def offset(self):
        """Gets the offset of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The offset of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this UserTermsAndConditionsPage.


        :param offset: The offset of this UserTermsAndConditionsPage.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def empty(self):
        """Gets the empty of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The empty of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this UserTermsAndConditionsPage.


        :param empty: The empty of this UserTermsAndConditionsPage.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def page_number(self):
        """Gets the page_number of this UserTermsAndConditionsPage.  # noqa: E501


        :return: The page_number of this UserTermsAndConditionsPage.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this UserTermsAndConditionsPage.


        :param page_number: The page_number of this UserTermsAndConditionsPage.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

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
        if issubclass(UserTermsAndConditionsPage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserTermsAndConditionsPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other