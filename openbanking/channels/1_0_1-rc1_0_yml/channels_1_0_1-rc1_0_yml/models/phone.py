# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1-rc1.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Phone(object):
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
        'type': 'str',
        'country_calling_code': 'str',
        'area_code': 'str',
        'number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'country_calling_code': 'countryCallingCode',
        'area_code': 'areaCode',
        'number': 'number'
    }

    def __init__(self, type=None, country_calling_code=None, area_code=None, number=None):  # noqa: E501
        """Phone - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._country_calling_code = None
        self._area_code = None
        self._number = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if country_calling_code is not None:
            self.country_calling_code = country_calling_code
        if area_code is not None:
            self.area_code = area_code
        if number is not None:
            self.number = number

    @property
    def type(self):
        """Gets the type of this Phone.  # noqa: E501

        Identificação do Tipo de telefone da dependência. p.ex.FIXO, MOVEL.  # noqa: E501

        :return: The type of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Phone.

        Identificação do Tipo de telefone da dependência. p.ex.FIXO, MOVEL.  # noqa: E501

        :param type: The type of this Phone.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIXO", "MOVEL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def country_calling_code(self):
        """Gets the country_calling_code of this Phone.  # noqa: E501

        Número de DDI (Discagem Direta Internacional) para  telefone de acesso ao Canal - se houver. p.ex. '55'  # noqa: E501

        :return: The country_calling_code of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._country_calling_code

    @country_calling_code.setter
    def country_calling_code(self, country_calling_code):
        """Sets the country_calling_code of this Phone.

        Número de DDI (Discagem Direta Internacional) para  telefone de acesso ao Canal - se houver. p.ex. '55'  # noqa: E501

        :param country_calling_code: The country_calling_code of this Phone.  # noqa: E501
        :type: str
        """

        self._country_calling_code = country_calling_code

    @property
    def area_code(self):
        """Gets the area_code of this Phone.  # noqa: E501

        Número de DDD (Discagem Direta à Distância) do telefone da dependência - se houver. p.ex. '19'  # noqa: E501

        :return: The area_code of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this Phone.

        Número de DDD (Discagem Direta à Distância) do telefone da dependência - se houver. p.ex. '19'  # noqa: E501

        :param area_code: The area_code of this Phone.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def number(self):
        """Gets the number of this Phone.  # noqa: E501

        Número de telefone da dependência - se houver  # noqa: E501

        :return: The number of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Phone.

        Número de telefone da dependência - se houver  # noqa: E501

        :param number: The number of this Phone.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if issubclass(Phone, dict):
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
        if not isinstance(other, Phone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
