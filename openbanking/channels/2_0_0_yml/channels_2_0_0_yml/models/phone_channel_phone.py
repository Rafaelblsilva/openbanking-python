# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PhoneChannelPhone(object):
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
        'country_calling_code': 'str',
        'area_code': 'str',
        'number': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'country_calling_code': 'countryCallingCode',
        'area_code': 'areaCode',
        'number': 'number',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, country_calling_code=None, area_code=None, number=None, additional_info=None):  # noqa: E501
        """PhoneChannelPhone - a model defined in Swagger"""  # noqa: E501
        self._country_calling_code = None
        self._area_code = None
        self._number = None
        self._additional_info = None
        self.discriminator = None
        self.country_calling_code = country_calling_code
        self.area_code = area_code
        self.number = number
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def country_calling_code(self):
        """Gets the country_calling_code of this PhoneChannelPhone.  # noqa: E501

        Número de DDI (Discagem Direta Internacional) para  telefone de acesso ao Canal - se houver.  # noqa: E501

        :return: The country_calling_code of this PhoneChannelPhone.  # noqa: E501
        :rtype: str
        """
        return self._country_calling_code

    @country_calling_code.setter
    def country_calling_code(self, country_calling_code):
        """Sets the country_calling_code of this PhoneChannelPhone.

        Número de DDI (Discagem Direta Internacional) para  telefone de acesso ao Canal - se houver.  # noqa: E501

        :param country_calling_code: The country_calling_code of this PhoneChannelPhone.  # noqa: E501
        :type: str
        """
        if country_calling_code is None:
            raise ValueError("Invalid value for `country_calling_code`, must not be `None`")  # noqa: E501

        self._country_calling_code = country_calling_code

    @property
    def area_code(self):
        """Gets the area_code of this PhoneChannelPhone.  # noqa: E501

        Número de DDD (Discagem Direta à Distância) para  telefone de acesso ao Canal - se houver.  # noqa: E501

        :return: The area_code of this PhoneChannelPhone.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this PhoneChannelPhone.

        Número de DDD (Discagem Direta à Distância) para  telefone de acesso ao Canal - se houver.  # noqa: E501

        :param area_code: The area_code of this PhoneChannelPhone.  # noqa: E501
        :type: str
        """
        if area_code is None:
            raise ValueError("Invalid value for `area_code`, must not be `None`")  # noqa: E501

        self._area_code = area_code

    @property
    def number(self):
        """Gets the number of this PhoneChannelPhone.  # noqa: E501

        Número de telefone de acesso ao canal.   # noqa: E501

        :return: The number of this PhoneChannelPhone.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PhoneChannelPhone.

        Número de telefone de acesso ao canal.   # noqa: E501

        :param number: The number of this PhoneChannelPhone.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def additional_info(self):
        """Gets the additional_info of this PhoneChannelPhone.  # noqa: E501


        :return: The additional_info of this PhoneChannelPhone.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this PhoneChannelPhone.


        :param additional_info: The additional_info of this PhoneChannelPhone.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

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
        if issubclass(PhoneChannelPhone, dict):
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
        if not isinstance(other, PhoneChannelPhone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
